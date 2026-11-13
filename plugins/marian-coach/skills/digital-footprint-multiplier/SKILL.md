---
name: digital-footprint-multiplier
description: Score how a software developer or an engineering manager looks to a recruiter, a hiring manager or an AI screening tool, from public evidence only. Input is one LinkedIn profile URL; the skill reads the profile in the user's own Chrome, researches the open web (GitHub, talks, posts, podcasts, mentions), and returns a multiplier from 0.4 to 1.7 where 1.0 is a typical 2026 profile, the evidence behind every criterion, and an upbeat plan for the next week, month and quarter. Use it whenever someone shares a LinkedIn link and asks "how do I look online", "score my profile", "digital footprint", "will I pass AI screening", "audit my LinkedIn or GitHub before I apply", "what should I fix before a promotion or a job search", or asks for /digital-footprint-multiplier, even if they never say the word multiplier. NOT for the self-reported twelve-step score (use market-value-multiplier), and NOT for writing the LinkedIn posts themselves.
---

# digital-footprint-multiplier

Version 1.1 · 2026-11-12. By Marian Kamenistak, engineering-leadership mentor.

Where it comes from: the criteria and their weights are distilled from 3,662 1:1 leadership sessions with 317 engineering leaders since 2019, where "I sent out hundreds of CVs and nothing came back" is a story that returns every week. The profiles that get the call share the same visible proof; the ones that do not are usually missing the proof, not the skill.

Before a person reads your CV, something else reads you: a recruiter with ninety seconds, a hiring manager who looks you up, sometimes a screening tool that compares your CV with your LinkedIn. They can only judge what they can see. This skill looks at a developer or an engineering manager the same way, from the outside, and turns what it finds into one number and a plan.

- **1.0** is a typical 2026 profile for the role: complete, honest, forgettable.
- **0.4** is a profile the internet has not met yet. **1.7** is a profile that brings the roles to you.
- The number is about **visibility of proof**, not about how good the person is at the job. Say so in every report.

## The nine steps

The multiplier gets a name, so the person remembers where they stand and what the next step is called.

| Step | Multiplier | Name | Share of profiles |
|---|---|---|---|
| 1 | 0.40 to 0.47 | Hidden gem | 4% |
| 2 | 0.48 to 0.62 | First sparks | 7% |
| 3 | 0.63 to 0.77 | Warming up | 12% |
| 4 | 0.78 to 0.92 | Nearly there | 17% |
| 5 | 0.93 to 1.08 | On the radar | 20% |
| 6 | 1.09 to 1.26 | Worth a second look | 17% |
| 7 | 1.27 to 1.43 | Hard to ignore | 12% |
| 8 | 1.44 to 1.61 | In demand | 7% |
| 9 | 1.62 to 1.70 | Magnet | 4% |

The steps are cut from a bell curve, the way a stanine scale is: step 5 sits on 1.0, each step is half a standard deviation wide (one standard deviation = half a level), and most profiles land in the middle. The shares are the design of the scale, not a measurement; say "by design" when you quote one, and never tell a person they are "in the top 7%" as a fact.

The scoring model (two role profiles, criteria, weights, level anchors, plays, the nine steps) is in `model.json` beside this file. The arithmetic is in `scripts/score.py`. Read `model.json` before scoring; do not rephrase the anchors from memory.

## Who you may run it on

Run it on the person who asked, or on someone who knows and agreed (a mentee, a candidate who sent their link, a colleague who said yes). If the user names a third person and it is not clear they know, ask once. A footprint report is a mirror for its owner; used on someone behind their back it becomes a file about them, and that is not what this is for.

Stay inside professional, public material. Leave out anything about health, family, religion, politics, home address, or other people who appear on the profile.

## What you need

| Input | If missing |
|---|---|
| A LinkedIn profile URL | Ask for it. Do not guess between people with the same name |
| The role profile: `developer` or `engineering_manager` | Read it from the current title (`detect` lists in `model.json`; check the manager list first, because "engineering manager" also contains "engineer"); when the title could be either (tech lead, staff engineer with reports), say which one you picked and why, in one line |
| What they are aiming at (optional): a promotion, a new job, a target role | Score against the role they hold today |

When an aim is given, the score still describes today, but the plan serves the aim: check whether the headline, About and Featured carry the words of that aim and link to its proof (a speaker page for speaking work, a case study for a fractional seat), prefer plays that move the aim, and list the aim's own gaps under "Before you apply".

## Workflow

### 1. Read the LinkedIn profile, in the user's own Chrome

Use the Chrome browser tools (load them with one ToolSearch call), open a new tab, and read:

1. the profile itself (headline, About, experience, education, Featured, follower and connection counts);
2. `<profile>/details/experience/`, `/details/skills/`, `/details/recommendations/` when the main page truncates them;
3. `<profile>/recent-activity/all/` for the last 12 months of their own posts (reposts and likes do not count as voice).

LinkedIn loads slowly and in pieces: wait four to five seconds after each page opens, and scroll to the bottom before reading. The activity page shows only the newest posts at first; scroll it several times, and write in the report which period you were able to read ("posts from the last five weeks") instead of assuming twelve months.

Read only. Do not connect, follow, message, like, endorse or change any LinkedIn setting, and do not open more than one person's profile per run. The visit shows up in that person's "who viewed your profile", which is one more reason for the consent rule. If LinkedIn shows a login wall, stop and ask the user to log in; never type credentials. Close the tab when you are done.

Copy the exact lines you will cite (headline, a result line, a recommendation's first sentence). The score may only rest on what you can quote.

When the profile is the user's own, LinkedIn also shows blocks only the owner sees (analytics, "who viewed you", recruiter-only settings). Ignore them: a stranger cannot see them, so they are not footprint.

### 2. Research the open web

Details and search patterns: `references/research.md`. In short: confirm identity first (two matching signals: employer, city, photo, a link from LinkedIn), then look for code, products, talks, podcasts, articles, mentions and community roles. Keep every URL.

Paid research tools the user has connected (Firecrawl, DataForSEO, Exa and similar) are welcome when they find what plain search cannot. Ask once before the first paid call unless the user has already allowed it, keep one run under about 25 paid calls, and name what was spent in the report.

### 3. Pick the criteria and score

1. Take the criteria of the role profile from `model.json`.
2. For each criterion choose a level: 0, 0.5, 1, 1.5 or 2, by comparing the evidence with the written anchors for 0, 1 and 2.
3. A level above 0 needs evidence: a quoted line or a URL. Level 0 needs the list of places you looked. "Probably has" is level 0.
   - Half levels sit between two anchors: 0.5 when part of the level 1 anchor is visible, 1.5 when level 1 is fully met and part of level 2 is visible. Say which part is still missing; that sentence is the person's next step.
   - A public appearance is a talk, a panel, a podcast or a long article under their name. Mentoring at an event, attending, and reposts are not appearances; mention them under network signals instead.
   - When the newest role has no description, judge outcomes on the most recent roles that do, and count the empty one under "Easy to screen".
4. If a criterion truly cannot be observed (an employer that forbids public code, a profile in a language you cannot read), set it to `null` with the reason. The script drops it and scales the other weights back to 100. At most two.
5. Write the scores to a JSON file and run the script. Never do the arithmetic in your head.

```bash
python3 scripts/score.py developer /path/to/scores.json     # or engineering_manager
python3 scripts/score.py --selftest
```

The script refuses a score without evidence. It returns the multiplier, its named step, what one level up is worth for each criterion, and the projection for the plan.

### 4. Build the plan

Take the three criteria where reaching the next anchor is worth the most (the script lists them), and pick plays from `model.json` (adapt the wording to this person; invent nothing about them). Sort them by time:

- **This week:** things that take under two hours. At least two.
- **This month:** one or two things that need a few evenings.
- **This quarter:** one thing that needs other people (a talk, a project in use, a recommendation from a manager).
- **Before you apply:** a short checklist for the week before a promotion case or a job application.

Put the planned levels into `plan` in the JSON so the script prints the projection: today, after the week, after the month, after the quarter. Count a step in the period when it pays off, not when it starts: a recommendation requested this week and received next month belongs to the month.

### 5. Write the report

ALWAYS use this structure:

```markdown
# <First name>, your digital footprint: <M.MM>x · <step name> (step <n> of 9)

<step line>. One sentence on what the number means: visibility of proof, 1.0 = a typical 2026 <role> profile.
One line: which profile you scored against and why, and the aim if one was given.

## What already works
Three things a recruiter or a screening tool likes today, each with the quoted line or the link.

## The score
| Criterion | Weight | Level | Evidence |
(one row per criterion; "not visible yet" instead of zero; "could not be observed" for null)

## Your next steps
**This week** (under 2 hours each) · what to do, and what it is worth (+0.0x)
**This month**
**This quarter**
**Before you apply or pitch** (checklist, in the words of the aim)

Projection: today <a>x → after the week <b>x → after the month <c>x → after the quarter <d>x

## What I could not see
Private work, anything behind a login, criteria set to null, people with the same name I left out.

## Method
Evidence only, read on <date>. Sources: LinkedIn plus <n> public pages. Paid research: <what, or none>.
```

Show the report in the chat. Save it to a file only when the user asks, and never publish a report about a named person.

## Tone: "yes, I can do that"

The reader should finish the report wanting to open LinkedIn, not close the laptop.

- Start with what works. Everyone has three things.
- A gap is "not visible yet", and it always comes with the next action and how long it takes. Never "weak", "poor", "lacking", "fails".
- Speak to the person: "you", plain words, short sentences. Many readers are not native English speakers.
- Be specific and a little playful: name the step and the next one up, show the gain ("this one is worth +0.08"), celebrate the cheap wins.
- Stay honest. Do not raise a level to be kind, and do not promise a salary: the multiplier is not pay.
- No hype words (unlock, leverage, empower, game-changer), no absolutes about people (never, always, nobody).

**Example of the register:**
"Your GitHub has the project. It just has no front door yet. Give `invoice-parser` a README with one screenshot and pin it: twenty minutes, and proof of work moves from a first sign to typical. Worth +0.05."

## Developer or engineering manager

Both use the same scale and the same script. The developer profile weighs proof of work and outcomes most; the manager profile weighs business and team outcomes, scope, and people who vouch for how they lead. A staff or principal engineer without reports is a developer. A tech lead with reports who spends most of the week on people is a manager; say which one you chose.

Founders, fractional leaders, consultants and mentors use the manager profile, read a little wider: "reports" are the people they led or served, clients included; "manager" is whoever they answered to, a client's CEO included; and when several roles are marked as current, judge outcomes on the role they want to be hired for and the largest one.

## With the twelve-step score

`market-value-multiplier` asks the person twelve questions. This skill asks the internet. When both exist, show them side by side: where the self-score is higher than the footprint, the work is real and not visible yet, and that gap is the plan.

## Calibration

The level "typical for 2026" is defined by written anchors, not by a dataset of scored profiles, and the shares of the nine steps are the bell curve's, not counted. Keep each run's scores JSON. After about 30 real runs, compare the median level per criterion with 1 and the share of runs in each step with the table above, rewrite the anchors that sit far from it; note the change and the date in `model.json`.
