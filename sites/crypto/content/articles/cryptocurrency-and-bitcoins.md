---
title: "Cryptocurrency and Bitcoins: Security, Compliance, and Operations"
description: "Learn how cryptocurrency and bitcoins relate, and review the security, compliance, and operational questions organizations should assess before handling them."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["security_compliance_operations"]
tags: ["cryptocurrency bitcoins"]
author: "editorial_team"
primary_keyword: "cryptocurrency and bitcoins"
owned_question: "How do cryptocurrency and bitcoins relate, and what operational security and compliance considerations should organizations assess before handling them?"
risk_level: "medium"
---

Cryptocurrency is a broad category of digital assets that can be transferred between users of a blockchain network; Bitcoin is one particular cryptocurrency and network within that category. For an organization, that distinction matters because the relevant transaction rules, security controls, and operational dependencies must be assessed for the specific system and activity—not inferred from the word “crypto.”

## What cryptocurrency means—and where Bitcoin fits

Cryptocurrency is a digital asset, credit, or unit that can be cryptographically transferred between users of a blockchain network. The term describes a category, not a single asset or operating model. A cryptocurrency system can support peer-to-peer exchange through distributed record-keeping rather than a conventional central transaction processor, although users may still rely on centralized wallets, exchanges, gateways, or other intermediaries. [source](<https://csrc.nist.gov/glossary/term/Cryptocurrency>) [source](<https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype>)

Bitcoin is one specific example in that category. Its original network design uses hashes to link blocks and hash-based proof of work to order transaction history. Those are characteristics of Bitcoin’s design; they should not be treated as a definition of every cryptocurrency. [source](<https://bitcoin.org/bitcoin.pdf>)

It is also important not to equate a system’s stated decentralized design with the absence of concentrated control. Crypto and decentralized-finance systems can exhibit substantial de facto centralization, but the degree and location of that concentration need assessment for a specific network, asset, application, and time window. [source](<https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks>)

For organizational review, start with the particular asset and system in scope. Identify which network is involved, what kind of transaction or service the organization plans to use, and whether an intermediary is part of the workflow. A category-level description cannot establish how a specific implementation operates.

## How cryptocurrency and bitcoins move through an organization

A useful operational map separates the network from the services around it. A peer-to-peer cryptocurrency design uses distributed record-keeping rather than a conventional central transaction processor. But an organization may interact with that design through a centralized exchange, wallet provider, gateway, or another intermediary. The service involved can therefore be a separate operational dependency from the underlying network. [source](<https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype>)

Centralized exchange functions illustrate why role-mapping matters. An exchange operator may combine trading, proprietary activity, lending, token issuance, and custody, but not every exchange performs every function. Combining roles can create operational dependencies and conflicts. An organization should establish which functions its particular counterparty performs instead of assuming that “exchange” describes only a trading venue. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

A practical workflow review can document:

- The asset and network involved, and the organizational purpose of the activity.
- The services or counterparties that participate in the workflow, including any intermediary roles.
- Who is responsible for initiating, reviewing, approving, and recording organizational activity.
- What records the organization needs to reconcile and retain, and who is responsible for doing so.
- How staff should escalate a suspected error, security event, or interruption.

These are review questions, not universal technical requirements. The evidence available here does not specify a standard approval model, reconciliation method, record-retention period, or incident procedure for every organization. Those details require assessment of the organization’s own activity and the relevant system.

## Security controls to assess before handling cryptoassets

Begin with a clear boundary between the network’s protocol behavior and the organization’s responsibilities. Knowing that an asset belongs to the cryptocurrency category does not establish how a particular organization controls access, approves activity, handles operational interruptions, or responds to incidents. Those arrangements must be documented for the system and services actually in use.

Ask who can initiate and approve activity, what oversight applies, and how the organization detects and escalates unexpected events. Document the responsibilities of internal teams and external providers rather than treating them as interchangeable. Where an intermediary performs several functions, include those functions and their dependencies in the review; the fact that an operator combines roles does not show that every venue does so or establish the safeguards at a particular venue. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Security claims also need to be specific. Distinguish a documented process from an assurance that an asset or service is “secure,” and require evidence for any claim about protection, backup, recovery, or continuity. The allowed evidence does not establish a particular control’s effectiveness or provide a universal backup or recovery method. An organization should record those unresolved points rather than infer that a control will prevent loss or guarantee recovery.

The same caution applies to system-level claims. Peer-to-peer design does not mean that every user avoids intermediaries, and stated decentralization does not by itself establish where operational control resides. Assess the particular network, application, and counterparties relevant to the planned activity. [source](<https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype>) [source](<https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks>)

## Compliance and jurisdiction questions that require local evidence

This explainer does not determine whether an activity is regulated, whether a license or registration is required, or what compliance obligations apply. Those questions depend on the organization’s activities, counterparties, and relevant jurisdictions, and require current authoritative evidence specific to that context.

Before drawing conclusions, document where the organization operates, what it intends to do, and which counterparties are involved. Verify regulatory status and applicable requirements against authoritative sources for the relevant locations. Do not infer legal status from the label “cryptocurrency,” from Bitcoin’s particular network design, or from a service’s description of itself.

Tax treatment, fees, and asset or service availability are also outside the evidence established here. They require current, location-specific verification; no general statement in this article should be used as a substitute for that research. If a question requires a legal, tax, or technical conclusion, escalate it to qualified advisers or internal specialists with the relevant context.

## A decision checklist for organizational readiness

Before proceeding with a cryptocurrency-related activity, use a bounded review:

1. **Define the scope.** Name the asset, network, intended use, and organizational activity. Keep Bitcoin’s specific technical design distinct from general claims about cryptocurrency.
2. **Map roles and dependencies.** Identify the network, intermediaries, and counterparties in the workflow. Confirm which functions each counterparty actually performs; exchange operators may combine functions, but this is not universal. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)
3. **Assign organizational responsibilities.** Record who owns access decisions, approvals, recordkeeping, and incident escalation. The evidence here does not prescribe a universal operating model, so document the organization’s actual one.
4. **Require support for security claims.** Record which controls and recovery processes are documented, what evidence supports claims about them, and what remains unresolved. Do not treat an assurance as proof of an outcome.
5. **Verify local obligations.** Research regulatory, licensing, compliance, tax, fee, and availability questions using current authoritative evidence appropriate to the relevant jurisdiction and activity.
6. **Escalate open questions.** Route unresolved legal, tax, technical, and operational issues to appropriately qualified advisers or internal specialists. Category-level information alone does not establish readiness.

The central decision is not whether “cryptocurrency” in general is suitable for an organization. It is whether the organization understands the specific system and workflow under consideration, has documented its responsibilities and dependencies, and has verified the questions that require current, local, or system-specific evidence.

## Sources and references

- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
- [Cryptocurrency - Glossary](https://csrc.nist.gov/glossary/term/Cryptocurrency) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
