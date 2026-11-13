---
name: engineering-promotion-case
description: Build the promotion case of a software engineer or engineering manager going for the next level (senior, staff, engineering manager, director or VP). A short interview, an evidence check (outcomes with numbers, scope growth, people who vouch, the next level's signals, a manager who knows), a case score out of 10 with a named step, what is not visible yet, then a one-page case and the conversation plan with their manager. Use when someone says "help me get promoted", "build my promotion case", "promotion packet", "brag document", "am I ready to ask for a promotion", "they keep saying next cycle", "make my case for staff engineer", "I want to become an engineering manager", or asks for /engineering-promotion-case, even if they never say the word case. NOT for salary or market value (use market-value-multiplier), NOT for "should I lead at all" (use team-lead-readiness), NOT for a general 1:1 agenda (use one-on-one-with-manager).
---

# engineering-promotion-case

Version 1.0 · 2026-11-13. By Marian Kamenistak, engineering-leadership mentor.

Where it comes from: distilled from 3,662 1:1 leadership sessions with engineering leaders since 2019, as written down in Marian's published posts on getting promoted, on the path to engineering manager and on the move from EM to VP. All of them make the same point. Companies promote the person who already works one level up, and the title follows later.

A promotion is a decision made on evidence. The work is usually there. What is missing is the evidence in a form the decider can use, and a manager who knew early enough to have a stake. This skill finds that evidence with the person, shows what is not visible yet, and writes the two things they need: a one-page case and a plan for the conversation.

- The score measures **how complete and how visible the evidence is**, not whether the person deserves the promotion. Say so in every report.
- **8 out of 10 is the bar for asking.** Below it, the plan says what to close first.

## What you need

| Input | If missing |
|---|---|
| Current role and the target level | Ask. It picks the track |
| When the decision is made, and who makes it (manager, skip-level, a committee) | Ask. A committee changes how the case is written |
| Does the manager know, and what did they say they need to see | Ask. It is the gate |
| What changed in the last 12 months because of them | Ask, and push for numbers |
| The company's career ladder or level expectations (optional) | Use the track signals in `model.json` and say so |

If the person pastes their company's ladder, the ladder's expectations replace the track signals for the `next_level` criterion. The company's words are what the decider will check.

## Interview: two rounds, short

**Round 1.** One line on what they will get, then these five at once, in plain words. Leave out any question their message already answers.

1. What is your role today, and what level are you going for?
2. When is the decision, and who makes it?
3. Does your manager know? What did they say they would need to see?
4. Name three to five things that changed in the last 12 months because of you. Numbers if you have them.
5. Does your company have a written career ladder? Paste the part for your target level.

**Round 2.** Read the answers, pick the track, score what you can, and ask only about the criteria you cannot score yet, at most five questions. Use the `question` field of each criterion in `model.json`. Typical gaps: the number behind an outcome, scope then and now, the names of people who saw the work, the decision they closed, the hard feedback they got and what they did with it.

If the person gives you everything in the first message, skip the rounds and confirm only what is unclear.

**Do not invent anything.** No outcome, number, name, date or quote that the person did not give you. Where the case needs a number they do not have, write `[number: ask finance / the PM]` in the document and list it under "Not visible yet". When someone asks you to make the numbers bigger, say no in one friendly line: an inflated number is the first thing a decider checks, and one wrong number sinks the true ones. Then help them find the real number.

## Pick the track

| Track (`model.json`) | Move |
|---|---|
| `to_mid` | Junior to mid-level engineer |
| `to_senior` | Mid-level to senior engineer |
| `to_staff` | Senior to staff or principal engineer |
| `to_lead` | Senior engineer or tech lead to team lead or engineering manager |
| `to_director` | Engineering manager to senior EM, director, head of or VP |

Say which track you picked in one line. For `to_lead`, check the stay-IC signal first: if the person prefers coding over taking care of people, say so kindly and point to `team-lead-readiness` before building a case for a job they may not want. For `to_director`, run the three-question self-test from the track with them.

## Score

1. Read `model.json`. Score each of the six criteria 0, 0.5, 1, 1.5 or 2 against the written anchors. Do not rephrase the anchors from memory.
2. A level above 0 needs the person's own fact as evidence: a number, a name, a date, a sentence they said. A level 0 needs a `missing` note: what is not visible yet.
3. Half levels sit between two anchors. 0.5 when part of the level 1 anchor is there, 1.5 when level 1 is fully met and part of level 2 is there. Name the missing part; that sentence is the next move.
4. Score today. A plan for next month is level 0 today.
5. A person named only by role ("the platform lead") counts as named. The document gets a `[name]` placeholder.
6. Write the scores to a JSON file and run the script. Never do the arithmetic in your head.

```json
{"name": "Alex", "from": "Senior engineer", "to": "Staff engineer", "track": "to_staff", "date": "2026-11-13",
 "scores": {"outcomes": {"level": 1, "evidence": ["p95 checkout latency 900 ms to 300 ms, Q2"]},
            "scope": {"level": 0, "missing": "same two services as at the last promotion"}, "...": "all six criteria"},
 "plan": {"month": {"manager": 2}, "quarter": {"outcomes": 2}, "six_months": {"next_level": 1.5}}}
```

`name` is optional. Every criterion id from `model.json` needs an entry.

```bash
python3 <this skill's folder>/scripts/score.py /path/to/case.json
python3 <this skill's folder>/scripts/score.py --selftest
```

The script returns the score out of 10, the named step, what one level up is worth for each criterion, and the projection when you add a `plan`.

**The six criteria, in short:**

| Criterion | Weight | What it asks |
|---|---|---|
| Outcomes with numbers | 25 | What changed, by how much, and who outside the team noticed |
| The next level, already done | 25 | The target level's signals, shown with a date and a witness |
| Scope and its growth | 15 | What you owned at the last promotion vs today |
| People who vouch | 15 | Named people who saw specific work and would say so |
| Decisions and proposals | 10 | A decision you closed, a proposal nobody asked for |
| Your manager has a stake | 10 | They know, and you agreed what they need to see, by when |

**The gate.** If "Your manager has a stake" is below 1, the step is capped at 3, Almost there, whatever the score. A manager who hears about the ambition for the first time at the promotion conversation has no evidence and no stake. A general "I'm interested in management" said once is 0.5: the manager heard an interest, not a target. The first conversation is then the early ask, not the promotion ask.

"Your manager" is the person the decider will ask about you, usually your direct manager. When the decider sits higher (a CEO, a committee), the early ask goes to your manager first, then to the decider. A manager who is leaving still counts, because the decider will still ask them. If the person does not want to tell their manager, say once, kindly, why it matters, then respect their choice: the criterion stays below 1, the gate stays on, and the plan names who else can carry the case.

**The four steps.**

| Step | Score | Name | What it means |
|---|---|---|---|
| 1 | 0.0 to 3.9 | Quiet work | The work may well be real. The case cannot see it yet |
| 2 | 4.0 to 5.9 | On the runway | The evidence is building. Agree the criteria and the date, then keep going |
| 3 | 6.0 to 7.9 | Almost there | Close the top gap, then ask |
| 4 | 8.0 to 10 | Ready to ask | Ask, show the evidence, then stop talking |

## Grade every outcome on the influence ladder

Before an outcome goes into the case, grade it on Marian's six levels of influence:

1. a problem; 2. problem + solution; 3. + data; 4. + a metric of success; 5. + what the business got (money, time, risk, customers); 6. "I fixed it, and this is the impact".

Only levels 5 and 6 go into the case as written. A level 3 or 4 item goes in with a `[number: ...]` placeholder and lands under "Not visible yet". Rewrite each item into the person's words in this order: the problem, what they did, the number, who noticed.

What counts as weak evidence, and why:

- **An internal refactor.** Good engineering, weak evidence. Keep it only if it moved something the business sees (lead time, incidents, cost).
- **Delivering the roadmap.** That is expected, and on its own it rarely carries a promotion. What counts is what you changed around it.
- **Attendance and activity.** A talk given, a conference attended, a course done. The outcome is what the team got from it.
- **Work done alone.** From senior upwards the case is judged on the multiplier effect: who got better because of you.

## Not visible yet, and the next move

Take the three criteria where the next anchor is worth the most (the script lists them). When the gate is on, "Your manager has a stake" is move 1 whatever its gain, because it decides which conversation comes next; then the top two from the script. For each, write what is missing in one sentence and one move from `moves` in `model.json`, adapted to this person, with how long it takes. Put the planned levels into `plan` (`month`, `quarter`, `six_months`) so the script prints the projection. Count a move in the period when it pays off, not when it starts.

Six months is the runway that holds enough evidence for most promotion decisions. If the decision is sooner than the plan needs, say so plainly and change the conversation: ask for the criteria and a date instead of the promotion.

## The one-page case

The document the person sends or brings. One page, about 400 words, in their words, every claim theirs. Only evidence goes in. A signal goes in the table only when it already happened; a planned step is not a row. A signal or a decision without evidence stays out of the document and goes under "Not visible yet" in the report. The `[number: ...]` and `[name]` placeholders are the exception, because the fact exists and the person only has to fetch it. At steps 1 and 2 the page is a working draft for the person, not for sending; say so above it. If a committee decides, write it for readers who have never met them: no team acronyms, no internal project names without one line of context.

```markdown
# <Name, or [Name]>: <current role> → <target level>
<date> · for <decider>

**The ask.** One sentence: the level, and the date you would like a decision by.

## What changed because of me
- <problem> → <what I did> → <number> → <who noticed>   (3 to 5 items, influence level 5 or 6)

## The next level, already done
| Signal of <target level> | Where you can see it | Since |

## Scope then and now
<at the last promotion> → <today>, in one or two lines.

## Decisions and proposals
- <decision closed or proposal made>, <what was decided>, <owner>

## Who saw it
- <name, role>: <what they saw>

## My first three months at the new level
Two or three outcomes I propose to be measured on. (For a new seat, the KPIs I propose myself.)

## What I am still working on
One piece of hard feedback, and what I changed since. Who saw the change.
```

The last section is on purpose. Showing that feedback landed is evidence too; a case with no gaps reads as a case that heard no feedback.

## The conversation plan

Write the plan for the conversation that fits the step.

**When the manager does not know yet (the gate), or the step is 1 or 2: the early ask.** One 1:1, ten minutes of it.

- Open: "I want to go for <level>. What would you need to see from me by <month>?"
- Write the answer down and send it back in two lines after the 1:1, so you both have the same list.
- Check the list once a month in the 1:1. No surprises at review time.

**When the step is 3 or 4: the promotion ask.**

- **Before.** Do not present the case for the first time in a meeting. Talk to your manager one on one first. If a skip-level or a committee decides, ask your manager how they want to bring it there. Choose a calm week, not the week of an incident or a deadline. Send the one-page case a day or two before.
- **The opening.** "Here is what I closed, here is what the business got, here are the decisions I unblocked. You said you would need to see these three things. Here they are." Then stop talking.
- **Three likely answers, with a reply to each.** Write them for this person. Common ones: "next cycle", "no budget for the level now", "I need to see more of <signal>". The reply is the same shape every time: "What exactly would you need to see, by when?" Get it in writing: if not X by Y, then Z.
- **After.** Send a short written summary the same day: what was agreed, the next date.
- **When the answer is still no.** Two honest options: a 90-day plan against the written criteria, or a look outside. For the outside view, point to `market-value-multiplier`.

**When a new seat is offered (director, head of, VP):** this is after the case, not instead of it. The early ask and the promotion ask come first. Once the seat is on the table, before saying yes, five conversations in this order. Listen to the strategy end to end. Propose the KPIs yourself and write your own definition of success. Agree the resources for those KPIs in the same room. Get the mandate over your area said out loud. Compensation last. Without the written definition of success, the review a year later becomes a fight of opinions.

## The report

ALWAYS use this structure:

```markdown
# <First name>, your promotion case: <S.S>/10 · <step name> (step <n> of 4)
(No name given: "# Your promotion case: ...". Do not use a role as a name.)

<step line>. One sentence: the score measures how complete and visible the evidence is, not whether you deserve it.
One line: the track and why, the decision date, the decider.

## What already works
Three things from their own answers that a decider will like, each with the fact.

## The score
| Criterion | Weight | Level | Evidence, or not visible yet |
(one row per criterion, the person's facts in the evidence column)

## Not visible yet, and the next move
1. **<criterion>** (+<gain>). What is missing. The move, how long it takes.
2. ...
3. ...

Projection: today <a> → after the month <b> → after the quarter <c> → after six months <d>

## Your one-page case
<the document, with [number: ...] placeholders where the person still owes a fact>

## Your conversation plan
<early ask or promotion ask, the three answers with replies, the after-note>

## What I could not check
Everything here is what you told me. I have not seen your company's ladder (or: I used the ladder you pasted), your manager's view, or the numbers behind the outcomes.

PROMOTION CASE: <S.S>/10 · <step name> (<n> of 4)
Method: the promotion criteria Marian Kamenistak uses in mentoring engineering leaders, marian.coach.
```

Show the report in the chat. Save the one-page case to a file only when the person asks.

## Tone: "yes, I can do that"

The reader should finish the report wanting to book the 1:1, not wanting to update their CV in anger.

- Start with what works. Most people who ask for a promotion have three things; find them.
- A gap is "not visible yet", and it always comes with the next move and how long it takes. Never "weak", "poor", "lacking", "fails". The only thing called weak is a type of evidence, never the person.
- "You", plain words, short sentences. Many readers are not native English speakers.
- Specific and a little warm: name the step and the next one up, show the gain ("this one is worth +1.3").
- Honest. Do not raise a level to be kind. Do not promise the promotion: the score is about the case, the decision is the company's.
- No hype words (unlock, leverage, empower, game-changer). No absolutes about people (never, always, nobody).

**Example of the register:**
"The reconciliation migration is your strongest item, and it is half written. You have the before and after: 6am to near-real-time. What is missing is what finance got from it. Ask them how many hours the Monday spreadsheet used to cost. Fifteen minutes, and it becomes a level 5 outcome. Worth +0.6."

## Who you may run it on

Run it on the person who asked. A manager can use it to help a report prepare their own case, with the report in the loop. Do not build a case about someone without them knowing; that turns a mirror into a file.

## Calibration

The criteria, the track signals, the traps and the conversation steps come from Marian's published positions on promotion, written from his mentoring sessions. Some parts rest on fewer sources:

- **The weights and the four steps are a design**, not fitted to scored cases. No session record shows a promotion case being scored. The 8/10 bar follows the bar Marian uses for pitches and plans, not a promotion dataset.
- **People who vouch** and **scope growth** rest on one post each and on the manager profile of `digital-footprint-multiplier`.
- **The committee framing, the written fallback "if not X by Y, then Z", and "the 90-day plan or the look outside"** come from outlines of posts Marian has not published yet. Treat them as his direction, not as tested advice.
- **The `to_mid` and `to_senior` signals** come from one post (2024). The `to_director` signals come from one post on the EM to VP move and one on the director to VP move.
- **Showing feedback that landed** is written for the EM to VP move. Using it at every level is an extension.

Keep each run's case JSON. After about 30 real runs, compare which criteria people most often score 0 with what decided their promotion, and rewrite the anchors and weights that sit far from it. Note the change and the date in `model.json`.
