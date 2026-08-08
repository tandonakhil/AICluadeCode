#!/usr/bin/env python3
"""Refuses to stay quiet when a project's dashboard disagrees with its own record.

Written 2026-08-03 after the human found conclave-finance-studio's row in
memory/INDEX.md reading "gate 1 Intake" while the project was at gate 9 — five
days and eight gates stale. The orchestrator's contract already said a step that
leaves the dashboard stale is not finished. The rule existed; nothing checked it.

This is deliberately mechanical. It does not judge whether a project SHOULD have
moved; it only reports where two records of the same fact disagree, or where a
record carries no date at all. A file with no `updated` field is the worst case,
because it cannot even be found to be stale.
"""
import json, pathlib, re, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
GATES = ["Intake","Team","Plan","Functional","Experience","Architecture",
         "Code","Test","Verify","Review","Deploy"]

def today():
    return datetime.date.today().isoformat()

def check():
    problems = []
    index = (ROOT/"memory"/"INDEX.md").read_text()

    for state_path in sorted(ROOT.glob("projects/*/pipeline-state.json")):
        name = state_path.parent.name
        try:
            d = json.loads(state_path.read_text())
        except Exception as e:
            problems.append((name, "pipeline-state.json does not parse: %s" % e))
            continue

        # 1. undated state is undetectable staleness
        if not d.get("updated"):
            problems.append((name, "pipeline-state.json has no `updated` field — "
                                   "staleness cannot be detected, only noticed"))
        # 2. the state must name a gate that is actually open
        live = [g for g in d.get("gates", []) if g.get("status") == "active"]
        pos = d.get("position", "")
        for g in live:
            if g["name"] not in pos and str(g["n"]) not in pos:
                problems.append((name, "gate %s (%s) is active but `position` reads %r"
                                       % (g["n"], g["name"], pos)))
        # 3. a gate marked done after an active one is out of order
        seen_active = None
        for g in d.get("gates", []):
            if g.get("status") == "active":
                seen_active = g["n"]
            elif seen_active is not None and g.get("status") == "done" and g["n"] > seen_active:
                # A later gate done while an earlier one is active is the normal
                # shape of a LOOP-BACK, not an error -- but only if the route
                # change was recorded. An unexplained one is the real defect.
                if not d.get("route_changes") and not d.get("loop_backs"):
                    problems.append((name, "gate %s is done while gate %s is active, "
                                           "with no loop_backs or route_changes entry "
                                           "explaining it" % (g["n"], seen_active)))
        # 4. a project that has reached Code should carry a live link
        reached_code = any(g.get("n", 0) >= 7 and g.get("status") in ("done", "active", "warn")
                           for g in d.get("gates", []))
        if reached_code and not d.get("served_url"):
            problems.append((name, "reached gate 7 but `served_url` is null — the dashboard "
                                   "shows no live link for a project that has something to show"))

        # 5. INDEX.md must agree with the state file
        row = [l for l in index.splitlines() if l.startswith("| %s " % name)]
        if not row:
            problems.append((name, "no row in memory/INDEX.md"))
        else:
            cells = [c.strip() for c in row[0].split("|")]
            stage = cells[3] if len(cells) > 3 else ""
            highest = max([g["n"] for g in d.get("gates", [])
                           if g.get("status") in ("done","active","warn")] or [0])
            claimed = [i+1 for i,gn in enumerate(GATES) if gn.lower() in stage.lower()]
            # An ENHANCEMENT re-enters an earlier gate on a finished project, so a
            # row naming an early gate against a high-water mark is the normal shape
            # of that -- not staleness. Same refinement the loop-back rule needed.
            # It is only a defect when nothing explains the re-entry.
            enhancing = ("complete" in stage.lower()
                         or "enhancement" in stage.lower()
                         or (ROOT / "projects" / name / "FEATURES.md").exists()
                         and "## In Development" in (ROOT / "projects" / name / "FEATURES.md").read_text())
            if claimed and max(claimed) < highest and not enhancing:
                problems.append((name, "INDEX.md says %r but pipeline-state reaches gate %s, "
                                       "with no 'complete'/'enhancement' marker and no "
                                       "FEATURES.md In Development entry to explain the re-entry"
                                       % (stage, highest)))
            date_cell = cells[5] if len(cells) > 5 else ""
            if d.get("updated") and re.match(r"\d{4}-\d{2}-\d{2}", date_cell or ""):
                if date_cell < d["updated"]:
                    problems.append((name, "INDEX.md dated %s, pipeline-state updated %s"
                                           % (date_cell, d["updated"])))
    return problems

if __name__ == "__main__":
    problems = check()
    if not problems:
        print("dashboard: consistent across every project")
        sys.exit(0)
    print("DASHBOARD IS STALE — %d disagreement(s)\n" % len(problems))
    for name, why in problems:
        print("  %-28s %s" % (name, why))
    print("\nA step that leaves the dashboard stale is not finished (ORCHESTRATOR.md).")
    sys.exit(1)
