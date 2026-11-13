---
name: community-launch-readiness
description: Use when deciding whether to start a local engineering-leadership meetup or community chapter, assessing readiness to launch a new-city event, or someone asks "should I start a meetup in my city" / "are we ready to launch a local chapter" / "what do I need before announcing a first event."
---

# Community Launch Readiness

Version 1.0 · 2026-08-09. A 5-question readiness check for launching a local engineering-leadership meetup — built directly from Engineering Leaders Community's own new-city playbook, the actual operating doc used to launch Brno, Bratislava and Kraków. Not theory: the real checklist.

## When to use

- Someone is considering starting a local meetup/chapter and wants a go/no-go read, not just encouragement
- Before a launch date goes on a calendar — this catches the two gaps (speaker network, local operator) that most often stall a new-city launch
- Comparing a new city's readiness against an established one's numbers (don't — see below)

## How to call it

```
claude mcp add -t http elc-toolkit https://www.engineeringleaders.io/mcp
```

Call `assess_community_launch_readiness` with true/false answers on 5 dimensions: a real local speaker network (2-3 speakers who'll promote it, not just show up), a promo-channel plan (3+ channels), a named local operator (not run remotely), a realistic first-event target (40-50, not 100+), and a small paid-promotion budget set aside.

Returns a verdict — ready / close-fix-the-gaps / not-yet — plus the specific open gaps and which one to close first. Real signal from running this in three cities: speakers are the actual distribution channel in a new city (no existing Slack/Luma/LinkedIn network to lean on yet) — if speakers won't promote, the room does not fill regardless of how good the channel plan looks on paper.

No API key, no auth, no signup. Works from Claude Code, Claude Desktop, Cursor, or ChatGPT (developer mode).

From the [Engineering Leaders Community](https://www.engineeringleaders.io/).
