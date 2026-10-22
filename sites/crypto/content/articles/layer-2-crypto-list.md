---
title: "Layer 2 Crypto List: Representative Networks and Their Designs"
description: "Explore a layer 2 crypto list of representative blockchain networks, grouped by design and explained with clear inclusion criteria and scope."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 crypto list"
owned_question: "Which blockchain networks are commonly classified as crypto layer 2s, and how can readers distinguish their designs?"
risk_level: "medium"
---

A reliable layer 2 crypto list should include only networks whose documentation establishes a specific relationship to a base blockchain. The evidence available here supports explaining rollups as a category and distinguishing their design patterns, but it does not identify individual networks with documented architecture. Rather than supply unsupported names, this reference sets out what can be classified, what remains unverified, and how to build a network-by-network directory without treating inclusion as a ranking or endorsement.

## What counts as a layer 2 in this list?

A layer 2 (L2) is commonly understood through its relationship to a base layer, sometimes called a Layer 1. For this article, the relevant evidence-based category is the rollup: a system that separates transaction execution from the base layer while publishing data there, where base-layer consensus establishes the published record. Rollups differ in proof systems, data formats, sequencing, upgrade arrangements, and bridge designs. [source](<https://ethereum.org/developers/docs/scaling/>)

The label “L2” is not enough by itself. Industry usage is not fully uniform, so classification should follow documented architecture rather than a project’s name or marketing description. The available evidence also distinguishes a rollup from systems that publish data elsewhere: in L2BEAT’s terminology, a rollup uses a Layer 1 for consensus and data availability, while publishing data elsewhere introduces external data-availability assumptions and is classified differently.

Accordingly, a candidate entry needs documentation identifying its base layer and explaining where execution occurs, how results connect to that layer, what proof or dispute approach is used, and where data is made available. A representative directory would not be exhaustive, and token existence would not establish that a network qualifies. Inclusion would identify an architectural category, not imply a security assessment, endorsement, or ranking.

The evidence supplied for this article does not include network-specific documentation establishing named candidates and their current architectures. It would therefore be misleading to present a named directory as verified. The categories and verification checklist below show what a supportable list can say and what it still needs to establish.

## Layer 2 crypto list: representative networks by design

The supported rollup categories are optimistic rollups and validity rollups. These are useful organizing headings for a directory, but they do not, by themselves, supply verified network names. A network-specific list would need to connect each named system to a source that establishes its base-layer relationship and relevant design features. No such network-by-network evidence is available here, so no individual network is assigned to either category.

### Optimistic rollups

An optimistic rollup is described through a challenge-based approach to validating state transitions. In the documented model, state transitions are accepted optimistically and can be disputed through a challenge period and fraud-proof process. This description identifies a design pattern; it does not establish that a particular deployment has a working proof implementation, active challengers, particular upgrade controls, or a specific withdrawal design. Those details must be examined for the deployed system.

For a directory entry, the technical source should explain the relevant challenge or dispute mechanism and how it connects to the named base layer. If documentation only uses the phrase “optimistic rollup” without substantiating those details, the label should not be expanded into claims about a particular implementation’s operation or security.

### Validity rollups

A validity rollup uses a different state-transition approach: the canonical rollup state on the base layer is updated after a verifier contract accepts a cryptographic validity proof for the proposed offchain state transition. This is a description of the mechanism, not proof that every implementation is secure or that every relevant system detail has been checked. Correctness still depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

A directory should therefore state what the documentation establishes about the proof and verifier, rather than treating “validity” or “zero knowledge” as a complete assessment. The supplied evidence supports the category-level distinction, but not the assignment of named networks to it.

### Other scaling systems and classification boundaries

Not every system described as scaling a blockchain necessarily fits the rollup definition used here. The classification depends on the architecture, including the relationship to base-layer consensus and data availability. If a system publishes data elsewhere, the cited L2BEAT terminology treats that as an external data-availability assumption and classifies it differently from a rollup.

This boundary is useful when organizing a global directory: label a system according to the documented design, not simply because it processes activity away from a base chain. Where the relationship is unclear or sources use competing classifications, present the uncertainty or omit the entry until the evidence supports a precise description.

## How the listed layer 2 designs differ

Optimistic and validity rollups differ chiefly in how the proposed state transition is challenged or established. The optimistic model uses a challenge period and a fraud-proof process to dispute incorrect execution. In the validity model, a base-layer verifier accepts a cryptographic proof for the proposed offchain state transition before the canonical state is updated. These are architectural descriptions, not universal guarantees about deployed systems.  [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

Data availability is another key distinction for classification. A rollup’s documented relationship to its base layer includes publishing data there, while systems that publish data elsewhere add external data-availability assumptions and are classified differently in the cited terminology. An entry should explain this relationship rather than assume that every project using the L2 label relies on the same arrangement. [source](<https://ethereum.org/developers/docs/scaling/>)

Architecture labels also should not be mistaken for complete security scores. The L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization; it is not a complete security score. A higher stage does not by itself prove that contracts, proof systems, bridges, or implementations are bug-free. [source](<https://l2beat.com/stages>)

For readers comparing entries, the practical distinction is therefore documentary: what base layer is involved, what role it plays, and what proof, dispute, and data-availability arrangements the sources actually describe. The same category label does not establish that two systems have identical implementations or operating conditions.

## How to verify a network’s layer 2 classification

A consistent editorial check can help make a named directory precise and prevent category labels from carrying more meaning than the evidence supports:

1. **Identify the base layer.** Find documentation that names the base blockchain and describes the system’s relationship to it. A general claim that a project “scales” another network is not enough to describe the architecture.
2. **Locate execution and publication.** Check whether transactions execute outside the base layer and what the system publishes to it. Rollup descriptions separate execution from the base layer while relying on publication there for the record established by base-layer consensus. [source](<https://ethereum.org/developers/docs/scaling/>)
3. **Describe the proof or dispute approach.** Look for documentation of a challenge period and fraud-proof process, or a validity proof accepted by a base-layer verifier. Avoid inferring one mechanism from a broad category name alone.  [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)
4. **Check data availability.** Establish where transaction data is published and whether the architecture relies on an external data-availability arrangement. This detail affects whether a system fits the rollup classification used here.
5. **Keep maturity separate from security.** If a maturity framework is cited, explain what it measures and what it does not. A stage or label is not a complete assessment of contracts, proof systems, bridges, or implementations. [source](<https://l2beat.com/stages>)

For publication, record the technical source URLs and the dates they were checked for every network-specific statement. This article does not claim to have checked or tested individual networks, and it does not supply verification dates. If the available documents do not establish a candidate’s base-layer relationship or design, mark its classification as unresolved or leave it out instead of filling gaps by inference.

## What this list does not tell you

This reference does not establish the security, reliability, decentralization, adoption, or suitability of any individual network. The supported evidence explains category-level architecture and classification boundaries; it does not support ranking named networks or asserting their current operational status.

It also does not report current fees, supported assets, availability, or operating conditions. Those claims would require separate, dated evidence specific to each network. Nor does this article assess token value, recommend investments, or provide bridging instructions. Readers evaluating a particular system should consult its current technical documentation and relevant risk disclosures rather than infer operational facts from an architectural label.

The result is intentionally narrower than a populated directory: it gives a consistent basis for classifying representative networks, while making clear that unsupported names should not be presented as verified entries. A complete list can be expanded when network-specific documentation establishes the required relationship and design details.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
