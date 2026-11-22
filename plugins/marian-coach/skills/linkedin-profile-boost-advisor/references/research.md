# Research: where this skill comes from

Searched GitHub on 2026-11-22 with `gh search repos` ("linkedin profile optimizer", "linkedin headline about section optimizer", "linkedin optimizer SKILL.md") and `gh search code --filename SKILL.md "linkedin profile"`. Read the SKILL.md or README of the ten below, and noted licences from `gh repo view`. Where a repo has no licence, all rights are reserved by its author, so nothing was copied from it; ideas and structure only, written fresh. For the MIT-licensed ones nothing was copied either; the credit says where an idea came from.

| # | Source | Licence | What it does well | What this skill took |
|---|---|---|---|---|
| 1 | [Flitternie/linkedin-optimizer](https://github.com/Flitternie/linkedin-optimizer) | MIT | Reviews "in recruiter order" (photo, headline, About, Featured, Experience...); a source of truth built from CV, site and publications; separate consent for edits | The review order; the rule that dates, affiliations and metrics come from a source; the boundary that edits need the owner's say-so |
| 2 | [artificialguybr/resume-ats-linkedin-optimizer](https://github.com/artificialguybr/resume-ats-linkedin-optimizer) (`references/04-linkedin.md`) | MIT | Field limits table, headline formulas, pinned-skills order, honest note that ranking weights are directional | The limits table (re-labelled "reported, 2026"); "title field vs keywords field" idea; the honesty about numbers |
| 3 | [Pu11en/linkedin-recruiter-inbound](https://github.com/Pu11en/linkedin-recruiter-inbound) | MIT | Evidence bank with VERIFIED / NEEDS_DETAIL / UNVERIFIED tags; one recruiter-readable lane; refuses to claim algorithm facts; candidate performs every action | The facts sheet with source tags and the "confirm public" flag; the single-lane step; the no-algorithm-claims stance |
| 4 | [cyalcala/linkedin-profile-optimizer-skill](https://github.com/cyalcala/linkedin-profile-optimizer-skill) | none | Keyword map from target job descriptions; Featured as a proof shelf; outputs sized to the task | The keyword map from ads with a gap check; Featured as proof of outcomes |
| 5 | [BrianRWagner/ai-marketing-claude-code-skills](https://github.com/BrianRWagner/ai-marketing-claude-code-skills) (`linkedin-profile-optimizer`) | MIT | Quick / standard / deep modes; before-and-after bullets; an AI-search visibility check | Before-and-after format in the report; the idea that a profile is also read by AI tools |
| 6 | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills) (`skills/linkedin-profile`) | MIT | Short and clear: hook before the fold, first person, quality checklist, anti-patterns | The hook-first About and a short anti-pattern list |
| 7 | [ziqi-lydia/linkedin-profile-optimizer](https://github.com/ziqi-lydia/linkedin-profile-optimizer) | none | Studies benchmark profiles in the field before rewriting | Considered: not adopted, because comparing against other named people's profiles conflicts with the consent rule |
| 8 | [henriquesantanati/linkedin-profile-score](https://github.com/henriquesantanati/linkedin-profile-score) | MIT | Scores a profile from LinkedIn's own CSV data export, with a rubric | Left out on purpose: scoring belongs to `digital-footprint-multiplier`. Kept the PDF/export route as an input |
| 9 | [KBRmau/linkedin-profile-optimizer](https://github.com/KBRmau/linkedin-profile-optimizer) | none | Developer-focused audit from the profile PDF, one fix prompt per problem, bullet shape "action + metric + tech + impact" | The "save to PDF" input route; the idea of one fix per finding |
| 10 | [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) | MIT | A family of small LinkedIn skills (profile, post writer, hook extractor, humanizer, content planner) | The split between profile work and post work; hence the posting starter is four posts, not a content engine |

Also read for the limits table and Featured ideas: LinkedIn's own help pages on profile sections (no copying).

## What no source did, and this skill does

- Rewrites experience from outputs to outcomes with one sourced number per bullet, and refuses to invent a number (script check).
- Puts buried stories (press, paper, audit, TV) into Featured and a first post.
- Aims at a named target (role, place, date) and hands the score to `/digital-footprint-multiplier` instead of copying one.
- Consent rule for third-party profiles.

## Credit and licences

No code or prose from the above is included. The MIT-licensed projects are credited for ideas above; their licence texts require a notice only when text or code is copied. If a later version copies text from any of them, add its licence file here as `LICENSE-<name>.md` and name the passage.
