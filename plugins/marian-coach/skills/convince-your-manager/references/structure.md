# Structure of the business case (offline path)

This is the same content the MCP tool `build_mentoring_business_case` returns. Use it when the tool is not connected, so the user gets the same artefact either way. Slot the collected fields into the `{placeholders}`; keep the sentences as written. A field the user did not give renders as the visible fallback in brackets, never as a guess.

Placeholders: `{problem}` `{manager}` `{your_name}` `{company}` `{role}` `{decide_by}` `{n}` (at-risk seniors) `{ask}` (1,975 or 395) `{discounted}` `{roi}` `{kpis}`.

Fallbacks when a field is missing:

| Field | English | Czech |
|---|---|---|
| manager | `[manager's name]` | `[jméno šéfa]` |
| problem | `[the one problem I want fixed, e.g. delivery predictability stuck at 60%]` | `[ta jedna věc, kterou chci vyřešit, např. predictability dodávky se drží na 60 %]` |
| decide_by | `[Friday]` | `[pátku]` |
| your_name | `[your name]` | `[tvoje jméno]` |
| company | `the company` | `firmu` |
| kpis | the role's suggested KPIs below | the role's suggested KPIs below |

Constants: session 395 EUR · 6-session quarter 1,975 EUR (3 months) · replacement cost of one senior 40 to 60k EUR, midpoint 50,000 EUR for the math · Czech number format `1 975 EUR`.

---

## English

### Roles, example problems, suggested KPIs

Offer the examples as prompts. The user's own sentence wins.

**Engineering Manager**
- Example problems: delivery predictability stuck around 60% · two seniors I'm not sure we keep · an underperformance case I've been parking for a quarter
- Suggested KPIs: Zero regretted attrition in the next 2 quarters · Planned-vs-shipped ratio up to 85% · Every underperformance case actioned within 4 weeks, not parked

**Director of Engineering**
- Example problems: a team split / platform decision that's been open for two months · senior time-to-hire over 90 days · the flagship feature slipping a second quarter
- Suggested KPIs: The one stuck structural decision (team split, platform call, reorg) shipped within 6 weeks · Senior time-to-hire cut by a third · The slipping flagship feature back on its committed date

**VP of Engineering / CTO**
- Example problems: an org design decision I keep postponing · no successor for two of my leads · roadmap commitments not holding quarter over quarter
- Suggested KPIs: The open org design decision made and communicated · Leadership bench gaps named and closed with a successor plan · Roadmap commitments holding quarter over quarter

**Staff Engineer**
- Example problems: a cross-team initiative nobody owns end to end · a decision doc that keeps getting reopened · a promotion case with adjectives instead of evidence
- Suggested KPIs: One decision doc written, circulated, and accepted · One cross-team initiative led end to end · Promotion case documented with evidence, not adjectives

**Product Manager**
- Example problems: roadmap tradeoffs I lose to seniority, not numbers · surprise escalations from stakeholders every sprint · discovery-to-delivery predictability nobody measures
- Suggested KPIs: Roadmap tradeoffs defended with numbers, not seniority · Stakeholder alignment: no surprise escalations for a quarter · Discovery-to-delivery predictability measured and improving

### Email

Body order: greeting · p1 · p2 · p3 followed by the numbered KPI list · p4 · first-time line (only if first time in role) · at-risk line (only if at-risk seniors > 0) · p5 · close · signature (`{your_name}`). Blank line between paragraphs.

**Learning-budget version (`ld_budget`)**

- Subject: `Learning budget request: leadership mentoring, 1,975 EUR, reviewed at 90 days`
- Greeting: `Hi {manager},` (fallback `Hi [manager's name],`)
- p1: `I want to fix one thing in the next 90 days: {problem}. I'd like to use my learning budget on it.`
- p2: `The ask: 6 mentoring sessions over 3 months with Marian Kamenistak (marian.coach), an engineering leader who has run 3,662 sessions with people in my role. 6 sessions (5 paid + 1 free) = 1,975 EUR without VAT, invoiced to us by him as a sole trader, our PO number on the invoice.`
- p3: `What you'd see by session 6:` then the KPIs as `1. … 2. … 3. …`
- p4: `We put these on paper before session 1 and review them together at session 3 and session 6. The intro call is free, any session I rate under 8/10 isn't charged, and if the KPIs don't move in 90 days we stop.`

**No-budget-line version (`no_budget`, one pilot session)**

- Subject: `Budget ask: one 395 EUR mentoring session as a pilot, then we decide`
- Greeting: `Hi {manager},` (fallback `Hi [manager's name],`)
- p1: `I want to fix one thing in the next 90 days: {problem}. I'd rather test outside help on it before asking for a real budget, so this is a small ask.`
- p2: `The ask: one 60-minute session with Marian Kamenistak (marian.coach), an engineering leader who has run 3,662 sessions with people in my role. 395 EUR without VAT, invoiced to us by him as a sole trader, our PO number on the invoice. If it's useful, the session counts toward a 6-session quarter (1,975 EUR) when I continue within 30 days. If it isn't, we've spent 395 EUR and I stop bringing it up.`
- p3: `What I'd bring back from the pilot: a written plan for {problem}, with the targets for the next 90 days:` then the KPIs as `1. … 2. … 3. …`
- p4: `The intro call is free and any session I rate under 8/10 isn't charged.`

**Shared lines (both versions)**

- First time in role: `This is my first {role} seat. Most managers get their first leadership training about a decade after they start leading people (HBR / Zenger Folkman). I'd rather not run that experiment on this team.`
- At risk, n = 1: `One more number: we have 1 senior person I'm not sure we keep. Replacing one costs 40 to 60k EUR. This costs 1,975.`
- At risk, n ≥ 2: `One more number: we have {n} senior people I'm not sure we keep. Replacing one costs 40 to 60k EUR. This costs 1,975.`
- p5: `Pricing is public at marian.coach/pricing/. I'll write up what I learn for the team.`
- Close: `Can I get a yes by {decide_by}?`
- Signature: `{your_name}` (fallback `[your name]`)

### Slack / Teams version

`{manager}, quick one. I want to fix one thing in the next 90 days: {problem}. I'd like to use {budget_line} for 1:1 mentoring with Marian Kamenistak (marian.coach): {ask_line}. Targets on paper before session 1, review at 3 and 6, any session I rate under 8/10 isn't charged. Sending you a one-pager with the numbers. Ok to decide by {decide_by}?`

- `{budget_line}`: ld_budget → `my learning budget` · no_budget → `a small pilot budget`
- `{ask_line}`: ld_budget → `6 sessions over 3 months, 1,975 EUR` · no_budget → `one 395 EUR session first, then we decide`

### Five talking points

1. `The problem is {problem}. Fixed looks like: {kpis}.` (KPIs joined with `; `)
2. `This is 1:1 with someone who held my role, on my situation, not a course. {ask_line}.`
3. `Risk is capped: free intro call, sessions under 8/10 aren't charged, review at session 3, stop at 90 days if nothing moves.`
4. At risk > 0: `Money: replacing one of the {n} seniors we might lose costs 40 to 60k EUR. This is {ask} EUR.` · At risk = 0: `Money: one prevented departure or one quarter of roadmap slip pays for it 20 times over.`
5. `I'll write up what I learn for the team, and the invoice goes to us with our PO number.`

### One-pager (12 sections, this order)

Title: `Mentoring engagement proposal: {your_name}, {role}`

1. **The problem to fix in the next 90 days** — `{problem}` (capitalise the first letter)
2. **What success looks like by session 6** — the KPIs as bullets
3. **What it is**
   - ld_budget: `6 one-hour 1:1 sessions over 3 months, plus async access between sessions, with Marian Kamenistak (marian.coach). Engineering leader; scaled engineering at Mews from 8 to 80 teams through Series C; 3,662 mentoring sessions with 317 leaders since 2019; average session rating 9.79/10.`
   - no_budget: `Pilot: one 60-minute 1:1 session with Marian Kamenistak (marian.coach). Engineering leader; scaled engineering at Mews from 8 to 80 teams through Series C; 3,662 mentoring sessions with 317 leaders since 2019; average session rating 9.79/10. If continued within 30 days, the session counts toward the 6-session quarter.`
4. **Investment** (table)
   - ld_budget: `6 sessions (5 paid + 1 free)` → `1,975 EUR without VAT` · `Intro call` → `free` · `Invoiced to` → `{company} by Marian Kamenistak (sole trader), PO number on the invoice` · `Payment` → `on invoice`
   - no_budget: `Pilot: 1 session` → `395 EUR without VAT` · `If continued within 30 days` → `counts toward the 6-session quarter, 1,975 EUR total` · `Intro call` → `free` · `Invoiced to` → `{company} by Marian Kamenistak (sole trader), PO number on the invoice` · `Payment` → `on invoice`
5. **How we measure it** — `Targets on paper before session 1, baseline written down` · `Review with my manager at session 3` · `Final review at session 6` · `Stop clause: no movement in 90 days, we stop`
6. **Risk controls** — `Intro call is free` · `Any session rated under 8/10 isn't charged` · `Public pricing: marian.coach/pricing/`
7. **Budget source** — ld_budget: `Learning & development budget, individual allocation.` · no_budget: `Discretionary team budget; one session as a pilot before any larger ask.`
8. **Why now** (only if first time in role) — `First {role} seat. HBR / Zenger Folkman (2012): the average manager gets first leadership training at 42, about a decade after starting to lead people. CEB/Gartner: about 60% of new managers underperform or fail in their first two years.`
9. **Alternatives considered** (only if any were given) — one bullet per alternative, then the closing bullet:
   - conference: `Conference: similar money, two days of talks, no follow-through on my problem.`
   - course: `Course: cheaper, generic, no accountability.`
   - internal_coach: `Internal mentor or coach: free, but inside my reporting line, so the messy version of the problem doesn't get said.`
   - closing: `1:1 on my problem with targets and a stop clause is the cheapest of these per outcome.`
10. **Napkin math**
    - at risk > 0: the math lines (below), ending with `Halved to be safe: {discounted} EUR against {ask} EUR = {roi}x.`
    - at risk = 0: `Replacing one senior engineer costs 40 to 60k EUR (Gallup: one-half to two times salary). This costs {ask} EUR. One prevented departure or one quarter of roadmap slip pays for it 20 times over.`
11. **What I give back** — `A written summary for the team after session 6.`
12. **Decision requested by** — `{decide_by}. Next step: I book the free intro call and bring back the plan for sign-off.`

### Napkin math (how the numbers are computed)

- Attrition line: `Attrition avoided: {n} senior person/people at risk x 50,000 EUR (replacing a senior costs 40 to 60k EUR; Gallup: one-half to two times salary) = {value} EUR` where value = n x 50,000.
- Optional lines, only if the user volunteers the inputs (the tool accepts them as legacy fields): `Cost of delay avoided: {rev} EUR annual revenue on the slipping item / 4 (one quarter earlier) = {value} EUR` · `Team lift: {team} engineers x {sal} EUR x 2% (a deliberately conservative lift) = {value} EUR`.
- Total = sum of the lines. Discounted = total / 2. ROI = discounted / ask, one decimal. Closing line: `Halved to be safe (the CFO discount): {discounted} EUR against {ask} EUR = {roi}x`. Note: `After halving, the case clears the ask {roi} times over.`
- Zero at-risk and no optional inputs: no total is claimed. Note: `No at-risk seniors given, so no total is claimed. Replacing one senior costs 40 to 60k EUR; against {ask} EUR one prevented departure pays for it 20 times over.`

Worked check: 2 at-risk seniors, learning budget → 2 x 50,000 = 100,000 EUR; halved 50,000; against 1,975 = 25.3x.

### How to size the value (static framing, precedes the math in the tool's report)

Heading: `What the mentoring is worth over 6 months, added up from four lines`
- `Money saved: attrition prevented, mis-hires avoided, firefighting hours cut`
- `Cost of delay avoided: roadmap items shipping on time instead of a quarter late`
- `Missed opportunity recovered: the initiative nobody had bandwidth to lead`
- `Roadmap slippage avoided: commitments that hold, planned vs shipped`

Rule: `Count only the lines you can defend in front of a CFO, then halve the total. If it still clears the ask several times over, send it. Managers approve numbers with a review date, rarely feelings.`

### If they push back (five objections)

1. **"There's no budget for this."** — `Most companies keep an L&D or conference line per person; this is what it's for. If ours is spent, I can start with one 395 EUR session and we decide after, or we split it across two quarters.`
2. **"Why not our internal coach or a senior colleague?"** — `I'll use them too. This is someone who ran engineering at scale and sits outside my reporting line, so I can bring the messy version of the problem. Two different tools.`
3. **"Why not a course or a conference?"** — `A course covers the general case; my problem is specific and has a deadline. The sessions are on my actual situation, with targets we agreed. And it's cheaper than one recruiter fee.`
4. **"How do we know it works?"** — `Targets on paper before session 1, review at session 3 and 6, sessions I rate under 8/10 aren't charged, and we stop at 90 days if nothing moves. That's more measurement than most training gets.`
5. **"What if you leave after we pay for it?"** — `People usually leave when they stall in a role, not after someone invests in them. This is about doing this job better here, and I'll write up what I learn for the team.`

### Sources (the whole list; nothing else is cited)

1. Replacing an employee costs one-half to two times their annual salary. — Gallup, 2019 — https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx
2. Average age at first leadership training: 42, about a decade after first supervising people. — HBR / Zenger Folkman, 2012 — https://hbr.org/2012/12/why-do-we-wait-so-long-to-trai
3. About 60% of new managers underperform or fail in their first two years. — CEB / Gartner (secondary citation) — https://www.forbes.com/sites/williamarruda/2023/02/15/why-most-new-managers-fail-and-how-to-prevent-it/ (only when first time in role)
4. Meta-analysis of 39 randomised samples: workplace coaching has a moderate, replicated positive effect. — De Haan & Nilsson, Academy of Management Learning & Education, 2023 — https://journals.aom.org/doi/10.5465/amle.2022.0107
5. 3,662 sessions, 317 leaders since 2019, average session rating 9.79/10. — marian.coach — https://www.marian.coach/engineering-leadership-statistics/

### Engagement terms

- 6 sessions across 3 months
- Targets on paper before session 1
- Review at session 3, final review at session 6
- Intro call free
- Any session rated under 8/10 is not charged

### Next steps

- Send the email first, then ask for 15 minutes
- Bring the one-pager to the conversation, leave it with them to forward
- Book the free intro call once you have a yes: https://www.marian.coach/meet
- Invoice goes to your company with your PO number

### Worked examples (already public; illustration only, never transplant their numbers into the user's case)

- **Engineering Manager, team of 8.** Fully loaded team cost around 800,000 EUR a year. One senior engineer has a foot out the door and delivery predictability sits near 60%. KPIs: regretted attrition zero, planned-vs-shipped from 60% to 85%, the open underperformance case actioned within 4 weeks. Math: counting only the retention line, replacing that senior costs 40 to 60k EUR, the pack costs 1,975 EUR. One prevented departure pays for the mentoring 15 times over.
- **Director, 3 teams, 24 engineers.** A reorg decision has been stuck for two quarters, and the flagship feature with roughly 300,000 EUR of annual revenue attached is slipping with it. KPIs: reorg decided and shipped within 6 weeks, the feature back on its committed date, both open senior roles closed. Math: counting only cost of delay, shipping one quarter earlier on a 300,000 EUR revenue line is worth about 75,000 EUR. Halved for CFO skepticism, that is 37,000 against 1,975. Still 14x.
- **Staff Engineer.** A build-vs-buy platform decision with 100,000+ EUR a year riding on it, and influence that stops at the team boundary. KPIs: the decision doc written, defended and accepted; one cross-team initiative led end to end; the promotion case documented. Math: one platform choice gone wrong recurs every year at six figures, and replacing a staff engineer runs 6 to 9 months of salary. Either line alone beats the pack price by an order of magnitude.

---

## Czech (čeština)

Diacritics on. Default tykání; `formal` = vykání. Where a line differs, both are given as `ty:` / `Vy:`. English tech terms stay untranslated (session, intro call, KPI, PO, review). Role labels stay English (Engineering Manager, Director of Engineering, VP of Engineering / CTO, Staff Engineer, Product Manager).

### Příklady problémů a navrhované KPI

**Engineering Manager**
- Příklady: predictability dodávky se drží kolem 60 % · dva senioři, u kterých hrozí, že odejdou · underperformance case, který odkládám už kvartál
- KPI: Nulová nechtěná fluktuace v příštích 2 kvartálech · Poměr naplánováno vs. dodáno nad 85 % · Každý underperformance case řešený do 4 týdnů, ne odložený

**Director of Engineering**
- Příklady: rozdělení týmu / platformové rozhodnutí, které je otevřené dva měsíce · time-to-hire seniorů přes 90 dní · vlajková feature klouže druhý kvartál
- KPI: Jedno zaseklé strukturální rozhodnutí (rozdělení týmu, platforma, reorg) hotové do 6 týdnů · Time-to-hire seniorů kratší o třetinu · Klouzající vlajková feature zpátky na slíbeném termínu

**VP of Engineering / CTO**
- Příklady: org design rozhodnutí, které pořád odkládám · žádný nástupce za dva z mých leadů · roadmap commitmenty nedrží kvartál po kvartálu
- KPI: Otevřené org design rozhodnutí přijaté a odkomunikované · Mezery v leadership bench pojmenované a zavřené plánem nástupnictví · Roadmap commitmenty drží kvartál po kvartálu

**Staff Engineer**
- Příklady: cross-team iniciativa, kterou nikdo nevlastní od začátku do konce · decision doc, který se pořád znovu otvírá · promotion case s přídavnými jmény místo důkazů
- KPI: Jeden decision doc napsaný, obeslaný a přijatý · Jedna cross-team iniciativa vedená od začátku do konce · Promotion case doložený důkazy, ne přídavnými jmény

**Product Manager**
- Příklady: roadmap tradeoffy, které prohrávám na senioritu, ne na čísla · překvapivé eskalace od stakeholderů každý sprint · predictability od discovery po delivery, kterou nikdo neměří
- KPI: Roadmap tradeoffy obhájené čísly, ne senioritou · Sladění se stakeholdery: kvartál bez překvapivé eskalace · Predictability od discovery po delivery měřená a rostoucí

### E-mail

Pořadí: oslovení · p1 · p2 · p3 + číslovaný seznam KPI · p4 · řádek první role (jen když je to první role) · řádek o seniorech v riziku (jen když > 0) · p5 · závěr · podpis (`{your_name}`).

**Verze s rozpočtem na rozvoj (`ld_budget`)**

- Předmět: `Žádost o rozpočet na rozvoj: leadership mentoring, 1 975 EUR, vyhodnocení po 90 dnech`
- Oslovení: ty `{manager} ahoj,` / Vy `Dobrý den, {manager},` (bez jména: ty `Ahoj,` / Vy `Dobrý den,`)
- p1: `Chci v příštích 90 dnech vyřešit jednu konkrétní věc: {problem}. Chci na to použít svůj rozpočet na rozvoj.`
- p2: `O co jde: 6 mentoringových sessions během 3 měsíců s Marianem Kamenistakem (marian.coach), engineering leaderem, který má za sebou 3 662 sessions s lidmi v mé roli. 6 sessions (5 placených + 1 zdarma) = 1 975 EUR bez DPH, fakturuje nám jako OSVČ, na faktuře bude naše číslo objednávky.`
- p3: ty `Co uvidíš do šesté session:` / Vy `Co uvidíte do šesté session:` + KPI `1. … 2. … 3. …`
- p4: `Cíle dáme na papír před první session a společně je projdeme po třetí a po šesté. Intro call je zdarma, session, kterou ohodnotím pod 8/10, se neplatí, a když se KPI za 90 dní nepohnou, končíme.`

**Verze bez rozpočtové položky (`no_budget`, jedna pilotní session)**

- Předmět: `Žádost o rozpočet: jedna mentoringová session za 395 EUR jako pilot, pak se rozhodneme`
- Oslovení: stejné jako výše
- p1: `Chci v příštích 90 dnech vyřešit jednu konkrétní věc: {problem}. Než budu žádat o skutečný rozpočet, chci si pomoc zvenku nejdřív vyzkoušet, takže je to malá žádost.`
- p2: `O co jde: jedna 60minutová session s Marianem Kamenistakem (marian.coach), engineering leaderem, který má za sebou 3 662 sessions s lidmi v mé roli. 395 EUR bez DPH, fakturuje nám jako OSVČ, na faktuře bude naše číslo objednávky. Když to bude užitečné, session se započítá do kvartálu o 6 sessions (1 975 EUR), pokud budu pokračovat do 30 dnů. Když ne, stálo nás to 395 EUR a už to nebudu otvírat.`
- p3: `Co z pilotu přinesu: písemný plán na {problem} s cíli na příštích 90 dní:` + KPI
- p4: `Intro call je zdarma a session, kterou ohodnotím pod 8/10, se neplatí.`

**Společné řádky**

- První role: `Je to moje první role jako {role}. Většina manažerů dostane první leadership trénink zhruba deset let po tom, co začne vést lidi (HBR / Zenger Folkman). Nechci ten experiment dělat na tomhle týmu.`
- V riziku, n = 1: `Ještě jedno číslo: máme 1 seniora, u kterého hrozí, že odejde. Nahradit ho stojí 40 až 60 tisíc EUR. Tohle stojí 1 975.`
- V riziku, n = 2 až 4: `Ještě jedno číslo: máme {n} seniory, u kterých hrozí, že odejdou. Nahradit jednoho stojí 40 až 60 tisíc EUR. Tohle stojí 1 975.`
- V riziku, n ≥ 5: `Ještě jedno číslo: máme {n} seniorů, u kterých hrozí, že odejdou. Nahradit jednoho stojí 40 až 60 tisíc EUR. Tohle stojí 1 975.`
- p5: `Ceník je veřejný na marian.coach/cs/cenik/. Co se naučím, sepíšu pro tým.`
- Závěr: ty `Dostanu do {decide_by} ano?` / Vy `Dostanu od Vás do {decide_by} ano?`
- Podpis: `{your_name}` (bez jména `[tvoje jméno]`)

### Verze pro Slack / Teams

ty: `{manager}, rychlá věc. Chci v příštích 90 dnech vyřešit jednu věc: {problem}. Chci na to použít {budget_line} na 1:1 mentoring s Marianem Kamenistakem (marian.coach): {ask_line}. Cíle na papíře před první session, review po třetí a šesté, session pod 8/10 se neplatí. Pošlu ti jednostránkový podklad s čísly. Rozhodneme do {decide_by}?`

Vy: totéž s `Pošlu Vám jednostránkový podklad s čísly.`

- `{budget_line}`: ld_budget → `svůj rozpočet na rozvoj` · no_budget → `malý pilotní rozpočet`
- `{ask_line}`: ld_budget → `6 sessions během 3 měsíců, 1 975 EUR` · no_budget → `nejdřív jedna session za 395 EUR, pak se rozhodneme`

### Pět bodů do rozhovoru

1. `Problém: {problem}. Vyřešeno znamená: {kpis}.`
2. `Je to 1:1 s někým, kdo dělal mou roli, na mé konkrétní situaci, ne kurz. {ask_line}.`
3. `Riziko je omezené: intro call zdarma, session pod 8/10 se neplatí, review po třetí session, po 90 dnech končíme, když se nic nepohne.`
4. V riziku > 0: `Peníze: nahradit jednoho z {n} seniorů, které můžeme ztratit, stojí 40 až 60 tisíc EUR. Tohle je {ask} EUR.` · V riziku = 0: `Peníze: jeden odchod, kterému předejdeme, nebo jeden kvartál skluzu na roadmapě to zaplatí dvacetkrát.`
5. `Co se naučím, sepíšu pro tým, a faktura jde na firmu s naším číslem objednávky.`

### Jednostránkový podklad (12 sekcí, v tomto pořadí)

Titulek: `Návrh mentoringu: {your_name}, {role}`

1. **Co chci vyřešit v příštích 90 dnech** — `{problem}`
2. **Jak vypadá úspěch do šesté session** — KPI jako odrážky
3. **Co to je**
   - ld_budget: `6 hodinových 1:1 sessions během 3 měsíců plus async přístup mezi nimi, s Marianem Kamenistakem (marian.coach). Engineering leader; v Mews rozšířil engineering z 8 na 80 týmů přes Series C; 3 662 mentoringových sessions se 317 leadery od roku 2019; průměrné hodnocení sessions 9,79/10.`
   - no_budget: `Pilot: jedna 60minutová 1:1 session s Marianem Kamenistakem (marian.coach). Engineering leader; v Mews rozšířil engineering z 8 na 80 týmů přes Series C; 3 662 mentoringových sessions se 317 leadery od roku 2019; průměrné hodnocení sessions 9,79/10. Při pokračování do 30 dnů se session započítá do kvartálu o 6 sessions.`
4. **Investice** (tabulka)
   - ld_budget: `6 sessions (5 placených + 1 zdarma)` → `1 975 EUR bez DPH` · `Intro call` → `zdarma` · `Faktura na` → `{company}, vystaví Marian Kamenistak (OSVČ), číslo objednávky na faktuře` · `Platba` → `na fakturu`
   - no_budget: `Pilot: 1 session` → `395 EUR bez DPH` · `Při pokračování do 30 dnů` → `započítá se do kvartálu o 6 sessions, celkem 1 975 EUR` · `Intro call` → `zdarma` · `Faktura na` → `{company}, vystaví Marian Kamenistak (OSVČ), číslo objednávky na faktuře` · `Platba` → `na fakturu`
5. **Jak to měříme** — `Cíle na papíře před první session, výchozí stav zapsaný` · `Společné review po třetí session` · `Závěrečné review po šesté session` · `Stop klauzule: když se za 90 dní nic nepohne, končíme`
6. **Kontrola rizika** — `Intro call zdarma` · `Session hodnocená pod 8/10 se neplatí` · `Veřejný ceník: marian.coach/cs/cenik/`
7. **Zdroj rozpočtu** — ld_budget: `Rozpočet na vzdělávání a rozvoj (L&D), individuální alokace.` · no_budget: `Diskreční rozpočet týmu; před větší žádostí jedna session jako pilot.`
8. **Proč teď** (jen první role) — `První role jako {role}. HBR / Zenger Folkman (2012): průměrný manažer dostane první leadership trénink ve 42 letech, zhruba deset let po tom, co začne vést lidi. CEB/Gartner: zhruba 60 % nových manažerů v prvních dvou letech nepodává výkon nebo selže.`
9. **Zvažované alternativy** (jen když byly zadané) — `Konference: podobné peníze, dva dny přednášek, žádné pokračování na mém problému.` · `Kurz: levnější, obecný, bez zodpovědnosti za výsledek.` · `Interní mentor nebo kouč: zdarma, ale uvnitř mé reportovací linie, takže neřeknu tu neučesanou verzi problému.` · závěr: `1:1 na mém problému s cíli a stop klauzulí vychází na výsledek nejlevněji.`
10. **Počty na ubrousek**
    - v riziku > 0: řádky výpočtu, závěr `Pro jistotu půlka: {discounted} EUR proti {ask} EUR = {roi}x.`
    - v riziku = 0: `Nahradit jednoho senior engineera stojí 40 až 60 tisíc EUR (Gallup: půl až dvojnásobek platu). Tohle stojí {ask} EUR. Jeden odchod, kterému předejdeme, nebo jeden kvartál skluzu to zaplatí dvacetkrát.`
11. **Co dám zpět** — `Písemné shrnutí pro tým po šesté session.`
12. **Rozhodnutí potřebuji do** — `{decide_by}. Další krok: rezervuji intro call zdarma a přinesu plán ke schválení.`

### Počty na ubrousek (řádky)

- `Odvrácená fluktuace: {n} senior/senioři v riziku x 50 000 EUR (nahradit seniora stojí 40 až 60 tisíc EUR; Gallup: půl až dvojnásobek platu) = {value} EUR`
- volitelné: `Odvrácená cena zpoždění: {rev} EUR ročních tržeb na klouzající položce / 4 (o kvartál dřív) = {value} EUR` · `Zlepšení týmu: {team} engineerů x {sal} EUR x 2 % (záměrně konzervativní odhad) = {value} EUR`
- závěr: `Pro jistotu půlka (CFO diskont): {discounted} EUR proti {ask} EUR = {roi}x` · poznámka: `Po půlení případ pokryje žádanou částku {roi}x.`
- nula v riziku: `Bez zadaných seniorů v riziku nic nenárokujeme. Nahradit jednoho seniora stojí 40 až 60 tisíc EUR; proti {ask} EUR to jeden odvrácený odchod zaplatí dvacetkrát.`

### Jak spočítat hodnotu

`Kolik mentoring vynese za 6 měsíců, sečteno ze čtyř řádků`
- `Ušetřené peníze: odvrácený odchod, nepovedený nábor, hodiny strávené hašením`
- `Odvrácená cena zpoždění: položky roadmapy dodané včas, ne o kvartál později`
- `Získaná příležitost: iniciativa, na kterou nikdo neměl kapacitu`
- `Odvrácené klouzání roadmapy: závazky, které drží, plán vs. dodáno`

Pravidlo: `Počítej jen řádky, které obhájíš před CFO, a pak výsledek vyděl dvěma. Když pořád několikanásobně převyšuje částku, o kterou žádáš, pošli to. Manažeři schvalují čísla s termínem review, pocity málokdy.`

### Když budou namítat

1. **„Na tohle nemáme rozpočet."** — `Většina firem má na osobu položku L&D nebo konference; přesně na tohle je. Když je naše vyčerpaná, můžu začít jednou session za 395 EUR a rozhodneme se potom, nebo to rozdělíme do dvou kvartálů.`
2. **„Proč ne náš interní kouč nebo zkušenější kolega?"** — `Ty využiju taky. Tohle je někdo, kdo vedl engineering ve velkém a stojí mimo mou reportovací linii, takže můžu přinést tu neučesanou verzi problému. Dva různé nástroje.`
3. **„Proč ne kurz nebo konference?"** — `Kurz řeší obecný případ; můj problém je konkrétní a má termín. Sessions jsou o mé skutečné situaci s cíli, na kterých se dohodneme. A je to levnější než jedna provize recruiterovi.`
4. **„Jak poznáme, že to funguje?"** — `Cíle na papíře před první session, review po třetí a šesté, session pod 8/10 se neplatí a po 90 dnech končíme, když se nic nepohne. To je víc měření, než má většina školení.`
5. ty **„Co když po tom odejdeš?"** / Vy **„Co když po tom odejdete?"** — `Lidi obvykle odcházejí, když v roli stagnují, ne po tom, co do nich někdo investoval. Tohle je o tom dělat tuhle práci líp tady, a co se naučím, sepíšu pro tým.`

### Zdroje

1. Nahradit zaměstnance stojí půl až dvojnásobek jeho ročního platu. — Gallup, 2019 — https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx
2. Průměrný věk při prvním leadership tréninku: 42, zhruba deset let po tom, co člověk začne vést lidi. — HBR / Zenger Folkman, 2012 — https://hbr.org/2012/12/why-do-we-wait-so-long-to-trai
3. Zhruba 60 % nových manažerů v prvních dvou letech nepodává výkon nebo selže. — CEB / Gartner (sekundární citace) — https://www.forbes.com/sites/williamarruda/2023/02/15/why-most-new-managers-fail-and-how-to-prevent-it/ (jen první role)
4. Metaanalýza 39 randomizovaných vzorků: koučink na pracovišti má střední, opakovaně potvrzený pozitivní efekt. — De Haan & Nilsson, Academy of Management Learning & Education, 2023 — https://journals.aom.org/doi/10.5465/amle.2022.0107
5. 3 662 sessions, 317 leaderů od roku 2019, průměrné hodnocení sessions 9,79/10. — marian.coach — https://www.marian.coach/cs/engineering-leadership-statistics/

### Podmínky

- 6 sessions během 3 měsíců
- Cíle na papíře před první session
- Review po třetí session, závěrečné po šesté
- Intro call zdarma
- Session hodnocená pod 8/10 se neplatí

### Další kroky

- Nejdřív pošli e-mail, pak si řekni o 15 minut
- Vezmi na schůzku jednostránkový podklad a nech jim ho k přeposlání
- Až máš ano, rezervuj intro call zdarma: https://www.marian.coach/meet
- Faktura jde na firmu s vaším číslem objednávky

### Spočítané příklady (veřejné; jen ilustrace, čísla nikdy nepřenášej do případu uživatele)

- **Engineering Manager, tým 8 lidí.** Plně nákladový tým kolem 800 000 EUR ročně. Jeden senior má nohu ze dveří a predikovatelnost dodávek se drží kolem 60 %. KPI: nulová nechtěná fluktuace, plán vs. dodáno z 60 % na 85 %, otevřený případ podvýkonu vyřešený do 4 týdnů. Počty: jen retenční řádek, nahradit toho seniora stojí 40 až 60 tisíc EUR, balíček stojí 1 975 EUR. Jeden odvrácený odchod zaplatí mentoring patnáctkrát.
- **Director, 3 týmy, 24 engineerů.** Rozhodnutí o reorganizaci leží dva kvartály a s ním klouže i vlajková funkce, na které visí zhruba 300 000 EUR ročních tržeb. KPI: reorganizace rozhodnutá a nasazená do 6 týdnů, funkce zpět na slíbeném datu, obě otevřené seniorní pozice zavřené. Počty: jen cena zpoždění, dodat o kvartál dřív na tržbách 300 000 EUR má hodnotu asi 75 000 EUR. Po vydělení dvěma kvůli skepsi CFO je to 37 000 proti 1 975. Pořád 14x.
- **Staff Engineer.** Rozhodnutí build vs. buy, na kterém visí 100 000+ EUR ročně, a vliv, který končí na hranici týmu. KPI: decision doc napsaný, obhájený a přijatý; jedna mezitýmová iniciativa dotažená od začátku do konce; podklad k povýšení sepsaný. Počty: špatná volba platformy se vrací každý rok v řádu statisíců a nahradit staff engineera stojí 6 až 9 měsíčních platů. Kterýkoli z těch řádků sám o sobě překonává cenu balíčku o řád.
