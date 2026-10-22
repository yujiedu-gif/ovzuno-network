---
title: "zk proof projects: a guide to privacy and identity use cases"
description: "Explore zk proof projects by privacy and identity use case, learn how their roles differ, and check what evidence supports each project's claims."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: []
author: "editorial_team"
primary_keyword: "zk proof projects"
owned_question: "What kinds of projects use zero-knowledge proofs for privacy or identity, and how can readers distinguish their roles and limitations?"
risk_level: "medium"
---

Zero-knowledge proof projects for privacy and identity are best compared by the job their proofs perform—not by the label alone. With the evidence available here, the defensible examples are an architecture for privacy applications, a rollup pattern, selective disclosure through Zcash viewing keys, and a private-business-record coordination architecture. The evidence does not establish a current roster of named identity applications or project deployment statuses, so this map describes documented functions rather than ranking or endorsing projects.

## What counts as a zk proof project?

For this map, a project or architecture qualifies when the allowed technical evidence documents zero-knowledge proofs as part of a privacy-related function. A zero-knowledge proof is a cryptographic object that a verifier can check without receiving the underlying private witness data. Here, *witness* means the private input used to generate a proof; a *commitment* is a public value associated with the claim being checked. These terms describe a general application pattern, not a guarantee that every relevant fact stays private.

A useful distinction is between the proof mechanism and the system that uses it. In a documented Ethereum privacy-application pattern, private witness data and off-chain proof generation are separated from a public commitment and an on-chain verifier. The verifier checks the proof; the broader application determines how inputs are collected and what claim the proof represents. The pattern’s soundness, circuit design, setup assumptions, metadata, key management, and data availability remain system-specific risks. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

The allowed evidence supports architectural patterns, not a verified directory of current products. It does not establish which named applications are live, whether a particular feature is in production, or whether it has undergone independent security review. Accordingly, the categories below identify functions documented by the evidence, not project maturity or operational availability.

## Group projects by the job their proofs perform

**Privacy applications: prove a claim while limiting disclosure.** A privacy application can generate a proof from private inputs and present a public commitment to an on-chain verifier. This can separate the underlying witness from the information the verifier receives. It does not, by itself, show that the private inputs are true, that they were collected appropriately, or that surrounding application data reveals nothing. The proof establishes only what the specified circuit and verifier check. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

**Rollup infrastructure: prove a state transition.** A ZK rollup is a system that performs execution and stores state off-chain while submitting state-change summaries and cryptographic validity proofs to Ethereum. This is an infrastructure role: the proof concerns whether a proposed state transition satisfies the system’s rules. It is not automatically a tool for private identity credentials or private user activity. Proof systems, data-publication policies, operator designs, and escape mechanisms vary by implementation. [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

A related but distinct rollup design uses a base-layer verifier contract to accept a validity proof for a proposed off-chain state transition before updating canonical rollup state. The evidence supports that mechanism, but correctness still depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. A verified transition should not be confused with a general guarantee about application privacy or identity claims. [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

**Selective visibility: share a defined view without spending authority.** Zcash viewing keys provide protocol-defined selective visibility into shielded transaction data without providing spending authority. The exact information visible depends on the key type and protocol version, and disclosure is not equivalent to a universal financial audit. This is a privacy-and-disclosure function; the evidence does not establish it as a general-purpose identity credential system. [source](<https://zips.z.cash/protocol/protocol.pdf>)

**Private-system coordination: retain business data while coordinating state.** The Baseline Protocol reference architecture coordinates multiple private systems of record using messaging, cryptography, proofs, and a consensus-controlled state machine, while business data remains in the systems of record. This is a coordination architecture rather than a standalone identity product. Implementations choose the state machine, privacy method, governance, messaging, and operational controls; the specification does not make every implementation trustless. [source](<https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html>)

These examples occupy different layers. An application uses a proof to support a user-facing claim; a rollup uses one to support a state-transition process; a viewing key governs selective access to transaction information; and a coordination architecture links private business systems. Their shared use of cryptographic proofs does not make their functions interchangeable.

## zk proof projects: compare scope, deployment, and trust assumptions

When assessing a specific project, first identify the exact claim its proof is intended to establish. For an application, ask what private input goes into proof generation and what commitment or result is exposed to the verifier. For a rollup, identify whether the proof concerns a proposed state transition and what data is published. For selective viewing, check which key type and protocol version determine visibility. For private-system coordination, identify which components and policies the implementation selects. These questions follow the documented mechanisms; they do not presume that every project provides the same disclosures or controls.

Next, separate proof verification from the truth of inputs and the behavior of the surrounding system. A verifier accepting a proof means that the proof meets the verifier’s encoded conditions; it does not independently establish facts that were never represented in those conditions. Likewise, a commitment does not itself explain where input data came from, who issued a credential, or whether a service handles metadata in a privacy-preserving way. In each case, verify what is proven and what remains an application, issuer, operator, or user responsibility.

Then check status using project-specific technical materials. The evidence available for this map describes reference architectures and protocol mechanisms, but does not provide a named project’s current release status, deployment record, or independent audit evidence. Do not translate an architecture into a claim that a feature is deployed, widely used, or independently validated. Where project documentation does not specify status or security review, treat it as unknown.

## Evidence and limitations to check before relying on a project

A practical evidence review should match each statement to the right documentation. Technical specifications can support descriptions of proof inputs, public outputs, and verification behavior. Application documentation is needed to establish how a feature is exposed to users and what information it collects or shares. Implementation-specific security and operational claims need evidence about that implementation; a general proof pattern cannot fill the gap.

For privacy claims, ask what is public, what remains in private systems, and which metadata or operational details the technical materials address. The privacy-application pattern explicitly leaves metadata, key management, and data availability as system-specific risks. For a private-system architecture, the reference design likewise leaves implementation choices—including privacy methods and operational controls—to implementers. Neither description supports a blanket claim that all data is confidential or that every deployment is trustless. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>) [source](<https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html>)

For identity-related claims, this evidence base has a narrower limit: it supports selective viewing of shielded transaction information, but does not substantiate a catalog of credential issuers, identity applications, or deployed identity-verification products. Do not infer identity issuance or credential validity from the presence of a proof. A proof can show that a specified condition was met under a system’s rules; the evidence here does not establish who created the underlying information or whether it is accurate.

The same caution applies to security, recovery, compliance, fees, yields, and availability. The allowed evidence does not substantiate project-specific claims in those areas, so they should not be assumed from the use of zero-knowledge proofs. No jurisdiction-specific legal, tax, or regulatory conclusion follows from the mechanisms described here.

## How to use the project map

Start with the function you need: privacy-app verification, rollup state-transition verification, selective disclosure of shielded transaction data, or coordination among private business systems. Compare projects only when their documented roles are similar. Then follow each project’s technical materials to establish what is proven, what is visible, how the system is implemented, and what its current status is.

If a capability or safeguard is not documented in the evidence you review, record it as unknown rather than treating missing information as proof that it exists or does not exist. That discipline keeps the project map useful without turning a cryptographic mechanism into an unsupported claim about a product, deployment, identity, or privacy outcome.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zcash Protocol Specification, NU6.1](https://zips.z.cash/protocol/protocol.pdf) — Electric Coin Company and Zcash protocol contributors; retrieved 2026-10-18.
- [Baseline Core Version 1.0 - Part 1](https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html) — OASIS Open; retrieved 2026-10-19.
