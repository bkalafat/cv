# Codex agent team

This folder contains a project-local Codex subagent team. Codex discovers the
profiles from [`../../.codex/agents/`](../../.codex/agents/) and the project
rules from [`../../AGENTS.md`](../../AGENTS.md).

The six roles are intentionally narrow:

- `planner`: scope and acceptance criteria
- `architect`: repository mapping and design
- `implementer`: code or content changes
- `tester`: targeted validation
- `security-reviewer`: high-confidence security review
- `release-reviewer`: final release gate

The setup is inspired by the patterns found in `wshobson/agents`
(portable Codex agent/skill catalog), `ruvnet/ruflo` (planner/swarm/reviewer
orchestration), and `stablyai/orca` (parallel isolated worktrees). It is kept
small and native to Codex rather than installing a large external framework.

## Use

From the repository root, ask Codex to use the named agents, for example:

```text
Use planner and architect in parallel. After their results, have implementer
make the change, then run tester, security-reviewer, and release-reviewer.
```

Project-scoped configuration is in [`../../.codex/config.toml`](../../.codex/config.toml).
Codex only loads it when the project is trusted.
