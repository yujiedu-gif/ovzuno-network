---
title: "erc 20 erc 721: How Ethereum Token Standards Differ"
description: "Compare erc 20 erc 721 by token identity, interface expectations, and application fit, with practical criteria for choosing a standard for a smart contract."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "comparison"
topics: ["smart_contract_dapps"]
tags: ["ERC-20", "ERC-721", "fungible tokens", "non-fungible tokens", "Ethereum token standards"]
author: "editorial_team"
primary_keyword: "erc 20 erc 721"
owned_question: "How do ERC-20 and ERC-721 differ in token representation, interface, and typical smart-contract use, and what should a builder evaluate when choosing between them?"
risk_level: "medium"
---

For a builder choosing between ERC-20 and ERC-721, the central distinction is whether the application represents interchangeable units through balances or individually identified tokens through ownership records. ERC-20 specifies a common interface for fungible-token balances, transfers, and approvals; ERC-721 standardizes ownership lookup, approvals, and transfers for distinct token IDs. Neither interface, by itself, establishes the real-world meaning or legal effect of an asset. [source](<https://eips.ethereum.org/EIPS/eip-20>) [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

## What ERC-20 and ERC-721 Represent

Fungibility describes whether units are treated as interchangeable within an application’s model. With a fungible-token interface, the application can work with a quantity associated with an address. Non-fungibility describes a model in which tokens have distinct identities, so an application can refer to a particular token rather than only a quantity.

ERC-20 defines a common interface for balances, direct transfers, approvals, and events. ERC-721 standardizes ownership lookup, approvals, operator authorization, transfer behavior, and transfer events for distinct tokens. These standards describe contract interfaces; they do not determine what a token represents outside the contract or whether that representation has legal effect. [source](<https://eips.ethereum.org/EIPS/eip-20>) [source](<https://eips.ethereum.org/EIPS/eip-721>)

A token record and the asset it refers to are not automatically the same thing. A digital token can combine a ledger record about an asset and its owner with programmable rules governing use or transfer, but the record alone does not determine legal title, enforceability, or the quality of the represented asset. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

## How Token Identity and Balances Differ

ERC-20 represents token quantities through balances associated with addresses. Its interface includes direct transfers and approvals that let another address spend up to an authorized amount. The interface does not specify issuance policy, backing, market value, compliance, or implementation safety. Builders should treat ERC-20 as an interface for token operations, not a complete account of an asset’s properties. [source](<https://eips.ethereum.org/EIPS/eip-20>)

ERC-721 represents ownership through distinct token identifiers. Its interface supports looking up a token’s owner and handling approvals and transfers for identified tokens. A token ID is useful for distinguishing contract-level records; it does not by itself prove that a linked item is authentic, establish rights to that item, or show that controlling the token controls an off-chain asset. ERC-721 supports standardized records for distinguishable token IDs that applications can associate with digital or physical subjects, but the meaning and legal effect of those subjects depend on additional systems and terms. [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://eips.ethereum.org/EIPS/eip-721>)

The distinction concerns representation. It does not establish that every unit of a particular token has the same value or that every ERC-721 token refers to a unique physical object. Those questions depend on the specific token and any associated systems.

## ERC-20 and ERC-721 Interface Expectations

For ERC-20, applications commonly need to account for balances, direct transfers, and approvals for delegated spending. An approval is an authorization for another address to spend up to a specified amount under the interface. Builders should identify where their application requests or relies on that authorization and make the intended operation clear to users. ERC-20’s interface does not settle how an application should design its broader workflow. [source](<https://eips.ethereum.org/EIPS/eip-20>)

For ERC-721, applications commonly need ownership queries, token transfers, approvals, and operator authorization. These operations concern identified tokens, so the application must keep track of which token is involved and what authorization applies. Standardized transfer behavior and events provide interface expectations, but they do not establish that a holder has rights outside the contract or that a particular implementation is bug-free. [source](<https://eips.ethereum.org/EIPS/eip-721>)

A standard’s interface is not a guarantee that every contract implements every feature an application may want. Before integrating a token, check the authoritative specification and verify which required interfaces and behaviors the selected implementation actually supports. Keep the distinction clear between what the standard specifies and what an individual contract or application adds.

## Choosing a Standard for an Application

Begin with the asset behavior and user actions the application needs:

- If the application needs interchangeable units and aggregate balances, ERC-20’s balance-and-transfer interface may fit. Evaluate whether its approval behavior also matches the intended workflow. [source](<https://eips.ethereum.org/EIPS/eip-20>)
- If the application needs distinct on-chain identities and ownership tracking for individual tokens, ERC-721 may fit. Evaluate whether its ownership, authorization, and transfer behavior covers the required operations. [source](<https://eips.ethereum.org/EIPS/eip-721>)
- If the application’s asset model is unclear, first specify whether users act on a quantity or on an individually identified item. Then compare those requirements with the relevant interface rather than treating the standard as a complete application design.

Next, map the application’s transfer flows. Determine whether users transfer directly, authorize another address to act, or need the application to read balances or token ownership. Also identify which events or contract interactions the application must process. These checks help reveal integration needs without assuming that the standards themselves supply marketplace, wallet, or other application-specific functionality.

If the application relies on metadata or a connection to an off-chain subject, examine that dependency separately from token ownership. An ERC-721 token can be associated with a digital or physical subject, but the token record does not alone establish the subject’s authenticity or legal effect. ERC-4519 defines an interface for linking NFTs to physical assets or IoT devices through asset addresses and owner or user authentication states. That interface does not remove the need to assess the device, key protection, issuer, firmware, and the process that connects off-chain and on-chain records. [source](<https://eips.ethereum.org/EIPS/eip-721>) [source](<https://eips.ethereum.org/EIPS/eip-4519>)

The choice is conditional: match the standard to the representation and operations the application needs, then verify that the selected implementation and surrounding systems provide any additional required behavior.

## Implementation and Operational Caveats

Interface conformance and contract security are different questions. A standard describes expected interface behavior; it does not establish that a particular implementation is secure. Review the contract’s actual behavior and test the workflows on which the application depends. Do not treat a standard label as evidence that an implementation’s approvals, transfers, or other logic meet the application’s requirements.

For ERC-20, examine how the application uses balances, transfers, and delegated-spending approvals. For ERC-721, examine how it identifies tokens, checks ownership, and handles token or operator approvals and transfers. In either case, verify expected failure handling and confirm which interface features the chosen implementation supports. These are implementation checks, not properties guaranteed by the standard’s name.

Keep external claims within their evidence. A token identifier does not, on its own, establish rights to an associated asset, and an interface does not settle legal, tax, regulatory, or compliance questions. Those topics are outside this technical comparison and require evidence specific to the relevant circumstances. For the standard-selection decision, focus on whether the application needs quantities or individually identified tokens, then verify the interface and implementation against its concrete workflows. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

## Sources and references

- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
- [ERC-4519: Non-Fungible Tokens Tied to Physical Assets](https://eips.ethereum.org/EIPS/eip-4519) — Ethereum Improvement Proposals; retrieved 2026-10-18.
