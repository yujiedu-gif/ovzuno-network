---
title: "Zero Knowledge Proof: How It Works"
description: "Understand Zero Knowledge Proof, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: []
author: "editorial_team"
primary_keyword: "zero knowledge proof"
owned_question: "What is a zero-knowledge proof, and how does it work in blockchain systems?"
risk_level: "medium"
---

# Zero Knowledge Proof: How It Works

A zero-knowledge proof lets one party demonstrate that a statement is true without revealing the private information used to establish it. In blockchain systems, this idea can support privacy applications or help verify state changes processed outside a base layer. Those are related uses of proofs, but they solve different problems: hiding witness data is not the same as scaling transaction execution.

The phrase “zero knowledge” describes a property of a proof interaction or system, not a guarantee that an entire application reveals nothing. Public commitments, transaction timing, metadata, published data, software behavior, and key-management practices can still disclose information or affect security. The exact properties depend on the implementation.

## What Zero Knowledge Proof means

A proof system involves a statement to be checked, information that supports the statement, a method for producing a proof, and a method for verifying it. The supporting information is often called a **witness**. A prover uses the witness to generate a proof; a verifier checks whether that proof establishes the claimed statement under the system’s rules.

In a privacy application, the witness may be private while a commitment and proof are public. An Ethereum.org-described architecture separates private witness data and off-chain proof generation from a public commitment and an on-chain verifier that checks the proof. This separation can let a contract verify a claim without receiving the underlying witness. It does not, by itself, establish that the whole application is private: proof soundness, circuit design, setup assumptions, metadata, key management, and data availability remain system-specific risks.

A second use appears in Ethereum zero-knowledge rollups. In that architecture, execution and state storage move offchain, while state-change summaries and cryptographic validity proofs are submitted to Ethereum. A validity rollup updates its canonical rollup state after a base-layer verifier contract accepts a validity proof for the proposed offchain state transition. Here the proof is used to validate a computation or state change; it does not necessarily conceal all transaction information.

These examples also clarify the system boundary. A proof can establish a defined statement under specified verification rules. It cannot independently ensure that the statement is useful, that the application’s inputs are appropriate, or that all surrounding services behave as intended.

## Core components of Zero Knowledge Proof

The components vary by application, but an evaluation commonly needs to identify the following:

- **Statement:** The precise proposition the verifier is meant to accept, such as whether a proposed state transition satisfies the rules encoded by a system.
- **Witness:** The private or offchain information used to construct the proof. Which information is hidden—and from whom—depends on the design.
- **Circuit or relation:** The formal rules connecting the witness to the statement. In a privacy application, circuit design is one of the implementation-specific risks; teams should establish what the circuit actually checks rather than infer behavior from the “zero-knowledge” label.
- **Proof-generation software:** The software that processes the witness and produces a proof. In the cited privacy-application architecture, this work occurs offchain. That describes the architecture, not a requirement that every proof system generate proofs in the same way.
- **Commitment or public input:** Information made available to the verifier. In the Ethereum.org privacy-application pattern, a public commitment accompanies the proof. A commitment is not a promise that all related activity is unobservable; surrounding data and metadata need separate assessment.
- **Verifier:** Software that checks a proof against the expected statement and public inputs. In the cited pattern, an on-chain verifier checks the proof. In the rollup model, a base-layer verifier contract accepts a validity proof before the canonical rollup state is updated.
- **State and publication path:** For a rollup, teams need to distinguish offchain execution and storage from the summaries and proofs submitted to Ethereum. Data-publication policies and escape mechanisms vary by implementation.
- **Keys and disclosure controls:** Key handling can affect what information is exposed and who can act on it. For example, Zcash’s protocol-defined viewing keys provide selective visibility into shielded transaction data without spending authority. The exact information visible depends on key type and protocol version, and such disclosure is not equivalent to a universal financial audit.

A blockchain is a separate part of this picture, not a synonym for a proof system. NIST characterizes a blockchain as a tamper-evident and tamper-resistant digital ledger implemented in a distributed fashion, usually without a central repository and often without a central authority. Participation, consensus, privacy, finality, and governance vary across blockchain systems.

## How Zero Knowledge Proof works

A generic proof workflow can be understood as a sequence, though particular systems may combine or implement steps differently:

1. **Define the claim.** The application specifies what the verifier should accept. A useful review begins with this exact statement: vague claims make it hard to assess what a successful verification means.
2. **Prepare the witness and public inputs.** The prover obtains the information needed to support the claim and identifies what will be supplied publicly. In a privacy-oriented design, the witness may remain offchain while a commitment is public.
3. **Generate the proof.** Proof-generation software uses the witness and the system’s rules to produce a proof. In the cited Ethereum.org privacy-application architecture, proof generation is offchain.
4. **Submit the proof for verification.** The verifier checks the proof against the statement and relevant public inputs. In the privacy-application pattern, an on-chain verifier performs this check. The verifier’s acceptance is meaningful only in relation to the rules it implements.
5. **Apply the verified result.** An application may use acceptance to authorize an action or update state. In an Ethereum validity-rollup model, the canonical rollup state is updated after a base-layer verifier contract accepts a cryptographic validity proof for the proposed offchain state transition.
6. **Check what remains observable.** Verification does not erase information already published or necessarily hide timing, metadata, or other application activity. For a rollup, teams should inspect what state-change summaries and other data are submitted to Ethereum, as well as the implementation’s data-publication policy.

A rollup workflow adds a distinct execution pattern: execution and state storage occur offchain, and state-change summaries plus validity proofs are submitted to Ethereum. The base-layer verifier’s acceptance is a condition for updating canonical rollup state in the described model. It should not be confused with a claim that every rollup uses the same proof system, publication policy, operator design, or escape mechanism.

## Trust and control boundaries

A proof’s verification result is one component of a larger system. In a privacy application, the public verifier can check a proof without receiving the private witness in the described architecture. That does not establish that witness data was handled safely before proof generation, that keys were protected, or that metadata is non-revealing. Those questions depend on the application and its operations.

For validity rollups, the base-layer verifier contract is a central control point for accepting a proposed state transition. But correctness still depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. A proof acceptance should therefore be treated as evidence that the implemented verification conditions passed—not as a universal guarantee about every dependency or operational pathway.

Operators and users may also interact with services or keys outside the verifier. A team should map who generates proofs, who can submit them, where relevant data is stored or published, and how disclosures are controlled. The accepted sources do not establish one universal custody, recovery, operator, or governance model for all zero-knowledge systems.

## Limitations and failure modes

“Zero knowledge” does not mean “no information is ever revealed.” A system may expose public inputs, commitments, state-change summaries, or metadata. In a rollup, data-publication policies vary; in a privacy application, metadata and data availability remain system-specific risks.

Nor does proof verification remove implementation risk. The accepted privacy-application claim identifies proof soundness, circuit design, setup assumptions, metadata, key management, and data availability as risks that remain specific to the system. For validity rollups, the proof system, verifier implementation, data availability, governance, and bridge contracts still affect correctness.

Finally, a blockchain’s properties should not be inferred from the proof alone. NIST’s overview notes that blockchain systems vary in participation, consensus, privacy, finality, and governance. A proof does not make those broader system characteristics uniform. Teams should avoid treating the presence of a zero-knowledge proof as evidence of a particular privacy level, decentralization model, or operational guarantee unless the implementation documents and supports that specific claim.

## What teams should verify

Before relying on a zero-knowledge design, technical decision-makers can use an evidence-led review:

1. **Write down the statement.** What exact proposition does the proof establish? What is outside its scope?
2. **Map private and public data.** Identify the witness, public inputs, commitments, published summaries, and potentially observable metadata. Confirm who can access each item and at what stage.
3. **Inspect the circuit or relation.** Determine which rules it encodes and how circuit design affects the claim being verified.
4. **Trace proof generation and verification.** Identify the software that generates proofs, where it runs, what the verifier checks, and which contract or component applies the result.
5. **Review dependencies.** For a privacy application, examine proof soundness, setup assumptions, key management, and data availability. For a validity rollup, examine the proof system, verifier implementation, data availability, governance, and bridge contracts.
6. **Check publication and escape behavior.** For a rollup, establish what summaries and data are submitted to Ethereum and what the implementation documents about data-publication policies and escape mechanisms. These vary by implementation.
7. **Separate proof validity from disclosure rights.** If viewing keys are used in a Zcash context, verify the key type and applicable protocol version. Viewing keys provide selective visibility without spending authority, but visibility is not a universal audit.
8. **Keep system claims scoped.** Record which behavior is documented for the specific application or rollup, and do not generalize it to all zero-knowledge systems or blockchains.

The practical takeaway is that a zero-knowledge proof is a verification mechanism for a defined statement, not a complete privacy or security architecture on its own. Understanding the statement, witness, public inputs, proof-generation path, verifier, and surrounding dependencies lets a team assess what the proof establishes—and what it leaves unresolved.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Zcash Protocol Specification, NU6.1](https://zips.z.cash/protocol/protocol.pdf) — Electric Coin Company and Zcash protocol contributors; retrieved 2026-10-18.
