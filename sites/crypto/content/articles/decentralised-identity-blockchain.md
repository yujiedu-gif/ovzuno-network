---
title: "Decentralised Identity Blockchain: Architecture and Trade-offs"
description: "Learn how a decentralised identity blockchain can support identifiers and credential verification, what stays off-chain, and which privacy and recovery trade-offs to"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "decentralised identity blockchain"
owned_question: "How can a blockchain support decentralised identity, and which identity functions belong on-chain versus off-chain?"
risk_level: "medium"
---

A decentralised identity blockchain can provide a shared place to publish or verify selected identity-related records, but it does not need to store a person’s credential or personal details on-chain. The identity flow—who issues a credential, who holds it, and what a verifier checks—depends on the system’s design. The allowed evidence here does not establish a particular identity standard, proof format, status mechanism, or recovery method, so those details must be assessed for the implementation in question.

## What decentralised identity means in a blockchain context

A useful way to map an identity system is by the roles involved. An **issuer** creates a credential, such as a statement about a person or organization. A **holder** receives and manages it. A **verifier** asks to check information presented by the holder. These are functional roles; one organization or application might perform more than one, depending on the design.

A credential is not the same thing as an identifier. An identifier is a reference used to distinguish or locate an identity-related subject or record. A credential is a claim made by an issuer. A verifier needs a way to assess both the claim and the issuer’s authority to make it; the mere presence of a record on a blockchain does not establish that a claim is true.

Decentralisation describes aspects of system architecture and governance, not a guaranteed privacy outcome. For example, blockchain participation may be permissionless, with participation in block publication open, or permissioned, with ledger access or maintenance controlled by authorized participants. Some systems can also combine open transaction submission with restricted validation or other controls. Those choices affect who can write, read, validate, or administer records; they do not, on their own, determine what personal information is disclosed.

Cryptographic keys may be used to authorize actions associated with an identity or to support a presentation. But the available evidence does not establish an identity-specific key model or prove that possession of a key establishes a person’s real-world identity. A design must explain how it connects keys, identifiers, issuers, and the claims being verified.

## What a blockchain contributes to decentralised identity

A blockchain may serve as a shared registry for selected information—for example, records that help participants determine which issuer-controlled information to consult. This is an architectural option, not a requirement for every identity system. The evidence available for this article does not document a specific identity registry or establish that identifier records, issuer keys, credential references, or status information must be stored on-chain.

The key distinction is between **record coordination** and **identity proofing**. A ledger can coordinate records under its own participation and validation rules. It does not independently establish that an issuer checked a person’s identity correctly, that a credential’s contents are accurate, or that the person presenting it is the person described. Those conclusions depend on the issuer’s processes and the verifier’s checks, which must be specified outside the general label “blockchain identity.”

Permission models provide one way to describe who may participate. Permissionless participation is open in the relevant sense; permissioned systems restrict ledger maintenance to authorized users, and may also restrict reading or transaction access. A real system can separate these rights. Therefore, “decentralised” should be unpacked into operational questions: who may create records, who validates them, who can change system rules, and who can access the information?

Some identity architectures may use a registry on a blockchain, another kind of registry, or no blockchain at all. The allowed evidence does not support a universal claim that a blockchain is necessary or superior for identity. The practical question is whether shared record coordination solves a defined problem without creating unacceptable data exposure, governance dependence, or operational complexity.

## How credentials move from issuer to verifier

A technology-neutral flow can be described in stages, while leaving implementation-specific mechanisms open:

1. **Issuance:** An issuer creates a credential containing one or more claims and provides it to a holder. The system needs to define how the holder can identify the issuer and how the verifier can assess the credential’s authenticity.
2. **Holder management:** The holder keeps or accesses the credential through a chosen application or service. Whether the holder directly controls the relevant keys and data depends on the implementation; “holder” does not itself guarantee self-custody.
3. **Presentation:** A verifier requests information, and the holder supplies a credential or a presentation derived from it. The evidence supplied for this article does not establish selective-disclosure proofs or any specific cryptographic presentation method. Do not assume that a system can reveal only a requested claim without verifying its technical specification.
4. **Verification:** The verifier checks the presented information using the system’s defined procedures. Depending on the design, that may involve checking issuer authenticity, proof validity, and whether the credential remains valid or has been revoked. The allowed claims do not document any particular status mechanism or the reliability of such checks.

This flow separates responsibilities. The blockchain protocol governs ledger participation and records according to its rules. An identity application handles its own user experience and data handling. Issuers are responsible for the claims they issue; holders decide what to present; verifiers decide what checks they require. A blockchain record cannot substitute for these roles or make their processes trustworthy by itself.

Before implementation, document the exact checks at each step. For example: What evidence connects an issuer to the credential? What does the verifier validate? How is status information obtained, and what happens if that service or registry cannot be reached? If the design uses cryptographic proofs, identify the proof system and what it proves rather than treating “proof” as a complete explanation.

## On-chain and off-chain data boundaries

**On-chain** means recorded in the blockchain’s ledger; **off-chain** means held or processed elsewhere. A design may put coordination information on a ledger while keeping credential contents and personal data in a holder’s application or another system. But the permitted evidence does not establish what is commonly done across decentralised identity implementations, nor does it establish a universal rule that personal data must remain off-chain.

Treat the data boundary as an implementation question. Map every item the system creates or reads: credential contents, identifiers, references, timestamps, status information, and any cryptographic material. Record where each item is stored, who can read it, how long it is retained, and whether it is submitted to a ledger or service. A record that contains no obvious name may still reveal information in context or enable correlation; the evidence available here does not support a claim that hashes or other transformed data are automatically anonymous.

Review the whole data path, not just the blockchain transaction. Applications, registries, issuer systems, and verifier services may handle information beyond what appears in a ledger. A privacy assessment should therefore state what participants can observe, what records can be linked, and which assumptions depend on particular service operators or governance arrangements. If these facts are unknown, identify them as unresolved rather than describing the system as private.

## Trade-offs to assess before implementation

A design review should start with key and recovery responsibilities. Identify who controls keys used to access credentials or authorize presentations, what happens if a device or key is lost, and who can restore access. The evidence for this article does not establish a standard recovery process. Avoid claiming that a system is recoverable, user-controlled, or resistant to account loss without documenting the specific mechanism and its dependencies.

Next, examine credential status and service availability. If a verifier needs a status check, determine what source it consults, who operates that source, and how the verifier behaves when it is unavailable. The allowed evidence does not establish how revocation works in a given identity system, or whether a status check can be performed without exposing additional information. These are design questions, not properties to infer from using a blockchain.

Governance and interoperability also need explicit answers. Determine who can issue recognized credentials, who sets verification rules, how changes are approved, and whether participants can use credentials across the applications they need. Permissioned access may restrict who maintains a ledger, while permissionless access may open participation; neither label alone resolves trust, accessibility, or user-consent questions.

Finally, require implementation-specific evidence for claims about security, recovery, fees, availability, regulation, tax, jurisdiction, or compliance. The evidence available here does not support universal claims on those topics. A sound assessment names the system and version, identifies the relevant operators and data flows, and distinguishes documented behavior from assumptions. That keeps the central architectural point clear: a blockchain can coordinate selected records, while identity claims, credential handling, privacy, and recovery depend on the surrounding system.

## Sources and references

- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
