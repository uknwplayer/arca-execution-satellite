# CircleCI Public Executor Candidate

Status: prepared, not live-verified.

This repository contains a bounded CircleCI configuration in `.circleci/config.yml`.

The intended first live proof uses API/manual triggering only. Do not add an automatic push trigger for Proof 005.

Pipeline parameters:

- `arca_job_id`
- `arca_profile` = `smoke` or `python-unit`

The executor identity is `circleci-public-linux`.

This candidate receives only public repository content and no ARCA Core secrets. A successful CircleCI run is required before changing its trust/admission state.
