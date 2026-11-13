"""Digital footprint multiplier: the arithmetic, so the number never depends on a mood.

  python3 score.py <developer|engineering_manager> <scores.json>
  python3 score.py --selftest

scores.json:
  {"name": "Jana Nováková", "url": "https://www.linkedin.com/in/...", "date": "2026-11-12",
   "scores": {"headline": {"level": 1.5, "evidence": ["headline: 'Payments Platform Engineer'"]},
              "voice":    {"level": 0,   "looked": ["LinkedIn activity, 12 months", "web search: name + talk"]},
              "proof_of_work": {"level": null, "why": "employer forbids public code"}},
   "plan": {"week": {"headline": 2}, "month": {"voice": 1}, "quarter": {"proof_of_work": 1}}}

Rules the script enforces, because the score is evidence only:
  - a level is 0, 0.5, 1, 1.5 or 2, or null for "cannot be observed" (at most two criteria);
  - a level above 0 needs at least one evidence item (a quoted line or a URL);
  - level 0 needs a "looked" list: where you checked before saying "not visible yet";
  - null criteria drop out and the other weights are scaled back to 100.

Same scale as market-value-multiplier: all 0 -> 0.4, all 1 -> 1.0, all 2 -> 1.7.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = json.load(open(os.path.join(HERE, "..", "model.json"), encoding="utf-8"))
LEVELS = (0, 0.5, 1, 1.5, 2)


def multiplier(avg):
    """avg is the weighted average level, 0..2."""
    return 0.4 + 0.6 * avg if avg <= 1 else 1.0 + 0.7 * (avg - 1)


def band(m):
    """Nine steps cut from a bell curve; the step follows the multiplier as displayed (two decimals)."""
    shown = round(m + 1e-9, 2)
    for b in MODEL["bands"]:
        if shown < b["below"]:
            return b


def weights(profile, levels):
    """Weights of the observable criteria, scaled back to 100."""
    crit = [c for c in MODEL["profiles"][profile]["criteria"] if levels.get(c["id"]) is not None]
    total = sum(c["weight"] for c in crit)
    return {c["id"]: c["weight"] * 100.0 / total for c in crit}


def score(profile, levels):
    w = weights(profile, levels)
    return multiplier(sum(w[k] * levels[k] for k in w) / 100.0)


def check(profile, data):
    crit = MODEL["profiles"][profile]["criteria"]
    assert sum(c["weight"] for c in crit) == 100, "weights of %s do not add up to 100" % profile
    ids = [c["id"] for c in crit]
    s = data["scores"]
    missing = [i for i in ids if i not in s]
    assert not missing, "no score for: %s" % ", ".join(missing)
    extra = [i for i in s if i not in ids]
    assert not extra, "unknown criteria: %s" % ", ".join(extra)
    na = [i for i in ids if s[i].get("level") is None]
    assert len(na) <= 2, "more than two criteria marked unobservable: research them instead"
    for i in ids:
        lv = s[i].get("level")
        if lv is None:
            assert s[i].get("why"), "%s is null: say why it cannot be observed" % i
            continue
        assert lv in LEVELS, "%s: level %r is not one of %s" % (i, lv, LEVELS)
        if lv > 0:
            assert s[i].get("evidence"), "%s: level %s needs evidence (a quoted line or a URL)" % (i, lv)
        else:
            assert s[i].get("looked"), "%s: level 0 needs a 'looked' list (where you checked)" % i


def report(profile, data):
    check(profile, data)
    crit = MODEL["profiles"][profile]["criteria"]
    levels = {c["id"]: data["scores"][c["id"]].get("level") for c in crit}
    w = weights(profile, levels)
    m = score(profile, levels)
    b = band(m)
    out = ["%s · %s profile · %s" % (data.get("name", "?"), MODEL["profiles"][profile]["name"], data.get("date", "")),
           "MULTIPLIER %.2fx · %s (step %d of 9). %s" % (m, b["name"], b["step"], b["line"]), "",
           "| Criterion | Weight | Level | Next anchor is worth |", "|---|---|---|---|"]
    gains = []
    for c in crit:
        lv = levels[c["id"]]
        if lv is None:
            out.append("| %s | %d | could not be observed | - |" % (c["name"], c["weight"]))
            continue
        # The next step is the next written anchor: 0 or 0.5 -> 1, 1 or 1.5 -> 2. At 2 there is nothing to gain.
        target = 2 if lv >= 1 else 1
        nxt = dict(levels); nxt[c["id"]] = target
        g = score(profile, nxt) - m
        name = MODEL["levels"][str(lv).replace(".0", "")]
        if lv >= 2:
            out.append("| %s | %.0f | %s (%s) | at the top |" % (c["name"], w[c["id"]], lv, name))
            continue
        gains.append((g, w[c["id"]], c["name"], target))
        out.append("| %s | %.0f | %s (%s) | to %s: +%.2f |" % (c["name"], w[c["id"]], lv, name, target, g))
    # Largest gain first; equal gains go to the heavier criterion.
    gains.sort(key=lambda x: (-round(x[0], 4), -x[1]))
    out += ["", "Biggest gains to the next anchor: " + " · ".join("%s (to %s) +%.2f" % (n, t, g) for g, _, n, t in gains[:3])]
    plan = data.get("plan") or {}
    if plan:
        cur = dict(levels); line = ["today %.2fx" % m]
        for horizon in ("week", "month", "quarter"):
            for k, v in (plan.get(horizon) or {}).items():
                assert k in cur, "plan names an unknown criterion: %s" % k
                assert v in LEVELS, "plan level %r for %s" % (v, k)
                assert cur[k] is None or v >= cur[k], "plan lowers %s" % k
                cur[k] = v
            line.append("after the %s %.2fx" % (horizon, score(profile, cur)))
        out += ["", "Projection: " + " → ".join(line)]
    return "\n".join(out)


def selftest():
    for p, prof in MODEL["profiles"].items():
        ids = [c["id"] for c in prof["criteria"]]
        assert sum(c["weight"] for c in prof["criteria"]) == 100, p
        for lv, want in ((0, 0.4), (1, 1.0), (2, 1.7)):
            got = score(p, {i: lv for i in ids})
            assert abs(got - want) < 1e-9, (p, lv, got)
        half = score(p, {i: 0.5 for i in ids}); assert abs(half - 0.7) < 1e-9, half
        na = {i: 1 for i in ids}; na[ids[0]] = None
        assert abs(score(p, na) - 1.0) < 1e-9
        assert abs(sum(weights(p, na).values()) - 100) < 1e-9
        for c in prof["criteria"]:
            assert set(c["levels"]) == {"0", "1", "2"} and set(c["plays"]) == {"week", "month", "quarter"}, c["id"]
        data = {"name": "Test", "scores": {i: {"level": 1, "evidence": ["x"]} for i in ids}, "plan": {"week": {ids[0]: 2}}}
        assert "MULTIPLIER 1.00x" in report(p, data)
        bad = {"name": "Test", "scores": {i: {"level": 1} for i in ids}}
        try:
            report(p, bad); raise SystemExit("evidence rule not enforced")
        except AssertionError:
            pass
    assert [band(x)["step"] for x in (0.4, 0.47, 0.48, 0.7, 0.92, 1.0, 1.08, 1.09, 1.27, 1.47, 1.61, 1.62, 1.7)] == [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9]
    assert sum(b["share"] for b in MODEL["bands"]) == 100 and band(1.0)["name"] == "On the radar"
    print("selftest ok: %s" % ", ".join(MODEL["profiles"]))


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        selftest()
    elif len(sys.argv) == 3 and sys.argv[1] in MODEL["profiles"]:
        print(report(sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))))
    else:
        sys.exit(__doc__)
