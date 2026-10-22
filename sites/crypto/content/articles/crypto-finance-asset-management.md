---
title: "Crypto finance asset management: wallets, custody, and operational controls"
description: "Explore how wallets and custody support crypto finance asset management, including key control, transaction authorization, operational safeguards, and evaluation."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["wallets_custody"]
tags: []
author: "editorial_team"
primary_keyword: "crypto finance asset management"
owned_question: "How do wallet and custody systems support the operational management of crypto assets, and which responsibilities and controls should organizations define?"
risk_level: "high"
---

Crypto finance asset management, viewed through wallets and custody, is the operational work of controlling access to crypto assets and authorizing their use—not a recommendation about what to buy, sell, or hold. The key question for an organization is who can initiate and authorize transactions, and what evidence supports those permissions. The limited evidence available here does not establish a general wallet or custody operating model, so organizations must verify implementation details rather than assume them.

## What crypto asset management means in a wallet-and-custody context

In this context, “management” means organizing the access and transaction responsibilities associated with crypto assets. It is distinct from portfolio strategy. A wallet-and-custody arrangement is part of an organization’s operating infrastructure, but the evidence available here does not define all the systems or agreements that may sit behind it.

A useful role map starts with the organization that sets the purpose and authorization rules, the people or services involved in carrying out those rules, and the network that records transactions. Do not treat those roles as interchangeable. A transaction appearing in a network record does not, by itself, explain the organization’s internal approval process or identify who had authority to act.

The evidence for this article is narrow: it describes Bitcoin transaction structure and a particular exchange trading model. It does not provide enough support to specify general wallet functions, custody arrangements, key-management procedures, or organizational controls. Those details need to be established from documentation for the actual systems and agreements under consideration.

## How wallets and custody divide asset-control responsibilities

A custody model concerns how access and control are assigned. This article does not have sufficient evidence to describe the full range of self-managed and third-party custody arrangements or to say which is appropriate for an organization. Decision-makers should therefore ask providers and internal system owners to document who holds or can use the relevant authorization capability, who may approve a transaction, and where those responsibilities are recorded.

One supported example is a centralized exchange: after assets are deposited, the exchange can provide trading through its internal order book. That describes the exchange’s trading model, not a universal custody rule, and it does not establish how a particular platform allocates legal ownership or other responsibilities. A separate supported distinction is that an exchange can provide near-real-time trading and order functionality after deposit, while the precise performance and liquidity vary by venue, asset pair, and market conditions.

These examples should not be generalized into a claim that every exchange or wallet works the same way. For any specific arrangement, verify the documented transaction path, the roles involved, and the contractual allocation of responsibility. The available evidence does not establish a standard approval threshold, recovery process, or separation of duties.

## Controls to define before managing crypto assets

Before implementation, an organization can use a control inventory to identify matters it must resolve. The items below are questions to answer with system-specific evidence, not claims that a particular safeguard is universally available or effective:

- **Roles and authorization:** Who may request, approve, and carry out a transaction? Are these responsibilities distinct in the actual design? Request a documented workflow rather than inferring controls from a product label.
- **Access and continuity:** Which people or services can access the system, and what happens if access is unavailable or disputed? The evidence here does not establish a general backup, recovery, or incident-response method.
- **Transaction review:** What information can an approver inspect before authorizing an action, and how is the outcome recorded? Do not assume a network record proves that an organization’s internal authorization requirements were met.
- **Records and reconciliation:** Which records will the organization compare, and who is responsible for resolving discrepancies? The available claims do not prescribe a reconciliation method or record-retention period.

Bitcoin provides a narrow illustration of why transaction records need careful interpretation. In its UTXO model, a non-coinbase input spends a specific prior output identified by transaction ID and output index; the transaction’s new outputs remain unspent until a later input spends them. This describes how Bitcoin transaction value is traced, not how an organization should assign ownership, identify a wallet operator, or maintain internal books. Wallet ownership and service labels require additional evidence and can be wrong.

For that reason, operational controls should be documented separately from the network’s transaction mechanics. A record of a transaction can support review of what the network recorded, but it does not alone answer who within an organization approved the action or whether it followed internal policy.

## Questions for evaluating wallet and custody infrastructure

Use diligence questions to turn broad assurances into verifiable operating details. Request current, implementation-specific documentation and compare it with the organization’s intended workflow.

1. **Transaction path:** What system constructs and submits transactions, and which components or people participate before a transaction is recorded? Ask for the end-to-end sequence, including exceptions.
2. **Authority and responsibility:** Who can authorize actions, and how is that authority assigned? Request clear responsibility allocation rather than inferring it from terms such as “managed” or “secure.”
3. **Dependencies:** Which external services or internal systems must operate for the workflow to proceed? The available evidence does not establish a general standard for service continuity or outage handling.
4. **Evidence and records:** What records can the organization inspect, and what do they establish? BIP 122 is a draft URI proposal that describes common explorer lookup objects—transactions by hash, blocks by hash or height, and addresses. It is not evidence that every explorer supports the same references or that an explorer record proves internal authorization.
5. **Limits of claims:** For any statement about recovery, security, fees, availability, supported assets, service continuity, or regulatory status, request current authoritative documentation specific to the arrangement. The evidence available here does not substantiate those claims generally.

Keep the scope of each answer precise. For example, a source describing exchange order-book functionality does not establish key recovery, asset segregation, or incident handling. Likewise, a transaction reference or explorer lookup does not establish the identity of the person or service that authorized an action.

## Governance, compliance, and limits of a general framework

An organization should assign a clear owner for approving its operating policy and monitoring whether documented procedures are followed. It should also specify who can approve exceptions and how those decisions will be recorded. These are governance questions to resolve internally; the evidence cited here does not prescribe a specific policy or review schedule.

Treat legal, tax, licensing, and compliance questions as dependent on the jurisdiction and the details of the arrangement. This article does not provide legal or tax conclusions, determine regulatory status, or establish applicable compliance obligations. Obtain current, qualified advice and authoritative documentation before relying on any such conclusion.

Finally, distinguish a documented control from a guarantee. A system description can explain a stated process, but it does not, on the evidence available here, prove that an organization’s complete arrangement prevents errors, ensures recovery, or removes operational or counterparty risks. A sound evaluation therefore maps responsibilities first, verifies each claimed control against the actual implementation, and leaves unsupported conclusions unresolved until reliable evidence is available.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Transactions](https://developer.bitcoin.org/devguide/transactions.html) — Bitcoin Developer Guide; retrieved 2026-10-19.
- [BIP 122: URI Scheme for Blockchain References and Exploration](https://bitcoin.org/bip/122/) — Bitcoin Improvement Proposals; retrieved 2026-10-18.
