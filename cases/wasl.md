# Wasl — offline-aware generator billing

**Domain:** Mobile software, payments accounting, data-integrity controls  
**Stage:** Tested engineering build; physical offline acceptance remains pending

## Problem

Generator subscription operators in Iraq may manage accounts and payments in places where mobile internet is unreliable. Mistakes in month-end rollovers or concurrent payments can alter financial balances.

## Implementation and tests

- Modeled payments and bills in integer Iraqi dinars rather than floating-point currency.
- Implemented guarded payment updates and month-end billing invariants.
- Made adjustments auditable through new correction records instead of silently modifying payment history.
- Added rules and tests addressing overpayment, simultaneous receipt generation and carry-forward balances.
- Recorded automated results: **271 Flutter tests**, **142 backend/security-rules tests** and **28 accounting audit tests**.

## Important limitation

The **critical offline queue and reconnection path had not passed acceptance on a real Android handset** at the documented checkpoint. Automated tests provide evidence for core logic, not proof of real-world offline reliability. This is not advertised as a finished commercial deployment.

## Research relevance

Resilient mobile systems, consistency, financial integrity, offline-first UX and explicit safety boundaries.

[Back to portfolio](../README.md)
