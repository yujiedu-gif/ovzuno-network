---
title: "Zero Knowledge Proof Example: How It Works"
description: "Understand Zero Knowledge Proof Example, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification p."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: []
author: "editorial_team"
primary_keyword: "zero knowledge proof example"
owned_question: "What are practical examples of zero-knowledge proofs, and what does each demonstrate?"
risk_level: "medium"
---

# Zero Knowledge Proof Example: How It Works

A zero-knowledge proof is useful when one party needs to demonstrate that a statement is true without revealing all the information used to establish it. In practice, the phrase “zero knowledge proof example” can refer to several different system designs. A privacy application can prove a claim about private data; a rollup can prove that an offchain state transition is valid; and a coordination protocol can use proofs while business records remain in separate systems.

These examples share a proof-based approach, but they do not provide the same privacy or operational guarantees. The key is to identify what is private, what is proved, who verifies the proof, and what other data or controls the system relies on.

## What Zero Knowledge Proof Example means

Consider a privacy application in which a user has private witness data: information needed to support a claim. The application can generate a proof offchain, while a public commitment and an onchain verifier let another party check the proof. The verifier checks whether the proof satisfies the relevant verification rules; it need not receive the private witness itself. This is a documented architecture for Ethereum privacy applications, not a guarantee that every application hides every related detail.

The example has a system boundary. It includes at least the private input, the rule being proved, the proof-generation process, the public commitment, and the verifier. The proof addresses a specific statement under a specific design. It does not, by itself, establish that the input was collected fairly, that a user’s device is secure, or that all surrounding activity is private.

It also helps to distinguish three practical uses:

- **Private-data proof:** Demonstrates that private witness data satisfies a rule, with a public commitment and verifier checking the proof.
- **Rollup validity proof:** Demonstrates that a proposed offchain state transition meets the rollup’s validity rules, so a base-layer verifier contract can accept it.
- **Private-system coordination:** Uses messaging, cryptography, proofs, and a consensus-controlled state machine to coordinate multiple systems of record while business data stays in those systems.

These examples demonstrate different properties. A proof about private data is not automatically a rollup proof, and a rollup’s validity proof is not necessarily a proof that the user’s activity is confidential.

## Core components of Zero Knowledge Proof Example

A useful way to map an implementation is to identify its components and the evidence each one handles.

1. **Private input or witness.** This is data used to support the statement. In a privacy application, proof generation can occur offchain so the witness need not be sent to the onchain verifier. The application’s actual handling of the witness still depends on its software and operational design.
2. **Statement and proof rules.** The circuit or other proof-system rules define what the proof establishes. The claim is only as meaningful as those rules: a verifier accepting a proof does not establish propositions that the rules never encoded.
3. **Commitment or state reference.** A public commitment can link verification to the relevant data or state without publishing the underlying witness. In a rollup, the relevant public material includes state-change summaries submitted to Ethereum.
4. **Proof generator.** The component that produces a proof from the input and rules. Its placement and operation are implementation choices; the privacy-application architecture separates offchain proof generation from onchain verification.
5. **Verifier.** Software or a contract checks whether the proof is valid for the stated rules and public inputs. For a validity rollup, a base-layer verifier contract accepts a cryptographic validity proof before the canonical rollup state is updated.
6. **State, messaging, and data publication.** These matter because proof verification is only one part of a working system. Rollups submit state-change summaries and cryptographic validity proofs to Ethereum, while data-publication policies and operator designs vary. In Baseline Core 1.0, systems coordinate through messaging, cryptography, proofs, and a consensus-controlled state machine, with business data kept in the systems of record.
7. **Keys and access controls.** Some designs add selective disclosure. Zcash viewing keys, for example, provide protocol-defined visibility into shielded transaction data without spending authority. The exact information exposed depends on the key type and protocol version.

This component map helps prevent a common category error: treating “the proof is valid” as equivalent to “the entire application is private, correct, available, and governed safely.” Those are separate questions.

## How Zero Knowledge Proof Example works

The following flows show what each example demonstrates and where verification occurs.

### 1. A privacy application proves a claim about private data

1. The application defines a statement and the rules that a proof must satisfy.
2. A user or application supplies the private witness needed to support that statement.
3. A proof is generated offchain. The architecture separates this private witness data and proof generation from the public commitment and onchain verifier.
4. The system makes the public commitment available to the verifier, along with the proof and required public inputs.
5. The onchain verifier checks the proof against the rules and public information. The verifier’s acceptance establishes only that the proof passed that verification process; it does not reveal the witness or independently validate every fact about the surrounding application.

This example demonstrates how a system can permit public verification without sending the private witness to the onchain verifier. It does not establish that metadata is hidden, that the proof system has no setup assumptions, or that keys and inputs are handled safely. Those remain system-specific risks.

### 2. A rollup proves an offchain state transition

1. Transactions are executed and state is stored offchain under the rollup’s design.
2. The rollup submits state-change summaries and cryptographic validity proofs to Ethereum.
3. A base-layer verifier contract checks the validity proof for the proposed offchain transition.
4. In the validity-rollup model, the canonical rollup state is updated after the verifier contract accepts the proof.

This example demonstrates proof-based verification of a state transition. It should not be read as a claim that rollup activity is private: the described function is to verify transition validity, and rollup designs differ in data-publication policies, proof systems, operators, and escape mechanisms. Correctness also depends on the proof system, verifier implementation, data availability, governance, and bridge contracts.

### 3. Several private systems coordinate without moving all business records

The Baseline Protocol reference architecture provides a different example. Multiple private systems of record coordinate using messaging, cryptography, proofs, and a consensus-controlled state machine while keeping business data in the systems of record. The proof-related mechanisms support coordination; the architecture does not imply that every implementation uses the same state machine, privacy method, governance, messaging, or operational controls.

The demonstration here is coordination across systems with records remaining in their respective systems—not automatic confidentiality of every interaction or trustlessness of every deployment. The OASIS Baseline Core 1.0 specification leaves important implementation choices to the deployment.

### 4. Viewing shielded data without spending authority

Zcash viewing keys illustrate selective visibility rather than a general-purpose proof that can be interpreted as a full audit. The protocol defines incoming and full viewing-key mechanisms for visibility into shielded transaction data, and these keys do not provide spending authority. What a key reveals depends on its type and protocol version. Disclosure through a viewing key is not equivalent to a universal financial audit.

Together, these examples show why the question “What does the proof demonstrate?” should be answered before asking what information the system hides. A proof can concern a private-data claim or a state transition, while a viewing key concerns authorized visibility into specified protocol data.

## Trust and control boundaries

A proof verifier is one boundary, not the whole trust model. For a privacy application, the proof’s soundness, circuit design, setup assumptions, metadata, key management, and data availability remain system-specific risks. A sound verification result does not remove those dependencies.

For a validity rollup, the base-layer verifier contract is a defined check, but the overall result also depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. Proof systems, data-publication policies, operator designs, and escape mechanisms vary by implementation.

For Baseline Core 1.0, the reference architecture coordinates private systems, but implementations choose key elements including the state machine, privacy method, governance, messaging, and operational controls. The specification does not make every implementation trustless. For Zcash viewing keys, the key type and protocol version determine the scope of visibility; possession of viewing access is not spending authority.

A practical boundary map therefore asks who controls the witness, proof generation, verification code, keys, data publication, and system configuration. It also asks which party can change the rules or operational process. The source-defined examples establish the kinds of components involved, but deployment-specific answers require evidence about the implementation being evaluated.

## Limitations and failure modes

A proof can be valid while the application remains unsuitable for a particular purpose. The circuit may encode a narrower statement than users assume; setup assumptions or key management may introduce risks; metadata may reveal information; and required data may not be available. These are explicit system-specific considerations for the privacy-application architecture.

A rollup proof does not remove dependencies on the verifier implementation, data availability, governance, or bridge contracts. Different rollups also make different choices about proof systems, publication policies, operators, and escape mechanisms. A proof of a state transition should not be confused with a guarantee about all operational or access paths.

Coordination across private systems does not make an implementation trustless by default. The Baseline reference architecture leaves choices about governance and operational controls to implementations. Similarly, a Zcash viewing key’s disclosure is bounded by its key type and protocol version and should not be treated as universal audit visibility.

Across all four examples, the central limitation is scope: verification supports the statement and inputs the design specifies. It does not automatically certify facts beyond them, guarantee system-wide privacy, or settle operational dependencies.

## What teams should verify

Before relying on a zero-knowledge design, technical and operational teams can use the following evidence-led checklist:

- **State the exact claim.** What proposition is being proved: a claim about private witness data, a rollup state transition, or a coordination condition? What is outside that proposition?
- **Trace private data.** Where is the witness created, held, and used? Which information is public, committed, or sent to a verifier? What metadata may remain visible?
- **Inspect the proof boundary.** Identify the proof rules, public inputs, commitment, proof generator, and verifier. Confirm which verifier accepts the proof and what acceptance means in that implementation.
- **Check security assumptions and dependencies.** For a privacy application, review proof soundness, circuit design, setup assumptions, key management, metadata, and data availability. For a rollup, also examine the verifier implementation, governance, and bridge contracts.
- **Follow the state and data flow.** For a rollup, determine what state-change summaries and other data are submitted to Ethereum and how its data-publication policy works. Do not infer confidentiality from validity verification alone.
- **Map operators and controls.** Identify who operates proof generation, verification, messaging, state machines, and system configuration. For a Baseline implementation, verify its chosen state machine, privacy method, governance, messaging, and operational controls rather than assuming the specification fixes them.
- **Scope disclosure keys.** If viewing keys are involved, identify the key type and protocol version, then document what information that combination reveals and what it does not. Keep visibility distinct from spending authority and from a universal audit.
- **Test failure and recovery paths.** For a rollup, document the implementation’s escape mechanisms and dependencies. For each design, establish what happens when proof generation, verification, data availability, or required services do not work as intended, using implementation-specific documentation.

The most useful “zero knowledge proof example” is not simply one that uses cryptography. It is one whose statement, inputs, verifier, data flows, and dependencies are explicit enough that a reviewer can tell exactly what the proof establishes—and what remains outside its scope.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zcash Protocol Specification, NU6.1](https://zips.z.cash/protocol/protocol.pdf) — Electric Coin Company and Zcash protocol contributors; retrieved 2026-10-18.
- [Baseline Core Version 1.0 - Part 1](https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html) — OASIS Open; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
