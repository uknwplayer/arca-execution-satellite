# ARCA Execution Satellite

Public, sanitized execution satellite for the ARCA Executor Mesh.

This repository is intentionally **not ARCA Core**. It exists to prove that ARCA can treat a GitHub-hosted public runner as one replaceable Execution Provider without exposing private ARCA state.

## Safety boundary

The initial proof accepts only fixed execution profiles. It does **not** accept arbitrary shell commands, private repository contents, credentials, secrets, or Core mutation requests.

```text
ARCA private control plane
       |
       | publication/sanitization boundary (future)
       v
public execution request
       |
       v
GitHub-hosted public runner
       |
       v
bounded profile
       |
       v
result + SHA-256 + artifact
       |
       v
ARCA validates provenance before use
```

## Initial profiles

- `smoke` — verifies the execution substrate.
- `python-unit` — executes this satellite's public unit tests.

The workflow is **manual-only (`workflow_dispatch`)** in v0.1. A push does not automatically launch a runner.

## Authority

An execution result is evidence, not authority. The satellite cannot merge or promote ARCA Core code and does not receive Core credentials.
