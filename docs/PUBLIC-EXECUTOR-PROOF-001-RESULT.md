# ARCA Public Executor Proof 001 — Result

Status: PASS  
Date: 2026-09-20  
Executor: `github-public-satellite`

## Objective

Prove that a public GitHub-hosted runner can act as a bounded ARCA Execution Provider without receiving private ARCA state, arbitrary shell input, secrets, or Core mutation authority.

## Run

- Workflow: `ARCA Public Executor Proof`
- Run: `35510728727`
- Run number: `1`
- Event: `workflow_dispatch`
- Head SHA: `6e31d3f38b9325de1ad6412c35126d82da648222`
- Profile: `smoke`
- Request ID: `manual-smoke-001`
- Conclusion: `success`

## Contract validation

The runner executed four public contract tests:

- arbitrary execution profile rejected;
- invalid request identifier rejected;
- smoke profile allowed;
- smoke profile executes without caller-supplied shell.

Result: **4/4 PASS**.

## Execution result

The bounded executor returned:

```json
{
  "executor_id": "github-public-satellite",
  "ok": true,
  "profile": "smoke",
  "request_id": "manual-smoke-001",
  "result_sha256": "3849ab8bda29b10047a3916c3a7a3a30a6f26c5af7ab206af03986e3f5df7e57"
}
```

The `result_sha256` is the executor's semantic hash over the canonical result payload before that hash field is appended.

The final `execution-result.json` file SHA-256 was:

```text
5ad1c4d65d88d31be821acc99318df7e410207df0caebaa5298aae6c1d1b98a5
```

GitHub stored artifact `arca-public-executor-result-35510728727`:

- artifact ID: `10605531035`
- size: 530 bytes
- artifact archive digest: `sha256:87a041e3e18745ae5abef45afac0d4c6ea7bcde7ba314c17527fa59242560a11`
- retention: 7 days

These hashes cover different objects and therefore are intentionally different.

## Authority boundary

This proof does not grant the provider authority over ARCA Core.

The provider:

- did not receive Core secrets;
- did not receive private repository contents;
- did not accept arbitrary caller-supplied shell;
- did not merge or promote code;
- produced an execution result only.

## Result

`github-public-satellite` is accepted as an **experimental lab Execution Provider** for bounded public jobs.

This is not Core promotion and does not alter ARCA Core.
