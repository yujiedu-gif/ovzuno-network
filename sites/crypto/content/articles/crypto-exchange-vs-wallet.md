---
title: "Cryptocurrency Exchange vs Wallet: Custody and Control"
description: "Compare crypto exchanges and wallets by private-key control, trading, custody, internal balances, blockchain settlement, withdrawals, recovery, and security."
date: "2026-10-18"
draft: false
content_type: "comparison"
topics: ["exchange-market-infrastructure"]
tags: ["crypto exchange vs wallet", "difference between crypto wallet and exchange", "exchange wallet vs personal wallet", "custodial exchange vs self custody wallet", "crypto wallet or exchange"]
author: "editorial_team"
primary_keyword: "cryptocurrency exchange vs wallet"
owned_question: "How does a cryptocurrency exchange differ from a wallet in custody, execution, and control?"
risk_level: "medium"
---

A cryptocurrency exchange and a crypto wallet solve different problems. An exchange is primarily a venue for buying, selling, or converting assets. A wallet is primarily a system for managing the cryptographic keys and addresses used to authorize blockchain transactions.

The categories overlap. A centralized exchange can provide customers with a hosted wallet or deposit address. A self-custodial wallet can include a swap interface that connects to an exchange or decentralized protocol. The important comparison is not the name on the screen, but who controls the keys, where a trade is recorded, and what the user must trust.

## The short answer

| Question | Centralized crypto exchange account | Self-custodial crypto wallet |
| --- | --- | --- |
| Primary function | Trading and account services | Key management and transaction authorization |
| Who normally controls the private keys? | The exchange or its custodian | The wallet user or a user-defined signing arrangement |
| Where are trades recorded? | Often first on the exchange's internal ledger | A swap or transfer is normally submitted to a blockchain or connected protocol |
| How does the user authenticate? | Account credentials, often with multifactor authentication | Private-key signature, hardware approval, threshold signing, or similar method |
| How is access recovered? | Provider-defined account recovery | Seed phrase, backup, hardware, multisignature, social recovery, or another wallet-specific method |
| Main dependency | Exchange solvency, security, custody, controls, and withdrawal access | Correct key backup, device security, transaction review, and compatible network access |

This table describes common models, not every product. A custodial wallet can resemble an exchange account, and an exchange can support external-wallet settlement. Product documentation and transaction evidence should decide the classification.

## What a cryptocurrency exchange does

A centralized cryptocurrency exchange creates an account relationship between a customer and an operator. The customer may deposit fiat money or crypto assets, place orders, convert balances, and request withdrawals. The exchange can provide an order book, quoting, matching, custody, compliance checks, reporting, and customer support in one system.

BIS research describes centralized exchanges as venues that commonly maintain buy and sell orders in an internal order book. After assets are deposited, trades can update account balances without submitting a separate blockchain transaction for every fill. This allows rapid matching and more complex order functions, but the customer relies on the exchange's records and controls.

The account balance is therefore not necessarily a distinct onchain balance assigned to that customer. An exchange can pool assets across blockchain addresses and maintain customer entitlements in its own database. A deposit becomes visible to the account after the exchange detects and credits an incoming blockchain transaction. A withdrawal begins as an internal request and becomes an onchain transaction when the exchange authorizes and broadcasts it.

An exchange may also combine several roles. BIS notes that a crypto exchange operator can combine third-party trading, proprietary trading, lending, token issuance, and custody. Not every venue offers every service, but the possibility matters: a trading interface alone does not reveal who holds assets, how customer claims are recorded, or what happens if the operator fails.

## What a crypto wallet does

NIST defines a wallet as software or hardware used to generate, manage, store, or use asymmetric keys and blockchain addresses. The wallet prepares or displays transaction data and uses the appropriate private key or signing arrangement to authorize a request. It then sends the signed transaction to a node or service for network propagation.

A wallet does not normally contain cryptocurrency in the way a physical wallet contains cash. The blockchain records asset state and transaction history. The wallet holds or accesses the authority needed to produce a valid signature. The SEC staff's custody bulletin likewise explains that wallets generally store private keys or passcodes rather than the crypto assets themselves.

Wallet interfaces add other functions: balance display, fee estimation, token discovery, address books, network selection, contract interaction, and transaction history. Those features often rely on RPC providers, indexers, explorers, or third-party APIs. Controlling a signing key does not mean the wallet independently verifies all data it displays.

## Custodial and self-custodial wallets

The word *wallet* does not answer the custody question. A hosted or custodial wallet is controlled by a provider that manages the signing keys. The user authenticates to the provider, and the provider decides whether and when to sign a transfer. Many centralized exchange accounts use this model.

In self-custody, the user controls the private keys or a user-defined signing arrangement. According to the SEC staff bulletin, self-custody places responsibility for protecting keys and recovery material on the user. Losing every valid key and backup can permanently remove access. Sharing a seed phrase or approving a malicious transaction can give another party effective control.

Self-custody is not limited to one key on one phone. A wallet can use hardware signing, multiple signatures, threshold cryptography, separate devices, institutional policies, or recovery contacts. The security model should be described precisely rather than reduced to the phrase “not your keys.”

Third-party custody shifts key management to an exchange or another custodian. The provider may offer password reset, identity-based recovery, transaction screening, or managed security. It also becomes a dependency. The SEC staff bulletin advises checking how a custodian safeguards assets, whether it uses other service providers, how assets may be commingled or used, which fees apply, and what happens if the custodian is hacked, shuts down, or enters bankruptcy. Legal treatment varies, so a technical comparison cannot establish customer rights in every jurisdiction.

## Where a trade or transfer is recorded

An exchange trade and a blockchain transfer are different events. Suppose a customer deposits an asset to a centralized exchange, sells it, and buys another asset. The deposit is an onchain transaction. The trades may be internal ledger entries. A later withdrawal is another onchain transaction. There may be no public blockchain transaction corresponding to each internal fill.

A transfer from one self-custodial wallet address to another is submitted to the relevant network. After validation and inclusion, an explorer can show the transaction identifier, addresses, asset movements, fees, and status. The explorer interprets blockchain data; it is not itself the settlement system.

A decentralized-exchange swap initiated from a wallet is usually onchain or settles through connected smart contracts, although orders, quotes, routing, or user interfaces can still use offchain services. The wallet authorizes the contract call, while the DEX mechanism determines execution. That is different from both a standalone wallet transfer and a centralized exchange's internal order book.

Internal transfers between two customers of the same exchange may never leave the operator's database. They can be quick and inexpensive but depend entirely on the operator's ledger. When auditability or final settlement matters, identify the actual transaction hash and receiving address rather than treating an account-history entry as onchain evidence.

## Security and recovery responsibilities

The two models move risk rather than eliminating it.

With an exchange account, risks include stolen credentials, weak account recovery, insider misuse, platform compromise, frozen withdrawals, operational failure, asset commingling, legal restrictions, and insolvency. Multifactor authentication and withdrawal controls can reduce some account attacks, but they do not prove that customer assets are segregated or available.

With a self-custodial wallet, risks include private-key or seed loss, insecure backups, malware, malicious browser extensions, counterfeit hardware, address substitution, unsafe approvals, phishing, and signing a transaction whose effects were misunderstood. A blockchain usually cannot reverse a valid signature merely because the user was deceived.

Recovery also works differently. An exchange can use identity checks and account procedures to restore access, subject to its policies. A self-custodial wallet can only recover through mechanisms established in advance, such as a seed phrase, backup key, multisignature quorum, threshold recovery, or contract-based recovery. A wallet vendor cannot reconstruct a key it never possessed.

For either model, separate four questions: who can sign, who can reset access, who can block a transfer, and who can restore operation after device or provider failure.

## Costs, speed, and operational limits

Exchange trading fees and blockchain network fees pay for different activities. A centralized exchange can charge trading fees, spreads, custody or account fees, conversion fees, and withdrawal fees. Its quoted withdrawal charge may differ from the network fee actually paid for a batched blockchain transaction.

A self-custodial wallet may charge no account fee while still requiring network fees for transfers and smart-contract calls. An integrated swap can add protocol fees, price impact, routing costs, or service charges. “Free wallet” does not mean every transaction is free.

Internal exchange trades can complete before any blockchain settlement because they update the venue's ledger. Deposits and withdrawals remain subject to the exchange's confirmation policy, review process, limits, maintenance windows, and supported networks. Wallet transactions depend on network conditions, chosen fee, contract behavior, and finality rules.

Asset names are not enough. An exchange and wallet must support the same token contract and network. Sending an asset over an unsupported chain or to an incompatible address format can make recovery difficult or impossible.

## How to choose the operating model for a task

The right model depends on the task and control requirements, not on a universal ranking.

An exchange account can be useful when the primary task is matching orders, converting between fiat and crypto, accessing venue liquidity, or obtaining account-level reporting. The review should cover the legal entity, custody structure, supported withdrawal routes, fees, security controls, and failure procedures.

A self-custodial wallet can be useful when the primary task is direct signing, onchain payments, smart-contract interaction, independent withdrawal, or holding keys under an internal policy. The review should cover backup, approval controls, device security, transaction simulation, supported networks, and the node or RPC dependency.

A business may use both. For example, it can execute a conversion through an exchange and withdraw operational funds to a controlled wallet, while keeping separate approval rules for treasury and payments. The architecture should minimize unnecessary balances and permissions at each provider rather than assuming one account fits every task.

## Questions to verify before relying on either

Before using an exchange or wallet, identify the actual control model:

- Who controls each signing key, and can any one party transfer assets alone?
- Is the displayed balance an onchain address balance or a claim recorded in a provider database?
- Which legal entity provides custody, trading, recovery, and customer support?
- Can assets be withdrawn to an external address, on which networks, under which limits and fees?
- What happens if credentials, a device, a key share, or a seed phrase is lost?
- Which actions require an onchain transaction, and where is the transaction identifier shown?
- Does the wallet rely on one RPC, indexer, swap provider, bridge, or other backend?
- Are customer assets segregated, commingled, lent, pledged, or held through another custodian?
- Which protections are contractual, technical, regulated, insured, or merely marketing claims?

A cryptocurrency exchange is a trading and account system; a wallet is a key-management and authorization system. They can appear in the same product, but their responsibilities remain distinct. Following custody, signing authority, ledger location, and withdrawal flow provides a clearer comparison than relying on the label “exchange” or “wallet.”

## Sources and references

- [Wallet - Glossary](https://csrc.nist.gov/glossary/term/wallet) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
