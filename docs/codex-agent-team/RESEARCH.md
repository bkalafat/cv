# Agent team research

Research date: 2026-09-08

## Selection summary

The strongest candidates combining GitHub popularity, custom or specialist
agents, and Codex compatibility were:

| Candidate | Reported GitHub stars | Best fit | Source |
| --- | ---: | --- | --- |
| `ruvnet/ruflo` | 71.5K | Broad swarm/meta-harness orchestration | https://github.com/ruvnet/ruflo |
| `stablyai/orca` | 63.8K | Parallel agents with isolated worktrees | https://github.com/stablyai/orca |
| `wshobson/agents` | 39.5K | Portable Codex agent and skill catalog | https://github.com/wshobson/agents |
| `Yeachan-Heo/oh-my-claudecode` | 39.0K | Teams-first workflow model; Claude-oriented | https://github.com/Yeachan-Heo/oh-my-claudecode |
| `iOfficeAI/AionUi` | 32.7K | Desktop/cowork orchestration UI | https://github.com/iOfficeAI/AionUi |

Star counts are snapshots from the research run and can change. They are not
treated as a quality guarantee.

## Reddit signal and limitation

Recent RSS-visible discussions included:

- “Run an office of your clones to do your work with your ChatGPT subscription”
  (2026-08-15): https://www.reddit.com/r/ChatGPT/comments/1vozofe/
- “How on earth did people get anything done before agents?”
  (2026-08-31): https://www.reddit.com/r/ChatGPT/comments/1w39d70/

Reddit search endpoints returned rate-limit/access errors during the research
run, and RSS did not expose reliable score or comment counts. Therefore this
is a recent discussion signal, not a defensible “most upvoted in the last two
months” ranking. The repository selection should not be presented as a
statistically complete Reddit ranking.

## Codex format verified

OpenAI's current local Codex documentation defines project custom agents as
standalone TOML files under `.codex/agents/`. Each file requires:

- `name`
- `description`
- `developer_instructions`

Optional settings include `model`, `model_reasoning_effort`, `sandbox_mode`,
MCP servers, and skills configuration. Sources:

- https://developers.openai.com/codex/subagents/
- https://developers.openai.com/codex/config-reference/
- https://developers.openai.com/codex/guides/agents-md

The local team uses only the required fields plus conservative reasoning and
read-only settings where appropriate, so it remains easy to update as Codex
evolves.
