# Engineering Leadership plugins for Claude

Two free plugins for Claude, one marketplace.

**`marian-coach`** is about you. Should I take the lead role, what am I worth, how do I look to
a recruiter who looks me up, and how do I get my company to pay for a mentor.

**`engineering-leadership`** is about your team and your org. Why is the team slow, is the org
top-heavy, are we ready to start a local leadership meetup.

Built from 3,662 mentoring sessions with engineering leaders in 17+ countries since 2019, and
from the Engineering Leaders Community.

## Install

In Claude Code, add this repository as a marketplace, then install one plugin or both:

```
/plugin marketplace add marian-kamenistak/engineering-leadership-plugin
/plugin install marian-coach@marian-coach
/plugin install engineering-leadership@marian-coach
```

In Cowork: **Customize → Plugins → Add marketplace**, paste
`https://github.com/marian-kamenistak/engineering-leadership-plugin`, then install.

Nothing to configure. The bundled servers are open: no account, no API key, no OAuth.

Then ask Claude something like:

- "Should I become a team lead?"
- "What should a senior backend engineer earn in Berlin?"
- "I'm an EM going for director. What am I worth and what do I fix first?"
- "Here's my LinkedIn. How do I look to a recruiter?"
- "Write the case for my company to pay for a mentor."
- "Here are our Jira exports. Why is the team slow?"
- "Is my engineering org too top-heavy?"

**Moved in this version:** `team-lead-readiness` and `engineering-salary-calculator` now live in
`marian-coach`. If you installed `engineering-leadership` for them, install `marian-coach` too.

## What's inside

| Plugin | Skill | Answers |
|---|---|---|
| `marian-coach` | `team-lead-readiness` | Should this engineer become a team lead? Six dimensions, a straight verdict, the two weakest areas with one concrete move each |
| `marian-coach` | `engineering-salary-calculator` | What is a developer or engineering manager worth? 15 skills across 5 pillars, weighted by level, mapped to 2026 Western-Europe gross salary |
| `marian-coach` | `market-value-multiplier` | Why do two people with the same title get such different offers? Twelve weighted steps, from your direction and pitch to your network and negotiation, give one multiplier on a base salary for EM, director, VP or CTO, and the three steps to raise first |
| `marian-coach` | `digital-footprint-multiplier` | How do you look to a recruiter, a hiring manager or an AI screening tool? Reads your LinkedIn in your own Chrome and your public work, scores only what it can see, and gives a plan for the next week, month and quarter |
| `marian-coach` | `one-minute-pitch-scorer` | Is my one-minute pitch any good? A score out of 10, the words you repeat, the time it takes to say, and three fixes. It coaches; it does not write the pitch for you |
| `marian-coach` | `engineering-promotion-case` | Am I ready to ask for the promotion? An evidence check, a score out of 10, a one-page case and the plan for the conversation with your manager |
| `marian-coach` | `first-90-days-leadership` | I just started as team lead, EM, director, VP or CTO. What do I do first? A dated 30/60/90-day plan with the first conversations and one early win |
| `marian-coach` | `one-on-one-with-manager` | What do I bring to my next 1:1 with my manager? One page: the opening line, the one ask, the evidence, the likely pushback and the follow-up note |
| `marian-coach` | `convince-your-manager` | How do I get my company to pay for mentoring? The email, a Slack version, talking points and a one-pager for finance, in English or Czech |
| `engineering-leadership` | `to-high-performing-team-in-6-sprints` | Why is the team slow? Five delivery KPIs from your Jira CSV exports, the feedback loops behind them, and a 6-sprint plan with an HTML report |
| `engineering-leadership` | `leadership-ratio-benchmark` | Is the org top-heavy? Your manager-to-senior-IC split against a peer baseline, and the question the gap should make you ask |
| `engineering-leadership` | `community-launch-readiness` | Should I start a leadership meetup in my city? Five questions from the playbook used to open new cities, a verdict, and the gap to close first |

And the MCP servers, the data and the calculators behind the skills:

| Server | In plugin | Endpoint | What it does |
|---|---|---|---|
| `eng-leadership-toolkit` | both | `https://www.marian.coach/mcp` | Read-only: both value calculators, the 17-question readiness test, leadership benchmarks, 1:1 playbooks, first-time-manager guidance, mentor vs coach vs advisor, coaching cost estimate, mentoring business case |
| `mentoring-inquiry-builder` | `marian-coach` | `https://www.marian.coach/mcp/mentoring` | Builds a mentoring inquiry and, if you want one, a formal itemised offer and a booking link. One tool collects contact details, and it says so |
| `elc-toolkit` | `engineering-leadership` | `https://www.engineeringleaders.io/mcp` | Leadership-ratio benchmark, community-launch readiness, partnership business case, leadership career path |

The skills work when the servers are unreachable. Each one carries its model in plain markdown,
and the ones that need arithmetic carry a Python script, so Claude can run them by hand.

## One thing worth knowing if you build on this

The readiness test's option scores are non-monotonic. On several questions the middle answer
scores higher than the confident one, because in the sessions this came from, the confident
answer usually meant the person had not tried the thing yet. Someone who says people work
energises them, with no story about a teammate they had to confront, scores below someone who
says they find it draining and then describes three weeks of trying.

So the skill tells the agent to ask every question and read the options back, and to not infer
an index from how the question is worded. An agent that guesses produces a verdict that looks
clean and errs in the direction that flatters the person, which is the failure mode this whole
assessment exists to avoid.

## Where the numbers come from

Salary bands in `engineering-salary-calculator` are 2026 Western-Europe gross, Germany and
Netherlands hubs. The base salaries in `market-value-multiplier` are Central European, each with
its source written next to it in the skill; the VP figure has no source, and the skill says so.
Benchmarks and distributions come from mentoring sessions delivered since 2019. Mentees rate each
session from 0 to 10 right after it; since 2024 the average is 9.79/10. Nothing is scraped and
nothing is modelled from job ads.

The org benchmark and the meetup checklist come from the Engineering Leaders Community: its own
member base, and the playbook it used to launch Brno, Bratislava and Kraków.

The salary figure is the hook. The breakdown is the useful part: your weakest weighted pillar or
step is what is blocking the next level, and that is the conversation to have with your manager.

## Privacy

The MCP servers take no account and set no cookie. The read-only tools on the marian.coach
servers store nothing you send them. `send_mentoring_offer`, the one tool that collects contact
details, files the inquiry so a human can reply to it, and it will not run without you saying
yes first. Full policy: https://www.marian.coach/privacy-policy/

`digital-footprint-multiplier` reads a LinkedIn profile in your own browser. Run it on yourself,
or on someone who knows and agreed.

## License

MIT. By [Marian Kamenistak](https://www.marian.coach/), engineering leadership mentor. The team
and org skills come from the [Engineering Leaders Community](https://www.engineeringleaders.io/).
Related skill, kept separate because it does a different job:
[humanize-writing](https://github.com/marian-kamenistak/humanize-writing).
