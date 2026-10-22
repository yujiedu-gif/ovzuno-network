---
title: "Digital assets business: activities, protocols, and infrastructure"
description: "Learn what a digital assets business may do, how crypto protocols and infrastructure support its activities, and which operational questions need further review."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "digital assets business"
owned_question: "What does a digital assets business do, and how can its activities depend on crypto assets, protocols, and supporting infrastructure?"
risk_level: "medium"
---

A digital assets business is an organization whose products or operations involve digital assets or crypto networks. The label describes a broad area of activity, not a particular technology or legal status. To understand a specific business, identify what it does, which protocol functions it depends on, and what supporting services it operates or relies on.

## What counts as a digital assets business?

There is no single rigid definition of “digital assets business” in the evidence used here. A practical way to use the term is for an organization that builds, operates, or uses products involving digital assets or crypto networks. “Web3,” sometimes used for a related vision of the internet, also has no single rigid definition; it is commonly used as a catch-all for a user-owned, decentralized vision. Neither label specifies an organization’s actual activities. ([source](<https://ethereum.org/web3/>))

Separate three things when describing a business:

- **The activity:** what the organization does, such as developing software or incorporating a network into a business process.
- **The asset:** the digital item or unit involved.
- **The protocol and infrastructure:** the rules and technical systems that support the activity.

These categories answer different questions. A business can work with a crypto network without creating its own token, and a token’s technical design does not, by itself, describe every service or responsibility of an organization using it.

The term is not a legal classification here. A business label alone does not establish whether an organization is licensed, regulated, or subject to a particular tax treatment. Those questions require evidence specific to the jurisdiction, activity, asset, and organizational structure.

## Business activities built around digital assets

A useful, non-exhaustive map groups activity by function rather than by buzzword. An organization might develop protocol software, provide an application that interacts with a network, arrange access to digital assets, or use a network as one part of a business process. These are examples for analysis—not a universal taxonomy or a determination of legal status.

In practice, the business model can combine functions. Software development may be one activity, while operating an interface or managing customer access may be another. Each can rely on different systems and controls. Naming the function first helps avoid treating all work involving crypto assets as though it has the same technical dependencies.

A network that coordinates real-world infrastructure offers one example of layered dependencies. One research description of decentralized physical infrastructure networks (DePINs) identifies layers spanning physical devices, communication and data handling, blockchain records, incentives, and application services. Implementations may combine, omit, or centralize parts of those layers, so the label does not establish how a particular system works. ([source](<https://arxiv.org/abs/2406.02239>))

Cross-network activity offers another distinction. Assets are not physically moved from one ledger to another; bridge designs coordinate value across chains through mechanisms such as minting, burning, locking, releasing, or swapping. The exact accounting and redemption path depends on the bridge design. A business relying on such a service therefore needs to understand the specific mechanism rather than infer its operation from a general label. ([source](<https://ethereum.org/developers/docs/scaling/sidechains/>))

These examples show why a business activity should be described separately from the protocol mechanism beneath it. A product may depend on one or more network functions, but that dependence does not mean the network performs the organization’s entire service.

## How protocols and infrastructure support the business

A protocol is a set of rules and mechanisms a network uses to coordinate activity. A business may depend on a protocol to record transactions or provide an environment in which software interacts with digital assets. The protocol’s role is distinct from the company’s application, customer process, and operational decisions.

A practical dependency map asks what each component contributes:

- **Protocol:** Which network rules or functions does the business rely on?
- **Application:** What software presents the service or coordinates user actions?
- **Asset handling:** Who or what manages access to the relevant assets and keys?
- **Network access:** How does the application read network data or submit activity?
- **External services:** Are there providers or infrastructure components whose operation affects the service?

This is a checklist, not an assertion that every business uses every component. The architecture must be established for the specific organization. In particular, a protocol’s ability to support an operation does not establish that a company has implemented it correctly, that its service is always available, or that a user can recover access after a problem.

Cryptography is not a single, all-purpose guarantee. It is a discipline applying methods to information-security goals that include confidentiality, data integrity, source authentication, and non-repudiation; a particular cryptographic primitive usually serves only a subset of those goals. When reviewing a system, ask what a cryptographic mechanism is intended to establish and what remains dependent on software, operations, or other components. ([source](<https://csrc.nist.gov/glossary/term/cryptography>))

For example, Ethereum proof of stake uses ETH deposits as slashable economic collateral for validator participation. That describes a protocol mechanism; it does not establish that every business using Ethereum operates a validator or that a third-party service has the same arrangement. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

## Operational dependencies and risk questions

After mapping the activity and technical components, review the operational dependencies. These questions make that review concrete without assuming that a particular system is secure or suitable:

1. **Asset access:** Which party or system can authorize activity involving the assets? What key-management and access processes are actually in place?
2. **Transaction processing:** What components construct, submit, and monitor transactions? Which steps belong to the protocol, and which belong to the business or its providers?
3. **Software changes:** Which applications or protocol components can change, who controls those changes, and what processes govern them?
4. **Third-party reliance:** Which external services are needed for the business to function, and what would be affected if one became unavailable or changed its service?
5. **Failure and recovery:** How would the organization respond to lost access, an application error, a network interruption, or a protocol change? What evidence supports the stated recovery process?

These are investigation prompts, not claims that a specific outage, loss, fee, or failure will occur. The evidence available here does not establish service-level availability, recovery guarantees, current fees, yields, or security outcomes for a particular product. Those claims require product- and system-specific support. Likewise, a protocol feature should not be treated as proof of the behavior of a company’s implementation.

A useful review records the dependency, the party responsible for it, and the evidence available about its operation. For example, an organization may describe a process as “onchain,” but that phrase alone does not tell a reader which application submits activity, what services provide network access, or who manages asset access. Keep the description at the level the evidence supports, then identify unanswered operational questions rather than assume their answers.

This discipline also helps when a business combines activities. A software provider and an organization that manages access to assets may depend on related protocols, yet have different operational responsibilities. Map each activity separately, then note where they share components or rely on an external provider. The result is a clearer account of what the protocol contributes and what remains part of the organization’s own service design and controls.

## What varies by jurisdiction and business model

Legal, regulatory, and tax treatment cannot be determined from the phrase “digital assets business” alone. A concrete assessment needs current, jurisdiction-specific evidence and must account for the activity, asset characteristics, and organizational structure. This explainer does not state licensing duties, tax outcomes, compliance obligations, or service availability for any jurisdiction.

For a business review, first document the actual service and its technical dependencies. Then seek appropriately qualified, sourced analysis for the relevant locations and organizational arrangement. Keeping those steps separate helps prevent a broad technology description from being mistaken for a legal conclusion.

## Sources and references

- [What is Web3 and why is it important?](https://ethereum.org/web3/) — ethereum.org; retrieved 2026-10-19.
- [Decentralized Physical Infrastructure Network (DePIN): Challenges and Opportunities](https://arxiv.org/abs/2406.02239) — arXiv; retrieved 2026-10-19.
- [Sidechains](https://ethereum.org/developers/docs/scaling/sidechains/) — ethereum.org; retrieved 2026-10-18.
- [Cryptography](https://csrc.nist.gov/glossary/term/cryptography) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
