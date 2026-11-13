# marian-coach

Your own career as an engineering leader. Are you ready to lead, what are you worth, how do you
look from outside, and how do you get your company to pay for a mentor. Five skills and two open
MCP servers, built from 3,662 mentoring sessions with engineering leaders since 2019.

## Install

```
/plugin marketplace add marian-kamenistak/engineering-leadership-plugin
/plugin install marian-coach@marian-coach
```

## Components

- `skills/team-lead-readiness`: six-dimension assessment, verdict, two gaps with one move each
- `skills/engineering-salary-calculator`: 15 skills, 5 pillars, weighted by level, 2026 European bands
- `skills/market-value-multiplier`: twelve weighted steps, one multiplier on a base salary for EM, director, VP or CTO, three steps to raise first
- `skills/digital-footprint-multiplier`: how your public profile and work look to a recruiter, a hiring manager or an AI screening tool, and a plan
- `skills/one-minute-pitch-scorer`: scores your one-minute pitch out of 10, counts the words you repeat, times it, and coaches you to fix it in your own words
- `skills/engineering-promotion-case`: an evidence check of your promotion case, a score out of 10, then a one-page case and the plan for the talk with your manager
- `skills/first-90-days-leadership`: a dated 30/60/90-day plan for a new team lead, EM, director, VP or CTO, with the first conversations and the one early win
- `skills/one-on-one-with-manager`: a one-page agenda for your next 1:1 with your manager: the opening line, the one ask, the evidence, the pushback and the follow-up note
- `skills/convince-your-manager`: the email, Slack note, talking points and one-pager that get your company to pay for mentoring
- `.mcp.json`: `eng-leadership-toolkit` (`https://www.marian.coach/mcp`) and
  `mentoring-inquiry-builder` (`https://www.marian.coach/mcp/mentoring`)

Both servers are authless streamable HTTP. Installing the plugin connects them; there is no key
to paste and no account to make. If they are unreachable the skills still run, because each
carries its model in markdown.

## Ask Claude

"Should I become a team lead?" · "What should a senior backend engineer earn in Berlin?" · "I'm
an EM going for director. What am I worth?" · "Here's my LinkedIn. How do I look?" · "Write the
case for my company to pay for a mentor."

Full documentation, privacy and sources: https://github.com/marian-kamenistak/engineering-leadership-plugin

MIT. By [Marian Kamenistak](https://www.marian.coach/), engineering leadership mentor.
