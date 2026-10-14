# Syntra — reliable building-automation telemetry

**Domain:** Industrial control, building management systems (BMS), mobile monitoring  
**Role:** Owner-led product and integration engineering under Telos Nexus  
**Stage:** Field-tested beta; **read-only only**, not a production control system  
**Stack:** Flutter/Dart, Delta Controls enteliWEB, BACnet object semantics, API integration

## Problem

BMS interfaces can conflate *network connectivity*, *equipment running state* and *alarms*. During testing, an enteliWEB aggregate alarm endpoint did not agree with alarm states visible on individual points. If a monitoring application silently interprets a lost link as a machine failure, an engineer may act on false information.

## Approach

- Built site/controller/point discovery from real enteliWEB reads.
- Distinguished **LIVE**, **DEMO**, **STALE**, **OFFLINE**, **NO LINK**, running and actual point-fault states.
- Derived and compared alarm visibility from point-level event states and status flags, instead of trusting only the aggregate alarm endpoint.
- Kept unrecognized alarm states visible and preserved last-known alarm evidence when connectivity disappeared.
- Kept all field paths **read-only** with no controller commands or setpoint overrides.

## Evidence and result

Field checks covered **one Delta R9-Edge 1180 controller, 32 points and one AHU**, using enteliWEB. Point state, equipment grouping and alarms were exercised against actual hardware rather than only screenshots or a simulator.

A known mismatch with the vendor's aggregate alarm endpoint remains under investigation: the result was a more trustworthy and explicitly qualified monitoring interface, **not** a claim that the vendor defect was fixed.

## What remains

Larger-site scaling, multi-site behavior, endurance/soak tests and commercial app distribution have not been proven. A public source-code release is not currently planned.

## Research relevance

Trustworthy cyber-physical system observability; data provenance and confidence; safe human-in-the-loop monitoring; interoperability of OT systems.

[Back to portfolio](../README.md)
