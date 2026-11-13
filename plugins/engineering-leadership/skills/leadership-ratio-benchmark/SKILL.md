---
name: leadership-ratio-benchmark
description: Use when assessing whether an engineering org's manager-to-senior-IC split looks healthy, whether an org is top-heavy, whether its senior IC track is real, or someone asks "how many managers should we have" / "is my org too top-heavy" / "what's a healthy manager-to-engineer ratio". Returns the org's own split and the one structural question that shape should prompt; it deliberately does not score the org against a borrowed peer ratio.
---

# Leadership Ratio Benchmark

Version 1.1 · 2026-11-13. Reads an engineering org's manager-to-senior-IC split and returns the one structural question that shape should prompt.

Built by the Engineering Leaders Community: 3,300+ engineering leaders across Prague, Brno, Bratislava and Kraków since 2019.

## What changed in 1.1

Version 1.0 compared your split with the community's own composition (69% managers, 21% senior ICs) and gave a verdict from the point difference. That comparison was wrong, and the tool stopped making it on 5 September 2026. The community's shares are of its whole member base and add up to 90, not 100, while your two counts are shares of each other only. Different denominators cannot be subtracted. And who joins a leadership community says nothing about how your company should look. In testing, 1.0 called a clearly top-heavy org "no structural red flag".

## When to use

- Someone shares headcount numbers (managers vs. senior/staff ICs) and asks if the split looks right
- A structural question: "do we have too many managers", "is our IC track real or just a title", "why does delivery feel management-heavy"
- Before recommending an org redesign: look at the shape first, don't guess

## How to call it

Count only people senior enough to plausibly hold a management role: managers, tech leads, senior and staff ICs. Leave junior and mid ICs out, or the split means nothing.

Connect the MCP server:

```
claude mcp add -t http elc-toolkit https://www.engineeringleaders.io/mcp
```

Then call `benchmark_leadership_ratio` with `{ "managers": <n>, "senior_ics": <n> }`. It returns:

- **Your split**, for example "67% manager / 33% senior IC (18 and 9 people)".
- **One question, picked by which group is bigger.**
  - More managers than senior ICs: is there a real senior/staff IC track someone can grow into without taking headcount, or does "senior" here mostly mean "manager"?
  - More senior ICs than managers: is management capacity the bottleneck (spans too wide, delivery slipping on coordination), or is this deliberate and your senior ICs are genuinely unblocked?
- **A note on the community figure** and why it is not a target to hit.

No API key, no auth, no signup. Works the same from Claude Code, Claude Desktop, Cursor, or ChatGPT (developer mode).

## Reading the result

The useful comparison is your own org against itself: count the same two groups again in six or twelve months and see which way the shape moved, and why. A skew is not a verdict on your people. It is a prompt to ask why the shape looks the way it does.
