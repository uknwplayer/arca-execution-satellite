# ARCA Public Executor Proof 004 — Multi-Executor

Status: PASS  
Date: 2026-09-20

## Objective

Prove that one ARCA Execution Provider family can expose multiple independent executors with different capabilities and identities, and that Jobs can be routed to a queue dedicated to the selected executor.

## Executor A — Linux

- executor_id: `github-public-linux`
- runner: `ubuntu-latest`
- queue: `queue/requests/*.json`
- request: `linux-smoke-002`
- dispatch commit: `34500814ce699ef475cbb9bd2fc68229e3285e2f`
- run: `35511955476`
- result: **success**
- contract tests: **10/10 PASS**
- request SHA-256: `e6339e69ae50c44d1d85986b4b0102085552b5bf2a8b847ea4850e87d413bbbe`
- semantic result SHA-256: `d9eed596c909795334f34bb28f77cdd8d2ff40f383e7777d762067ab2892e7cf`
- result file SHA-256: `6168df573ae7ad4753c935bb2ed2bd6ef5e0ce5f50b316720e35f7d0da22f903`
- artifact digest: `sha256:96dcb4e36ebe29a0d09c4da36bad8efdbb9ec67c5ed8d92bd0ed77f50fcd64f5`

## Executor B — Windows

- executor_id: `github-public-windows`
- runner: `windows-latest`
- queue: `queue/windows/requests/*.json`
- request: `windows-smoke-001`
- dispatch commit: `6f2268c80594ce30da658669b5123ef202bd2668`
- run: `35511900077`
- result: **success**
- contract tests: **10/10 PASS**
- request SHA-256: `beea6aa2a6f8db9434087fa3cde169763be055d599cb6b294fba48a3fc7e309a`
- semantic result SHA-256: `6325b5466d05b99b64617dd8edda4ad0ce6403fbd5f57d392d29b35b37555af5`
- result file SHA-256: `1c00e86bd6ca60e7d1c66ae2922b921de25dd021d567685ebd17ff2478de2d6a`
- artifact digest: `sha256:8e8b2518a913aa019cc22b19efa78f63042e08ea3b542bf1a5a69a01196ad83d`

## Routing implication

The lab scheduler now has enough information to distinguish:

```text
requires os.linux
  -> github-public-linux

requires os.windows
  -> github-public-windows
```

Both executors use the same provider-family contract but have separate identities, queues, runner operating systems, runs, artifacts and provenance.

## Authority boundary

Both executors remain public lab providers. Neither receives private ARCA state, secrets, arbitrary caller-controlled shell, or authority to merge/promote ARCA Core code.

This proof is not a Core promotion.
