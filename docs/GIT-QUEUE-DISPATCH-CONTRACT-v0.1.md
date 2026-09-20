# Git Queue Dispatch Contract v0.1

Status: experimental

The public satellite may accept a bounded Job by a new file under:

`queue/requests/<request_id>.json`

The filename is the idempotency key. Creation fails if the same request already exists.

A request MUST contain exactly:

```json
{
  "schema": "arca.public-executor-request.v0.1",
  "profile": "smoke",
  "request_id": "example-001",
  "public_only": true,
  "secrets_allowed": false
}
```

The queue rejects unknown fields, arbitrary shell input, private jobs and secret-bearing jobs.

A push that changes exactly one request file starts the queued executor. The dispatch commit SHA becomes the provider correlation identifier and the resulting GitHub run is correlated by `head_sha`.

This is a public lab execution transport. It grants no authority to merge or promote ARCA Core code.
