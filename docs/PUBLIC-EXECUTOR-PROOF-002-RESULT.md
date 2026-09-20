# ARCA Public Executor Proof 002 — Result

Status: PASS  
Date: 2026-09-20  
Executor: `github-public-satellite`

## Objective

Prove that the public execution satellite can perform an actual bounded Python workload, rather than only a substrate smoke check.

## Run

- Workflow: `ARCA Public Executor Proof`
- Run: `35510862300`
- Run number: `2`
- Event: `workflow_dispatch`
- Head SHA: `6e13af7658c30e0ba43758dc9033bd3e72c4a77a`
- Profile: `python-unit`
- Request ID: `python-unit-001`
- Conclusion: `success`

## Pre-execution contract validation

The satellite first re-ran its public boundary tests.

Result: **4/4 PASS**.

The tests confirm that arbitrary execution profiles and invalid request identifiers are rejected while the bounded profiles remain usable.

## Python workload

The `python-unit` profile invoked the satellite's public unit-test workload using an argv-based Python subprocess.

The profile completed with exit code `0`, causing the bounded executor to return:

```json
{
  "executor_id": "github-public-satellite",
  "ok": true,
  "profile": "python-unit",
  "request_id": "python-unit-001",
  "result_sha256": "6177538ac9c2de3394626ab888f25c6d3d4da312db1e43ee7455d896326986a3"
}
```

The final `execution-result.json` file SHA-256 was:

```text
8fec6dce3572d3f90fc34dfcf088cbec3a9b9f8d281ce7e149db7d53a2c729f3
```

GitHub stored artifact `arca-public-executor-result-35510862300`:

- artifact ID: `10605305811`
- size: 585 bytes
- artifact archive digest: `sha256:11f5ac5c61059cf8ca14f920ae76166648207830ce1fbf0b3d2bef8bab4fb0a5`
- retention: 7 days

The semantic result hash, final JSON file hash and artifact archive digest intentionally cover different objects.

## Result

The provider has now demonstrated both:

1. execution-substrate availability; and
2. successful bounded Python workload execution.

`github-public-satellite` therefore remains **LAB_ADMITTED / EXPERIMENTAL_VERIFIED** as a public Execution Provider.

This evidence does not promote the provider into ARCA Core and grants no authority to mutate or merge Core code.
