#!/usr/bin/env python3
"""Regenerates PORTFOLIO_STATUS.md's at-a-glance table from pipeline-state.json.

Written 2026-08-03. The table had been hand-maintained, was five days stale, and
was missing TWO ENTIRE PROJECTS -- conclave-finance-studio and conclave-dashboard
-- from the view whose whole job is "where every project stands, at a glance".
A hand-maintained summary of machine-readable state will always drift; this makes
the state the source and the table a rendering of it.

Only the table between the AT-A-GLANCE markers is touched. Prose, per-project
sections and notes are left exactly as written.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
START = "<!-- AT-A-GLANCE:START -->"
END = "<!-- AT-A-GLANCE:END -->"

def row(state_path):
    d = json.loads(state_path.read_text())
    name = state_path.parent.name
    gates = d.get("gates", [])
    done = [g for g in gates if g.get("status") in ("done", "warn")]
    active = [g for g in gates if g.get("status") == "active"]
    total = len(gates) or 11
    pos = d.get("position") or (("Gate %s — %s" % (active[0]["n"], active[0]["name"])) if active else "—")
    # a released project says so; otherwise report the honest position
    link = d.get("served_url") or "—"
    if link != "—":
        link = "[live](%s)" % link
    return "| [%s](#%s) | %s | %s | %s | %d of %d | %s | %s |" % (
        name, name, d.get("template", "custom"), pos,
        d.get("env", "dev, local"), len(done), total,
        link, d.get("updated", "—"))

def main():
    p = ROOT / "admin" / "PORTFOLIO_STATUS.md"
    t = p.read_text()
    states = sorted(ROOT.glob("projects/*/pipeline-state.json"))
    header = ("| Project | Template | Position | Env | Gates done | Live | Last activity |\n"
              "|---|---|---|---|---|---|---|")
    table = "\n".join([header] + [row(s) for s in states])
    block = "%s\n%s\n%s" % (START, table, END)

    if START in t and END in t:
        t = re.sub(re.escape(START) + r".*?" + re.escape(END), block, t, flags=re.S)
    else:
        # first run: replace the legacy hand-written table under "## At a glance"
        t = re.sub(r"(## At a glance\n\n)\|.*?\n\n", r"\1" + block + "\n\n", t, flags=re.S)
    t = re.sub(r"\*\*Last regenerated\*\*: \d{4}-\d{2}-\d{2}",
               "**Last regenerated**: %s  ·  table generated from `pipeline-state.json` by "
               "`admin/regen-portfolio-glance.py`, not hand-maintained" % max(
                   json.loads(s.read_text()).get("updated", "0000-00-00") for s in states), t)
    p.write_text(t)
    print("regenerated %d project rows" % len(states))
    for s in states:
        print("  " + s.parent.name)

if __name__ == "__main__":
    main()
