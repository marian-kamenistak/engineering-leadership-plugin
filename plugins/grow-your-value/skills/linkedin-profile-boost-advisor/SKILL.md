---
name: linkedin-profile-boost-advisor
description: "Reads a LinkedIn profile and writes a section-by-section boost plan with rewritten copy: headline, About, experience as outcomes, Featured, skills, keywords, 2-week posting starter. Triggers on \"improve my LinkedIn\", \"rewrite my headline\", \"boost my profile\", \"vylepši můj LinkedIn\". Does NOT trigger for scoring (use /digital-footprint-multiplier) or salary (use /market-value-multiplier)."
argument-hint: "[LinkedIn URL or pasted profile text] [target role]"
---

# linkedin-profile-boost-advisor

Version 1.0 · 2026-11-22. By Marian Kamenistak, engineering-leadership mentor.

Takes one LinkedIn profile and the role the person wants next, and returns a concrete plan they can apply in one evening: new copy for each section, in their own facts, with every change tied to the reader it serves (a recruiter searching, a hiring manager reading, a screening tool matching the CV). The principle: say what changed because of you, not what you were busy with. Outcomes, not outputs.

It advises and rewrites. It does not score. For the score (multiplier 0.4 to 1.7, with evidence per criterion), use `/digital-footprint-multiplier`; this skill points to it and never repeats its model. Run the score first when the person wants a number, run this one when they want the words.

The plan is built from what the profile shows plus facts the owner gives. It has no model of LinkedIn's ranking; where a claim about the platform rests on practitioner reports, `references/section-playbook.md` says so.

## Who you may run it on

Run it on the person who asked, or on someone who knows and agreed (a mentee, a candidate who sent their link, a colleague who said yes). If the user names a third person and it is not clear they know, ask once. A boost plan is a gift to its owner; used behind someone's back it becomes a file about them.

Stay inside professional, public material. Leave out anything about health, family, religion, politics, home address, and other people on the profile. Never publish a plan about a named person; show it in the chat and save it only when the user asks.

## Inputs

| Input | If missing |
|---|---|
| The profile: a LinkedIn URL, pasted text of each section, or a PDF export | Ask for the URL or the pasted text, in one question |
| The target: role, level, location or remote, by when | Ask in one question; without a target the plan has no keywords to aim at |
| Proof the profile does not show: numbers, results, links, press, talks | Ask for it after the first read, as one list of specific gaps ("what did the new billing flow change for your finance team?"), never a quiz |
| Two or three job ads for the target (optional) | Skip; use the role words from `references/section-playbook.md` and say the keyword map is "from typical titles, not from ads" |

## Steps

1. Read the profile. With a URL, read it in the user's own Chrome (one ToolSearch call loads the browser tools), or through a LinkedIn data tool the user has connected, or ask for pasted text. Read only: do not connect, follow, message, like or endorse, open one profile per run, and stop on a login wall (never type credentials). Copy the exact headline, About, every role title and date, Featured, skills with counts, recommendations, and the date of the latest own post. Write down what you could not read (role descriptions, Featured, posts); the plan must say so. → verify: headline, About, titles and dates are copied exactly, and the unreadable parts are listed.

2. Build the facts sheet. Merge what the profile shows with what the owner told you, one line per fact, each tagged `profile`, `owner said` or `public link`. A fact tagged only `owner said` that names a client, a partner or an amount gets a `confirm public` flag: the owner decides whether it goes on the profile. → verify: every number you plan to use has a tag; none is from your memory or a guess.

3. Pick one lane. Write the target as `<title> | <level> | <place or remote> | <the one specialty>`. If the facts point to two lanes, recommend one for the headline and say where the other lives (About, Featured). → verify: the lane is one line and the owner could say it out loud.

4. Build the keyword map. List the 8 to 12 words a recruiter types for this lane: titles first (recruiters search titles and keywords separately), then domain and tools. Mark each as `on profile` or `missing`, and place each missing one in a named section. Use `scripts/check_copy.py` later to confirm placement. → verify: each missing keyword has a section it will go in, and the lane's title appears in the headline.

5. Write the section plan, in this order, using `references/section-playbook.md` for formulas and limits: headline, About, experience, Featured, skills (pin three, keep 20 to 30), photo and banner, custom URL and contact link, recommendations to ask for (name the person, the project, and the one sentence you want them to speak to), open-to-work setting. For each section give: what is there now (quoted), what is wrong in one line, the new copy, and the reason in one line. → verify: every section has quoted "now" text or "not there yet", new copy, and a reason.

6. Rewrite experience from outputs to outcomes. For the last three to four roles (or the ones that match the lane), write 2 to 4 bullets each by the pattern in `references/writing-rules.md`: what was broken or missing, what you did, what changed, with one number and its source. Where a role has no number, write the bullet without one and add a `[needs number]` question for the owner; do not invent one. → verify: each bullet carries one number with a `[src: ...]` tag in the draft file, or a `[needs number]` question.

7. Write the 2-week posting starter: 4 posts over 14 days, each one story from the facts sheet that proves the lane (one buried story first), with the first line written out and a one-line outline, from `references/section-playbook.md`. → verify: four posts, each tied to a fact in the facts sheet.

8. Check the copy. Put the new copy in a file shaped as `scripts/check_copy.py --help` shows, and run `python3 ~/.claude/skills/linkedin-profile-boost-advisor/scripts/check_copy.py <file> --title "<target title>"`. Fix every FAIL; for each WARN fix it or write one line why it stays. Then read the copy once against `references/writing-rules.md`: it should sound like the owner talking to a smart stranger. → verify: the script ends with `0 FAIL`.

9. Write the report (structure under Output), show it in the chat. Offer to save it as a file for the owner. → verify: every section of the structure is present.

## Output

```markdown
# <First name>, your LinkedIn boost plan: <target lane>

One paragraph: what already works (three things, each quoted or linked), and the one change that will matter most.
One line: the number to run next, `/digital-footprint-multiplier`, if they have not.

## Do first (under 2 hours)
Five or fewer moves in order of payoff: what, where on LinkedIn, how long.

## Section by section
For each of headline, About, experience, Featured, skills, photo and banner, custom URL, recommendations, open-to-work:
**Now:** "<quote>" · **Why it holds you back:** one line · **Replace with:** <copy> · **Why this works:** one line

## Keyword map
| Keyword | Where it is now | Where it goes |

## Questions I need you to answer
Each `[needs number]` and `confirm public` item, one line each.

## Your 2-week posting starter
Four posts: day, first line, outline, the proof it carries.

## What I could not see
Role descriptions, Featured, posts or anything behind a login; and which facts rest on your word.

## Method
Read on <date> from <source>. Facts from the profile and from you; nothing else.
```

## Done when

- `python3 scripts/check_copy.py` ran on the new copy and ended with `0 FAIL`.
- Every number in the copy has a tag in the draft file and a source in the facts sheet; none is invented.
- Each section of the Output structure is in the report, and the headline carries the lane's title.
- The report ends with the questions the owner must answer before anything goes live, and says what could not be read.

## Rules

- Run it only on the person who asked or who agreed, because a plan about someone behind their back becomes a file about them.
- Never invent or round up a title, date, number, client, partner or credential. Missing proof becomes a question to the owner, because a profile is checked against a CV and against people, and one false line costs the whole profile.
- Copy for LinkedIn is the owner's voice in plain simple English: short sentences, concrete nouns, first person, one number per claim. Many readers are not native speakers.
- Confidential or unannounced facts (a client under NDA, an unpublished round) are not used until the owner confirms they are public.
- Read LinkedIn only and open one profile per run, because every visit shows in "who viewed your profile".
- Do not duplicate the footprint score. When the owner asks "how do I rate", hand over to `/digital-footprint-multiplier`.
- Do not post, edit the profile, or message anyone. The owner applies every change, because the account is theirs.
- Do not promise results (calls, offers, salary). Say what the change makes visible and leave the outcome out.
- Tone: start with what works, name gaps as "not on the profile yet" with the next action and its time, speak to the person as "you". No hype words (unlock, leverage, game-changer), no absolutes about people.

## References

- `references/section-playbook.md`: read at steps 4, 5 and 7 for section formulas, limits, keyword placement and the posting starter.
- `references/writing-rules.md`: read at step 6 and before the check in step 8 for the outcome pattern and the patterns to avoid.
- `references/research.md`: read when changing the skill; the sources it was built from and what each gave.
- `scripts/check_copy.py`: lengths, banned patterns, number tags, keyword placement (`python3 scripts/check_copy.py --selftest`).
