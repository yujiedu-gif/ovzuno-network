---
title: "Crypto for institutions: use cases, operating models, and risks"
description: "Explore crypto for institutions through use cases, operating models, governance, and risk questions, with a framework for evaluating organizational needs."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["institutional_crypto_treasury"]
tags: ["crypto institutions"]
author: "editorial_team"
primary_keyword: "crypto for institutions"
owned_question: "What does using crypto for institutions involve, and which treasury, operational, governance, and risk considerations shape an institution’s approach?"
risk_level: "medium"
---

For an institution, using crypto can mean holding digital assets, using blockchain-based services, or incorporating blockchain records into business processes. The right evaluation begins by defining the activity and its business purpose, then identifying the people, controls, counterparties, technical dependencies, and unresolved risks involved. These categories are not interchangeable: each can call for a different operating model and review.

## What using crypto means for an institution

A digital asset may be recorded or transferred using a blockchain network, but institutional activity is broader than holding an asset. An organization might evaluate an asset position, a payment or settlement process, or an application that uses blockchain infrastructure. The term “crypto for institutions” therefore describes a set of possible activities, not one standardized service or organizational capability.

A wallet is part of the access model, not a container holding coins. It generally manages private keys or passcodes used to access and authorize crypto assets. That distinction matters when mapping responsibility: the organization needs to know which system authorizes activity, who or what controls the relevant credentials, and what records it relies on. The specific answers depend on the wallet and operating arrangements under consideration. [source](<https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0>)

Cryptographic tools also have different functions. The broader field includes digital signatures, hash functions, key management, message authentication, random-bit generation, and encryption. It is not accurate to treat “cryptography” as one control that solves every security or operational need; an institution should identify which function a design uses and what it does not establish. [source](<https://csrc.nist.gov/Projects/cryptographic-standards-and-guidelines>)

A useful first distinction is between holding an asset and using infrastructure. Holding raises questions about authorization, custody, access, and recovery. Using a service or process raises questions about how transactions or records are created, reviewed, and reconciled, and which external systems or participants are involved. The same organization could consider both, but one does not automatically answer the governance questions associated with the other.

## Institutional crypto use cases and operating choices

Institutions can organize their evaluation around three broad categories: treasury exposure, payments or settlement, and blockchain-based business operations. These are lenses for defining a proposed activity, not claims that an activity will improve performance or produce a particular business result.

**Treasury exposure** concerns whether and how an organization would hold a digital asset as part of its financial activity. The decision is not simply about the asset: it also involves who can authorize access or transfers, what evidence supports the organization’s records, and how responsibilities are assigned. This article does not assess assets or provide a treasury-management procedure.

**Payments or settlement** focuses on how value or payment instructions move between participants and how an organization determines that an obligation has been met. A proposed process needs a clear account of the parties, the relevant records, any service dependencies, and the conditions for recognizing completion. A technical record or transaction state should not be assumed to answer every business-process question without review of the arrangement.

**Blockchain-based operations** use a blockchain service or record as part of a business workflow rather than treating the activity solely as an asset holding. For example, a decentralized exchange design can allow a user to retain control of assets while a trade executes or settles through smart contracts on a blockchain. That example illustrates one operating pattern; it does not describe every exchange design or remove possible dependence on interfaces, relayers, administrators, or off-chain components. [source](<https://www.bis.org/publ/work1227.pdf>)

For each category, map the workflow before drawing conclusions about benefits. Identify who initiates an action, who approves it, what system records it, which parties must act, and how the organization checks the result. If a proposal claims lower cost, faster processing, greater transparency, or another benefit, treat that as a proposition to test against the specific design and activity. The available evidence here does not establish those outcomes for a particular institution or implementation.

## Governance, controls, and organizational readiness

Institutional review is cross-functional because the activity may touch financial authority, legal review, compliance, information security, operations, and technology. Assigning an owner to each question helps surface gaps before a technical or commercial proposal is treated as an approved operating model.

Start with decision rights. Specify who may propose, approve, execute, monitor, and stop an activity. Consider whether the same person or system would hold multiple roles, and document where independent review is expected. These are governance questions for the organization to resolve; the permitted evidence does not establish a universal segregation-of-duties design.

Next, define the information and records needed to oversee the activity. Establish which system or party supplies each record, who checks it, and how discrepancies are escalated. If an institution uses keys or other cryptographic material, key management includes lifecycle functions such as generation, storage, distribution, use, recovery, revocation, and destruction. A review should cover the relevant lifecycle rather than focusing only on initial setup. [source](<https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines>)

Assess readiness at the level of the intended workflow. Ask whether existing systems can support the required approvals and records; whether staff understand their responsibilities; and whether the organization has a defined path for exceptions and incidents. The answer may differ between a limited assessment, a new payment process, and an ongoing asset position. Do not infer that a blockchain component supplies the surrounding organization’s controls or operating capacity.

## Risk questions institutions should resolve

Risk review should be specific to the proposed activity. A useful discussion separates market and liquidity exposure from counterparty, operational, cyber, and technology concerns. The relevant questions depend on what the institution is doing; a broad label such as “crypto use” is not a risk assessment.

For any asset-related activity, clarify what happens if market conditions, access, or liquidity differ from expectations. For any service involving other organizations, identify the dependencies and what the institution understands about each party’s role. The available evidence does not support general claims that a particular activity will be liquid, recoverable, available, or protected from loss.

For technology and security, request evidence tied to the exact design and operating conditions. Distinguish protocol behavior from the controls of a wallet, application, custodian, exchange, or other service. A technical feature should not be treated as proof of an end-to-end security outcome. Similarly, recovery arrangements need to be described for the actual setup; a general statement about key management is not evidence that a particular organization can recover access.

For collateral-dependent designs, identify the dependencies rather than relying on a label. A crypto-collateralized stablecoin model can depend on overcollateralized smart-contract positions, price oracles, collateral-ratio rules, and liquidation processes, and can still face oracle, contract, governance, liquidity, collateral-price, or bad-debt failures. This is an example of design-specific questions, not a conclusion about every digital asset or every stablecoin. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf>)

Claims about fees, yields, availability, recovery, security, or compliance need evidence for the relevant provider, product, jurisdiction, and time. If evidence is absent or does not cover the institution’s use case, record the issue as unresolved rather than turning it into an assumption.

## How to evaluate a proposed institutional crypto activity

A bounded evaluation can end with a documented decision, conditions, or a decision not to proceed. It need not begin with selecting an asset or provider.

1. **Define the objective and scope.** State the organizational problem or process under review, the activity involved, and what is explicitly out of scope. Separate holding an asset from using a blockchain-based service or workflow.
2. **Map the operating model.** Draw the steps from initiation through review and recording. Name the responsible internal roles and external dependencies, and note where a key, application, or service participates.
3. **Set review and evidence requirements.** Identify the control owners, records, security and recovery evidence, and assumptions that require validation. Ask whether evidence applies to the specific design rather than to a broad category.
4. **Obtain current jurisdiction-specific review.** Validate applicable regulatory, licensing, compliance, and tax questions against current authoritative information and qualified advice for the relevant jurisdiction. This overview does not determine legal or tax treatment.
5. **Record the decision and revisit conditions.** Document the rationale, outstanding issues, accountable owners, monitoring expectations, and events that should prompt review. If an essential dependency or control remains unverified, preserve that limitation in the decision record.

This framework helps finance, treasury, risk, and technology teams discuss the same activity in operational terms. It does not establish that a particular use is suitable, that a provider meets an institution’s needs, or that a proposed benefit or protection will materialize. The decision should rest on the organization’s objective, its actual operating model, and evidence that addresses its specific risks.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Cryptographic Standards and Guidelines](https://csrc.nist.gov/Projects/cryptographic-standards-and-guidelines) — National Institute of Standards and Technology; retrieved 2026-10-19.
