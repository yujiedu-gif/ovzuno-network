---
title: "zk proof: Meaning, Core Properties, and Limits"
description: "Learn what a zk proof is, how prover and verifier roles work, and what completeness, soundness, and zero-knowledge do—and do not—establish."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: []
author: "editorial_team"
primary_keyword: "zk proof"
owned_question: "What is a zk proof, what properties make it zero-knowledge, and what can a verifier conclude from one?"
risk_level: "medium"
---

A zk proof is a cryptographic method for showing that a defined statement satisfies specified conditions while limiting what the proof reveals about the private information used to support it. A verifier can conclude only what the statement and verification rules establish; the proof does not automatically validate broader claims or the information behind them.

## What a zk proof is

A proof system involves a **prover**, who supplies evidence, and a **verifier**, who checks it. The prover’s goal is to demonstrate that a particular statement meets the system’s conditions. A **witness** is the information used to support that statement; it may be private. The **proof** is the evidence presented for verification, and the **verification rules** specify how the verifier checks it.

“Zero-knowledge” describes a property of the proof: under the relevant formal model and assumptions, it should reveal no more about the witness than the statement’s validity. That is not a general promise that every related fact remains private. A statement can itself disclose information, and information outside the proof may also be visible. The claim is limited to what the proof reveals under its defined conditions.

This distinction helps separate a mathematical guarantee from a broad privacy claim. A proof may be designed to keep a witness undisclosed while showing that a specific condition holds. It does not, simply by being called zero-knowledge, establish that all inputs, outputs, metadata, or surrounding activity are private. Those questions depend on the scope of the statement and the system in which the proof is used.

## The statement, witness, and verifier

The **statement** is the proposition being checked. The **witness** is the supporting information that satisfies the conditions associated with that proposition. The **prover** uses the witness to produce a proof; the **verifier** checks the proof against the statement and the system’s verification rules.

Consider an abstract example: a statement says that a secret matches a specified public condition. The secret is the witness. The prover produces a proof, and the verifier checks whether it meets the rules for that statement. If verification succeeds, it supports the particular claim that the secret satisfies the specified condition. The verifier need not receive the secret itself as part of the proof.

This example is conceptual, not a description of a deployed system. It also does not show that the condition is meaningful, that the secret came from a reliable source, or that a real-world event occurred. Those conclusions would require information beyond the abstract relationship between statement, witness, proof, and verification.

The distinction between a statement and a witness is useful when reading claims about proof-based systems. Ask what is being asserted, what information supports it, and what the verifier actually checks. If a description moves from “the proof verifies this condition” to a larger conclusion, the additional step needs its own justification.

## Three properties that define zero-knowledge proofs

Three properties are commonly used to describe a zero-knowledge proof system: completeness, soundness, and zero-knowledge. Each concerns how the system behaves under specified conditions. They are not interchangeable, and none is an all-purpose guarantee about every implementation or surrounding system.

**Completeness** means that when a statement is valid and an honest prover has a suitable witness, the proof should be accepted under the specified verification rules. Put simply, a valid case should be capable of producing an accepted proof. The property depends on the system’s definitions of a valid statement and a suitable witness; it does not say that every statement is valid or that every claim presented to a verifier is true.

**Soundness** means that a prover should not be able to convince the verifier that a false statement is valid, except within the system’s defined error bounds. Those bounds and the assumptions under which soundness holds are part of the particular system’s formal account. Soundness therefore does not mean that deception is impossible in every circumstance. It describes a qualified property of verification, not a guarantee about unrelated claims or about implementation quality.

**Zero-knowledge** means that the proof should reveal no more about the witness than the validity of the statement, under the relevant formal model and assumptions. The verifier still learns whether the statement passes the verification rules. Zero-knowledge is therefore not “the verifier learns nothing”; it is a limit on what the proof reveals about the witness beyond the statement’s validity. Nor does the property establish that information outside the proof is concealed.

Taken together, the properties describe a system intended to accept valid proofs from honest provers, resist convincing verification of false statements within defined bounds, and limit information revealed about the witness. These guarantees have conditions and formal assumptions. A general definition of the properties is not a finding that a particular design or implementation satisfies them.

## What a valid proof does—and does not—show

A successful verification supports the statement encoded and checked by the proof system. The careful conclusion is that the proof passed the relevant verification rules for that statement. The verifier should not silently expand that conclusion into a broader claim about the statement’s usefulness, its context, or the accuracy of information that may have been used to construct it.

One important boundary is external information. An Ethereum smart contract cannot directly obtain off-chain facts that are not present in deterministic blockchain state without an oracle or transaction mechanism. Oracle designs add assumptions about data quality, freshness, availability, and trust. This is a specific example of a broader interpretive caution: verifying a proof about a defined input does not, on its own, establish that an external source reported the input accurately.

A proof’s conclusion is also distinct from the security of the entire system that uses it. For example, a zero-knowledge privacy application can separate private witness data and off-chain proof generation from a public commitment and an on-chain verifier. That architecture does not settle system-specific risks, which include proof soundness, circuit design, setup assumptions, metadata, key management, and data availability. The existence of a verification step should not be treated as a universal security or privacy certificate.

The same care applies to selective disclosure. Zcash viewing keys provide protocol-defined selective visibility into shielded transaction data without providing spending authority. The exact information visible depends on key type and protocol version; disclosure is not equivalent to a universal financial audit. This illustrates why a verifier’s access or conclusion must be described precisely rather than generalized into a claim that a proof reveals, conceals, or validates everything of interest.

## Questions to ask when evaluating a proof claim

Use the following questions to keep an explanation within what verification can support:

- **What exact statement is being checked?** Phrase the conclusion as narrowly as possible. Do not add a real-world implication that is absent from the statement.
- **What are the public inputs, and what is intended to remain private?** Separate the statement’s visible information from the witness and from any information outside the proof.
- **Which proof system and assumptions does the claim refer to?** The general properties of zero-knowledge proofs do not establish that a particular system satisfies them.
- **What does the verifier actually check?** Identify the verification rules and limit the conclusion to that check.
- **Where does the information used by the statement come from?** Cryptographic verification does not, by itself, establish the accuracy of external data or the trustworthiness of its source.
- **Which surrounding claims need independent evidence?** Security, privacy beyond the proof, recovery, compliance, and real-world outcomes are not established merely by using the term “zero-knowledge proof.”

The practical rule is to identify the statement, distinguish it from its witness, and read verification as evidence only for the defined claim under the system’s rules and assumptions. Completeness, soundness, and zero-knowledge explain what a proof system is designed to provide. They do not turn a successful verification into proof of everything a reader might want to know.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Zcash Protocol Specification, NU6.1](https://zips.z.cash/protocol/protocol.pdf) — Electric Coin Company and Zcash protocol contributors; retrieved 2026-10-18.
