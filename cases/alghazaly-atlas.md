# Al-Ghazaly Knowledge Atlas — source-first research infrastructure

**Domain:** Arabic digital humanities, document processing, search, trustworthy AI  
**Stage:** Public research interface with machine-readable corpus; human scholarly review incomplete  
**Live:** [alghazaly.telosnexus.space](https://alghazaly.telosnexus.space)

## Problem

Large scans of Arabic source materials are difficult to search and cite reliably. Machine OCR can look convincing even where a scholarly transcription is not verified; a research system must not silently convert one into the other.

## Implementation

- Built an Arabic-first source browsing/search interface with page-level evidence.
- Worked with **84 materialized source editions** and **37,145 rendered page images**, with **36,638 selected OCR-backed pages** in a project-trusted operational baseline.
- Kept separate labels for original image evidence, machine OCR, project operational baseline and **human-verified** texts.
- Linked atlas topics to located corpus references without upgrading uncertain machine text into accepted scholarship.
- Implemented data-integrity checks, bounded acquisition processing and recovery procedures.

## A concrete engineering incident

The runtime source directory was lost in October 2026. Restoring from a separate library, the project recovered **84/84 raw source objects** and **82/84 derivative PDFs** with hash verification. Two derived PDFs were **not** silently regenerated as verified originals because their expected hashes did not match. Their absence was documented.

## Limits

**Zero pages had human-canonical scholarly verification** at the referenced checkpoint; rights for editions also require review. This is a research-access instrument, not a peer-reviewed critical edition or a claim to own source-text rights.

## Research relevance

Document provenance, retrieval, Arabic NLP/OCR, trustworthy digital archives, data integrity and transparent evidence tiers.

[Explore the Atlas](https://alghazaly.telosnexus.space) · [Back to portfolio](../README.md)
