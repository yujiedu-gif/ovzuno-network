---
title: "L1 crypto list: a scoped reference to Layer 1 networks"
description: "Use this l1 crypto list to identify candidate Layer 1 networks, understand inclusion criteria, and verify classifications without treating tokens as networks."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["1 crypto list"]
author: "editorial_team"
primary_keyword: "l1 crypto list"
owned_question: "Which blockchain networks belong on a clearly scoped list of Layer 1 crypto networks, and what evidence supports each inclusion?"
risk_level: "medium"
---

This L1 crypto list cannot responsibly name individual networks from the evidence available here: none of the permitted claims supplies network-specific protocol documentation establishing a candidate’s Layer 1 role. The list therefore records no named networks. It provides inclusion criteria and a verification method so readers can assess candidates without treating a token ticker or a project label as proof of classification.

## What qualifies for this L1 crypto list?

Layer 1, often shortened to L1, is common usage for a base blockchain network and its protocol; it is not a separately standardized technical category. For this list, a candidate would qualify only when the network’s own primary documentation supports its role as a base network, rather than merely showing that it has a token or connects to another chain. This operational criterion makes the list auditable while recognizing that projects may use architectural labels differently.

The evidence boundary matters. The accepted claims supplied for this article describe general blockchain architecture and several particular architectural concepts, but they do not identify a set of individual networks with documentation proving each one meets the criterion. Naming familiar projects from general knowledge would not meet the requested evidentiary standard. Accordingly, the empty list is a limitation of this article’s evidence, not a claim that no Layer 1 networks exist.

A network and its native token are also different things for purposes of classification. A ticker names an asset, not the technical responsibilities of the system associated with it. To include a candidate, the entry would need to identify the network, point to primary protocol documentation, and explain which base-layer functions that documentation attributes to it. Token ownership, token utility, price, and investment prospects are outside this classification exercise.

## The L1 crypto list, organized by network

| Network | Native token | Evidence for Layer 1 classification | List status |
|---|---|---|---|
| No named network included | Not assessed | No network-specific primary protocol documentation is available in the permitted evidence | Omitted pending verification |

This table deliberately does not substitute examples or inferred classifications for evidence. An entry belongs here only after its official documentation has been reviewed against the stated criteria. The available claims do not establish the classification of any specific named network, so adding one would imply more evidence than this article has.

When evidence becomes available, a useful entry should state the network name, the relevant official document and its version or access date, and a concise rationale grounded in that document. It should list a native token separately, if relevant, without confusing the asset with the network. Entries should be arranged consistently—such as alphabetically—rather than by perceived quality, performance, or token characteristics. This list supplies no rankings and makes no recommendations.

The absence of a network from this table should not be read as a negative assessment of that network. It means only that the supplied evidence does not support including it under this article’s verification rule. Likewise, inclusion in a future version would establish only that the documentation supports the classification, not that the network is suitable for a particular purpose.

## How to verify a Layer 1 classification

Begin with the candidate network’s primary protocol documentation. Identify what system the document describes and which functions it assigns to that system. In particular, look for evidence that the network provides its own base-layer role, rather than relying on a name, token listing, promotional description, or an unexplained use of the term “Layer 1.” The classification should follow documented architecture, not branding.

Then trace the relevant dependencies. Ask which system is responsible for establishing or validating the state that the candidate claims as its own, and whether another chain supplies an essential part of the candidate’s operation. The question is not simply whether two chains communicate; it is which chain performs the role being used to justify the classification. If the documentation does not make that boundary clear, record the uncertainty or leave the candidate off the list rather than resolving it through inference.

Layer 1 assessment should also distinguish functions of the base network from functions assigned to external systems. This is a general assessment question, not a formal definition that settles every architecture. It helps keep the review focused: record which functions the documentation attributes to the candidate and which it assigns elsewhere.

For reproducibility, record the title and version of the primary documentation when available, or the date it was checked. A classification should reflect the documentation reviewed, not imply that a label is permanent or universally agreed. If the project’s terminology differs from the list’s working criterion, preserve that difference and explain the architecture the evidence actually describes.

A blockchain explorer can support a separate inspection of on-chain objects, but it does not answer the classification question on its own. A draft URI proposal describes common explorer references for transactions by hash, blocks by hash or height, and addresses. Those references can help locate activity; they do not establish which network performs base-layer functions. [source](<https://bitcoin.org/bip/122/>)

## How the list differs from Layer 2 and scaling comparisons

This is a scoped reference list, not a detailed comparison of Layer 1 and Layer 2 systems or an evaluation of scaling trade-offs. A system’s relationship with another network may be relevant when tracing dependencies, but that relationship alone does not settle whether it meets this list’s criterion. For example, some Ethereum Layer 2 systems derive some security from Ethereum’s Layer 1 consensus; the specific guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. That qualified example illustrates why architecture and dependencies need to be checked, not why any particular unverified candidate should be added here. [source](<https://ethereum.org/developers/docs/scaling/>)

Readers looking for a comparison between networks, or for an assessment of scaling designs, need a separate analysis with evidence and criteria suited to that question. This list does not say which network is best, fastest, or cheapest, and it does not determine suitability for a particular application or organization. Its narrower task is to show what evidence would support a Layer 1 classification and to avoid presenting unsupported candidates as established entries.

## What this list does not establish

A Layer 1 classification is not a security, decentralization, performance, adoption, availability, or operational-suitability rating. A distributed network’s node count alone does not establish operator independence, geographic diversity, implementation diversity, or block-production power. A classification therefore cannot replace a network-specific examination of how its participants and systems operate. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

Nor does a network’s inclusion establish its fees, yields, recovery options, or service availability. Those are separate, context-specific claims and require appropriate current evidence. No such findings are made here. The list also makes no legal, regulatory, tax, or compliance determination; none follows merely from classifying a network’s architecture.

The practical answer is consequently bounded: a network belongs on this list only when its own primary protocol documentation supports the stated base-layer criterion. Because the permitted evidence here does not support that conclusion for any named network, the list remains unpopulated rather than guessing. Readers can apply the verification steps above to a candidate and record the documentation and date before treating its classification as established.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [BIP 122: URI Scheme for Blockchain References and Exploration](https://bitcoin.org/bip/122/) — Bitcoin Improvement Proposals; retrieved 2026-10-18.
