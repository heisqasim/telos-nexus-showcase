# SADS — evidence-grounded Arabic education AI

**Domain:** AI, Arabic search, structured datasets, assessment and education  
**Stage:** Public Mathematics V2 experience deployed; other subjects in preparation  
**Live:** [sads.telosnexus.services/app](https://sads.telosnexus.services/app)

## Problem

Turning archived Iraqi school exam materials into trustworthy AI-assisted study tools requires accurate linkage between a question, a worked solution and a scan of the original source. Errors in extraction, source identity or citations can mislead students.

## Approach

- Converted **305 source pages** into a structured and reproducibly checked Math dataset.
- Indexed **935 canonical questions** and **935 source-transcribed solutions**, with **1,527 historical appearance/source records**.
- Made provenance visible in the Question Vault, historical browsing and source-linked assistance.
- Built Ask SADS around retrieval from this subject corpus before generation, followed by **citation validity checks**.
- Chose **retrieval-only** output when a provider could not produce a valid grounded answer.
- Kept measured historic exam-ranking results separate from later platform functionality. No retrospective improvement of old forecasts.

## Result and limits

The Mathematics application and source-grounded question-answer workflow were deployed and passed production verification. **Source-transcribed solutions are not claimed to be ministry-certified answer keys.** Other V2 subject corpora have not reached the same verified readiness.

The project is a public working application and a source-integrity engineering effort; it is **not** an independently published paper, a verified general educational effectiveness trial, or a promise of exam prediction accuracy.

## Research relevance

Arabic-language retrieval, hallucination controls, citation verification, data lineage, reproducibility and education access.

[Try Mathematics](https://sads.telosnexus.services/app) · [Back to portfolio](../README.md)
