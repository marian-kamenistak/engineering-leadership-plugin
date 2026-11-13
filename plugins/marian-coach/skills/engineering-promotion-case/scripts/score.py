"""Promotion case score: the arithmetic, so the number never depends on a mood.

  python3 score.py <case.json>
  python3 score.py --selftest

case.json:
  {"name": "Alex", "from": "Senior engineer", "to": "Staff engineer", "track": "to_staff",
   "date": "2026-11-13",
   "scores": {"outcomes":   {"level": 1, "evidence": ["p95 checkout latency 900 ms -> 300 ms, Q2"]},
              "next_level": {"level": 0.5, "evidence": ["owns the search part of the tech roadmap"]},
              "scope":      {"level": 0, "missing": "same two services as at the last promotion"},
              ...},
   "plan": {"month": {"manager": 2}, "quarter": {"outcomes": 2}, "six_months": {"next_level": 1.5}}}

Rules the script enforces, because the case is evidence only:
  - every criterion in model.json is scored, with 0, 0.5, 1, 1.5 or 2;
  - a level above 0 needs at least one evidence item (the person's own fact: a number, a name, a date);
  - level 0 needs a "missing" note: what is not visible yet;
  - if "manager" is below 1, the step is capped at 3 (the early ask comes first).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = json.load(open(os.path.join(HERE, "..", "model.json"), encoding="utf-8"))
LEVELS = (0, 0.5, 1, 1.5, 2)
CRIT = MODEL["criteria"]
HORIZONS = ("month", "quarter", "six_months")


def score(levels):
    """Case score 0..10 = 5 x weighted average level."""
    return 5.0 * sum(c["weight"] * levels[c["id"]] for c in CRIT) / 100.0


def step(s, levels):
    shown = round(s + 1e-9, 1)
    st = next(b for b in MODEL["steps"] if shown < b["below"])
    capped = False
    gate = [c["id"] for c in CRIT if c.get("gate")]
    if any(levels[g] < 1 for g in gate) and st["step"] > 3:
        st, capped = MODEL["steps"][2], True
    return st, capped


def check(data):
    assert sum(c["weight"] for c in CRIT) == 100, "weights do not add up to 100"
    assert data.get("track") in MODEL["tracks"], "track must be one of: %s" % ", ".join(MODEL["tracks"])
    s = data["scores"]
    ids = [c["id"] for c in CRIT]
    missing = [i for i in ids if i not in s]
    assert not missing, "no score for: %s" % ", ".join(missing)
    extra = [i for i in s if i not in ids]
    assert not extra, "unknown criteria: %s" % ", ".join(extra)
    for i in ids:
        lv = s[i].get("level")
        assert lv in LEVELS, "%s: level %r is not one of %s" % (i, lv, LEVELS)
        if lv > 0:
            assert s[i].get("evidence"), "%s: level %s needs evidence (their own fact)" % (i, lv)
        else:
            assert s[i].get("missing"), "%s: level 0 needs a 'missing' note (what is not visible yet)" % i


def report(data):
    check(data)
    levels = {c["id"]: data["scores"][c["id"]]["level"] for c in CRIT}
    sc = score(levels)
    st, capped = step(sc, levels)
    head = "%s -> %s · %s" % (data.get("from", "?"), data.get("to", "?"), data.get("date", ""))
    out = [(data["name"] + " · " + head) if data.get("name") else head,
           "PROMOTION CASE %.1f/10 · %s (step %d of 4). %s" % (sc, st["name"], st["step"], st["line"])]
    if capped:
        out.append("Capped at step 3: your manager has no stake yet. The early ask comes first.")
    out += ["", "| Criterion | Weight | Level | Next anchor is worth |", "|---|---|---|---|"]
    gains = []
    for c in CRIT:
        lv = levels[c["id"]]
        name = MODEL["levels"][str(lv).replace(".0", "")]
        if lv >= 2:
            out.append("| %s | %d | %s (%s) | at the top |" % (c["name"], c["weight"], lv, name))
            continue
        target = 2 if lv >= 1 else 1
        nxt = dict(levels); nxt[c["id"]] = target
        g = score(nxt) - sc
        gains.append((g, c["weight"], c["name"], target))
        out.append("| %s | %d | %s (%s) | to %s: +%.1f |" % (c["name"], c["weight"], lv, name, target, g))
    gains.sort(key=lambda x: (-round(x[0], 4), -x[1]))
    out += ["", "Biggest gains to the next anchor: " + " · ".join("%s (to %s) +%.1f" % (n, t, g) for g, _, n, t in gains[:3])]
    plan = data.get("plan") or {}
    if plan:
        cur = dict(levels); line = ["today %.1f" % sc]
        for h in HORIZONS:
            for k, v in (plan.get(h) or {}).items():
                assert k in cur, "plan names an unknown criterion: %s" % k
                assert v in LEVELS and v >= cur[k], "plan level %r for %s" % (v, k)
                cur[k] = v
            if plan.get(h):
                s2 = score(cur); st2, _ = step(s2, cur)
                line.append("after %s %.1f (%s)" % ("six months" if h == "six_months" else "the " + h, s2, st2["name"]))
        out += ["", "Projection: " + " -> ".join(line)]
    return "\n".join(out)


def selftest():
    ids = [c["id"] for c in CRIT]
    assert sum(c["weight"] for c in CRIT) == 100
    for lv, want in ((0, 0.0), (1, 5.0), (2, 10.0)):
        assert abs(score({i: lv for i in ids}) - want) < 1e-9
    full = {i: 2 for i in ids}
    assert step(10.0, full)[0]["name"] == "Ready to ask"
    for m in (0, 0.5):
        gated = dict(full); gated["manager"] = m
        st, capped = step(score(gated), gated)
        assert capped and st["step"] == 3, (m, st, capped)
    open_ = dict(full); open_["manager"] = 1
    assert step(score(open_), open_)[0]["step"] == 4
    assert [step(x, full)[0]["step"] for x in (0, 3.94, 3.96, 5.9, 6.0, 7.9, 7.96, 8.0, 10)] == [1, 1, 2, 2, 3, 3, 4, 4, 4]
    for c in CRIT:
        assert {"0", "1", "2"} <= set(c["levels"]) and set(c["moves"]) == {"month", "quarter"}, c["id"]
    data = {"name": "Test", "track": "to_staff", "scores": {i: {"level": 1, "evidence": ["x"]} for i in ids},
            "plan": {"month": {"manager": 2}}}
    assert "PROMOTION CASE 5.0/10" in report(data)
    bad = {"name": "Test", "track": "to_staff", "scores": {i: {"level": 1} for i in ids}}
    try:
        report(bad); raise SystemExit("evidence rule not enforced")
    except AssertionError:
        pass
    print("selftest ok")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        selftest()
    elif len(sys.argv) == 2:
        print(report(json.load(open(sys.argv[1], encoding="utf-8"))))
    else:
        sys.exit(__doc__)
