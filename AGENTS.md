# Local Codex agent team

This project uses the custom agents in `.codex/agents/`.

## Recommended workflow

1. Ask `planner` to define scope and acceptance criteria.
2. Ask `architect` to map the affected files and design the solution.
3. Ask `implementer` to make the agreed changes.
4. Run `tester` for targeted validation.
5. Run `security-reviewer` and `release-reviewer` before merging.

Use parallel agents only for independent read-only work. Keep implementation
and validation ordered when one depends on the other. CV content belongs in
`_data/*.yml`; avoid editing templates when a data-only change is sufficient.
