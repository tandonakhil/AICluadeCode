"""The static import-closure checker.

VENDORED from `projects/rate-case-analyzer/dev/tools/structural_checks/closure.py`
unmodified. Confirmed domain-free at harvest (2026-08-08): the only
project-specific string in the whole module was the *default value* of
`package_alias`, which is `"app"` — that is a convention shared by every
Conclave project's own layout, not an RCA name, and it is a parameter with a
default, not a hardcoded value. No RCA module, class or acceptance-criterion
name appears anywhere below.

Four properties that are design decisions, not incidental:

1. **It parses, it never imports.** ``ast.parse`` on each file; ``Import`` and
   ``ImportFrom`` (including relative) resolved to files inside the package;
   recursion to a fixed point. Importing to inspect would execute module bodies
   and would make a *runtime* check out of something the criterion requires to
   be static.

2. **It closes the dynamic-import escape hatch.** A static closure is evaded by
   ``importlib.import_module("app.stores.workproduct_store")``. So the checker
   also fails if any module in a boundary's closure references ``importlib``,
   ``__import__``, ``eval``, ``exec``, or subscripts ``globals()`` /
   ``sys.modules``. A static boundary check that ignores dynamic imports is a
   boundary check with a hole in it.

3. **It is a pure function of a package root path.** That is what makes the
   negative controls cheap: point the same function at a mutated fixture tree
   under ``tests/negative_controls/`` and assert it returns a violation. No
   mutation ever touches the real source tree.

4. **It reports a PATH through the graph**, not merely a verdict, because a
   boundary failure that does not say *how* the module was reached is a failure
   someone papers over with an unrelated edit.

Self-certification note (H3): an adopter can point this very function at
`accelerators/conformance-kit/src/` itself — pass `package_root=Path("accelerators/conformance-kit/src")`
and a boundary set forbidding imports of any `projects.*` or a named host
package — as a check that the accelerator does not secretly depend on its
origin projects. See `ACCELERATOR.md` H3 for the worked version of this.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

DYNAMIC_IMPORT_MARKERS = ("importlib", "__import__", "eval", "exec")


@dataclass(frozen=True)
class Violation:
    boundary: str
    kind: str  # "module" | "symbol" | "dynamic-import"
    detail: str
    path: tuple[str, ...] = ()

    def __str__(self) -> str:
        route = " -> ".join(self.path) if self.path else "(root)"
        return f"[{self.boundary}] {self.kind}: {self.detail}  via {route}"


def _module_name(file: Path, package_root: Path, package_alias: str) -> str:
    relative = file.relative_to(package_root).with_suffix("")
    parts = list(relative.parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join([package_alias, *parts]) if parts else package_alias


def build_module_map(package_root: Path, package_alias: str = "app") -> dict[str, Path]:
    """Map dotted module name -> file, for every ``.py`` under the root."""
    mapping: dict[str, Path] = {}
    for file in sorted(package_root.rglob("*.py")):
        mapping[_module_name(file, package_root, package_alias)] = file
    return mapping


def _resolve_relative(module: str, level: int, current: str) -> str:
    parts = current.split(".")
    # a package __init__ has no trailing module component to strip
    base = parts[: len(parts) - level + 1] if level <= len(parts) else []
    return ".".join([*base, module]) if module else ".".join(base)


def direct_imports(file: Path, current_module: str) -> tuple[str, ...]:
    tree = ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                found.append(_resolve_relative(node.module or "", node.level, current_module))
            elif node.module:
                found.append(node.module)
                found.extend(f"{node.module}.{alias.name}" for alias in node.names)
    return tuple(found)


def references_dynamic_import(file: Path) -> tuple[str, ...]:
    text = file.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(file))
    hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in DYNAMIC_IMPORT_MARKERS:
            hits.append(node.id)
        elif isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name) and node.value.id == "importlib":
                hits.append(f"importlib.{node.attr}")
            if isinstance(node.value, ast.Name) and node.value.id == "sys" and node.attr == "modules":
                hits.append("sys.modules")
        elif isinstance(node, ast.Subscript):
            target = node.value
            if isinstance(target, ast.Call) and isinstance(target.func, ast.Name):
                if target.func.id in ("globals", "vars"):
                    hits.append(f"{target.func.id}()[...]")
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names = (
                [a.name for a in node.names]
                if isinstance(node, ast.Import)
                else [node.module or ""]
            )
            for name in names:
                if name.split(".")[0] == "importlib":
                    hits.append(name)
    return tuple(sorted(set(hits)))


def closure(
    root_module: str, module_map: dict[str, Path]
) -> dict[str, tuple[str, ...]]:
    """Transitive import closure of ``root_module``.

    Returns module -> the path taken to reach it, so a violation can name the
    route rather than just the endpoint.
    """
    reached: dict[str, tuple[str, ...]] = {}
    prefix = root_module + "."
    submodules = [name for name in module_map if name.startswith(prefix)]
    root_file = module_map.get(root_module)
    is_package_root = root_file is not None and root_file.name == "__init__.py"

    if root_module not in module_map or is_package_root:
        # A package root such as "app". Seeding only with the package's own
        # __init__.py would make the closure of "app" the closure of an empty
        # file, which is how a whole-package boundary silently passes.
        seeds = [name for name in module_map if name == root_module or name.startswith(prefix)]
        if not seeds:
            seeds = submodules
        for seed in seeds:
            reached[seed] = (seed,)
        frontier = list(seeds)
    else:
        reached[root_module] = (root_module,)
        frontier = [root_module]

    while frontier:
        current = frontier.pop()
        file = module_map.get(current)
        if file is None:
            continue
        for imported in direct_imports(file, current):
            candidates = [imported]
            # `from app.stores import rows` yields "app.stores"; also try the
            # submodule form so package-level imports resolve to real files.
            for candidate in candidates:
                if candidate in module_map and candidate not in reached:
                    reached[candidate] = (*reached[current], candidate)
                    frontier.append(candidate)
                elif candidate not in module_map and candidate not in reached:
                    reached[candidate] = (*reached[current], candidate)
    return reached


def _matches(pattern: str, module: str) -> bool:
    if pattern == "*":
        return True
    if pattern.endswith(".*"):
        return module == pattern[:-2] or module.startswith(pattern[:-1])
    return module == pattern or module.startswith(pattern + ".")


def _symbol_hits(file: Path, symbols: tuple[str, ...]) -> tuple[str, ...]:
    """Symbol scan over the AST, not over raw text.

    Comments and docstrings are therefore exempt, which matters: a module may
    legitimately *document* that it performs no case-folding.
    """
    tree = ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
    wanted = set(symbols)
    hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in wanted:
            hits.append(node.attr)
        elif isinstance(node, ast.Name) and node.id in wanted:
            hits.append(node.id)
        elif isinstance(node, ast.Attribute):
            if isinstance(node.value, ast.Name):
                dotted = f"{node.value.id}.{node.attr}"
                if dotted in wanted:
                    hits.append(dotted)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names = (
                [a.name for a in node.names]
                if isinstance(node, ast.Import)
                else [node.module or ""] + [a.name for a in node.names]
            )
            for name in names:
                if name in wanted or name.split(".")[0] in wanted:
                    hits.append(name)
    return tuple(sorted(set(hits)))


def check(
    package_root: Path,
    boundaries,
    package_alias: str = "app",
) -> tuple[Violation, ...]:
    """Pure function of a package root path. Returns every violation found."""
    module_map = build_module_map(package_root, package_alias)
    violations: list[Violation] = []

    for boundary in boundaries:
        for root in boundary.roots:
            if getattr(boundary, "direct_only", False):
                file = module_map.get(root)
                reached = {root: (root,)}
                if file is not None:
                    for imported in direct_imports(file, root):
                        reached[imported] = (root, imported)
            else:
                reached = closure(root, module_map)

            for module, route in sorted(reached.items()):
                if module == root or module in boundary.except_modules:
                    continue
                for pattern in boundary.forbidden_modules:
                    if pattern == "*":
                        # zero-import boundary: any reached module is a violation
                        if module != root:
                            violations.append(
                                Violation(
                                    boundary.name,
                                    "module",
                                    f"{root} must have an EMPTY import closure but reaches {module}",
                                    route,
                                )
                            )
                        continue
                    if _matches(pattern, module):
                        violations.append(
                            Violation(
                                boundary.name,
                                "module",
                                f"{root} reaches forbidden module {module} (pattern {pattern})",
                                route,
                            )
                        )

            if boundary.forbidden_symbols:
                for module, route in sorted(reached.items()):
                    if module in boundary.except_modules:
                        continue
                    file = module_map.get(module)
                    if file is None:
                        continue
                    for hit in _symbol_hits(file, boundary.forbidden_symbols):
                        violations.append(
                            Violation(
                                boundary.name,
                                "symbol",
                                f"{module} references forbidden symbol {hit!r}",
                                route,
                            )
                        )

            for module, route in sorted(reached.items()):
                file = module_map.get(module)
                if file is None or module in boundary.except_modules:
                    continue
                hits = references_dynamic_import(file)
                if hits:
                    violations.append(
                        Violation(
                            boundary.name,
                            "dynamic-import",
                            f"{module} uses a dynamic-import escape hatch: {list(hits)}",
                            route,
                        )
                    )

    return tuple(violations)
