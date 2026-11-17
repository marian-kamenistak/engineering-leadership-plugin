#!/usr/bin/env python3
"""Market-value multiplier from the 12 steps.

Usage: multiplier.py <role> <s1> ... <s12> [--base EUR]
  role: em | director | vp | cto
  s1..s12: 0 (missing), 1 (standard for 2026) or 2 (strong), in step order
  --base: your own base salary in EUR a year; default is the Central Europe figure for the role
"""
import json, os, sys

MODEL = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "model.json")))


def multiplier(scores):
    """All 0 -> 0.4, all 1 -> 1.0, all 2 -> 1.7; linear in between on the weighted average."""
    a = sum(st["weight"] * s for st, s in zip(MODEL["steps"], scores)) / 100.0
    return 0.4 + 0.6 * a if a <= 1 else 1.0 + 0.7 * (a - 1)


def main(argv):
    base = None
    if "--base" in argv:
        i = argv.index("--base"); base = float(argv[i + 1]); argv = argv[:i] + argv[i + 2:]
    if len(argv) != 13 or argv[0] not in MODEL["roles"]:
        sys.exit(__doc__)
    role = MODEL["roles"][argv[0]]
    scores = [int(x) for x in argv[1:]]
    if any(s not in (0, 1, 2) for s in scores):
        sys.exit("each score is 0, 1 or 2")
    assert sum(st["weight"] for st in MODEL["steps"]) == 100
    m = multiplier(scores)
    base = base or role["base_eur"]
    print("| # | Step | Weight | Level | Raising it one level adds |")
    print("|---|---|---|---|---|")
    gains = []
    for st, s in zip(MODEL["steps"], scores):
        if s < 2:
            up = scores[:]; up[st["n"] - 1] = s + 1
            g = multiplier(up) - m
        else:
            g = 0.0
        gains.append((g, st))
        print("| %d | %s | %d | %s | %s |" % (st["n"], st["name"], st["weight"], MODEL["levels"][s],
                                              "+%.2f" % g if g else "at the top"))
    print("\nRole: %s. Base: EUR %s a year (%s)" % (role["name"], format(int(base), ","),
                                                   "your figure" if base != role["base_eur"] else "Central Europe default"))
    print("Market value: about EUR %s a year" % format(int(round(base * round(m, 1), -3)), ","))
    print("\nRaise these first:")
    for g, st in sorted(gains, key=lambda x: (-x[0], x[1]["n"]))[:3]:
        if g:
            print("- Step %d, %s (+%.2f): %s" % (st["n"], st["name"], g, st["skip"]))
    # The name is picked from the multiplier as displayed (one decimal), like the salary above.
    bands = MODEL["bands"]
    n = next((i for i, b in enumerate(bands, 1) if round(m, 1) < b["below"]), len(bands))
    print("\nMARKET VALUE MULTIPLIER: %.1fx · %s (%d of %d)" % (m, bands[n - 1]["name"], n, len(bands)))


if __name__ == "__main__":
    main(sys.argv[1:])
