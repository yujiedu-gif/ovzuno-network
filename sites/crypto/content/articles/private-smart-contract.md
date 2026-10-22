---
title: "Private Smart Contract: Meaning, Privacy Models, and Limitations"
description: "Learn what a private smart contract can keep confidential, how privacy approaches differ, and why code, inputs, state, and outputs may still be exposed."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "private smart contract"
owned_question: "What does “private smart contract” mean, which parts of a contract’s activity can remain private, and what limitations should builders account for?"
risk_level: "medium"
---

A **private smart contract** is a smart-contract system designed to limit who can learn particular parts of its activity, such as inputs, state, or outputs. The term does not specify which parts are hidden or from whom: privacy depends on the application’s architecture, the participating systems, and the information it reveals. Builders should identify the data and observers in scope before treating a design as private.

## What a private smart contract means

A smart contract is executable code and data deployed on a blockchain. “Private” can describe several different protections, which should not be treated as interchangeable:

- **Code confidentiality:** whether observers can inspect the program itself.
- **Input confidentiality:** whether observers can see data supplied to an operation.
- **Execution confidentiality:** whether they can observe intermediate computation or its trace.
- **State confidentiality:** whether they can read the contract’s stored data.
- **Output confidentiality:** whether they can see the result, or only a limited proof that the result meets a condition.

A system might protect one category while exposing others. For example, concealing input values would not, by itself, show that the program code, resulting state, or output is also confidential. The word “private” alone is not a technical guarantee; the design must specify what information is protected, which parties are trusted, and what evidence supports the claim.

Privacy is also distinct from correctness and security. A system can restrict access to business data while still depending on implementation choices for its state machine, cryptography, messaging, governance, and operational controls. An architecture that coordinates multiple private systems of record, for example, does not automatically make every implementation trustless or confidential in every respect. [source](<https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html>)

## What public blockchains can reveal

On a public blockchain, transaction and contract activity may leave records that participants can inspect. What those records expose depends on the chain and application, so builders should examine the actual data paths rather than assume either complete visibility or automatic confidentiality.

A useful starting point is to separate the contract’s internal business meaning from the information its surrounding application handles. A decentralized application can combine a smart contract on a network with a frontend interface. The interface is a distinct component: its requests, displays, and supporting services may handle information not represented in the contract’s on-chain state. [source](<https://ethereum.org/developers/docs/dapps/>)

The contract is not necessarily the only place where sensitive information exists. A business process may involve private databases, messages between participants, or application services. In the Baseline reference architecture, multiple private systems of record coordinate through messaging, cryptography, proofs, and a consensus-controlled state machine while business data remains in those systems of record. This illustrates an architectural separation; it does not establish that all deployments use the same privacy method or controls. [source](<https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html>)

Therefore, a privacy review should trace information across the whole application: what users submit, what services receive it, what the contract records, what other participants can access, and what the interface or supporting systems may disclose. The available evidence here does not establish a universal list of public transaction fields or a chain-independent visibility rule. Those details require documentation for the specific network and application.

## Private smart contract approaches and trade-offs

Privacy designs differ in what they reveal and how another party can verify a result. One documented pattern separates private witness data and off-chain proof generation from a public commitment and an on-chain verifier. The verifier checks the proof rather than receiving all of the private witness data. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

This pattern can let an application keep witness data separate from the public verification step, but it does not mean that every input, output, or surrounding action is hidden. The commitment and proof are public-facing elements, and the application must define what they disclose. The evidence also leaves proof soundness, circuit design, setup assumptions, metadata, key management, and data availability as system-specific risks. A proof-based design should therefore be assessed against its own implementation and threat model, not treated as a blanket privacy guarantee. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

Another architectural choice is to control participation in a network. Permissionless access and permissioned access describe different ways participation may be organized; real systems can also combine open transaction submission with restricted validation or other hybrid controls. This is an access model, not itself a confidentiality mechanism: limiting who can participate does not, without further evidence, establish which data those participants can read. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

A system may also coordinate private records without placing all business data in a shared state machine. The Baseline architecture is one example, but its implementations choose their state machine, privacy method, governance, messaging, and operational controls. Builders should not infer identical confidentiality or trust properties from a shared architectural label. [source](<https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html>)

These approaches should not be collapsed into one category. Proof-based verification, participant restrictions, and coordination among private systems address different design questions. A proposal should state which information is protected, who can access it, and how the system verifies the operation while maintaining the intended boundary.

## Where privacy protections can fail or stop

A privacy mechanism protects only what its design covers. If an application places sensitive information in a component outside that boundary, or reveals it through an output, the privacy claim may not extend to that information. Interfaces and other supporting components also matter: an application can combine a contract with a frontend, so evaluating the contract alone does not describe the full information flow. [source](<https://ethereum.org/developers/docs/dapps/>)

Likewise, a proof that an on-chain verifier accepts does not settle every question about the system. The documented proof pattern leaves key management, metadata, data availability, circuit design, setup assumptions, and proof soundness as matters to examine for the particular system. [source](<https://ethereum.org/latest/privacy-apps-on-ethereum/>)

Privacy should not be used as a synonym for anonymity, security, correctness, or legal compliance. The evidence available for this article supports specific architectural distinctions and limitations; it does not establish universal protections against timing analysis, access-pattern disclosure, compromised keys, or information exposed by user behavior. Those risks must be evaluated for the actual design rather than asserted or dismissed categorically.

## Questions to ask before choosing a design

Start with a concrete information-flow and threat-model review:

1. **What needs protection?** Name the specific data: code, inputs, intermediate computation, state, outputs, or business records held elsewhere.
2. **From whom?** Identify the observers the design is meant to exclude, including participating organizations and application-service operators.
3. **Where does each value travel?** Trace it from user interface through any private systems and contract interactions to stored state and outputs.
4. **What does the proposed mechanism actually prove or hide?** For proof-based systems, distinguish private witness data from public commitments and verifier results. For permissioned systems, distinguish access control from confidentiality.
5. **Who can access plaintext, keys, or recovery paths?** Request system-specific documentation identifying these parties and controls; do not infer their absence from an architecture label.
6. **What evidence supports the claim?** Seek technical documentation and independent security review that address the implementation, assumptions, and failure modes, not just the intended design.

A design is meaningfully assessable when its privacy claims name the protected information, the observers in scope, and the limits of verification or access controls. Without those details, “private smart contract” is a label rather than a usable statement of what builders can keep confidential.

## Sources and references

- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Baseline Core Version 1.0 - Part 1](https://docs.oasis-open.org/ethereum/baseline/baseline-core/v1.0/baseline-core-v1.0-part1.html) — OASIS Open; retrieved 2026-10-19.
- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
