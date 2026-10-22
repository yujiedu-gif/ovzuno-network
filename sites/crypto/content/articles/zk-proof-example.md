---
title: "zk proof example: Three Ways to Verify a Claim Privately"
description: "Explore a zk proof example for age checks, secret knowledge, and transaction validity, with a clear look at what each proof reveals and keeps private."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: ["zero-knowledge proof example", "proof of age without revealing date of birth", "private transaction verification"]
author: "editorial_team"
primary_keyword: "zk proof example"
owned_question: "What are clear examples of zero-knowledge proofs, and what information does each example reveal or keep private?"
risk_level: "medium"
---

A zero-knowledge proof example is a person proving they meet a stated age threshold without disclosing their full birth date. The verifier checks a defined claim using the proof and its public inputs; the underlying value can remain private. Similar examples can demonstrate knowledge of a secret or support verification of a transaction’s validity. In each case, the proof establishes only the statement the system checks, and what stays private depends on the system’s design.

## What makes an example a zero-knowledge proof?

A **prover** creates evidence for a claim, and a **verifier** checks that evidence. The claim is the statement being tested. A **witness** is private information used to support the statement, such as a birth date or secret value. **Public inputs** are the information made available to the verification process. A verifier can learn something from those inputs even when the witness itself is withheld.

A zero-knowledge privacy application can separate private witness data and off-chain proof generation from a public commitment and an on-chain verifier that checks the proof. This describes one possible architecture, not a promise that every application hides the same information. Proof soundness, circuit design, setup assumptions, metadata, key management, and data availability remain system-specific risks. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

To assess an example, identify four things: the exact claim, the public inputs, the private witness, and what the verifier can infer from the combination. The proof is not a general-purpose certificate about facts outside its statement. Nor does calling data a witness make every related detail private: information included as a public input is available to the verification process.

The scenarios below are illustrative, not descriptions of a particular credential or transaction product. They show how to frame a claim and its disclosure boundary without assuming that all proof systems use the same construction or reveal the same data.

## Age or eligibility without disclosing identity details

**Illustrative claim:** “This person meets the specified minimum-age threshold.” A hypothetical proof could be designed to let a verifier check that condition without receiving the person’s full date of birth.

**Public inputs:** The threshold and the statement being checked may be public. The proof system’s verification rules are also relevant to the check. The precise public inputs depend on the design; this example does not prescribe a universal format.

**Private witness:** The person’s birth date could be used as witness information. If the proof is designed to withhold that value, the verifier can check the threshold claim without receiving the full date itself.

**What the verifier can infer:** The verifier can infer whether the submitted proof supports the specified threshold claim under the system’s rules. That is narrower than learning the exact birth date or all the person’s identity details.

**Caveat:** The proof does not, by itself, establish who supplied the underlying date, whether that source is trustworthy, or whether a particular credential is valid or current. It also does not establish that the system has a particular issuance or revocation process. Those questions require evidence about the specific credential and verification flow; they cannot be inferred from the threshold proof alone.

This example is about limiting disclosure for one check, not about guaranteeing anonymity throughout an interaction. A verifier may receive information beyond the proof, and other parts of a system may handle data differently. The practical question is which inputs and outputs the particular verification flow exposes—not simply whether the full date appears in the proof.

## Proving knowledge of a secret without sharing it

**Illustrative claim:** “I know a secret value that satisfies a specified relation.” The relation is the rule the verifier checks; the secret value is the private witness. In a hypothetical example, the system could check whether a secret corresponds to a public commitment without asking the prover to reveal the value.

**Public inputs:** The relation and any information needed to define the check may be public. A public commitment could also be an input in this illustrative setup. The specific inputs depend on the proof’s design.

**Private witness:** The secret value itself can remain undisclosed if the proof is constructed to support that knowledge claim without revealing the value.

**What the verifier can infer:** The verifier can infer that the proof supports the claim that the prover knows a value satisfying the stated relation, according to the system’s verification rules. The verifier receives evidence to check, not necessarily the secret.

**Caveat:** This does not establish the prover’s real-world identity, how the secret was obtained, or whether the prover has a separate right or authority. Those are different claims. “The prover knows a value satisfying this relation” is narrower than “the prover is the rightful owner” unless the system also encodes and checks additional information that supports that conclusion.

Keeping the statement narrow helps prevent an overclaim. A knowledge proof concerns the relation it checks. It does not automatically answer broader questions about a person, the history of a secret, or the context in which the proof is presented.

## Private transaction validity as a zk proof example

**Illustrative claim:** “This proposed transaction satisfies the validity rules checked by the system.” In an Ethereum ZK rollup pattern, execution and state storage take place offchain while state-change summaries and cryptographic validity proofs are submitted to Ethereum. This is a specific architecture example: it describes where execution occurs and what is submitted, not a universal design for every private transaction. [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

In a validity-rollup model, a base-layer verifier contract accepts a cryptographic validity proof for a proposed offchain state transition before updating the canonical rollup state. The proof’s role is to support that transition under the system’s rules. Correctness still depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. [source](<https://ethereum.org/developers/docs/scaling/zk-rollups/>)

**Public inputs:** The state-change summaries submitted to Ethereum and the information used by the verifier are not made private merely because a validity proof is involved. The particular public inputs and published data depend on the system’s design.

**Private witness:** Some underlying transaction values or other data may be kept out of the proof’s public inputs, depending on the transaction design. This is a possibility to assess in a specific system, not a claim that every ZK rollup hides every transaction detail.

**What the verifier can infer:** The verifier checks the proposed state transition against the rules represented by the proof and verification process. A successful check supports that defined validity claim; it does not establish unrelated facts about the transaction or the whole system.

**Caveat:** A validity proof is not, by itself, a guarantee that the system is secure, compliant, or private in every respect. Its scope is the encoded claim and the checks performed. Published summaries and other public inputs may reveal information, and the system’s proof, verifier, data availability, governance, and bridge design remain relevant to the result.

## What these examples do not guarantee

Across all three examples, the proof establishes only the statement encoded and checked by the system. An age-threshold claim is not automatically proof of identity. A knowledge claim does not explain how the secret was obtained. A transaction-validity claim is not a complete assessment of the system that uses it.

Keep the proof separate from the surrounding information flow. Public inputs are available to the verification process, and metadata or other parts of an application may disclose information outside the proof. A proof’s privacy boundary therefore cannot be assessed by looking only at whether the witness is withheld; the statement, inputs, outputs, and system design all matter.

A useful review sequence is to write down the claim in one sentence, list the public inputs, identify the witness intended to stay private, and state precisely what the verifier can infer. Then distinguish that inference from any broader conclusion about identity, ownership, system security, or privacy. If a required detail about a specific credential or system is not established, treat it as an open question rather than filling in an assumed answer.

These examples show the central distinction: verification can establish a limited claim without requiring disclosure of the underlying value, but it does not make every connected fact private or prove more than the encoded statement. The verifier’s actual knowledge depends on the proof’s public inputs and the surrounding system, so each scenario must be evaluated on its own terms.

## Sources and references

- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
