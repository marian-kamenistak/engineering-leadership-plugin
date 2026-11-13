#!/usr/bin/env python3
"""Dated 90-day calendar and day-1 readiness for a new leadership role.

Usage:
  plan.py <role> <start YYYY-MM-DD> [--reports N] [--skip YYYY-MM-DD,...] [--ready id,id,...] [--today YYYY-MM-DD]
  plan.py --selftest

  role     tl | em | director | vp | cto
  start    the first working day in the role
  --reports  lead track: number of direct reports; prints the manager-time line (10 to 15% of your week each)
  --skip   a date inside each week to leave out of the plan (holidays, a planned trip);
           the plan moves one week later for each skipped week
  --ready  ids of the readiness items already in place (see model.json "readiness")
  --today  defaults to the real date; used to say which week the person is in
"""
import datetime as dt
import json, os, sys

MODEL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "model.json")))
D = dt.date


def track_for(role):
    for key, t in MODEL["tracks"].items():
        if role in t["roles"]:
            return key, t
    sys.exit("role must be one of tl, em, director, vp, cto")


def fmt(d):
    return d.strftime("%a %-d %b %Y")


def friday(monday):
    return monday + dt.timedelta(days=4)


def easter(y):
    """Western Easter Sunday (anonymous Gregorian algorithm)."""
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    return D(y, month, (h + l - 7 * m + 114) % 31 + 1)


def manager_time(reports):
    lo, hi = 10 * reports, 15 * reports
    line = "%d direct reports x 10 to 15%% = %d to %d%% of your week for them." % (reports, lo, hi)
    if hi >= 100:
        line += (" At 15%% each, they would need more than your whole week, and at 10%% you keep only %d%%. "
                 "Agree with your manager early which hands-on work goes to someone else." % max(0, 100 - lo))
    else:
        line += " About %d to %d%% is left for everything else, hands-on work included." % (100 - hi, 100 - lo)
    return line


def build(role, start, skip=(), ready=(), today=None, reports=None):
    key, t = track_for(role)
    monday0 = start - dt.timedelta(days=start.weekday())  # week 1 starts the Monday of the start week
    skip_mondays = {s - dt.timedelta(days=s.weekday()) for s in skip}
    rows, m, n = [], monday0, 0
    while n < len(t["weeks"]):
        if m in skip_mondays:
            rows.append((None, m, None))
        else:
            n += 1
            rows.append((t["weeks"][n - 1], m, n))
        m += dt.timedelta(days=7)
    week_monday = {n: mon for w, mon, n in rows if n}
    day90 = start + dt.timedelta(days=89)
    out = {"track": key, "track_name": t["name"], "start": start, "day90": day90, "rows": rows}

    # Holiday weeks a calendar can see: the turn of the year. Everything else the person must tell us.
    out["warn"] = []
    for w, mon, n in rows:
        if n and any(D(y, 12, 24) <= mon + dt.timedelta(days=i) <= D(y + 1, 1, 1)
                     for i in range(5) for y in (mon.year - 1, mon.year)):
            out["warn"].append("Week %d (from %s) falls over the end-of-year holidays. Most people are away: "
                               "consider --skip %s." % (n, fmt(mon), mon.isoformat()))

    for y in {mon.year for _, mon, _ in rows}:
        gf, em = easter(y) - dt.timedelta(days=2), easter(y) + dt.timedelta(days=1)
        hit = [n for w, mon, n in rows if n and (mon <= gf <= friday(mon) or mon <= em <= friday(mon))]
        if hit:
            out["warn"].append("Easter: Good Friday %s and Easter Monday %s fall in week%s %s. Public holidays in many "
                               "countries; ask, and skip or shorten those weeks if they apply."
                               % (fmt(gf), fmt(em), "s" if len(hit) > 1 else "", " and ".join(map(str, hit))))
    out["checkins"] = {k: friday(week_monday[v]) for k, v in t["checkins"].items()}
    if out["checkins"]["day_90"] > day90:
        late = out["checkins"]["day_90"]
        last_fri = day90 - dt.timedelta(days=(day90.weekday() - 4) % 7)
        out["checkins"]["day_90"] = last_fri
        out["warn"].append("Week 12 would end on %s, after day 90 (%s). The close-the-loop meeting moves to %s: "
                           "run weeks 11 and 12 together in that week." % (fmt(late), fmt(day90), fmt(last_fri)))
    out["audit"] = [week_monday[w] for w in t["audit_weeks"]]

    items = []
    for it in MODEL["readiness"]:
        text = it.get("item") or it[key]
        items.append((it["id"], text, it["id"] in ready))
    have = sum(1 for _, _, ok in items if ok)
    name = next(r["name"] for r in MODEL["readiness_names"] if have <= r["max"])
    out.update(items=items, have=have, total=len(items), name=name)
    out["mtime"] = manager_time(reports) if reports else None

    today = today or D.today()
    if today < start:
        out["now"] = "Before day 1: %d days to go." % (start - today).days
    elif today > day90:
        out["now"] = "Past day 90."
    else:
        cur = max((n for w, mon, n in rows if n and mon <= today), default=1)
        out["now"] = "Today is day %d, week %d of the plan." % ((today - start).days + 1, cur)
    return out


def render(o):
    t = MODEL["tracks"][o["track"]]
    print("Track: %s. Start: %s. Day 90: %s." % (o["track_name"], fmt(o["start"]), fmt(o["day90"])))
    print(o["now"])
    if t["before_day_1"]:
        print("\nBefore day 1 (before you sign, if you still can), in this order:")
        for c in t["before_day_1"]:
            print("%d. %s: %s" % (c["n"], c["topic"], c["do"]))
    print("\n| Week | Dates | Month | Focus |")
    print("|---|---|---|---|")
    for w, mon, n in o["rows"]:
        span = "%s to %s" % (max(mon, o["start"]).strftime("%-d %b"), friday(mon).strftime("%-d %b"))
        if not n:
            print("| - | %s | | skipped (holiday or away) |" % span)
        else:
            print("| %d | %s | %d | %s |" % (n, span, (n - 1) // 4 + 1, w["focus"]))
    c = o["checkins"]
    print("\nCheck-ins with your manager:")
    print("- End of month 1: %s" % fmt(c["month_1"]))
    print("- Day 60: %s" % fmt(c["day_60"]))
    print("- Day 90, close the loop: %s" % fmt(c["day_90"]))
    print("\nAudit time: block one to two days a week in the weeks starting %s." %
          ", ".join(m.strftime("%-d %b") for m in o["audit"]))
    for w in o["warn"]:
        print("\nNote: " + w)
    if o["mtime"]:
        print("\nManager time: " + o["mtime"])
    print("\nReady for day 1:")
    for i, text, ok in o["items"]:
        print("- [%s] %s (%s)" % ("x" if ok else " ", text, i))
    print("\nFIRST 90 DAYS: %d of %d in place · %s" % (o["have"], o["total"], o["name"]))


def selftest():
    o = build("em", D(2026, 12, 1), today=D(2026, 11, 13))
    assert o["track"] == "lead" and o["day90"] == D(2027, 2, 28), o["day90"]
    assert o["rows"][0][1] == D(2026, 11, 30) and o["checkins"]["day_90"] == D(2027, 2, 19)
    assert len(o["warn"]) == 2, o["warn"]  # weeks 4 and 5 sit over the holidays
    o = build("em", D(2026, 12, 1), skip=[D(2026, 12, 24), D(2026, 12, 31)])
    assert o["checkins"]["day_90"] == D(2027, 2, 26) and any("after day 90" in w for w in o["warn"])
    o = build("vp", D(2027, 1, 11), ready=["success", "track"], today=D(2027, 1, 20))
    assert easter(2027) == D(2027, 3, 28) and easter(2026) == D(2026, 4, 5)
    assert any("weeks 11 and 12" in w for w in o["warn"]), o["warn"]
    assert o["track"] == "exec" and o["have"] == 2 and o["name"] == "Fresh start"
    assert o["now"].startswith("Today is day 10, week 2"), o["now"]
    o = build("tl", D(2027, 6, 2), ready=[i["id"] for i in MODEL["readiness"]])
    assert o["have"] == 8 and o["name"] == "Ready for day 1" and not o["warn"]
    assert "70 to 105%" in manager_time(7) and "more than your whole week" in manager_time(7) and "keep only 30%" in manager_time(7)
    assert "40 to 60%" in manager_time(4) and "About 40 to 60% is left" in manager_time(4)
    print("selftest ok")


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    opts = {}
    for flag in ("--skip", "--ready", "--today", "--reports"):
        if flag in argv:
            i = argv.index(flag); opts[flag] = argv[i + 1]; argv = argv[:i] + argv[i + 2:]
    if len(argv) != 2:
        sys.exit(__doc__)
    ids = {i["id"] for i in MODEL["readiness"]}
    ready = [x for x in opts.get("--ready", "").split(",") if x]
    bad = [x for x in ready if x not in ids]
    if bad:
        sys.exit("unknown readiness id(s): %s. Use: %s" % (", ".join(bad), ", ".join(sorted(ids))))
    skip = [D.fromisoformat(x) for x in opts.get("--skip", "").split(",") if x]
    today = D.fromisoformat(opts["--today"]) if "--today" in opts else None
    reports = int(opts["--reports"]) if "--reports" in opts else None
    render(build(argv[0], D.fromisoformat(argv[1]), skip, ready, today, reports))


if __name__ == "__main__":
    main(sys.argv[1:])
