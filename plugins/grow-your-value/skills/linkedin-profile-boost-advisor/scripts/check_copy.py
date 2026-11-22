#!/usr/bin/env python3
"""Check new LinkedIn copy before it goes in the report.

Usage: python3 check_copy.py <copy.md> [--title "CTO"] [--keywords "a,b,c"]
       python3 check_copy.py --selftest

Input file: markdown with H2 sections. Recognised names (case-insensitive):
  ## Headline          one line
  ## About             free text
  ## Experience: <co>  bullets starting with "- "
  ## Post <n>          free text
Each bullet with a digit needs a tag [src: <where the number comes from>].
Tags are removed before lengths are counted. [needs number] marks a question to the owner.
Exit code 1 if any FAIL. Python 3 standard library only.
"""
import re
import sys

# Limits reported for 2026; see references/section-playbook.md. Confirm on LinkedIn before quoting.
LIMITS = {"headline": 220, "about": 2600, "experience": 2000, "post": 3000}
HOOK = 200  # characters shown before "see more" (about 200 to 300 on mobile/desktop; use the smaller)
HEAD_VISIBLE = 70  # characters of the headline visible in search results

BANNED = [
    "leverage", "unlock", "empower", "spearhead", "seamless", "robust", "cutting-edge",
    "game-chang", "synergy", "innovative", "transformative", "results-driven", "visionary",
    "passionate about", "proven track record", "i'm thrilled", "i am thrilled",
    "fast-paced world", "responsible for", "dynamic",
]
CONTRAST = re.compile(r"\b(it'?s|it is|this is) not (about )?[^.]{1,60}[,.;] ?(it'?s|it is|but)\b", re.I)
TRIPLE = re.compile(r"\b[a-z]+(?:-[a-z]+)?, [a-z]+(?:-[a-z]+)?,? and [a-z]+(?:-[a-z]+)?\b", re.I)
DASH = re.compile(r"[—–]| - ")
TAG = re.compile(r"\s*\[src:[^\]]*\]")
NUM = re.compile(r"\d[\d,.]*\s?(?:%|k|m|bn|x|\+)?", re.I)


def sections(text):
    out, name, buf = [], None, []
    for line in text.splitlines():
        m = re.match(r"##\s+(.*)", line)
        if m:
            if name is not None:
                out.append((name, "\n".join(buf).strip()))
            name, buf = m.group(1).strip(), []
        elif name is not None:
            buf.append(line)
    if name is not None:
        out.append((name, "\n".join(buf).strip()))
    return out


def kind(name):
    n = name.lower()
    for k in ("headline", "about", "experience", "post"):
        if n.startswith(k):
            return k
    return None


def check(text, title="", keywords=()):
    fails, warns, secs = [], [], sections(text)
    seen = {kind(n) for n, _ in secs}
    for need in ("headline", "about", "experience"):
        if need not in seen:
            fails.append(f"missing section: {need}")
    all_clean = ""
    for name, body in secs:
        k = kind(name)
        if not k:
            continue
        clean = TAG.sub("", body)
        all_clean += "\n" + clean
        low = clean.lower()
        if len(clean) > LIMITS[k]:
            fails.append(f"{name}: {len(clean)} characters, limit {LIMITS[k]}")
        for w in BANNED:
            if w in low:
                fails.append(f"{name}: banned phrase '{w}'")
        if CONTRAST.search(clean):
            warns.append(f"{name}: 'not X but Y' contrast, check by reading")
        if k in ("about", "experience", "post") and TRIPLE.search(clean):
            warns.append(f"{name}: list of three, fine for tools, rewrite if abstract")
        dashes = len(DASH.findall(clean))
        if k == "headline" and dashes:
            warns.append(f"{name}: dash in headline, use | or a comma")
        if k in ("about", "post") and dashes > 1:
            fails.append(f"{name}: {dashes} dashes, keep at most one")
        if "[needs number]" in body:
            warns.append(f"{name}: open question [needs number] for the owner")
        if k == "headline":
            if title and title.lower() not in clean[:HEAD_VISIBLE].lower():
                fails.append(f"{name}: '{title}' not in first {HEAD_VISIBLE} characters")
            if "\n" in clean:
                fails.append(f"{name}: more than one line")
        if k == "about":
            hook = clean[:HOOK].lower()
            if re.match(r"\s*(i am|i'm) (a |an )?(passionate|experienced|results)", hook):
                fails.append(f"{name}: hook opens with a self-label")
            if "?" in clean[:HOOK]:
                warns.append(f"{name}: question in the hook")
        if k == "experience":
            bullets = [l[2:].strip() for l in body.splitlines() if l.startswith("- ")]
            if not bullets:
                fails.append(f"{name}: no bullets")
            for b in bullets:
                has_src = "[src:" in b
                nums = NUM.findall(TAG.sub("", b))
                if nums and not has_src:
                    fails.append(f"{name}: number without [src: ...]: {b[:60]}")
                if len(nums) > 2:
                    warns.append(f"{name}: {len(nums)} numbers in one bullet: {b[:60]}")
                if re.match(r"(led|managed|responsible|spearheaded|worked)\b", b, re.I):
                    warns.append(f"{name}: bullet opens with an output verb: {b[:60]}")
    low_all = all_clean.lower()
    for kw in [k.strip() for k in keywords if k.strip()]:
        if kw.lower() not in low_all:
            warns.append(f"keyword not in any section: {kw}")
    return fails, warns


def report(fails, warns):
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print(f"{len(fails)} FAIL, {len(warns)} WARN")
    return 1 if fails else 0


def selftest():
    good = ("## Headline\nCTO | Health apps | Grew the team from 3 to 12\n\n## About\n"
            "I help small teams ship. At one startup, releases went from monthly to weekly.\n\n"
            "## Experience: Acme\n- Cut release time from 3 weeks to 2 days [src: owner said]\n")
    bad = ("## Headline\nPassionate leader - CTO\n\n## About\nI'm passionate about leverage — and more — really.\n\n"
           "## Experience: Acme\n- Led a team and raised 5 million\n")
    f, w = check(good, title="CTO", keywords=["releases"])
    assert not f, f
    f, w = check(bad, title="CTO")
    assert len(f) >= 4, f
    assert any("without [src" in x for x in f), f
    print("selftest ok")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        sys.exit(selftest())
    if not a or a[0].startswith("--"):
        print(__doc__)
        sys.exit(2)
    title = a[a.index("--title") + 1] if "--title" in a else ""
    kws = a[a.index("--keywords") + 1].split(",") if "--keywords" in a else []
    try:
        text = open(a[0], encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {a[0]}: {e}")
        sys.exit(2)
    sys.exit(report(*check(text, title, kws)))
