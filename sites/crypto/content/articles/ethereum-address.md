---
title: "Ethereum address: what it identifies and how it works"
description: "Learn what an ethereum address identifies, how it relates to accounts and wallets, and how addresses are used for transfers and Ethereum application interactions."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "ethereum address"
owned_question: "What is an Ethereum address, what does it identify, and how is it used to send and receive assets or interact with applications?"
risk_level: "medium"
---

An Ethereum address is a public identifier for an account or smart contract on Ethereum. It is used to direct transactions and application interactions, but it is not itself a wallet, a person’s identity, or proof of who controls the associated account.

## What an Ethereum address identifies

Ethereum has accounts that hold state, including balances and, for smart contracts, code. An address identifies a location in that system: it can belong to an externally owned account or identify a smart contract. A contract is a program with code and data at a network address that users can invoke by submitting transactions. [[source](<https://ethereum.org/developers/docs/smart-contracts/>)] [[source](<https://ethereum.org/developers/docs/smart-contracts>)]

The two account types have different roles. An externally owned account is controlled by the private key corresponding to its cryptographic address. A smart-contract address identifies code and data that can respond when invoked. The address is the identifier; the associated account state and behavior are maintained under Ethereum’s rules. [[source](<https://ethereum.org/developers/docs/accounts/>)] [[source](<https://ethereum.org/developers/docs/smart-contracts/>)]

This distinction matters because an address is not a complete record of ownership in the everyday sense. It identifies an on-chain account or contract, but does not by itself establish the real-world identity of a person or organization, or explain every right someone may claim in an asset.

## Ethereum address, account, wallet, and private key

These terms describe related but separate things:

- **Address:** A public identifier used to refer to an account or contract on the network.
- **Account:** The on-chain state associated with an address. Depending on the account type, that state may include a balance or contract code and data. [[source](<https://ethereum.org/developers/docs/smart-contracts/>)]
- **Wallet:** Software, hardware, or a service used to generate, manage, store, or use cryptographic keys and blockchain addresses. A wallet is an interface or key-management tool, not the account itself. [[source](<https://csrc.nist.gov/glossary/term/wallet>)]
- **Private key:** The credential corresponding to an externally owned account’s address. Control of that key is what controls that account; knowing or seeing the address alone does not grant that control. [[source](<https://ethereum.org/developers/docs/accounts/>)]

A wallet may help a user view account information and prepare interactions, but the address remains the public reference used by the network. An application can also include a frontend, contracts, and other off-chain services, so an application’s interface and its on-chain contract are distinct parts of the broader system. [[source](<https://ethereum.org/developers/docs/ethereum-stack/>)]

## How Ethereum addresses are used

For a transfer, an address identifies the account involved as a sender or recipient. A transaction can also call a smart contract by referring to its address; the contract’s program then processes the interaction according to its code. Ethereum smart contracts are programs at network addresses that users invoke through transactions. [[source](<https://ethereum.org/developers/docs/smart-contracts>)]

Applications use addresses to connect user actions with accounts and contracts. For example, an application may present a contract interaction while a wallet handles the signing step. The application, wallet, and protocol have different roles: the application provides an interface, the wallet manages key use, and Ethereum processes transactions under network rules. [[source](<https://ethereum.org/developers/docs/ethereum-stack/>)]

An address can be visible in public on-chain activity without revealing who is behind it. A valid transaction signature can support attribution to control of the relevant key, but the address or signature alone does not identify the human, organization, device, or service controlling it. [[source](<https://ethereum.org/developers/docs/accounts/>)]

## What to consider before using an address

An address should be understood in its network and transaction context. Ethereum’s address refers to an account in the Ethereum account model; account balances and histories do not carry across independent Ethereum networks. A matching-looking address on another network should therefore not be assumed to refer to the same account state or assets. [[source](<https://ethereum.org/developers/docs/smart-contracts/>)]

Also consider what the transaction is meant to do. A transfer to an account and a call to a contract are different kinds of interaction, even though both may involve an address. The address alone does not explain a contract’s functions or establish that an application’s description of the interaction is complete. [[source](<https://ethereum.org/developers/docs/smart-contracts>)]

This is a conceptual distinction, not a procedure for checking a particular destination. The address alone cannot confirm that it belongs to an intended recipient, that a contract is legitimate, or that an attempted interaction will have the result a user expects.

## What an Ethereum address does not tell you

An address does not, by itself, establish a verified real-world identity or prove who controls it. For an externally owned account, control depends on the corresponding private key; for a contract, the address identifies code and data rather than a person. [[source](<https://ethereum.org/developers/docs/accounts/>)] [[source](<https://ethereum.org/developers/docs/smart-contracts/>)]

Nor does an address prove that an asset, application, or contract is safe or legitimate. It is an identifier that enables the network and applications to refer to accounts and contracts. To understand what a particular contract does or what rights an asset represents requires information beyond the address itself.

## Sources and references

- [Introduction to the Ethereum stack](https://ethereum.org/developers/docs/ethereum-stack/) — ethereum.org; retrieved 2026-10-19.
- [Wallet - Glossary](https://csrc.nist.gov/glossary/term/wallet) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts) — ethereum.org; retrieved 2026-10-21.
- [Ethereum accounts](https://ethereum.org/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
