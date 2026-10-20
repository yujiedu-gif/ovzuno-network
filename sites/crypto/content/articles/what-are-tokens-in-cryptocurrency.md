---
title: "What Are Tokens in Cryptocurrency? Tokens vs. Coins"
description: "Learn what cryptocurrency tokens are, how they use blockchain infrastructure, and how they differ from coins native to their own networks."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["coins_tokens_protocols"]
tags: ["crypto tokens vs coins", "how cryptocurrency tokens work", "blockchain tokens", "native coins and tokens"]
author: "editorial_team"
primary_keyword: "what are tokens in cryptocurrency"
owned_question: "What are tokens in cryptocurrency, and how do they differ from coins?"
risk_level: "medium"
---

# What Are Tokens in Cryptocurrency? Tokens vs. Coins

## What is a cryptocurrency token?

A cryptocurrency token is a digital asset represented and managed through a blockchain’s infrastructure. On programmable networks, a token commonly follows a smart-contract interface or another network-level convention that defines how software can read or interact with its records. The token’s details depend on the network and its implementation; there is no single token design that describes every blockchain.

A token’s technical representation is not the same thing as the meaning people attach to it. A record may contain a balance or an identifier, and software may support specified operations. Those facts alone do not establish what the token represents outside the blockchain, what rights may accompany it, or whether a claim about it is accurate.

The Committee on Payments and Market Infrastructures (CPMI), in a 2024 report focused on regulated financial and real assets, describes a digital token as something that can combine a digital ledger record about an asset and its owner with programmable rules governing use or transfer. This definition is scoped to the report’s subject matter, not a universal description of every cryptocurrency token. In that context, the technical record does not by itself determine legal title, enforceability, or the quality of the represented asset.

This distinction between a record and its associated meaning is useful throughout the topic. A token standard can specify how balances, identifiers, or transfers are handled, but it does not automatically explain the asset’s purpose or establish associated rights. To understand a particular token, it is necessary to identify its network and implementation and to read claims about its function separately from the technical record.

## How do tokens differ from coins?

The usual distinction is based on a digital asset’s relationship to a blockchain. A **coin** is native to its own network: the network’s protocol issues or tracks it as part of the blockchain’s own operation. A **token** is created or managed using an existing blockchain’s infrastructure, often through programmable features such as smart contracts or token standards.

Ether illustrates the native-coin side of this distinction. It is Ethereum’s native cryptocurrency and is part of the protocol’s market for computation. ERC-20 and ERC-721, by contrast, are Ethereum token standards: they specify interfaces for assets represented through Ethereum’s programmable environment. The comparison is about where and how the asset fits into the network, not what the asset is worth or what rights it conveys.

The distinction is useful but not perfectly consistent in everyday language. Some sources may use “coin” and “token” loosely, and a name or label is not enough to establish an asset’s technical status. The network and the relevant protocol or standard provide better context. Nor should Ethereum’s terminology be assumed to apply identically to every blockchain: other cryptocurrencies can use different issuance, utility, accounting, and consensus rules.

| Question | Native coin | Blockchain token |
|---|---|---|
| Relationship to a network | Native to its own blockchain | Created or managed using an existing blockchain’s infrastructure |
| Technical context | The network’s protocol rules | The host network plus the token’s implementation or applicable standard |
| Example in this article | Ether, Ethereum’s native cryptocurrency | Assets using ERC-20 or ERC-721 conventions on Ethereum |

This table summarizes the relationship, not a complete classification of every digital asset. A token may depend on the host network’s rules and infrastructure, while its own standard or contract can define additional token-specific behavior. The exact division of responsibilities depends on the network and implementation.

## What can cryptocurrency tokens be used for?

Token implementations can support different functions, so the word “token” does not tell a reader which one applies. At a high level, tokens may be used to represent fungible balances, identify individual items, or form part of a system that attaches programmable rules to a record. These are technical possibilities, not guarantees about an individual asset’s purpose, backing, or rights.

ERC-20 is a common Ethereum fungible-token interface. It defines elements including total supply, balances, transfers, allowances, approvals, and `Transfer` and `Approval` events. These elements provide conventions for compatible software to interact with or observe a token implementation. They describe an interface; they do not establish the token’s backing, issuance policy, market value, compliance, or implementation safety.

ERC-721 is a non-fungible-token standard. For an ERC-721 NFT on an Ethereum chain, the combination of the smart-contract address and `uint256` token ID uniquely identifies the token. The token ID is unique within its contract. A name, symbol, or media item is not a reliable global identifier. This is a technical identification rule, not a statement about the item’s legal status, value, or associated rights.

A token might also appear in a system that represents an asset and applies rules to its use or transfer. The CPMI report’s description of digital tokens combines a ledger record about an asset and its owner with programmable rules, but its scope is regulated financial and real assets. It should not be stretched into a claim that every token represents an external asset or that a technical record proves ownership of one.

The practical takeaway is to treat labels as prompts for further questions. A description such as “fungible,” “non-fungible,” or “asset-representing” signals a technical or functional category only to the extent supported by the implementation and the relevant documentation. A category does not, by itself, establish legal classification, backing, enforceability, or economic value.

## How are tokens represented on a blockchain?

A token’s records and operations are governed by the relevant network and token implementation. On Ethereum, a standard such as ERC-20 describes a common interface that specifies supply, balance, transfer, allowance, approval, and event elements. ERC-721 specifies a non-fungible-token interface and identifies an NFT on an Ethereum chain through its contract address and token ID. Other networks and designs may use different rules, so these examples should not be generalized to every token.

A helpful way to interpret a token is to separate several layers:

1. **The blockchain:** Identify which network the token is associated with. This provides the context for the network-level rules and infrastructure involved.
2. **The interface or implementation:** Determine whether a token standard is specified, and check what that standard actually defines. An interface may describe operations without explaining the token’s broader purpose.
3. **The particular record:** Find out how the token or balance is identified. For an ERC-721 NFT on an Ethereum chain, the relevant identifier is the contract address together with the token ID; a name or media item is not a reliable global identifier.
4. **The associated claim:** Read separately any claim about what the token represents, who may have rights, or what an external asset is. Technical records do not settle every such question.

These layers help explain what a blockchain token is without treating every record as equivalent. The network supplies context; a standard may describe a shared interface; and a specific implementation determines how the token’s features are expressed. The scope of a standard matters: ERC-20 specifies an interface, not backing or safety, while ERC-721’s identification rule does not establish rights to any external item.

A record and a claim about an asset must also remain distinct. In the CPMI report’s specific context of regulated financial and real assets, a digital ledger record alone does not determine legal title, enforceability, or the quality of the represented asset. That limitation illustrates why technical behavior and legal or economic interpretation should not be collapsed into one description.

## Examples of coins and tokens

The following examples are limited to Ethereum and illustrate technical relationships rather than recommending or ranking assets:

- **Ether:** Ethereum’s native cryptocurrency and part of the protocol’s market for computation. It is an example of a cryptocurrency native to its network.
- **ERC-20 token implementations:** These use a common fungible-token interface with defined supply, balance, transfer, allowance, approval, and event elements. The standard does not determine backing, issuance policy, market value, compliance, or implementation safety.
- **ERC-721 NFTs:** On an Ethereum chain, an ERC-721 NFT is uniquely identified by its smart-contract address and token ID. Names, symbols, and media are not reliable global identifiers.

These examples show why “coin versus token” is a relationship-based distinction. Ether is native to Ethereum; ERC-20 and ERC-721 describe token interfaces for assets represented through Ethereum’s programmable environment. The examples do not imply that all tokens work alike or that a standard establishes an asset’s rights, backing, value, or legal classification.

## Why the distinction matters—and where it has limits

The distinction can help identify which network’s rules and infrastructure are relevant. A native coin belongs to its own network, while a token is created or managed using an existing network’s infrastructure. That difference can guide a technical description of the asset, but it does not answer every question about the asset itself.

For a clear account, start with the network, then identify whether the asset is native to it or follows a token standard or implementation. Read the standard’s scope rather than inferring properties from its name. For example, ERC-20’s interface covers specified token operations, not backing or safety; ERC-721 provides a method of identifying an NFT on an Ethereum chain, not proof of rights to an external asset.

Terminology can vary, and some systems may complicate a simple coin-versus-token distinction. When a label is ambiguous, the most useful description names the blockchain and the relevant protocol or token implementation. Keep that technical description separate from claims about what a token represents, what rights may accompany it, or how an external asset is treated. In the CPMI report’s context of regulated financial and real assets, the ledger record alone does not settle legal title, enforceability, or asset quality.

In short, a coin is native to its own blockchain, while a token uses an existing blockchain’s infrastructure. The distinction explains the asset’s technical relationship to a network; it does not, by itself, determine the token’s function, backing, rights, value, or legal status.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
