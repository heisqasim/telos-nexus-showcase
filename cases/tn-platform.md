# TN Platform — policy-controlled engineering and company operations

**Domain:** Internal tooling, software delivery, audits, integration architecture  
**Stage:** Initial engineering/control-plane foundation deployed on a cloud VM in documented checkpoints; later modules are at mixed planning/testing stages

## Purpose

An internal control surface for project state, engineering evidence, CI, deployments and the eventual operations of Telos Nexus.

## Engineering work

- Typed request flows with role/policy checks.
- Event, knowledge and project metadata models.
- CI/security/release evidence lineage.
- Cloud service installation/health/backups and monitoring foundations.
- Explicit separation between **observing** provider state and **writing** changes.

## Limits

This is an **internal operations platform**, not a market-proven SaaS product. Features described in future plans are not evidence of deployment. Provider-side write capabilities remain gated and must not be inferred from read-only connectivity.

[Back to portfolio](../README.md)
