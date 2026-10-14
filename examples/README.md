# Public, executable engineering examples

These small **independently authored, dependency-free examples** illustrate two engineering principles used in private project work. They are **not extracts of the private production repositories** and are **not substitutes for field or production acceptance testing**.

## Run the examples

Requires Python 3.10 or newer; no packages to install.

From the repository root:

```bash
python3 -m unittest discover -s examples -p 'test_*.py' -v
```

## Contents

- [Grounded AI citation guard](citation_guard.py) — validate that LLM output cites only evidence actually presented to it. Demonstrates *fail closed* behavior.
- [BMS observation model](bms_observation.py) — distinguish lost link, stale telemetry, equipment running state and alarming status without inventing plant conditions.

Corresponding real-world projects: [SADS](../cases/sads-education-ai.md) and [Syntra](../cases/syntra-bms.md).

**Safety note:** The BMS example is pure-data, read-only and does not connect to industrial networks or expose commanding functions. The AI example enforces a reference ID boundary, not semantic correctness of arbitrary answer text.
