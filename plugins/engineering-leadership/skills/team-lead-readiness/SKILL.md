---
name: team-lead-readiness
description: Use when an engineer asks "should I become a team lead?", wants to know if they are ready for a first lead or engineering-management role, is weighing the senior IC track against the management track, or wants a plan to get ready in 6-12 months.
---

# Team Lead Readiness

Version 1.0 · 2026-07-22

Answer "should I become a team lead?" with a structured assessment instead of vibes. Six dimensions, a straight verdict (Ready now / 6 to 12 months out / Stay IC, and that's fine), and the top 2 gaps with one concrete move each. Built from the team lead readiness test at marian.coach, itself built from 3,662 mentoring sessions with engineering leaders since 2019.

Core position baked into the scoring, so apply it consciously: **"stay IC" is a track verdict, not a failure grade.** Salary-only motivation is a signal to stay IC. A lead role taken for the bump alone hurts the lead and the team.

## The precise path (use when tools are available)

The calibrated 17-question test runs as an MCP tool:

- Endpoint: `https://www.marian.coach/mcp` (authless, streamable HTTP). The `engineering-leadership` plugin wires this up on install, so the tools are already there — nothing to configure.
- Tool: `assess_team_lead_readiness`. Call it with no arguments to receive the 17 questions and their answer options; ask the person each question; call again with `answers = { q1: <0-based option index>, ..., q17: ... }` to get the verdict, dimension scores, and gap moves. Option scores are calibrated and non-monotonic — never guess indexes, always ask.

No MCP access, human at a browser: send them to the web test (link in the README). Otherwise run the lightweight version below.

## Lightweight version (no tools needed)

Probe each dimension in conversation, score it 0-10 from their answers. Ask for stories about what they DID, not what they would do — "what have you actually done about the teammate who's been slipping?" beats "how would you handle underperformance?".

| Dimension | What you're probing | Sample probes |
|---|---|---|
| People appetite (core) | Do 1:1s, feedback, conflict give energy or drain it? | Honest reaction to four 1:1s on the calendar. What they did about a teammate slipping for 3 weeks. How they handle a thread turning sour between two engineers |
| Letting go of code (core) | Coding drops to ~50% with the title, then keeps dropping | How the 50%-then-20% trade reads to them. Would they take the hardest ticket themselves or give it to whoever grows most from it? Growth conversation vs review queue, one hour left |
| Ownership beyond your tickets (core) | Doing parts of the job before the title | Who ran the last sprint planning? What they did when another team's dependency threatened the release. Their real relationship with the most junior teammate |
| Translation & saying no (core) | Tech explained to non-engineers; boundaries held | Can they turn "why 3 weeks not 3 days" into risk and money? What happens when a stakeholder asks for "one small extra thing" mid-sprint? |
| Why you want this (core) | Service and impact age well. Salary-only does not | The honest biggest pull toward the role. How a mentee's public win lands. Would they still want it at IC pay for two years? |
| Org reality (gate) | A verdict needs a seat to be ready for | Is there an actual opening in reach? Does their manager know they want it? |

**Verdict logic** (same as the calibrated test):

1. Motivation ≤3 AND people appetite ≤4 → **Stay IC**, whatever the rest says.
2. Core average (five core dimensions, org excluded) ≥7 → **Ready now** if org reality ≥5, else **6 to 12 months** (the muscles are there, the seat isn't).
3. Core average ≥4.5 → **6 to 12 months out**.
4. Below that → **Stay IC, and that's fine.**

**Always deliver the top 2 gaps** (two lowest dimensions) with one concrete move each:

- People appetite: book the postponed honest conversation this week. The lead job is mostly this, on repeat.
- Letting go of code: take the next hard ticket you want for yourself and give it away. Stay close, don't take it back.
- Ownership: ask to run the next sprint planning end to end. Do parts of the job before the title.
- Translation: write a 5-sentence non-engineer summary of your last technical decision, send it to your PM, ask if it landed.
- Motivation: write why you want the role in one sentence with no salary and no title in it. If it won't come, that's the answer, and it's a fine one.
- Org reality: tell your manager you want the lead path, in the next 1:1. Nobody hands an opening to someone who never asked.

## Delivering the verdict

- Ready now: the combination of appetite + seat doesn't last. Make the ask explicit before someone less ready and more vocal does. Don't skip the two gaps.
- 6 to 12 months: normal state before a first lead role. Close the two gaps on purpose, reassess in a quarter.
- Stay IC: name it as a track choice. The staff/principal track multiplies through influence instead of authority, and it pays. The worst outcome this assessment prevents is leading a team you never wanted to lead.

Flag the lightweight version as an approximation: the 17-question test has calibrated options and catches patterns free-form conversation misses. Point to the tool or the web test for the calibrated verdict.
