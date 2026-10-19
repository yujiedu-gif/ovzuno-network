---
title: "What Is Cryptocurrency? How Digital Assets Move on a Network"
description: "Learn what cryptocurrency is, how wallets and blockchain networks process transfers, and how crypto assets differ from bank money and digital payments."
date: "2026-10-18"
draft: false
content_type: "definition"
topics: ["crypto-assets-and-protocols"]
tags: ["how cryptocurrency works", "cryptocurrency transactions", "crypto wallets", "digital assets"]
author: "editorial_team"
primary_keyword: "cryptocurrency"
owned_question: "What is cryptocurrency, and how does it differ from traditional money?"
risk_level: "low"
---

Cryptocurrency is a digital asset or unit whose ownership and transfer are managed by a computer network under a defined protocol. Instead of asking a bank to update a private account database, a user submits a signed transaction to the network. The network checks that request and, if it satisfies the rules, records the resulting change in a shared ledger.

NIST describes cryptocurrency as a digital asset, credit, or unit that can be cryptographically transferred from one blockchain-network user to another. That definition is deliberately technical. It does not say that every cryptocurrency functions well as money, has a stable value, or is suitable for investment. It identifies the common mechanism: digitally represented units, cryptographic authorization, and a network-maintained record.

## A practical definition of cryptocurrency

A cryptocurrency system usually combines three layers. The **protocol** is the set of software rules that defines valid transactions and ledger updates. The **ledger** records ownership and transfer history. The **network** consists of participants running software that receives, verifies, stores, and sometimes orders transactions.

The word *currency* can be misleading because crypto assets serve different purposes. Some are designed primarily to transfer value. Others pay network fees, coordinate access to an application, represent governance rights, or track another asset. Whether a particular asset is treated as money, property, a security, a commodity, or another legal category depends on its design and the applicable jurisdiction.

Cryptography supports the authorization process. A user controls a private key and derives a corresponding public address. The private key can create a digital signature that the network verifies without learning the key itself. The signature shows that the transaction was authorized by a key accepted by the protocol. It does not prove the signer's real-world identity or guarantee that the destination address was correct.

## How a cryptocurrency transfer works

The details vary by network, but a typical transfer follows the same broad sequence.

1. **A wallet constructs a transaction.** The instruction identifies the asset, amount, destination, fee parameters, and other network-specific data.
2. **The user authorizes it.** The wallet signs the transaction using the relevant private key. Custodial services may apply their own approval process before signing.
3. **The network receives the request.** Nodes check its format, signature, available balance or spendable outputs, and other protocol rules.
4. **The transaction is ordered and accepted.** Validators, miners, or another authorized mechanism place valid transactions into the network's agreed history.
5. **Applications wait for confirmation.** A wallet, exchange, or merchant monitors the ledger and decides when the transfer has enough finality for its risk policy.

This shared history addresses the double-spending problem. A digital file can normally be copied, so a payment system needs a reliable way to prevent one unit from being spent twice. Cryptocurrency protocols do this by validating proposed transfers against an agreed ledger state and rejecting conflicting attempts according to network rules.

A submitted transaction is not always a completed business payment. It may remain pending, fail because of fees or invalid data, or require additional confirmations. The recipient may also need accounting, identity, fraud, or compliance checks outside the blockchain.

## Coins, tokens, and stablecoins

A **native coin** belongs to the base protocol of a network. It is commonly used to pay transaction fees and may also reward participants who help operate or secure the network. Bitcoin on the Bitcoin network and ether on Ethereum are familiar examples.

A **token** is generally created through application logic on an existing programmable network. Its rules may be implemented by a smart contract rather than the base protocol. Tokens can represent many things, including application access, governance functions, claims, or digital assets.

A **stablecoin** is a crypto asset designed to maintain a value relative to a reference asset such as a national currency. The design may rely on reserves, overcollateralization, algorithms, or a combination of mechanisms. Calling an asset a stablecoin describes its objective, not a guarantee that redemption, liquidity, or market value will always remain stable.

These categories overlap in everyday language, so an operator should examine the exact issuer, protocol, contract, reserve arrangement, and redemption process rather than relying on a label alone.

## How cryptocurrency differs from conventional money

Both cryptocurrency and conventional electronic money can appear as numbers on a screen, but their operating models can be different. A bank deposit is normally a liability of a regulated institution recorded in that institution's ledger. Physical cash is issued by a monetary authority. A cryptocurrency may instead be issued according to protocol rules and transferred on a distributed ledger.

The ledger operator also differs. Banks and payment processors maintain central systems and can apply account controls, chargebacks, reversals, and legal orders through established procedures. A public cryptocurrency network validates transactions under protocol rules shared among network participants. Reversing an accepted transfer may be impossible at the protocol layer unless the recipient cooperates or an application provides a separate remedy.

Value behavior is another distinction. National currencies are supported by monetary and legal institutions. Many cryptocurrencies have market prices that can change sharply. Stablecoins attempt to reduce that volatility, but they introduce issuer, reserve, redemption, smart-contract, and market-liquidity dependencies.

These differences do not make every system purely centralized or decentralized. Most real products combine layers: a public network may sit beneath a custodial exchange, while a regulated payment service may use blockchain settlement behind a conventional user interface.

## What a wallet actually controls

A cryptocurrency wallet usually does not store coins as files. The ledger records the relevant balances or spendable outputs. The wallet stores or controls the credentials needed to authorize a change to that record.

In a **self-custodial wallet**, the user controls the private keys or recovery material. This reduces dependence on a custodian but makes key protection and recovery the user's responsibility. In a **custodial wallet**, a service controls the signing keys and maintains an account relationship with the user. This can support account recovery and operational controls, while introducing reliance on the custodian's security, solvency, and policies.

Multisignature and multiparty-computation systems can distribute authorization across several keys or participants. They change the control model, but they do not eliminate the need for secure devices, access policies, backups, monitoring, and incident response.

## Practical limits and risks

Protocol validation answers a narrow technical question: does the transaction satisfy the network's rules? It does not confirm that the sender understood the transaction, that an off-chain claim was true, or that a smart contract is safe.

Key theft can let an attacker create a technically valid transfer. Sending assets to the wrong address may be irreversible. Software defects can affect wallets, exchanges, bridges, or smart contracts even when the base ledger operates as designed. Network congestion and fee changes can also alter the speed and cost of settlement.

For a business, the relevant question is therefore not simply whether it should use cryptocurrency. It is which asset and network match the required payment or application flow, who controls signing, how finality is measured, how errors are handled, and which legal and operational responsibilities remain outside the protocol.

## Sources and references

- [Cryptocurrency - Glossary](https://csrc.nist.gov/glossary/term/Cryptocurrency) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
