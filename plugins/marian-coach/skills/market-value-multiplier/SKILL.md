---
name: market-value-multiplier
description: Score an engineering leader's market value as a multiplier from 0.4 to 1.7 across twelve weighted steps (direction, title, target companies, one-minute pitch, digital footprint, network, public speaking, AI level, outcome language, interview practice, negotiation, first months), and apply it to a base salary for an Engineering Manager, Engineering Director, VP of Engineering or CTO in Central Europe. Use whenever someone asks "what am I worth", "how do I double my salary", "why do I get no replies to my applications", "am I ready for a director or VP role", wants a job-search or promotion plan, shares a CV or LinkedIn profile for a market check, or mentions the 12 steps to a higher salary, even if they never say the word "multiplier".
---

# market-value-multiplier

Version 1.1, 2026-11-12.

Two people with the same title and the same years get offers that differ by a factor of four. The difference is rarely the craft. It is whether the market can see what they offer: a clear direction, a title that says what they are for, people who vouch for them, proof in public, and the words they use in the room.

This skill measures that as one number. Twelve steps, each with a weight. Skip all of them and you are worth 0.4 of the standard pay for your role. Do them at the 2026 standard and you are at 1.0. Do them well and you reach 1.7.

It does two jobs:

1. **Score.** Ask the twelve questions, calculate the multiplier and apply it to a base salary.
2. **Plan.** Name the steps that would raise the number most, and what to do about each this week.

The model (steps, weights, level descriptions, base salaries and their sources) is in `model.json` beside this file. Read it before scoring; do not rephrase the level descriptions from memory.

## What you need

| Input | Why | If missing |
|---|---|---|
| **The role** they hold or are going for: Engineering Manager, Engineering Director, VP of Engineering, CTO | The base salary depends on it | Ask |
| **Their own base salary** (optional) | The multiplier is more useful on a real number than on a market default | Use the Central Europe default from `model.json` and say so |
| **Answers to the twelve questions**, or a CV, LinkedIn profile or description to read them from | The score | Ask the questions |

Senior and staff engineers can use it too: score them against the Engineering Manager base and say that the base is for a manager.

## How to ask

Ask the questions in order, four at a time, in plain language. For each, show the three levels from `model.json` and let the person pick. People answer faster when they can see the options.

If they give you a CV or a LinkedIn profile first, read it and propose a level for every step you can judge, with the line that made you choose it. Then ask them to confirm or correct. Never score a step from what a person probably does. A profile cannot show step 6 (network), step 10 (the order of conversations) or step 11 (dry runs): ask those.

Score what is true today. A plan to do something next month is level 0.

## The twelve steps

| # | Step | Weight | Skip it and |
|---|---|---|---|
| 1 | Your vector: one role, one direction, a date | 10 | the pitch lies, the network calls are vague, the interviews wander |
| 2 | Your title and your number: business domain plus technical scope | 8 | you anchor low, or you dodge the question |
| 3 | Your dream companies: 10 to 15 names | 5 | you apply everywhere and hear back from few |
| 4 | Your one-minute pitch: largest outcome, differentiator, potential | 12 | nobody listens for the other 59 minutes |
| 5 | Your digital footprint: LinkedIn, GitHub, a pet project | 10 | the recommendation ends at the first question |
| 6 | Your network: list 50, reactivate 10, target 20 new | 12 | in five years your options will suck |
| 7 | Be heard: meetups, podcasts, conferences, communities | 8 | the roles go to peers who are louder, not better |
| 8 | Your AI level: Ask, Brief, Repeat, Connect, Supervise | 12 | you sit next to the AI and watch it work |
| 9 | Outcomes, not outputs: product, impact, mission, value | 8 | your work is a nine and it lands like a five |
| 10 | B-list first, then A-list | 3 | you burn your dream company on your worst interview |
| 11 | Interview dry runs, recorded | 5 | you get the meeting and then you freeze |
| 12 | Negotiate, then protect your first 3 to 6 months | 7 | you take the first offer out of relief |

The weights add up to 100. The pitch, the network and the AI level weigh the most: the best roles are filled through people before they are posted, the pitch is what those people repeat about you, and AI is the skill the market pays for and few can show.

## Calculate

Each step is scored 0 (missing), 1 (standard for 2026) or 2 (strong).

```
a          = sum(weight x score) / 100          (0 to 2)
multiplier = 0.4 + 0.6 x a          when a is 1 or less
multiplier = 1.0 + 0.7 x (a - 1)    when a is above 1
```

Round to one decimal, and apply the rounded multiplier to the base salary (0.9 x 95,000, not 0.856 x 95,000), so the two numbers a person sees agree.

The rounded multiplier also carries one of nine names (`bands` in `model.json`), from "Hidden gem" at 0.4 to "Magnet" at 1.7. The nine bands are cut from a bell curve (stanine scale: 4, 7, 12, 17, 20, 17, 12, 7, 4 percent; band 5 sits on 1.0). The shares are the design of the scale, not measured data.

Run the calculator, which sits beside this file:

```
python3 <this skill's folder>/scripts/multiplier.py <role> <s1> ... <s12> [--base EUR]
```

`role` is `em`, `director`, `vp` or `cto`. It prints the table, the market value, the three steps to raise first and the final line. If you cannot run code, calculate by hand with the formula and show the working.

## The base salaries

Gross, a year, Central Europe, 2026. They are defaults: tell the person where each comes from and ask them to overwrite it if they know their market better.

| Role | Default | Where it comes from |
|---|---|---|
| Engineering Manager | EUR 95,000 | Bulldogjob 2025 (median 32,000 PLN a month on B2B) and Hays Poland 2026 (40,000 PLN gross a month most often offered); the midpoint |
| Engineering Director | EUR 135,000 | Hays Poland 2026, IT Director or CIO, 50,000 PLN gross a month most often offered |
| VP of Engineering | EUR 150,000 | Unsourced. No Central European dataset for this title exists; it is set level with the CTO figure |
| CTO | EUR 150,000 | Antal 2026, Poland, EUR 82K to 220K base; TalentUp, Czechia, median base EUR 130K |

Say plainly that the VP figure has no source. Outside Central Europe, ask for their own base.

## The report

```
# Your market value

Role: <role>. Base: EUR <n> a year (<your figure | Central Europe default>)

| # | Step | Weight | Level | Raising it one level adds |
|---|---|---|---|---|
| ... the calculator's table ... |

**Multiplier: X.X. Market value: about EUR <n> a year.**

## Raise these first
1. **Step N, <name>** (+0.0X). <what is missing, in their own words>
   This week: <one action they can finish in a week>
2. ...
3. ...

## Already strong
- <the steps at level 2, one line each>

MARKET VALUE MULTIPLIER: X.Xx · <name> (N of 9)
```

Rules for the report:

- **Three steps to raise, ranked by the calculator.** For each, one action that fits in a week: write the vector sentence and send it to two people; rewrite the headline as domain plus scope; list fifty names; record a one-minute pitch on the phone.
- **Use their words and their facts.** Never invent an outcome, a number or a company for them. Where the plan needs one, ask for it.
- **The number is a direction.** Say once that it is a model built on twelve self-assessed answers and market defaults, and that a real offer depends on the company. Then stop hedging.
- **End with the `MARKET VALUE MULTIPLIER: X.Xx · <name> (N of 9)` line**, exactly in that form.

## Scoring honestly

- People overrate steps 4 and 9. Ask them to say the pitch or one outcome statement before you accept a 2.
- "Uses AI every day" is level 0 on step 8. The level is about what runs without them sitting next to it.
- A title with a programming language in it is level 0 on step 2, whatever the seniority.
- If someone is at 2 on every step, check three of them with a follow-up question. An honest 1.2 helps more than a flattering 1.7.

---

Built on the 12 steps Marian Kamenistak uses in mentoring engineering leaders, first presented at the Engineering Leaders Community meetup #37.
