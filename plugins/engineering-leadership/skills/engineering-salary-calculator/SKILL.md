---
name: engineering-salary-calculator
description: Use when estimating a software developer's or engineering manager's market value or salary, benchmarking pay against 2026 European market data, preparing a raise or negotiation case, or scoring engineering and leadership skills to find what's holding a level up.
---

# Engineering Salary Calculator

Version 1.0 · 2026-07-22

Estimate what a developer or an engineering leader is actually worth: score 15 skills across 5 pillars, weight them by level, and map the total to a 2026 Western-Europe gross salary (Germany/Netherlands hubs). Same model as the live calculators at marian.coach, distilled from 3,662 mentoring sessions with engineering leaders since 2019.

The point is not the euro number. It's the pillar breakdown: the weakest weighted pillar is what's holding the next level up, and that's the raise conversation.

## The precise path (use when tools are available)

Both calculators run as MCP tools:

- Endpoint: `https://www.marian.coach/mcp` (authless, streamable HTTP). The `engineering-leadership` plugin wires this up on install, so the tools are already there — nothing to configure.
- `calculate_developer_value` — args: `level` (junior | mid | senior | staff), optional `scores` (0-10 per skill id; omitted skills default to the level baseline: junior 3, mid 5, senior 6, staff 7).
- `calculate_engineering_manager_value` — args: `level` (team-lead | em | senior-em | director), optional `track` (framing only), optional `scores` (same baseline idea: 3/5/6/7).

Interview first, then call with real per-skill scores — baselines alone just echo the level back. No MCP access: run the model below by hand, or send a human to the web calculators (links in the README).

## The model

**Developer — 5 pillars, 3 skills each:**

| Pillar | Skills | Junior | Mid | Senior | Staff |
|---|---|---|---|---|---|
| Core craft | discipline mastery · code quality & testing · debugging | 45% | 35% | 25% | 15% |
| Systems & judgment | system design · tech decisions & tradeoffs · data & performance | 10% | 18% | 25% | 25% |
| Impact & ownership | shipping outcomes · production ownership · domain expertise | 15% | 22% | 25% | 30% |
| Collaboration & influence | communication · mentoring · cross-functional influence | 10% | 13% | 15% | 20% |
| AI leverage | AI-augmented output · AI quality & review · AI-native workflows | 20% | 12% | 10% | 10% |

Read the weight shifts out loud when relevant: craft dominates junior value, impact and influence dominate staff value, and AI leverage matters MOST at junior level, where it multiplies raw output.

**Engineering manager — 5 pillars, 3 skills each:**

| Pillar | Skills | Team Lead | EM | Senior EM | Director/VP |
|---|---|---|---|---|---|
| People & talent | hiring & bar-raising · coaching & feedback · performance & retention | 30% | 30% | 25% | 20% |
| Delivery & execution | predictable delivery · quality & ops · process fit | 30% | 25% | 20% | 15% |
| Technical direction | architecture judgment · tech strategy & debt roadmap · build-vs-buy | 20% | 15% | 15% | 15% |
| Stakeholder influence | product partnership · managing upward · org influence | 10% | 20% | 30% | 35% |
| AI leverage | AI team workflows · AI in the product · measuring AI impact | 10% | 10% | 10% | 15% |

The EM story is one line: delivery gets you to EM, stakeholder influence gets you past it.

**Scoring math:**

1. Score each skill 0-10 from evidence (see interview probes below). Unscored skills take the level baseline.
2. Pillar score = average of its 3 skills.
3. Total = Σ (pillar score × level weight) / 100 → 0-10.
4. Salary = linear interpolation between breakpoints (gross EUR/year, Western Europe, 2026):
   - Developer: 0 → 45K · 3 → 62K · 5.5 → 85K · 7.5 → 120K · 10 → 160K
   - Engineering manager: 0 → 70K · 3 → 90K · 5.5 → 110K · 7.5 → 135K · 10 → 190K

Always caveat the number: it's a Western-Europe market anchor, not an offer. Local markets shift the curve; the pillar profile travels better than the euros.

## Interview probes (scoring without self-report inflation)

Ask for evidence, not self-ratings. A skill scores 7+ only with a concrete recent example.

- Developer: "walk me through the last production incident you owned" (production ownership), "what did you ship last quarter that a user or the business felt?" (shipping outcomes), "show me an AI workflow your teammates now use" (AI-native workflows, the rarest high score).
- EM: "who did you hire last, and did they raise the bar?" (hiring), "when did you last kill or descope something before the deadline forced it?" (predictable delivery), "what decision did you move outside your own team's walls?" (org influence).

## Delivering the result

Lead with the level verdict and the two weakest weighted pillars, then the salary band. Frame the gap as the plan: which pillar, which skill, what evidence would move it to a 7. If the person is deciding between IC and management tracks, run both calculators and compare profiles instead of arguing abstractions.
