# ARCA Public Executor Proof 003 — Automatic Git Queue Dispatch

Status: PASS  
Date: 2026-09-20  
Executor: `github-public-satellite`

## Objective

Prove that an ARCA-compatible dispatcher can start a bounded public execution without a human pressing **Run workflow** and without requiring the dispatcher to hold GitHub Actions write authority.

## Dispatch

A bounded request was created at:

`queue/requests/auto-dispatch-001.json`

Dispatch commit SHA:

`ee1dcbfd4e6864aea54c3d90741811f29bc8e21c`

The queue filename acts as an idempotency key. The request declared:

- profile: `smoke`;
- public_only: `true`;
- secrets_allowed: `false`.

The path-scoped push event automatically started the queued executor.

## Correlated run

- Run ID: `35511368977`
- Event: `push`
- Head SHA: `ee1dcbfd4e6864aea54c3d90741811f29bc8e21c`
- Conclusion: `success`

The run was correlated directly by the dispatch commit SHA.

## Boundary validation

Nine contract tests passed before execution.

The queue contract rejects:

- arbitrary profiles;
- invalid request identifiers;
- mismatched request filename and request ID;
- non-public jobs;
- secret-bearing jobs;
- unknown request fields, including caller-controlled shell fields.

Result: **9/9 PASS**.

## Result hashes

Request SHA-256:

`f01684685f55189e9a7370194c21b67e2cf3f88a2d878f35d1d66dbe585431a7`

Semantic result SHA-256:

`f33d8fa0c3514f030b3020840a2fe9987107d49e7303631adb083660d3df9259`

Final `execution-result.json` SHA-256:

`5d793553cc514ee3514e4a049f67650f8cba42d4e1392fa545c059e23956691b`

Artifact archive:

- artifact ID: `10605337236`
- name: `arca-queued-executor-result-35511368977`
- digest: `sha256:6da4b0600e78fddf1a88fb8e9d010a377f9ab20fdefad8d0afddeecfa0d25ca7`

## Architectural result

The following path is now demonstrated:

```text
bounded ARCA Job
      |
      v
Git queue request
      |
      v
dispatch commit SHA
      |
      v
GitHub public execution satellite
      |
      v
validated result + artifact + provenance
```

This proves an automatic provider-dispatch mechanism. It does not grant the satellite authority over ARCA Core and does not promote any lab component into Core.
