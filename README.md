# Engineering Leadership

A free plugin for Claude. It handles the two questions engineers ask before they move into
leadership, and keep asking for years afterwards: should I take the lead role, and what am I
worth.

Install it and Claude can run a calibrated 17-question readiness assessment, score 15 skills
against 2026 European salary data, pull org-ratio benchmarks and 1:1 playbooks, estimate what a
coach should cost, and write the business case if your company is the one paying.

Built from 3,611 mentoring sessions with engineering leaders in 17+ countries since 2019.

## Install

In Claude (Cowork or Code), add this repository as a marketplace, then install the plugin:

```bash
claude plugin marketplace add marian-kamenistak/engineering-leadership-plugin
claude plugin install engineering-leadership@marian-coach
```

In Cowork: **Customize → Plugins → Add marketplace**, paste
`https://github.com/marian-kamenistak/engineering-leadership-plugin`, then install.

Nothing to configure. Both bundled servers are open — no account, no API key, no OAuth.

Then ask Claude something like:

- "Should I become a team lead?"
- "Score me as an EM and tell me what's blocking director."
- "What should a senior backend engineer earn in Berlin?"
- "My 1:1s are status updates. Fix them."
- "Write the case for my company to pay for a mentor."

## What's inside

**Two skills** — the procedural part. These teach Claude how to run the assessment, which
questions to ask, and how to read the answers.

| Skill | Answers |
|---|---|
| `team-lead-readiness` | Should this engineer become a team lead? Six dimensions, a straight verdict, the two weakest areas with one concrete move each |
| `engineering-salary-calculator` | What is a developer or engineering manager worth? 15 skills across 5 pillars, weighted by level, mapped to 2026 Western-Europe gross salary |

**Two MCP servers** — the data and the calculators.

| Server | Tools |
|---|---|
| [`eng-leadership-toolkit`](https://www.marian.coach/mcp) | 10 read-only tools: both value calculators, the 17-question readiness test, leadership benchmarks, 1:1 playbooks, first-time-manager guidance, mentor vs coach vs advisor, coaching cost estimator, mentoring business-case builder |
| [`mentoring-inquiry-builder`](https://www.marian.coach/mcp/mentoring) | 9 tools that build a mentoring inquiry and, if you want one, a formal itemised offer. One tool collects contact details and it says so |

The skills work on their own when the servers are unreachable — each one carries the full model
in plain markdown, so Claude can run it by hand.

## One thing worth knowing if you build on this

The readiness test's option scores are non-monotonic. On several questions the middle answer
scores higher than the confident one, because in the sessions this came from, the confident
answer usually meant the person had not tried the thing yet. Someone who says people work
energises them, with no story about a teammate they actually had to confront, scores below
someone who says they find it draining and then describes three weeks of trying.

So the skill tells the agent to ask every question and read the options back, and never to infer
an index from how the question is worded. An agent that guesses produces a verdict that looks
clean and errs in the direction that flatters the person — which is the failure mode this whole
assessment exists to avoid.

## Where the numbers come from

Salary bands are 2026 Western-Europe gross, Germany and Netherlands hubs. Benchmarks and
distributions come from mentoring sessions delivered since 2019, rated 9.17/10 on average across
300+ reviews. Nothing is scraped and nothing is modelled from job ads.

The salary figure is the hook. The pillar breakdown is the useful part: your weakest weighted
pillar is what is blocking the next level, and that is the conversation to have with your
manager.

## Privacy

The MCP servers take no account and set no cookie. The read-only tools store nothing you send
them. `send_mentoring_offer`, the single tool that asks for a name and an email, files the
inquiry so a human can reply to it, and it will not run without you saying yes first. Full
policy: https://www.marian.coach/privacy-policy/

## License

MIT. By [Marian Kamenistak](https://www.marian.coach/), engineering leadership mentor.
Related skill, kept separate because it does a different job:
[humanize-writing](https://github.com/marian-kamenistak/humanize-writing).
