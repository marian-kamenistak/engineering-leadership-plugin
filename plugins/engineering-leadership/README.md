# engineering-leadership

Your team and your org. Why is the team slow, is the org top-heavy, are we ready to start a local
leadership meetup. Three skills and two open MCP servers, from the
[Engineering Leaders Community](https://www.engineeringleaders.io/). Author: Marian Kamenistak.

## Install

```
/plugin marketplace add marian-kamenistak/engineering-leadership-plugin
/plugin install engineering-leadership@marian-coach
```

## Components

- `skills/to-high-performing-team-in-6-sprints`: five delivery KPIs from your Jira CSV exports, the feedback loops behind them, a 6-sprint improvement plan and an HTML report. Needs Python 3 and pandas (`requirements.txt`)
- `skills/leadership-ratio-benchmark`: your manager-to-senior-IC split against the community's peer baseline
- `skills/community-launch-readiness`: five questions from the playbook used to open new cities, a verdict, the gap to close first
- `.mcp.json`: `elc-toolkit` (`https://www.engineeringleaders.io/mcp`) and
  `eng-leadership-toolkit` (`https://www.marian.coach/mcp`)

Both servers are authless streamable HTTP. Installing the plugin connects them; there is no key
to paste and no account to make.

The 6-sprint skill ships with empty CSV templates in `data/templates/`. The demo data lives in
its source repo, kept out of this plugin for size:
https://github.com/marian-kamenistak/ai-skill-to-high-performing-team-in-6-sprints

## Ask Claude

"Here are our Jira exports. Why is the team slow?" · "Is my engineering org too top-heavy?" ·
"Should I start a leadership meetup in my city?"

Moved: `team-lead-readiness` and `engineering-salary-calculator` now live in the `marian-coach`
plugin, in the same marketplace.

Privacy: https://www.engineeringleaders.io/privacy/ for `elc-toolkit`,
https://www.marian.coach/privacy-policy/ for `eng-leadership-toolkit`.

Full documentation: https://github.com/marian-kamenistak/engineering-leadership-plugin

MIT. The ratio benchmark and the readiness check also run in the browser, in the
[ELC Toolkit](https://www.engineeringleaders.io/toolkit/).
