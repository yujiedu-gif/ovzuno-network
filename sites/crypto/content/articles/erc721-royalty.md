---
title: "ERC721 royalty: how NFT royalty information and payment enforcement work"
description: "Learn how ERC721 royalty information can be exposed, what ERC-2981 communicates, and why marketplace and transaction behavior determines whether payment occurs."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["ERC-2981", "NFT royalty information", "royalty recipient", "marketplace royalty enforcement"]
author: "editorial_team"
primary_keyword: "erc721 royalty"
owned_question: "How can an ERC-721 contract expose royalty information, and what determines whether a secondary sale actually pays it?"
risk_level: "medium"
---

An ERC-721 contract can expose royalty information through an interface such as ERC-2981, which reports a royalty recipient and amount for a stated sale price. That report is not a payment: whether a secondary sale pays a royalty depends on how the marketplace and transaction flow use the information and arrange payment.

## What an ERC721 royalty describes

ERC-721 standardizes ownership lookup, approvals, authorization, transfer behavior, and transfer events for distinct tokens. Those functions describe token control and movement; they do not, by themselves, make every transfer a sale or ensure that a royalty is paid when a transfer occurs. [source](<https://eips.ethereum.org/EIPS/eip-721>)

A token transfer, a sale, and a royalty payment are related but distinct concepts. A transfer changes ownership under the contract’s rules. A sale flow may involve a buyer providing consideration for the token. A royalty payment is a movement of value to a recipient. The ERC-721 transfer interface alone does not establish that these actions are linked or that a payment must accompany a transfer. [source](<https://eips.ethereum.org/EIPS/eip-721>)

The token’s identity is also separate from its royalty behavior. For an ERC-721 token on an Ethereum chain, the combination of the contract address and token ID identifies the token. That identification does not, by itself, say what royalty information the contract reports or whether a marketplace will use it. [source](<https://eips.ethereum.org/EIPS/eip-721>)

Royalty information can be exposed through an interface separate from ERC-721’s ownership and transfer functions. ERC-2981 standardizes retrieval of a royalty recipient and amount for a stated sale price. It communicates information to a caller; it does not itself establish that the caller will send funds. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## How ERC-2981 reports NFT royalty information

In a sale flow that uses ERC-2981, an application can ask the contract for a recipient and royalty amount associated with a stated sale price. The response gives the caller information it may incorporate into the flow. The interface standardizes retrieval of that information, while payment remains voluntary and requires implementation by a marketplace or participant. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

The sale price is an input to the information request. Therefore, when evaluating a particular integration, identify which price the caller supplies and what the contract reports in response. The interface’s report is tied to that stated price; it does not establish that the caller has captured every part of a commercial arrangement or that payment will follow. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

Do not confuse royalty information with token metadata. The optional ERC-721 metadata interface can expose a token URI referring to metadata for a specific token ID. The existence of such a URI does not, by itself, show that the contract provides an ERC-2981 response or that a sale flow will make a royalty payment. [source](<https://eips.ethereum.org/EIPS/eip-721>)

For developers, this distinction affects what an integration needs to read and what it needs to do. A royalty-information interface can answer a request for recipient and amount. The marketplace or other application must separately decide how to incorporate that response into the transaction. The standard specifies retrieval, not an automatic collection step. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## From royalty recipient to secondary-sale payment

A payment path requires more than a contract response. In general, the sale flow must query the relevant royalty information, interpret the returned recipient and amount, and arrange for value to reach that recipient. ERC-2981 standardizes the retrieval step; payment depends on marketplace or participant implementation. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

This separates three questions that are easy to collapse into one: Does the contract expose royalty information? Does the marketplace or other caller request and interpret it? Does the transaction actually include a payment? A positive answer to the first question does not answer the other two. The standard alone does not compel a marketplace to pay. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

An ERC-721 transfer can therefore occur without an associated royalty payment. Its transfer interface describes token movement, while ERC-2981 does not make that movement conditional on payment. Whether royalty information becomes part of a particular sale transaction depends on that transaction’s design and the parties or application implementing it. [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://eips.ethereum.org/EIPS/eip-2981>)

Transfers outside a sale flow illustrate the same boundary. ERC-2981 reports information for a stated sale price. A transfer that is not handled through a sale flow may have no sale price supplied to that query, and the interface does not establish that every transfer should trigger a royalty payment. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

In practical terms, “royalty support” can refer to different stages: a contract exposes information, an application reads it, or a transaction includes a payment. Those stages should not be treated as interchangeable. Evidence that a contract supports royalty information is not evidence that a given secondary sale paid the recipient. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## Implementation and integration checks

Evaluate the contract and sale flow separately. First, establish whether the relevant contract provides ERC-2981 royalty information. Then determine what recipient and amount it reports for the stated sale price used by the caller. The standard supports retrieval of that information, but it does not establish how every deployed contract responds or how every application uses the response. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

Next, inspect the marketplace or application’s transaction path. Determine whether it queries the royalty interface, how it handles the response, and whether the transaction arranges payment to the reported recipient. The relevant question is not merely whether a marketplace describes itself as supporting royalties; it is whether the specific sale flow incorporates the response into the transaction. That conclusion requires evidence about that implementation, not just the interface standard. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

Keep metadata checks distinct from royalty checks. A token URI can refer to token metadata, but the URI does not establish that a marketplace queries ERC-2981 or pays a royalty. Verify the relevant interface and payment path independently rather than treating metadata presence as proof of transaction behavior. [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://eips.ethereum.org/EIPS/eip-2981>)

Finally, keep conclusions limited to the implementation examined. ERC-721 standardizes ownership and transfer interfaces for distinct tokens, and ERC-2981 standardizes retrieval of royalty information. Neither standard, by itself, establishes the behavior of every contract, marketplace, or sale transaction. [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## Limits, compliance, and jurisdiction-specific claims

Royalty information should not be presented as guaranteed revenue or, without jurisdiction-specific legal evidence, as a legal entitlement. The technical point is narrower: ERC-2981 can report a recipient and amount for a stated sale price, while payment requires marketplace or participant implementation. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

The token record also does not resolve all external rights or obligations. NFT-associated rights can depend on applicable law, contractual terms, product transparency, and systems beyond the token record. That is separate from the technical question of whether an interface returns royalty information. [source](<https://www.copyright.gov/policy/nft-study/Joint-USPTO-USCO-Report-on-NFTs-and-Intellectual-Property.pdf>)

This explainer does not determine legal, tax, or regulatory treatment for any person or location. It makes no general claim about marketplace availability, fees, security, recovery, or compliance. The answer to the technical question is that an ERC-721 contract can expose royalty information through a separate interface such as ERC-2981, but an actual secondary-sale payment depends on how the relevant marketplace and transaction implement that information. [source](<https://eips.ethereum.org/EIPS/eip-2981>)

## Sources and references

- [ERC-2981: NFT Royalty Standard](https://eips.ethereum.org/EIPS/eip-2981) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Non-Fungible Tokens and Intellectual Property: A Report to Congress](https://www.copyright.gov/policy/nft-study/Joint-USPTO-USCO-Report-on-NFTs-and-Intellectual-Property.pdf) — United States Patent and Trademark Office and U.S. Copyright Office; retrieved 2026-10-18.
