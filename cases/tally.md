# Tally — multi-tenant QR restaurant workflows

**Domain:** Full-stack mobile/web, system architecture and role security  
**Stage:** Guest app and backend deployed, **pilot-ready**; restaurant field acceptance pending  
**Live:** [tally-guest.web.app](https://tally-guest.web.app)

## Problem

Restaurant staff often move orders between diners, cashier, kitchen and waiter using disconnected channels. For a multi-restaurant platform, access boundaries and authoritative price calculations are essential.

## Engineering approach

- Built a phone-friendly guest flow opened by table QR codes, without requiring an app installation.
- Separated dining, cashier, kitchen, waiter and owner workflow roles.
- Designed tenant-isolated data organization with role-aware write restrictions.
- Centralized sensitive pricing and order state transitions in privileged backend functions.
- Used web for guests and Flutter/Android for staff.
- Deployed Cloud Functions and a guest-facing web application for pilot use.

## Honest maturity

Technical deployment and pilot-ready components exist. **A full, verified live-restaurant operation has not yet been demonstrated**, and the staff APK remains debug-signed.

## Research relevance

Distributed client synchronization, security boundaries, state machines, human-centered workflow design and SMEs' digital transformation.

[Open guest interface](https://tally-guest.web.app) · [Back to portfolio](../README.md)
