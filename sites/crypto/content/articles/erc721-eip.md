---
title: "ERC721 EIP: How the Specification Defines the NFT Interface"
description: "Learn how ERC721 EIP connects the Ethereum proposal process to the NFT interface standard, including required behaviors, optional features, and implementation limits"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "erc721 eip"
owned_question: "How does ERC-721 relate to the Ethereum Improvement Proposal that specifies the NFT token standard, and what does that proposal require?"
risk_level: "medium"
---

ERC-721 is the Ethereum token interface specified by EIP-721. The EIP is the proposal document; a deployed contract is a particular implementation that may claim to follow that specification. To assess what a contract does, distinguish the standard’s defined interface from that contract’s own behavior and external application features.

## What ERC721 and EIP mean

An Ethereum Improvement Proposal (EIP) is a document used to propose and specify changes or standards for the Ethereum ecosystem. EIP-721 is the proposal that specifies the ERC-721 non-fungible token interface. “ERC-721” names the standard; “EIP-721” identifies the proposal document that sets out its specification.

That distinction matters when reading a contract’s documentation. The specification describes interface behavior for implementations to support; it is not itself a deployed program. A deployed contract has its own address and state, and its actual behavior depends on its code. The token identifier is unique within its contract, so identifying a particular ERC-721 token requires both the contract address and token ID—not just a name, symbol, or image link. [source](<https://eips.ethereum.org/EIPS/eip-721>)

## What the ERC721 EIP specifies

At a high level, ERC-721 standardizes records and operations for distinct tokens. Its interface covers looking up an owner, authorizing transfers, transferring tokens, and emitting transfer-related events. These functions give applications a common way to interact with a contract that implements the interface; they do not prescribe every feature of a marketplace or wallet.

The standard’s token identity is local to the contract: the contract address paired with its token ID identifies the token on an Ethereum chain. That standardized identity does not, by itself, establish what a token represents outside the contract or guarantee that associated media or rights are available.

It is useful to keep three layers separate. The contract provides the token interface and its own state. An application may read that interface and present information to a user. Other systems or terms may define the meaning and availability of referenced content. The ERC-721 interface does not collapse those layers into one guarantee.

## Required and optional interface features

The core ERC-721 interface specifies owner lookup, approvals, operator authorization, transfer behavior, and transfer events. When checking a contract’s declared support, a reader should verify that the relevant interface claims match the observable behavior being described, rather than assuming that a familiar label proves every feature is present.

ERC-721 also defines optional interfaces. One is a metadata extension that can expose a token URI referring to metadata for a specific token ID. Because this interface is optional, a token contract need not provide it to implement the core interface. And the URI reference does not itself guarantee that metadata or media will remain available, be accurate, or be permanent. [source](<https://eips.ethereum.org/EIPS/eip-721>)

Another optional extension is enumerability: it provides ways to enumerate tokens associated with a contract or owner. Treat it as an extension, not as a requirement of the core ERC-721 interface. An application that depends on metadata or enumeration should check whether the particular contract supports those features rather than infer support from the ERC-721 name alone.

A related but separate specification, ERC-2981, standardizes how a contract can report a royalty recipient and amount for a stated sale price. That signal is not part of ERC-721’s core transfer and ownership interface, and the standard does not compel a marketplace or buyer to make a royalty payment. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## What the specification leaves to implementers

ERC-721 specifies an interface, not a complete application design. It does not prescribe every contract’s policies, the way a marketplace displays or filters tokens, or how a user-facing application handles metadata. Implementations can differ in details beyond the standardized interface, so an application should not assume that all contracts provide identical extensions or presentation behavior.

The interface also does not establish that a contract is secure or that external information is trustworthy. For example, a metadata URI is a reference, not proof of the content’s correctness or continued availability. Likewise, a royalty-information response standardizes a reported recipient and amount; it does not guarantee payment. These limits follow from the narrow scope of the specified interfaces, not from a promise that every implementation behaves alike.

## How to verify an ERC-721 implementation

Start with the canonical EIP-721 text and identify which interface and optional extensions the contract claims to implement. Then compare those claims with the contract’s documented interface and the behavior relevant to the application. For token identity, use the contract address together with the token ID. If an application needs a token URI or enumeration, verify support for that optional interface separately.

Keep other assurances separate from interface conformance. A claim that a contract is audited, secure, recoverable, or operationally reliable requires evidence about that specific contract and its surrounding systems; the ERC-721 label alone does not supply it. The practical question is therefore not just “Is this an ERC-721?” but “Which specified interfaces does this contract expose, and what additional behavior does this application rely on?”

## Sources and references

- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-2981: NFT Royalty Standard](https://eips.ethereum.org/EIPS/eip-2981) — Ethereum Improvement Proposals; retrieved 2026-10-18.
