---
title: "Earn interest on crypto: mechanisms, infrastructure, and risks"
description: "Earn interest on crypto by understanding possible return mechanisms, asset control, infrastructure roles, and product-specific risks to verify."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "earn interest on crypto"
owned_question: "How can crypto interest products generate returns, what roles may exchanges and other infrastructure providers play, and which operational and counterparty risks should be verified?"
risk_level: "high"
---

Crypto interest products can generate returns through different arrangements, such as lending or credit activity, but the source of a return, who controls the assets, and what the customer can claim depend on the specific product. An exchange may provide custody or trading without itself being the borrower or return-generating counterparty, so operators should verify the documented roles and obligations rather than infer them from product access.

## What “interest” can mean in a crypto product

“Interest” is not enough to identify the underlying mechanism. A displayed or stated return may relate to a contractual obligation, an activity involving counterparties, or another product structure. The term alone does not establish where the return comes from or whether a customer has a right to repayment of the same assets, their value, or something else. Those details require product-specific documentation; the available evidence here does not establish terms for any particular offering.

Separate three questions when reviewing a product: What activity is intended to produce the return? Who holds or controls the assets during that activity? What does the customer’s agreement say is owed, and by whom? An answer to one does not resolve the others. For example, an exchange’s custody role does not, by itself, identify the counterparty or explain how a return is funded. Customer custody and ownership arrangements vary by platform and jurisdiction. [source](<https://www.bis.org/publ/work1227.pdf>)

Nor should a stated return be treated as proof of a guaranteed outcome or as equivalent to interest on a bank deposit. No general guarantee, protection, or uniform legal status follows from the word “interest.” The relevant evidence is the product’s current terms and the actual arrangement behind them.

## How crypto interest may be generated

Lending or credit activity is one possible high-level source of income: assets may be made available to a borrower or another counterparty under an arrangement that expects repayment. That description does not establish whether a particular product lends assets, how borrowers are assessed, what collateral is required, or who bears a shortfall. Those are product-specific facts and should not be filled in from the product’s label or promotional summary.

A second distinction is between a return paid under an intermediary’s product terms and rewards associated with protocol activity. These are not interchangeable mechanisms. The evidence available for this article does not establish the operation, terms, or risks of any specific staking or decentralized-protocol product, so those mechanisms cannot be described in detail or assumed to be present.

An intermediary might administer or deploy assets, but the product’s actual flow must be documented before stating that it does. To trace the mechanism, look for evidence identifying the asset recipient, the activity performed, any borrower or protocol involved, the party responsible for returning assets or value, and the conditions under which that obligation applies. If those roles are not clear in available materials, treat the source of the return as unverified rather than inferring it.

## Where exchanges fit in the infrastructure

An exchange can occupy more than one role, but those roles should be analyzed separately. In a common centralized-exchange model, a customer transfers funds and custody to the exchange before trading on its internal order book. [source](<https://www.bis.org/publ/work1227.pdf>) This describes a trading and custody arrangement; it does not establish that the exchange also lends those funds, invests them, or guarantees a return.

For an interest product, map the relevant parties independently: the customer, any custodian, the platform or administrator, a potential borrower or protocol, and the entity that owes any promised repayment or return. A company might perform multiple functions, or separate organizations might perform them; the product-specific evidence must establish which is the case. Do not infer responsibility from branding, a trading relationship, or the fact that assets appear in an account interface.

This role map also separates protocol behavior from provider obligations. A protocol may execute rules for onchain activity, while an intermediary may control accounts, custody, access, or communication with counterparties. The available evidence does not establish that any named product uses a protocol, custodian, or particular settlement process. Operators should identify those dependencies from current documentation before describing the product’s architecture.

## Operational and counterparty risks to examine

A useful review starts with the obligation and its dependencies, not a headline return. Where lending is involved, assess who owes repayment and what the documentation says happens if that party does not repay. Where assets are administered or pooled, verify who can control them and what terms govern withdrawals, loss allocation, and any separation of customer assets. The evidence provided here does not establish the answers for a particular product; they must be verified in its applicable agreements and operational materials.

Collateral may be relevant in some crypto-credit arrangements, but collateral does not eliminate risk. A common decentralized collateral model can depend on overcollateralized smart-contract positions, price oracles, collateral-ratio rules, and liquidation processes, and can still face oracle, contract, governance, liquidity, collateral-price, and bad-debt failures. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>) This is a bounded description of one model, not evidence that a given interest product uses it or that collateral ensures repayment.

Also distinguish custody exposure from credit exposure. Even when assets are held by an intermediary, that fact alone does not show whether they are lent, segregated, pledged, or otherwise deployed. Conversely, a product’s use of a protocol would not by itself establish how a customer’s claim is treated. Verify key-control responsibilities, access restrictions, incident-response procedures, and recovery arrangements in scoped documentation rather than assuming such controls exist or guarantee recovery. The available evidence does not substantiate specific controls for any product.

For any protocol-based component, determine what the user or provider must authorize and what the interface communicates. Ethereum-oriented DEX interface guidance, for example, says interfaces should clearly communicate token identity, allowances, quoted outputs, slippage, price impact, network fees, and transaction state; that guidance does not prove the safety of the underlying contracts or assets. [source](<https://ethereum.org/developers/docs/design-and-ux/dex-design-best-practice/>) It should not be generalized into evidence that a crypto interest product uses a DEX or that its contracts are safe.

## What evidence is needed for product claims

A defensible assessment ties each claim to current, relevant evidence. Product terms should identify the structure, the parties, asset handling, repayment or return obligations, withdrawal conditions, and how losses are allocated. Operational documentation should substantiate any claims about custody, key management, security controls, incident response, or recovery. If documentation does not answer a question, mark it as unresolved; a general description of crypto infrastructure cannot fill that gap.

Treat time-sensitive statements—such as yields, fees, supported assets, availability, or withdrawal timing—as claims requiring current product materials. None is established here. Likewise, legal, regulatory, tax, and compliance treatment is outside the scope of the evidence for this article and should not be inferred or generalized across jurisdictions.

Finally, distinguish documented terms from promotional language. A claim that assets are “protected,” “secure,” or “backed” needs evidence that specifies the relevant control, obligation, or supporting arrangement and its limits. A claim that an exchange “offers” a product does not, without further documentation, establish which entity holds assets, which party generates or owes a return, or what happens under stress. For infrastructure teams and business decision-makers, the practical test is whether each material role and dependency can be traced to a current, appropriately scoped source.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Decentralized exchange (DEX) design best practices](https://ethereum.org/developers/docs/design-and-ux/dex-design-best-practice/) — ethereum.org; retrieved 2026-10-18.
