---
title: "How to assess new layer 1 crypto projects"
description: "Learn how to assess new layer 1 crypto projects by architecture, scaling design, development status, and evidence—without relying on rankings or claims."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["blockchain_scaling"]
tags: ["Layer 1 blockchain projects", "blockchain scaling"]
author: "editorial_team"
primary_keyword: "new layer 1 crypto projects"
owned_question: "How can readers identify and assess new Layer 1 crypto projects by their architecture, scaling approach, development status, and evidence of network operation?"
risk_level: "medium"
---

To assess new Layer 1 crypto projects, define a dated meaning for “new,” confirm that each candidate is actually a base-layer network, and compare its documented architecture, scaling approach, development stage, and evidence of operation. Treat project descriptions as claims to verify, not as proof of performance, security, adoption, or readiness. The evidence available for this guide does not establish current project-specific launch dates, code histories, or network status, so it does not name or rank candidates.

## Define what counts as a new Layer 1 project

A useful shortlist begins with an inclusion rule. Choose a cutoff date and decide whether “new” means a network launched after that date, a project in active pre-launch development, or both as separate categories. These are research choices, not universal definitions. Record the cutoff and rule so another researcher can reproduce the search and understand why a candidate was included.

Next, establish what “Layer 1” means for your comparison. In common crypto usage, Layer 1 refers to the base blockchain network and its protocol. The term is common usage rather than a separately standardized technical category, so state how you apply it in your research. A practical assessment asks which network defines the relevant base state and what functions its own protocol performs. Distinguish those base-network functions from functions handled by external systems.

Do not classify a candidate by its token name, branding, or ecosystem alone. A project may be associated with a token, applications, wallets, infrastructure providers, or a scaling system without establishing that it operates a distinct base-layer protocol. For example, some Ethereum Layer 2 systems derive part of their security from Ethereum Layer 1 consensus; the exact guarantee depends on the system’s proof, data availability, settlement, governance, and exit mechanisms. That example illustrates why the underlying architecture matters more than a label. [source](<https://ethereum.org/developers/docs/scaling/>)

Keep each candidate’s network, token, and surrounding services as distinct records. A token may be associated with a network, but the token’s existence does not answer who validates the network’s state or where its core protocol functions occur. If the documentation does not make the distinction clear, mark Layer 1 classification as unresolved instead of inferring it. This avoids counting a rebrand, application, or external service as a new base-layer network without supporting evidence.

## Compare the scaling design, not headline claims

For each candidate, make an architecture record from attributable technical documentation. Identify where execution occurs, how the system establishes agreement on state, where transaction data is made available, and what roles nodes or validators perform. Do not assume that one project’s use of a term such as “validator,” “consensus,” or “data availability” matches another project’s definition. Record the source’s language and flag unanswered questions.

Separate mechanisms that documentation describes as implemented from mechanisms that appear only in proposals or roadmaps. A roadmap supports a statement about an intended direction, not a claim that the mechanism has been deployed or demonstrated. When a project describes a scaling method, look for the technical explanation of how it changes the work performed by the base network and what responsibilities remain elsewhere. If the documentation does not specify this, note the gap rather than supplying a mechanism from expectation.

Assess scalability as a set of design choices, not a single headline number. A useful review records what is documented about execution, consensus, data availability, network roles, and resource requirements. It also notes stated trade-offs, without assuming that a figure for throughput or latency captures the whole design. This article’s evidence does not provide project-specific measurements or a shared test method; it cannot support comparative performance conclusions.

If the architecture coordinates activity between separate chains through a bridge, examine the verification path rather than relying on the bridge label. Bridge security depends materially on who or what verifies the source-chain event; possible models include external validators, oracles, connected-chain validators, light clients, or challenge mechanisms. The particular model and its assumptions require project-specific evidence. [source](<https://ethereum.org/developers/docs/bridges>)

A bridge can coordinate token, message, data, or contract-call activity between otherwise isolated blockchain environments. That broad function does not mean that every bridge moves an asset in the same way or provides the same security assurances. For each candidate, record what the technical materials actually specify about verification and destination-chain processing; do not turn a general description into a conclusion about a specific project.

## Verify development and network status

Create a dated evidence trail for each candidate. Record the documentation title and its publication or update date, the code or release records checked, and the network-status material available when the review was conducted. These records help distinguish a project’s technical description from evidence that a particular implementation or network is operating. If you have not checked an item, mark it as unchecked rather than implying independent corroboration.

Use stage labels conservatively. A pre-launch effort, a test network, and a main network are different categories for a research record, but project teams may define and describe them differently. Record the project’s wording, the date, and the evidence that supports the status. If current operation cannot be established from the materials reviewed, state that the status was not verified as of the review date rather than assigning a stage based on promotional language.

Activity and performance claims need their own evidence. Before treating a stated result as verified, determine what was measured, how it was measured, which network or configuration was included, and over what period. If the source does not disclose the method or scope, label the claim unverified or leave it out. Do not use a project’s stated capacity, activity, or reliability as a substitute for evidence that can be checked independently.

The same discipline applies to code and release records. Attribute records to their source and date, and distinguish a repository or release entry from evidence that a deployed network is using the corresponding code. The materials available for this article do not establish current network status, code history, or performance for any named candidate. That limitation is a reason to avoid project examples, not a reason to fill the gap with assumptions.

## Use evidence to build a research shortlist

Apply the same fields to every candidate. A compact working record can include:

- **Network role:** The documented basis for treating the candidate as an independent Layer 1, or the unresolved point that prevents confirmation.
- **Scaling approach:** The described execution, consensus, data-availability, and node or validator roles, with proposed features separated from implemented ones.
- **Development stage:** The project’s dated status description and the evidence checked to corroborate it.
- **Evidence checked:** Technical documentation, attributable code or release records, and network-status materials, each with dates and scope.
- **Unresolved questions:** Missing definitions, unclear responsibilities, unverified activity or performance claims, and evidence needed for a later review.

Use primary technical materials to support design claims. For operation, seek records whose source, scope, and measurement method can be examined. These are different evidence tasks: a project’s documentation may explain its proposed architecture, while independent operational evidence is needed to substantiate claims about a live network or measured activity. Do not treat one type of evidence as a substitute for the other.

Decide in advance how the shortlist handles uncertainty. If the evidence does not establish a candidate’s Layer 1 role, keep it out of the confirmed set or put it in a separate “classification unverified” queue. If its role is clear but its current operation is not, retain the distinction in the record rather than collapsing both findings into a single yes-or-no label. This keeps the shortlist useful without presenting incomplete evidence as confirmation.

Date-stamp the assessment and preserve the sources behind it. A reviewer should be able to see what information was available at the time, which claims were checked, and which questions remain open. Revisit the record only when new evidence is available, and update the date and status rather than silently replacing an earlier conclusion. The result is a reproducible research shortlist—not a ranking, endorsement, or assessment of investment merit.

## Separate technical research from adoption and risk decisions

A documented architecture or launch stage does not, by itself, establish security, reliability, compliance, or adoption. Keep those conclusions out of a technical shortlist unless evidence directly supports them. A project’s stated design is not proof that its deployed implementation matches the description or that its operational controls work as claimed.

If using an external maturity framework, read what it measures and what it does not. For example, the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization; a higher stage is not a complete security score and does not prove that contracts, proof systems, bridges, or implementations are free of defects. This is a framework-specific example, not a general rating for Layer 1 projects. [source](<https://l2beat.com/stages>)

For separate questions about fees, yields, security properties, recovery options, compliance capabilities, or jurisdiction-specific access, obtain current evidence that directly addresses the relevant claim and scope. This guide’s evidence does not verify those matters for any particular project. Keep conclusions proportionate: state what was documented, what was independently checked, what remains uncertain, and when the review was conducted. A disciplined research record can identify technical questions for further work without turning limited documentation into a claim of readiness or suitability.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
