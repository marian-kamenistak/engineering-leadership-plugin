"""One-minute pitch scorer: the counting and the arithmetic, so neither depends on a mood.

  python3 pitch.py stats <pitch.txt> [--seconds N]   word count, time, repeated words, tech words, opener, close
  python3 pitch.py score <scores.json>               total out of 10, the band, the next fixes ranked
  python3 pitch.py --selftest

scores.json:
  {"role": "Engineering Manager",
   "scores": {"outcome":        {"level": 1,   "quote": "we shipped the new booking flow in six weeks"},
              "differentiator": {"level": 0,   "missing": "'I love building teams' fits any of five candidates"},
              "potential":      {"level": 1,   "quote": "now I want to lead a team of my own"},
              "story":          {"level": 1.5, "quote": "one story: the booking flow, then a question"},
              "landing":        {"level": 1,   "quote": "fits in about 60 s; ends on a statement"}}}

Rules the script enforces:
  - five criteria, each 0, 0.5, 1, 1.5 or 2; the total is out of 10;
  - a level above 0 needs a "quote" from the pitch (the words that earned it);
  - level 0 needs a "missing" line (what is not there yet).
"""
import json, re, sys

CRITERIA = [  # order = priority when two fixes are worth the same
    ("outcome", "Outcome, in money"),
    ("differentiator", "Differentiator"),
    ("potential", "Potential"),
    ("story", "One story, hooks in order"),
    ("landing", "Landing: length, value words, closing question"),
]
LEVELS = (0, 0.5, 1, 1.5, 2)
BANDS = [  # (below, name, line)
    (5, "First draft", "The material is there. It does not sell yet."),
    (7, "Getting there", "People listen. They do not ask a question yet."),
    (8, "Almost ready", "One or two fixes from a pitch that makes people ask."),
    (99, "Ready", "Ready for the conversations that matter. Keep it fresh."),
]
WPM_CALM, WPM_FAST = 130, 150  # spoken English, an assumption; a recorded time overrides it

STOP = set("""with that this have from they their them were been which what when where about into also just more than
then there these those would could should because being very your will some over only other after before while each
both here such like make made does done doing much many most even well back really thing things want know think
going need still able across within since every""".split())
TECH = """kubernetes k8s java kotlin python golang rust php javascript typescript react angular vue node nodejs aws azure
gcp microservices microservice monolith docker terraform kafka sql nosql postgres mongodb api apis cicd ci/cd devops
llm llms scala .net c# spring serverless graphql redis elasticsearch spark hadoop kotlin swift ios android flutter""".split()
FILLER = "passionate basically actually really literally synergy synergies journey innovative".split()
MONEY = re.compile(r"[€$£]|\b(eur|euro|euros|usd|dollars?|gbp|pounds|czk|kč|korun|pln|złotych|chf)\b", re.I)
NUMBER = re.compile(r"\d|\b(million|millions|billion|thousand|hundred|percent|half|double|doubled|tripled|twice)\b|%", re.I)
CV_MARKERS = re.compile(r"\b(years of experience|\d+ years in|started as|then moved to|graduated|my career)\b", re.I)


def words_of(text):
    return re.findall(r"[0-9A-Za-zÀ-ž#/.+'’-]*[0-9A-Za-zÀ-ž#+]", text)


def sentences_of(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def stats(text, seconds=None):
    text = text.strip().strip('"“”')
    w = words_of(text)
    n = len(w)
    low, high = n / WPM_FAST * 60, n / WPM_CALM * 60
    out = ["WORDS %d" % n]
    if seconds:
        out.append("TIME %d s as recorded (%.0f words a minute)" % (seconds, n / seconds * 60))
        t_low = t_high = seconds
    else:
        out.append("TIME about %.0f-%.0f s spoken (assumes %d-%d words a minute; a recorded time is better)"
                   % (low, high, WPM_CALM, WPM_FAST))
        t_low, t_high = low, high
    if t_high > 90:
        cut = n - int(90 * (n / t_high))
        out.append("LENGTH over 90 s: cut about %d words to land inside 90 s" % cut)
    elif t_low < 40:
        out.append("LENGTH under 40 s: room for one story or the closing question")
    else:
        out.append("LENGTH fits the 60-90 s window" if t_low >= 55 else "LENGTH short and fine: under a minute leaves room for questions")
    lower = [x.lower().strip("'’-.") for x in w]
    counts = {}
    for x in lower:
        if len(x) >= 4 and x not in STOP and not x.isdigit():
            counts[x] = counts.get(x, 0) + 1
    rep = sorted(((c, x) for x, c in counts.items() if c >= 3), reverse=True)
    out.append("REPEATED " + (", ".join("%s x%d" % (x, c) for c, x in rep) if rep else "none at 3 or more"))
    fill = [x for x in FILLER if x in counts]
    out.append("FILLER " + (", ".join("%s x%d" % (x, counts[x]) for x in fill) if fill else "none"))
    tech = {}
    for x in lower:
        if x in TECH:
            tech[x] = tech.get(x, 0) + 1
    out.append("TECH WORDS %d%s" % (sum(tech.values()), (": " + ", ".join("%s x%d" % (k, v) for k, v in tech.items())) if tech else ""))
    sents = sentences_of(text)
    first = sents[0] if sents else ""
    abbr = [x for x in words_of(first) if re.fullmatch(r"[A-Z]{2,4}s?", x) and x not in ("I", "OK")]
    out.append("OPENER \"%s\"%s" % (first[:120], ("  · abbreviation in the opener: " + ", ".join(abbr)) if abbr else ""))
    cv = sorted(set(m.group(0).lower() for m in CV_MARKERS.finditer(text)))
    out.append("CV MARKERS " + (", ".join(cv) if cv else "none"))
    nums = [s for s in sents if NUMBER.search(s)]
    money = [s for s in sents if MONEY.search(s)]
    out.append("NUMBERS in %d of %d sentences; MONEY in %d%s" % (len(nums), len(sents), len(money),
               (" · first number in sentence %d" % (sents.index(nums[0]) + 1)) if nums else ""))
    last = sents[-1] if sents else ""
    close = "question" if last.endswith("?") else ("thank-you" if re.search(r"thank", last, re.I) else "statement")
    out.append("CLOSE %s: \"%s\"" % (close, last[:120]))
    if sents:
        longest = max(sents, key=lambda s: len(words_of(s)))
        out.append("SENTENCES %d · average %.0f words · longest %d words" % (len(sents), n / len(sents), len(words_of(longest))))
    return "\n".join(out)


def band(total):
    for below, name, line in BANDS:
        if total < below:
            return name, line


def check(data):
    s = data["scores"]
    ids = [i for i, _ in CRITERIA]
    missing = [i for i in ids if i not in s]
    assert not missing, "no score for: %s" % ", ".join(missing)
    extra = [i for i in s if i not in ids]
    assert not extra, "unknown criteria: %s" % ", ".join(extra)
    for i in ids:
        lv = s[i].get("level")
        assert lv in LEVELS, "%s: level %r is not one of %s" % (i, lv, LEVELS)
        if lv > 0:
            assert s[i].get("quote"), "%s: level %s needs a quote from the pitch" % (i, lv)
        else:
            assert s[i].get("missing"), "%s: level 0 needs a 'missing' line" % i


def score(data):
    check(data)
    s = data["scores"]
    total = sum(s[i]["level"] for i, _ in CRITERIA)
    name, line = band(total)
    out = ["PITCH %s/10 · %s. %s" % (("%g" % total), name, line), "",
           "| Criterion | Level (0-2) | Next anchor is worth |", "|---|---|---|"]
    gains = []
    for k, (i, label) in enumerate(CRITERIA):
        lv = s[i]["level"]
        if lv >= 2:
            out.append("| %s | %g | at the top |" % (label, lv))
            continue
        target = 2 if lv >= 1 else 1
        gains.append((target - lv, lv, k, label, target))
        out.append("| %s | %g | to %d: +%g |" % (label, lv, target, target - lv))
    # Largest gain first; on a tie the criterion still at 0 goes first, then the fixed priority order.
    gains.sort(key=lambda g: (-g[0], g[1], g[2]))
    out += ["", "NEXT FIXES " + " · ".join("%s (to %d) +%g" % (lab, t, g) for g, _, _, lab, t in gains[:3])]
    if total < 8:
        need, run = 8 - total, 0
        for n, g in enumerate(gains, 1):
            run += g[0]
            if run >= need:
                extra = [g[3] for g in gains[3:n]]
                out.append("TO 8/10 you need +%g: %s" % (need, "the next fixes above get there" if not extra
                           else "the three fixes above plus " + " and ".join("%s (to %d)" % (g[3], g[4]) for g in gains[3:n])))
                break
        else:
            out.append("TO 8/10 you need +%g: every next anchor together reaches %g/10; the rest needs a second round"
                       " (criteria from 1 to 2)" % (need, total + run))
    mvm = 0 if total < 5 else (1 if total < 8 else 2)
    out.append("MARKET VALUE MULTIPLIER STEP 4 level %d (by design: under 5 -> 0, 5 to 7.5 -> 1, 8 and up -> 2)" % mvm)
    return "\n".join(out)


def selftest():
    def mk(levels):
        return {"scores": {i: ({"level": lv, "quote": "q"} if lv > 0 else {"level": 0, "missing": "m"})
                           for (i, _), lv in zip(CRITERIA, levels)}}
    # Calibration on the two anchors in the notes: "no differentiator, no numbers" lands near 5,
    # "leads with numbers, one story, closing question, one hook too many" lands near 8.
    assert score(mk([0, 0, 2, 1.5, 1.5])).startswith("PITCH 5/10 · Getting there")
    assert score(mk([2, 1.5, 1.5, 1, 2])).startswith("PITCH 8/10 · Ready")
    assert score(mk([0, 0, 0, 0, 0])).startswith("PITCH 0/10 · First draft")
    assert score(mk([2] * 5)).startswith("PITCH 10/10 · Ready")
    assert "NEXT FIXES Outcome, in money (to 1) +1 · Differentiator (to 1) +1" in score(mk([0, 0, 2, 1.5, 1.5]))
    assert "the three fixes above plus Landing: length, value words, closing question (to 2)" in score(mk([0, 0, 2, 1.5, 1.5]))
    assert "NEXT FIXES Outcome, in money (to 1) +1 · Differentiator (to 1) +1 · One story" in score(mk([0, 0, 1, 0, 0.5]))
    assert "every next anchor together reaches 6/10" in score(mk([0, 0, 1, 0, 0.5]))
    for bad in ({"scores": {i: {"level": 1} for i, _ in CRITERIA}}, mk([0.7, 1, 1, 1, 1])):
        try:
            score(bad); raise SystemExit("rule not enforced: %r" % bad)
        except AssertionError:
            pass
    txt = ("Hi, I'm Sam, EM at a fintech. I believe in ownership. Ownership matters. Ownership wins. "
           "We use Kubernetes and Java. We saved EUR 2 million in one year. What would you do?")
    st = stats(txt)
    assert "ownership x3" in st and "kubernetes x1" in st and "abbreviation in the opener: EM" in st, st
    assert "MONEY in 1" in st and "CLOSE question" in st, st
    st2 = stats("I'm a senior engineer, 8 years, Java, Kotlin, Kubernetes, AWS. I am passionate about code.")
    assert "abbreviation in the opener: AWS" in st2 and "REPEATED none" in st2 and "FILLER passionate x1" in st2, st2
    assert "LENGTH under 40 s" in stats(txt)
    assert "LENGTH over 90 s" in stats(" ".join(["word"] * 260))
    assert "TIME 60 s as recorded (130 words a minute)" in stats(" ".join(["word"] * 130), 60)
    print("selftest ok")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]:
        selftest()
    elif len(a) >= 2 and a[0] == "stats":
        sec = int(a[a.index("--seconds") + 1]) if "--seconds" in a else None
        print(stats(open(a[1], encoding="utf-8").read(), sec))
    elif len(a) == 2 and a[0] == "score":
        print(score(json.load(open(a[1], encoding="utf-8"))))
    else:
        sys.exit(__doc__)
