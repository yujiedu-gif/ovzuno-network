---
title: "IPFS Solidity: How Smart Contracts Refer to Off-Chain Content"
description: "Learn how IPFS Solidity designs connect contract state to off-chain content, what a content identifier represents, and what retrieval and persistence depend on."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["IPFS content addressing", "Solidity smart contract storage", "IPFS CID"]
author: "editorial_team"
primary_keyword: "ipfs solidity"
owned_question: "How can a Solidity smart contract refer to content stored on IPFS, and what does that design leave on-chain versus off-chain?"
risk_level: "medium"
---

A Solidity contract can store a reference to IPFS-addressed content—such as a content identifier (CID) or a URI containing one—without storing the referenced content in its own state. The contract can record or update that reference under its programmed rules, while an application or other retrieval path must obtain and interpret the content separately. A reference alone does not establish that the content will remain available.

## What IPFS and Solidity each do

Solidity is a programming language for defining smart-contract code and data. On Ethereum, a smart contract has persistent state and executable functions at an on-chain address, and it can emit events for applications to process. In an IPFS-and-Solidity design, that state can include a value used as a reference; it need not include the content that the reference identifies. [source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)

IPFS serves a different role in this arrangement: it is the content-addressing side, while Solidity provides contract logic and on-chain state. “Off-chain” here means that the referenced material is not part of the contract’s state. The contract may retain a pointer-like value, but that does not make the material part of the blockchain record or make the contract itself a content-serving application.

This distinction is useful when deciding which component is responsible for each task. Contract code can apply rules to the reference value it receives. An application can read that value, interpret it, and request the corresponding content through an IPFS-compatible retrieval path. The contract and the retrieval application therefore have related but separate roles.

## How a Solidity contract can reference IPFS content

A conceptual data flow can be described in four steps:

1. An application obtains or prepares content and receives an IPFS reference for it.
2. The application submits a transaction that passes the reference to a Solidity contract.
3. The contract stores or updates the reference according to its programmed rules.
4. A client later reads the reference and uses a separate retrieval path to request the content.

The reference could be represented in contract state as a string containing a CID or as a URI that includes a CID. The precise representation is a design decision: the available evidence does not establish one required Solidity type or format. Whatever the choice, the application and contract must agree on how the stored value is interpreted. A value that one client treats as a URI, for example, must not be assumed to have the same meaning to every other client unless the application design defines that convention.

Storing a reference also does not cause Solidity to fetch the referenced material during contract execution. Ethereum smart contracts cannot directly obtain off-chain facts that are not already in deterministic blockchain state without an oracle or transaction mechanism. An application retrieving content is a distinct operation; a contract’s stored value does not, by itself, supply the content to contract logic. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

This matters if a dApp’s user interface displays content alongside contract data. The interface may be showing a value read from the contract and material retrieved elsewhere. Those two results should not be conflated: the contract can establish what reference it recorded, while the application’s retrieval path determines whether it obtains and presents corresponding content.

## What belongs on-chain and what stays off-chain

In this pattern, the on-chain portion is the contract state: the reference and any other values the contract’s rules require. The off-chain portion is the material addressed by that reference and the retrieval work performed by the application or supporting infrastructure. The reference is a link between the two parts of the design, not a copy of the content inside contract state.

That boundary guides the design decision. If the contract only needs to record which reference is current, it can treat the reference as data. If contract logic needs the actual content to make a decision during execution, a reference alone does not provide that content. The design would need a supported way to supply the relevant data to execution; it should not assume that the contract can dereference an IPFS reference on demand.

The contract and application should define how references are created, stored, updated, and interpreted. For example, the contract may enforce its own rules about who can change a recorded value, while the application specifies how to parse that value and what content format it expects. These are design responsibilities, not automatic properties of putting a CID-like string in contract state.

The evidence available for this article does not establish current, context-specific storage costs, execution fees, or a quantitative rule for choosing on-chain versus off-chain data. Cost comparisons therefore need evidence for the particular network and design. The architectural distinction can still be made without claiming that either placement is universally cheaper or preferable.

## Content integrity, availability, and mutability

A content reference and successful access to content are separate concerns. The contract can retain a reference even if a particular application cannot retrieve the material through its chosen path. The design must therefore account for the retrieval path and for how the application behaves when the content cannot be obtained. The available evidence does not establish a general guarantee of IPFS persistence, gateway availability, or recovery for a particular reference.

A storage-verification example from another protocol illustrates why such claims must be scoped carefully. Filecoin Proof-of-Spacetime is designed to let a storage provider prove to the network that it continues to store a unique copy of committed data. That description concerns Filecoin’s protocol-specific mechanism; it does not mean that every IPFS reference automatically has that arrangement, or that a given application can retrieve the content. [source](<https://docs.filecoin.io/reference/general/glossary>)

The contract’s recorded value can also be distinguished from the content’s continued availability. If a contract changes its reference, it records a different value under its rules. The details—who may update it, how clients learn of the change, and whether older references remain meaningful—depend on the contract and application design. The evidence here does not establish CID construction details or the behavior of mutable naming systems, so no universal rule about those mechanisms should be inferred from the term “CID” alone.

## Design checks before using IPFS with Solidity

Before choosing this pattern, make the boundary explicit and check the following:

- **Define the stored format.** Specify whether the contract records a CID, a URI containing a CID, or another clearly defined reference, and document how an application should interpret it.
- **Set update rules.** Determine which contract rules govern who can set or change the reference. Make sure client behavior is consistent with those rules.
- **Plan retrieval behavior.** Identify how the application obtains content and what it does if retrieval fails, the returned material is unexpected, or the reference is outdated.
- **Assess continued availability.** Decide what arrangements the wider system relies on to keep content retrievable. Do not treat the contract’s record of a reference as proof of a persistence arrangement.
- **Review what is published.** Consider the content and the design before making it available through an external retrieval system. This article does not establish a suitable method for storing confidential or personal information on IPFS.
- **Make the distinction visible.** Let users inspect the reference recorded by the contract and distinguish it from material an application successfully retrieves and displays.

The practical question is whether the dApp can rely on off-chain content while treating retrieval and interpretation as responsibilities outside the contract. Solidity can store and apply rules to a reference. The addressed content, its availability, and the application experience for resolving it remain separate parts of the system. Choosing this architecture means defining those dependencies rather than assuming the reference alone supplies or preserves the content.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
- [Filecoin Glossary](https://docs.filecoin.io/reference/general/glossary) — Filecoin Docs; retrieved 2026-10-19.
