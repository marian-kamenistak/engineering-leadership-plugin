---
name: first-90-days-leadership
description: Build a dated 30/60/90-day plan for someone starting a new engineering leadership role (team lead, engineering manager, director, VP of Engineering or CTO), after a new hire or an internal promotion: a week-by-week calendar, the first conversations and what to listen for, the one early win, what not to change in month one, the check-in scripts for their manager, and a day-1 readiness count. Use when someone says "I start as engineering manager next month", "I just got promoted to team lead", "first 90 days", "30-60-90 day plan", "what should I do in my first week as EM", "I'm the new VP of Engineering", "new CTO", "my probation ends in three months", "how do I take over a team", or asks for /first-90-days-leadership, even if they never say 90 days. NOT for deciding whether to take the role or what to ask for in pay (use market-value-multiplier), and NOT for preparing a single 1:1 agenda (use one-on-one-with-manager).
---

# first-90-days-leadership

Version 1.0 · 2026-11-13. By Marian Kamenistak, engineering-leadership mentor.

Where it comes from: the plan is distilled from 3,662 1:1 leadership sessions with engineering leaders since 2019, and from the 30-60-90 playbook Marian first gave as a talk at an Engineering Leaders meetup. Most new leads who lose the seat lose it over communication and relationships, not over technical skill: relationships they started too late, and changes they made too early.

A new leadership role comes with a clock. Around day 90 your manager decides if the hire was right, and often the probation period ends the same week. This skill turns the first three months into a contract you can keep:

> **In three months, I'll embrace the new team, complete an internal audit, and present my battle plan.**

- **Month 1:** understand and support the team. Relationships before tickets.
- **Month 2:** improve how the team performs. Audit first, then one small change.
- **Month 3:** present what you found and what you propose, and check the value you add.

The week-by-week content for both tracks, the readiness items and the published team-health targets are in `model.json` beside this file. Read it before you build a plan; don't rephrase the week lines from memory. The dates and the arithmetic come from `scripts/plan.py`.

## What you need

| # | Question | Why it matters | Example answer |
|---|---|---|---|
| 1 | Your role, and is it your first time at this level? | Picks the track and the traps | "EM, first time managing" |
| 2 | Start date (or the day you started) | Every week in the plan gets a date | "1 March 2027" |
| 3 | New company or internal promotion? | Changes week 1 completely | "Promoted inside my own team" |
| 4 | The team: how many direct reports, any managers under you, anything you already know about the people | Manager time, first 1:1s, the hard conversation | "6 engineers, one applied for my role" |
| 5 | What you were hired to fix, in the words of the person who hired you | Becomes the definition of success | "Predictable releases" |
| 6 | Who you report to, and how long they've been in their seat | Shapes every check-in | "The CTO, 3 years in" |
| 7 | What you inherit: open problems, broken things, promises made before you | Feeds what to listen for and the early win | "A migration half done" |
| 8 | Company stage: growing fast, consolidating (cost, efficiency), or in a turnaround | Decides which audit numbers weigh most | "Consolidating after layoffs" |

Director, VP and CTO only: **have you signed yet?** If not, the plan starts before day 1.

Last, the eight readiness items from `model.json` as a short checklist in plain words, without the ids: "Which of these are already in place?" Planned leave in the next three months goes with question 2.

**How to ask.** If the message already answers a question, don't ask it again; ask the half that's missing. Ask the rest once, in one message, numbered, each with its example, so the person can answer in two minutes. On a questions-only turn, don't run the script yet. If they say "just give me something", build the plan and mark each guess as *assumed*. Never invent a fact about their team, their numbers or their company; a gap is "not known yet" with the person and the week to ask. A readiness item they didn't mention counts as not in place, and the report says so in one line.

## Pick the track

| Role | Track | Shape |
|---|---|---|
| Team lead, engineering manager | `lead` | The 12-week contract above. Two catch-ups a week with your manager in month 1, audit in weeks 5 to 10, presentation in week 10, close the loop in week 12 |
| Director, VP, CTO | `exec` | Five conversations before day 1, two months of listening, a costed proposal around day 60 to 75. Big changes start next quarter, after the proposal is agreed |

A head of engineering with managers under them is `exec`. A director with only engineers under them is `lead`; say which one you picked and why, in one line.

Then apply what fits:

- **Internal promotion.** The relationships exist, in the old shape. Week 1 is about telling each person what changes now and what stays. The most common first-90-days mistake Marian sees in new managers is being too friendly. Hold the first hard conversation early, in month one if there is one to have: "You're allowed to be warm. Being one of the gang is over."
- **First time at this level.** Name the coding trap: each direct report needs 10 to 15% of your week, so the script shows how much time is left for hands-on work. Of leadership, processes and delivery, pick the two that matter for this role and say them to your manager. Ask for a weekly informal chat, a buddy or a mentor.
- **Someone wanted your job.** That person gets the first 1:1 in week 1, in private. Say it plainly, then ask what they want to grow into.
- **Exec, already signed.** Compensation is done. Run the first four conversations (strategy, KPIs, resources, mandate) with your manager in weeks 1 and 2.
- **Exec, not signed.** The five conversations come before the signature, in order. "Once you have said yes, you have nothing left to trade."
- **Your manager is new too.** Write the definition of success together in week 1; you are both learning the company.
- **Two bosses.** When the person who set the expectation ("engineering is broken") isn't the person you report to, or a predecessor stays above you, both are in the KPI and mandate conversations. Check-ins go to your manager; the other person joins the day-90 decision, walked one by one first.

## Run the calendar

```bash
python3 <this skill's folder>/scripts/plan.py <role> <start YYYY-MM-DD> [--reports N] [--skip YYYY-MM-DD,...] [--ready id,id,...]
python3 <this skill's folder>/scripts/plan.py --selftest
```

`role` is `tl`, `em`, `director`, `vp` or `cto`. `--reports` (lead track only) adds the manager-time line. `--skip` takes one date inside each week the person is away (holidays, a trip); the plan moves one week later for each. The script warns about the end-of-year weeks and Easter; ask about other local holidays and planned leave. If the person can't answer, assume the warned weeks are off, skip them, and give the unskipped day-90 date as the fallback. `--ready` takes the readiness ids already in place (`success`, `manager`, `people`, `one_on_ones`, `audit`, `day90`, `support`, `track`). Score what is true today: "I'll book it next week" is not in place.

The script prints the dated weeks, the three check-in dates, the audit weeks, any warnings, the manager-time line and the readiness count. Use its dates as they are, including a moved day-90 meeting when skipped weeks push week 12 past day 90. Never compute a date or a percentage in your head; picking a day inside a week the script printed ("Tuesday of week 1") is fine.

## Build each part

**1. The contract and the definition of success.** Rewrite the contract sentence with their team and their problem. Then draft the definition of success at 3 and 6 months from question 5, with both sides: delivery ("are we delivering?") and discovery ("are we on the right scope?"). Use their words. Where a number is missing, write "baseline from the week-6 audit", never a target you made up. This draft goes to their manager in week 1.

**2. First conversations.** A table, in order, with a date from the script: who, the question to ask, what to listen for. Lead track: the manager first, then each direct report, the product counterpart, peers, one or two customers in week 2. Exec track: manager, peers, reports, skip-levels, twenty to thirty in total. Ask every peer the same question: "What would make me a success from your side?" Write the answers down; they become the relationship list.

**3. What to listen for.** A table of signals to expect given what they inherit: what they might hear, what it can mean, where the audit checks it. The audit always covers the same five areas:

| Area | You might hear | Check in the audit |
|---|---|---|
| Time on the roadmap | "We're always firefighting" | Share of the last three sprints spent on roadmap vs business-as-usual. Marian's published target: 60% or more |
| Backlog | "Nobody looks at the backlog" | Size, age, how many items are marked high priority |
| Stalled delivery | "Releases are scary" | Who owns release confidence today: the developers, QA, or nobody |
| Roadmap visibility | "Sales decides what we build" | Whether the team can show its roadmap on one page |
| People | Silence in ceremonies, one name in every answer | Underperformance, a knowledge bottleneck, a strained stakeholder |

The company stage sets how much each area weighs. Growing: speed and hiring. Consolidating: predictability, cost, and keeping the key people. Turnaround: stalled delivery and release confidence first. (The stage rule is Marian's; this mapping is this skill's design.)

**4. The one early win (week 7).** One candidate, picked from their inheritance, with the line "confirm after the week-6 audit". It's small, inside what their own team controls (if another team owns the system, the slice on their side of it), the team feels it within two weeks, and it needs nobody's budget. When they know nothing yet about what they inherit, the candidate is the smallest slice of the problem named most often in the first conversations. Marian's examples: a two-level code review, a fixed pipeline, one people issue. When the obvious problem is big (a release that fails every third time), the win is its smallest slice: the single most frequent cause, not the whole pipeline. One change per person at a time, and not the thing the manager will judge the whole quarter on.

**5. Not in month one.** A short list, specific to what they inherit. The defaults: no reorg, no new process or methodology, no backlog purge before the audit, no tool migration, no reversing the predecessor's decisions in public. Exec adds no platform migration and no vision speech. Asking hard questions about the roadmap in week 3 is allowed; that's not a change. "Don't be the person making changes in the first week to assert your authority."

**6. Check-ins with the manager.** Three scripts with the script's dates, in their words:

- **End of month 1 (lead):** "I've started building relationships, I've gotten to know our customers, I understand the product strategy and its purpose, and I've created a team charter." Then ask for feedback.
- **End of month 1 (exec):** what you heard, the four problems that came up most, no solutions yet.
- **Day 60:** the audit draft, the early win and how it landed, the two areas you'll propose. Ask what you are missing.
- **Day 90:** "Here's what I've discovered, why these priorities matter, and the proposal I recommend. Are you on board?" Walk the decision makers one by one before the meeting and send a pre-read. Lead with the payoff, then the dip, and bring any cut as options. Afterwards they ask themselves: "Am I adding value to my team?"

**7. Ready on day 1.** The eight items from `model.json` with the script's count. Each missing item is "not in place yet" with one action they can finish this week.

## The report

ALWAYS use this structure:

```markdown
# Your first 90 days: <role>, <team in a few words>, from <start date>

<the contract sentence, in their words>
Track: <lead | exec>, because <one line>. <internal promotion / first time / signed: one line each that applies>

## Before day 1 (exec, or when the start is still ahead)
<the five conversations, or the three things to do this week>

## Your definition of success (agree it with <manager> in week 1; exec not signed: before you sign)
- At 3 months: ...
- At 6 months: ...

## The calendar
<the script's table, plus one line per week on what that week means for them>

## First conversations
| When | Who | Ask | Listen for |

## What to listen for
| You might hear | It can mean | Check it with |

## The one early win
<candidate, why it fits the four rules, "confirm after the week-6 audit">

## Not in month one
- ...

## Check-ins with <manager>
**<date>, end of month 1:** <script>
**<date>, day 60:** <script>
**<date>, day 90:** <script>

## Not known yet
- <each open fact: who to ask, by which week>

## Ready on day 1: <n> of 8
| Item | In place | Next action this week |

FIRST 90 DAYS: <n> of 8 in place · <readiness name from the script>

The method comes from Marian Kamenistak's mentoring practice (marian.coach).
```

Rules for the report:

- **Their facts, their words.** Every name, number and problem comes from the conversation. Where the plan needs a number they don't have, the plan says where it will come from.
- **Targets are Marian's published ones or the person's own baseline.** The four published team-health targets are in `model.json`; name them as his targets, not as an industry standard.
- **One win, two priorities.** One early win in week 7; two areas in the week-10 presentation. Exec: three to five costed changes, grouped into two or three mission streams. Ten ideas is a backlog, not a plan.
- **Dates from the script.** If the person is already in week 5, say so, mark weeks 1 to 4 as catch-up and keep the rest.
- **End with the `FIRST 90 DAYS: n of 8 in place · <name>` line**, then the one source line, nothing else.

## Tone: "yes, I can do that"

The reader should finish the plan wanting to open their calendar. Start the calendar with the step they can take today. A gap is "not in place yet" plus the action and how long it takes. Never "weak", "poor", "failing". Plain words, short sentences, "you"; many readers are not native English speakers. No hype words, no absolutes about people. Be honest about the hard part: if they were hired to fix delivery and want to show impact fast, say plainly that month one is still for listening, and give them the week-3 question that shows they're working on it.

## Common mistakes to watch for in their answers

| They say | What to name | The rule |
|---|---|---|
| "I want to show impact fast" | Changes in month one to assert authority | "Chill out. Don't make drastic changes in your first month." |
| "My boss wants my reorg plan in week 2" | A change before you know the org | Trade it for a date: the listening plan in week 2, the proposal in week 10 or 11. Agree the trade before you sign |
| "The roadmap is fixed, I'll make it work" | Saying yes and hoping for a miracle | "How can we accomplish XYZ within this timeframe?" |
| "I'll do the 1:1s once things calm down" | Relationships started too late | "Waiting two months is too late; it sends the message that you prioritize the delivery pipeline over people." |
| "I'll keep coding most of the week" | The coding trap | Each report needs 10 to 15% of your week |
| "The team are my friends" | Too friendly | "Being one of the gang is over." |
| "They said I'll have full ownership" (exec) | A mandate on a handshake | Say the territory out loud and watch the room |
| "Stakeholders keep adding work" | Going off-roadmap to please people | Stay around 60% on the roadmap |
| "I'll fix all five things at once" | Too many changes in parallel | One change per person at a time |
| "I don't want to look like I need help" | Not asking for support | "You still have the privilege to ask for help until you say, 'Yes, I'm your person.'" |

## Calibration

What this rests on, and where it's thin:

- The 12-week lead track comes from one published playbook (a meetup talk, 2024). The exec track comes from Marian's director-to-VP guidance and his own first year as a VP: two months of listening, then the audit and three mission streams.
- No mentee's first 90 days are recorded in the material behind this version. The modifiers for internal promotion, "someone wanted your job" and "your manager is new too" apply his general rules (hard conversation early, relationships first, written definition of success); they are not tested against real cases yet.
- The company-stage mapping and the eight readiness items are this skill's design, not measured. The readiness names are labels, not a scale.
- The team-health targets (80% sprint completion, 60% roadmap, 10 to 15% manager time per report, 8/10 satisfaction) are Marian's published targets, not a benchmark dataset.
- Keep each run's inputs and plan. After about 20 real plans, check which weeks people skip or move, and whether the early win landed in week 7; rewrite the weeks that don't hold, and note the change and the date in `model.json`.
