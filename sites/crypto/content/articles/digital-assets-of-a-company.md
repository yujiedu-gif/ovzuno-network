---
title: "Digital assets of a company: types, control, and records"
description: "Learn what may count as digital assets of a company, how to distinguish crypto asset types and business uses, and what records support a preliminary inventory."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["digital asset company", "digital assets company"]
author: "editorial_team"
primary_keyword: "digital assets of a company"
owned_question: "What can count as a company's digital assets in a crypto context, and how should a business distinguish, classify, and document them?"
risk_level: "medium"
---

In a crypto context, a company’s digital assets can include cryptocurrency and other blockchain-based records or tokens that the company controls or uses. To build a preliminary inventory, describe each item by its form, purpose, network, and practical control, and retain the evidence behind those descriptions separately from conclusions about legal ownership, accounting, or tax treatment.

## What the term digital assets of a company can include

A blockchain is a tamper-evident and tamper-resistant digital ledger implemented in a distributed fashion. That technical definition helps distinguish blockchain-related assets from ordinary digital files and account data: being digital alone does not make something a crypto asset. Blockchain systems differ, so the definition does not settle how a particular network handles participation, consensus, privacy, finality, or governance. ([source](<https://csrc.nist.gov/pubs/ir/8202/final>))

Cryptocurrency is one category of blockchain-related digital asset. A company may also encounter records or representations associated with other items. For inventory purposes, describe what the system records and how the business uses it, without assuming that the record alone establishes an external right or a legal classification. Keep the description tied to evidence about the specific asset and arrangement.

Cross-network representations call for particular care. Bridges can coordinate activity between otherwise isolated blockchain environments, and transfer designs may use mechanisms such as locking, minting, burning, releasing, or swapping. The asset is not physically moved from one ledger to another; the exact accounting and redemption path depends on the bridge design. Accordingly, list the network and the representation recorded on it rather than treating matching names on different networks as proof that two records are identical. ([source](<https://ethereum.org/developers/docs/scaling/sidechains/>))

A company inventory is not a list of every electronic record the company possesses. It is a working description of items that are crypto-related in the company’s operations: for example, records or units on a blockchain that the company uses, or for which it is investigating its control or rights. If the connection is uncertain, flag the item for review instead of expanding the category by assumption.

## Classify assets by form, purpose, and control

Use separate fields rather than relying on a single broad label. A useful first pass has three dimensions:

- **Form:** Describe how the item is represented—for example, as a cryptocurrency unit, a token, or a cross-network representation. Include the network because a label without network context may not uniquely identify the record.
- **Purpose:** Record the company’s stated business use, such as payment, operations, access, or another function. This field reports the company’s purpose; it does not determine the item’s legal treatment or establish rights associated with it.
- **Control:** Identify who or what can authorize a transfer or change under the relevant technical arrangement. Record whether that authority is direct, shared, or dependent on another party or service, based on the evidence available.

Add an evidence field to each dimension. A company’s description of purpose is not the same kind of evidence as a technical record of an account or authorization. If the evidence does not establish a point, mark it unknown or unresolved rather than treating an internal label as proof.

For an Ethereum externally owned account, the corresponding private key controls the account. A valid signature supports attribution of that transaction to control of the key, but does not by itself identify the human, organization, device, or service controlling it. This is a technical account-control finding, not a complete conclusion about the company’s rights. ([source](<https://ethereum.org/developers/docs/accounts/>))

For example, if a business unit reports using an account, the inventory can record that stated use while separately noting who can authorize activity from the account. Do not turn the unit’s report into a claim that the company owns the recorded assets or has exclusive control. If a provider, shared authorization, or another party is involved, document that dependency as a feature of the arrangement, not as an inference about legal status.

## Build a preliminary company inventory

Create a register that lets finance, technology, and review teams see what has been identified and what still needs verification. A practical starting template is:

| Field | What to record |
|---|---|
| Asset description | Internal name and form; treat a name or ticker as a label, not a complete identifier. |
| Network and reference | The network and relevant public address, account, or token reference, where verified. |
| Quantity | The amount, the record used to check it, and when that record was reviewed. Mark unverified amounts clearly. |
| Business purpose | The company’s stated use and the business unit that reported it. |
| Control arrangement | Who can authorize movement or changes, whether authority is shared, and whether another party is involved. |
| Supporting records | Relevant agreements, approvals, transaction records, and technical documentation. |
| Open questions | Unresolved issues about identity, access, rights, control, or conflicting records. |

Treat this as an inventory aid, not as a valuation or accounting schedule. The quantity field should communicate the scope and source of the recorded information; it should not imply that an amount has been valued or classified for formal reporting. If a reference or quantity cannot be verified, say so directly.

A repeatable workflow is to identify the item, confirm the network and reference, record the stated purpose, and trace the evidence for practical control. Then attach or reference the supporting records and note discrepancies or gaps. Keep the technical facts, company statements, and agreement-based evidence distinguishable, since each supports a different kind of conclusion.

Limit sensitive wallet and credential details in general-purpose inventory documents. The register can describe who is authorized and where the supporting record is maintained without copying secrets or recovery material into a broadly shared file. If access to the evidence itself is restricted, record that restriction and the appropriate review path rather than including confidential material in the general inventory.

## Why ownership, custody, and access are different questions

**Technical control** concerns the ability to authorize an action under the relevant system. **Access** concerns the practical ability to use an account or service. **Ownership** concerns rights that require evidence beyond an account label or a technical record. These questions can overlap, but an inventory should not treat them as interchangeable.

A transaction signature, for example, can support a finding that a key authorized a particular transaction. It does not independently establish who controlled the key in the real world or whether that person acted for the company. Likewise, a record that a company uses an asset describes reported use; by itself, it does not settle ownership or exclusive control. ([source](<https://ethereum.org/developers/docs/accounts/>))

Preserve different kinds of evidence separately. Account references, authorization procedures, and transaction records can help describe technical control or activity. Agreements and approvals may be relevant to the company’s rights, responsibilities, or authority. Do not merge those sources into one unqualified statement. Where control is shared, provider-dependent, or unclear, record the condition and the evidence gap, then send the question for qualified review.

An inventory is most useful when it makes uncertainty visible. Use statuses such as verified, reported, or unresolved only when their meaning is clear to the people maintaining the register. For each unresolved question, note what evidence is missing and who should review it. This creates a traceable account of what the company knows without presenting a preliminary description as a definitive ownership determination.

## Where accounting, tax, and compliance conclusions require review

A technical asset label does not establish accounting classification, tax treatment, or regulatory status. Those conclusions can depend on facts not captured by the network record, including the company’s activity, the relevant jurisdiction, transaction details, and applicable agreements. A preliminary inventory should therefore document facts and open questions, not supply jurisdiction-specific conclusions.

Before using the register for formal reporting or decisions that depend on legal rights, accounting treatment, tax, or compliance, have qualified reviewers examine the relevant facts and current requirements. Verify that the asset identifier, control description, and supporting records correspond to the particular arrangement being reviewed. Do not state an obligation, outcome, or availability claim unless the evidence supports it for the relevant context.

The practical outcome is a clear, evidence-linked description of what the company has identified, how it says the item is used, what technical control evidence exists, and what remains uncertain. That distinction gives follow-up reviewers a usable starting point without confusing an asset label with ownership or a preliminary inventory with a legal, accounting, tax, compliance, or investment conclusion.

## Sources and references

- [Sidechains](https://ethereum.org/developers/docs/scaling/sidechains/) — ethereum.org; retrieved 2026-10-18.
- [Ethereum accounts](https://ethereum.org/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
