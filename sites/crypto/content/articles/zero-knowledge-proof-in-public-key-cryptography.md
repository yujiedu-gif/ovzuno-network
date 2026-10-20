---
title: "Zero Knowledge Proof in Public Key Cryptography: How It Works"
description: "Understand Zero Knowledge Proof in Public Key Cryptography, including its architecture, operating flow, participants, technical dependencies, limitations, and pract."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: []
author: "editorial_team"
primary_keyword: "zero knowledge proof in public key cryptography"
owned_question: "How do zero-knowledge proofs work with public-key cryptography?"
risk_level: "medium"
---

# Zero Knowledge Proof in Public Key Cryptography: How It Works

A zero-knowledge proof can let one party demonstrate that a statement is true without revealing the private data used to establish it. Public-key cryptography can support this arrangement by giving a verifier a public value or verification mechanism with which to check a proof, while the underlying witness remains private. The exact architecture depends on the application: a privacy application, a rollup, and a system coordinating private business records use proofs in different ways.

The key distinction is between **proving a defined statement** and **disclosing the information behind it**. A proof is not a general declaration that a system is secure, that all relevant data has been disclosed, or that an application’s surrounding operations are correct. To understand what a particular design establishes, teams need to identify its statement, inputs, verifier, and dependencies.

## What Zero Knowledge Proof in Public Key Cryptography means

In a proof system, a **prover** creates evidence for a claim, and a **verifier** checks whether that evidence satisfies the system’s verification rules. The private information used to support the claim is commonly called the **witness**. The verifier may receive a public commitment to relevant data and a proof, rather than the witness itself.

In an Ethereum privacy-application architecture, private witness data and off-chain proof generation can be separated from a public commitment and an on-chain verifier that checks the proof. This describes an architectural pattern, not a guarantee that every application has the same privacy or security properties. Proof soundness, circuit design, setup assumptions, metadata, key management, and data availability remain system-specific risks. [claim_private_proof_public_verify]

Public-key cryptography is relevant because a system can expose public information or a verification interface while keeping other data private. But the phrase “zero knowledge proof in public key cryptography” does not identify one universal protocol, algorithm, or deployment model. It describes a relationship between private evidence and public verification; the details depend on the proof system and application.

A useful way to set the boundary is to ask: **What precise statement does the verifier accept?** For a privacy application, that might be a statement defined by the application’s circuit and public commitment. In a rollup, it concerns whether a proposed state transition is valid under the rollup’s rules. In a coordination system, proofs may help reconcile records without moving the underlying business data into a shared public store. These are related uses of cryptographic proofs, but they are not interchangeable guarantees.

## Core components of Zero Knowledge Proof in Public Key Cryptography

A typical architecture can be understood through several components. Their exact names and implementation choices vary, so this is a functional map rather than a claim that every system contains a single standard stack.

- **Private witness and inputs:** Data the prover uses to construct a proof. In a privacy application, witness data may remain off-chain. Keeping it private at proof generation does not, by itself, establish that it is protected from every other service or disclosure path.
- **Statement and circuit or rules:** The claim the proof is intended to establish. A circuit or equivalent specification expresses the conditions that the verifier is meant to accept. Its design determines what is and is not covered by the proof.
- **Public commitment or other public inputs:** Values made available to the verifier and tied to the statement. A commitment can connect a proof to public application state without publishing the underlying witness, but the commitment’s meaning depends on the system’s design.
- **Prover and proof-generation software:** The component that uses the witness and the statement’s rules to produce a proof. In the cited Ethereum privacy-application pattern, proof generation is off-chain. [claim_private_proof_public_verify]
- **Verifier:** Software or a contract that checks the proof against the relevant public inputs and verification rules. Acceptance means the proof passed those checks; it does not automatically verify every operational, governance, or data-handling assumption around the application.
- **State and publication layer:** Some applications connect proofs to a public commitment; a rollup submits state-change summaries and validity proofs to Ethereum. Other systems coordinate private records while retaining business data in the systems of record. [claim_zk_pattern] [claim_baseline_private_records]

This component map also helps distinguish proof verification from access control. A proof can establish a defined proposition without giving the verifier the private witness. Separate keys or permissions may govern who can inspect data or authorize actions. For example, Zcash viewing keys provide protocol-defined selective visibility into shielded transaction data without providing spending authority. What a viewing key reveals depends on its type and protocol version, and that disclosure is not equivalent to a universal financial audit. [claim_zcash_viewing_keys]

## How Zero Knowledge Proof in Public Key Cryptography works

A general workflow can be traced in five steps. Treat it as a conceptual sequence: specific systems may add components, combine steps, or use different terminology.

1. **Define the claim.** The application specifies what must be true and which public information will be associated with the claim. The statement must be precise enough that the verifier’s acceptance has a clear meaning.
2. **Prepare the witness.** The prover supplies the relevant private data to the proof-generation process. In the Ethereum privacy-application architecture, this work can happen off-chain, while the private witness data is separated from public verification. [claim_private_proof_public_verify]
3. **Generate proof evidence.** The prover’s software uses the witness and the system’s rules to produce a proof. Whether this step is sound and correctly implemented depends on system-specific factors, including proof soundness, circuit design, and setup assumptions. [claim_private_proof_public_verify]
4. **Submit the proof and public inputs.** The verifier receives the evidence and the information needed to evaluate it. In the cited privacy-application pattern, the public side includes a commitment and an on-chain verifier. For an Ethereum ZK rollup, execution and state storage move off-chain, while state-change summaries and cryptographic validity proofs are submitted to Ethereum. [claim_private_proof_public_verify] [claim_zk_pattern]
5. **Verify and apply the result.** The verifier checks the proof under its rules. In the Ethereum zero-knowledge-rollup model, a base-layer verifier contract accepts a cryptographic validity proof for a proposed off-chain state transition before the canonical rollup state is updated. Correctness still depends on the proof system, verifier implementation, data availability, governance, and bridge contracts. [claim_validity_proof]

The rollup example illustrates why “proof accepted” needs a carefully defined interpretation. The proof supports a validity claim about a proposed state transition under the rollup’s rules. It does not remove the need to examine how data is published, which operator design is used, or what escape mechanisms exist. Those features vary by implementation. [claim_zk_pattern]

A different pattern appears in the OASIS Baseline Core 1.0 reference architecture. It coordinates multiple private systems of record using messaging, cryptography, proofs, and a consensus-controlled state machine, while business data remains in those systems of record. The specification leaves choices about the state machine, privacy method, governance, messaging, and operational controls to implementations; it does not make every implementation trustless. [claim_baseline_private_records]

These examples share the use of cryptographic proofs, but they have different system boundaries. A privacy application separates witness data from public verification. A rollup uses validity proofs in a state-transition and base-layer verification flow. A private-record coordination architecture uses proofs as part of coordinating separate systems. The appropriate questions therefore concern the particular statement and surrounding workflow, not the label “zero knowledge” alone.

## Trust and control boundaries

A proof system’s verification result is only one layer of a deployed application. A practical review separates what the cryptographic verification establishes from the other controls on which the system relies.

**Proof and verifier boundary:** Identify the exact statement, public inputs, and verification rules. Then identify which implementation produces and checks the proof. For rollups, the accepted model specifically places a base-layer verifier contract in the path to updating canonical rollup state, but correctness also depends on the verifier implementation and proof system. [claim_validity_proof]

**Data boundary:** Determine where the witness and application records live, what is submitted publicly, and whether required data remains available. In the cited privacy-application architecture, witness data and proof generation can remain off-chain while a public commitment and verifier support on-chain checking. Data availability remains a system-specific risk. [claim_private_proof_public_verify]

**Operator and governance boundary:** Identify which parties operate services, manage upgrades, set policies, or control state-machine and messaging choices. Ethereum ZK-rollup designs vary in operator design and escape mechanisms; the Baseline reference architecture likewise leaves governance and operational controls to implementations. [claim_zk_pattern] [claim_baseline_private_records]

**Key and disclosure boundary:** Separate the ability to prove a statement from the ability to view data or authorize spending. Zcash’s viewing-key mechanisms illustrate that selective visibility can be distinct from spending authority, while the information exposed depends on key type and protocol version. [claim_zcash_viewing_keys]

These boundaries prevent a common category error: assuming that privacy at the proof interface means every associated service, record, or transaction is private. The accepted architecture claims support specific patterns and limitations; they do not establish a universal privacy guarantee for all systems using proofs.

## Limitations and failure modes

The first limitation is **scope**. A verifier can check only what its rules and inputs define. If a statement omits a relevant condition, proof acceptance does not add that condition. Teams should compare the intended business or protocol claim with the actual statement encoded for verification.

The second is **implementation dependence**. Proof soundness, circuit design, setup assumptions, and verifier implementation affect what an accepted proof means. The cited privacy-application architecture explicitly identifies proof soundness, circuit design, and setup assumptions as system-specific risks; the rollup model also depends on its verifier implementation. [claim_private_proof_public_verify] [claim_validity_proof]

The third is **data availability and publication policy**. A proof may establish a validity claim without settling whether the data needed for users or other system participants is available. Data availability is listed as a system-specific risk for the privacy-application pattern and a dependency for canonical rollup-state correctness. Rollup data-publication policies vary by implementation. [claim_private_proof_public_verify] [claim_validity_proof] [claim_zk_pattern]

The fourth is **metadata and key management**. Keeping a witness out of the proof submission does not establish that metadata reveals nothing, or that keys are managed safely. Both metadata and key management are identified as system-specific risks in the privacy-application architecture. [claim_private_proof_public_verify]

The fifth is **surrounding-system dependence**. Governance and bridge contracts remain relevant to rollup correctness, while a private-record coordination specification does not make all implementations trustless. Proofs therefore cannot be treated as substitutes for examining the services, contracts, processes, and controls that interact with them. [claim_validity_proof] [claim_baseline_private_records]

Finally, **selective disclosure has limits**. A viewing key can enable protocol-defined access to some shielded transaction data without granting spending authority, but the visible information varies with key type and protocol version. That disclosure should not be characterized as a universal audit of a person’s or organization’s financial activity. [claim_zcash_viewing_keys]

## What teams should verify

Before relying on a zero-knowledge design that uses public-key cryptography, builders and operators can use the following evidence-led checklist:

1. **Write down the statement.** What exact proposition does the proof establish? Which conditions are included, and which remain outside the proof?
2. **Map private and public data.** Identify the witness, public inputs, commitments, summaries, and any records retained off-chain or in private systems of record. Confirm the description matches the architecture being evaluated. [claim_private_proof_public_verify] [claim_zk_pattern] [claim_baseline_private_records]
3. **Trace the proof path.** Record who generates the proof, where generation occurs, who submits it, and which verifier checks it. For a rollup, establish whether the described flow matches the model in which a base-layer verifier contract accepts a validity proof before canonical state updates. [claim_validity_proof]
4. **Inspect system-specific dependencies.** Review evidence about proof soundness, circuit design, setup assumptions, verifier implementation, data availability, metadata, and key management where applicable. Do not infer these properties merely from the use of a proof. [claim_private_proof_public_verify] [claim_validity_proof]
5. **Check publication and escape design.** For a rollup, establish its data-publication policy, operator design, and escape mechanisms; the cited architecture notes that these vary by implementation. [claim_zk_pattern]
6. **Separate proof checks from governance and operations.** Identify who controls upgrades, messaging, state-machine choices, and operational procedures. The Baseline reference architecture explicitly leaves such implementation choices open and does not imply that every deployment is trustless. [claim_baseline_private_records]
7. **Test disclosure and authority separately.** If selective viewing is offered, establish which key type and protocol version apply, what information becomes visible, and whether the key grants any authority. For Zcash viewing keys, protocol-defined visibility is distinct from spending authority and is not a universal financial audit. [claim_zcash_viewing_keys]
8. **Match evidence to the deployment.** Confirm that documentation describes the relevant protocol model and implementation. A reference architecture or general rollup description is not, on its own, evidence that every deployment has identical controls or behavior.

The central technical question is not simply whether a system uses a zero-knowledge proof. It is what statement the proof verifies, which public inputs bind it to the application, who controls the prover and verifier, and which data, key, governance, and operational assumptions remain outside cryptographic verification. That framing makes it possible to assess public verification and private witness handling without treating either as a blanket guarantee.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zcash Protocol Specification, NU6.1](https://zips.z.cash/protocol/protocol.pdf) — Electric Coin Company and Zcash protocol contributors; retrieved 2026-10-18.
- [Baseline Core Version 1.0 - Part 1](https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html) — OASIS Open; retrieved 2026-10-19.
