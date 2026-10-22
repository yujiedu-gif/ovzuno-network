---
title: "A Brief Survey of Cryptocurrency Systems: Design and Reporting Context"
description: "A brief survey of cryptocurrency systems, covering network designs, ledgers, consensus, and transaction records that may inform regulatory and tax-reporting research"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["regulation_tax_reporting"]
tags: ["brief survey cryptocurrency systems"]
author: "editorial_team"
primary_keyword: "a brief survey of cryptocurrency systems"
owned_question: "What are the main types of cryptocurrency systems, how do their core components differ, and why do those differences matter when assessing regulation and tax reporting?"
risk_level: "medium"
---

Cryptocurrency systems combine protocol rules, a ledger, network participants, and digital assets. Their designs can help researchers identify questions about control, services, and transaction records, but technical features alone do not determine legal classification or tax treatment. Those conclusions require current, jurisdiction-specific research and the relevant facts.

## What counts as a cryptocurrency system?

A cryptocurrency system is a set of components that work together. A protocol is the collection of rules that software follows; a ledger is the record maintained under those rules; and network participants run software that may update, store, or read the record. A cryptocurrency can support peer-to-peer digital exchange through distributed record-keeping rather than a conventional central transaction processor. People may still rely on intermediaries, including wallets, exchanges, and gateways. [source](<https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype>)

A token is not the entire system. A digital token can be a ledger record about an asset and its owner, with programmable rules governing use or transfer. But a technical record alone does not establish legal title, enforceability, or the quality of the represented asset. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

A wallet, application, and protocol are also distinct. A wallet is a means of interacting with a system; an application may provide services built around network functions; and the protocol supplies rules for system activity. In practice, a single service or organization may participate in more than one role. Analyzing a system therefore means identifying its separate layers and actors rather than treating “the token,” “the wallet,” and “the platform” as synonyms.

This overview focuses on the system-level distinctions that can guide further research. It does not explain exchange or on-ramp operations, recommend an asset, or establish a particular jurisdiction’s legal or tax rules.

## How cryptocurrency systems differ in design

Systems can differ in who may participate, how transaction records are maintained, and how changes to rules are coordinated. These are technical and organizational dimensions, not legal classifications. A peer-to-peer design, for example, does not mean that every user interacts directly with a network or that intermediaries are absent. [claim_bis_peer_to-peer]

The ledger is the record that participants and applications use to refer to system activity. When reviewing a system, ask what it records, who can update or read it, and what rules apply when participants propose conflicting updates. The existence of a distributed record does not show that influence is equally distributed or that control is fully decentralized. Crypto and DeFi systems can exhibit substantial de facto centralization even when their stated architecture or ethos emphasizes decentralization. The degree and location of concentration must be assessed for a specific network, asset, application, and time window. [source](<https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks>)

Participation labels such as “open” and “permissioned” describe aspects of access, but they do not settle who legally operates a service or which laws apply. Likewise, the number of participants or the distribution of software does not by itself establish who can change system rules or control a particular service. Those questions require system-specific evidence and, where legal conclusions are sought, jurisdiction-specific analysis.

Consensus and governance should be treated as related but separate concepts. Consensus concerns how participants coordinate on accepted records. Governance concerns how proposed rule or software changes are reviewed and coordinated. To understand a particular system, check its technical documentation for the stated processes and identify what is documented about proposing, implementing, and adopting changes. Do not infer governance arrangements from a general claim that a system is decentralized.

These distinctions matter for research because the protocol’s functions may differ from the functions of entities operating applications or services around it. A technical description can identify possible roles, but it cannot establish that a particular organization performs them or that a role has a specific legal status.

## From transaction to recorded activity

A transaction can be considered as a sequence of stages: an instruction is initiated, software and network participants process it under system rules, and an accepted instruction becomes part of the system’s record. The details of validation, ordering, and confirmation or finality differ among systems. A general description is not enough to establish those details; consult documentation for the specific system and distinguish its stated design from observed operation.

Keys and wallets are relevant because they relate to authorizing or accessing activity, but control of a key is not the same thing as operating the underlying network. Nor does a valid system record, by itself, settle who legally owns an asset or how an activity should be treated for reporting. A researcher should identify the relevant person or service, what role it performed, and what additional records or arrangements may bear on the question.

Provider roles can also overlap. A centralized crypto exchange operator may combine third-party trading, proprietary trading, margin lending, token issuance, and custody, although not every exchange performs every function. Combining roles can create operational dependencies and conflicts. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>) This is a reason to verify the specific provider’s services and terms rather than infer its activities from the label “exchange.” It does not establish that any particular provider performs every listed function.

The system’s record should also be distinguished from a person’s complete accounting or tax records. A ledger entry may document activity recorded by a network, but it does not automatically capture all relevant context about parties, services, rights, or circumstances. The available evidence does not specify tax-record requirements. Researchers should avoid treating the ledger as a complete answer to a tax or accounting question.

## Why system design matters for regulation and tax reporting

Technical design helps frame questions; it does not answer them. If a person or organization controls keys, operates infrastructure, issues a token, or provides custody or trading services, those roles may be facts to investigate. A system’s architecture alone does not establish an asset’s legal classification, and identifying a possible service function does not show that every operator performs it.

For an asset-backed token arrangement, ask what or whom the holder has a claim or right against and how backing assets relate to that claim. Legal effect, segregation, redemption, and insolvency treatment depend on the arrangement and applicable law. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>) The point is not that every token has the same structure, but that the ledger record should not be mistaken for a complete statement of the holder’s rights.

Tax reporting requires a separate inquiry. A system may record transfers, but that record does not determine the tax treatment of a particular event. Treatment depends on applicable rules and facts. This overview does not establish any jurisdiction’s tax categories, reporting duties, or deadlines. It also does not provide jurisdiction-specific regulatory or compliance conclusions. Before reaching either kind of conclusion, identify the relevant jurisdiction and verify current authoritative guidance or consult a qualified professional.

A useful research distinction is between three questions: what the system is designed to do, what a particular participant or provider actually does, and what applicable rules require. Evidence for one question does not automatically answer the others. A documented protocol feature, for example, does not by itself establish an operator’s legal responsibilities or a user’s reporting treatment.

## What evidence to check before drawing conclusions

Use a disciplined sequence when reviewing a system:

1. **Confirm the technical description.** Consult current, system-specific documentation for participation, ledger behavior, validation, and governance. Separate documented design from observed operation.
2. **Identify the relevant actor and role.** Determine whether the party is a user, application, network operator, issuer, exchange, or custodian. Do not assume one entity performs every possible function.
3. **Check rights separately from records.** For a token connected to an asset or claim, verify the governing arrangement and relevant documentation. A ledger entry alone does not establish legal rights. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)
4. **Verify regulatory and tax questions locally.** Use current authoritative sources for the applicable jurisdiction and facts, or seek qualified advice. Do not infer a legal or tax result from technical design alone.
5. **Treat changing or provider-specific statements as evidence questions.** Availability, fees, yields, security, and recovery require current, authoritative evidence about the relevant system or provider. Do not generalize those features across cryptocurrency systems.

This approach keeps system architecture, actual services, and applicable rules distinct. It gives researchers a practical starting point for regulatory and tax-reporting inquiries without turning a technical survey into a jurisdiction-specific conclusion.

## Sources and references

- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
