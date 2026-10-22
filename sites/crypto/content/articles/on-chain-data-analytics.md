---
title: "On chain data analytics across interoperable blockchains"
description: "Learn how on chain data analytics can compare blockchain activity across interoperable networks, including data alignment, attribution limits, and interpretation."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["cross_chain_interoperability"]
tags: []
author: "editorial_team"
primary_keyword: "on chain data analytics"
owned_question: "How can on-chain data analytics help people compare activity across interoperable blockchains, and what limits affect cross-chain conclusions?"
risk_level: "medium"
---

On-chain data analytics can help compare activity across interoperable blockchains by organizing observable records into comparable fields and examining related events across networks. The results are only as reliable as the data coverage, definitions, and attribution assumptions behind them: similar-looking records are not necessarily equivalent events, and a link between records does not by itself establish who acted or why.

## What cross-chain data analytics covers

On-chain data refers here to records exposed by a blockchain, such as transactions and other network-specific data. A blockchain transaction becomes part of a shared ledger after authorization, validation under that network’s rules, grouping into a block, and a consensus decision. The relevant checks, block structures, consensus, and finality rules differ by network. Consequently, a record’s meaning and status must be interpreted in the context of the chain that produced it. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

Analysis within one network can use that network’s own record structure and conventions. Cross-chain analysis adds a comparison step: an analyst selects records from separate networks and asks whether particular fields, events, or patterns can be meaningfully compared. A schema is a structured description of data fields and record types. For example, the documented Google Cloud Ethereum analytics schema separates blocks, transactions, receipts, logs, decoded events, token transfers, traces, and selected account-state records into queryable tables. That is an example of one documented Ethereum dataset, not a universal model for all chains. [source](<https://docs.cloud.google.com/blockchain-analytics/docs/schema>)

Interoperability can produce related activity on multiple networks, but it does not make their ledgers or records identical. The BIS analysis of cross-chain bridges identifies added smart-contract security risks, costs, and delays when connecting stablecoin records on separate blockchains; those findings concern the analysis described in that paper and should not be generalized to every bridge implementation. For analytics, the key distinction is that records on separate chains remain records in their respective network contexts. [source](<https://www.bis.org/publ/work1335.pdf>)

## Aligning records from different blockchains

Before comparing activity, decide which fields have comparable meanings. Networks can differ in transaction structure, event representation, identifiers, timestamps, and rules for when a record is considered confirmed or final. The evidence here establishes that transaction validation and consensus rules differ by network; it does not provide a universal mapping of formats or finality conventions. A cross-chain dataset therefore needs network-specific documentation rather than an assumption that one chain’s fields translate directly to another’s. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

Normalization means transforming selected records into a shared analytical format—for example, assigning consistent column names or units. It helps make a comparison possible, but it does not prove that records represent equivalent actions. A field labeled “transaction” in two datasets might describe different kinds of activity or include different stages of processing. Analysts should preserve the original chain and source fields alongside normalized values so that comparisons can be traced back to their inputs.

Coverage is another constraint. A dataset may include some record types while omitting others, and a queryable schema is not itself evidence that every event or network is represented. The Ethereum analytics example distinguishes records such as transactions, logs, token transfers, and traces, illustrating why the chosen data type matters. Reports should state which chains and record classes were included, the relevant time range, and any known exclusions. [source](<https://docs.cloud.google.com/blockchain-analytics/docs/schema>)

Timing and status also need explicit treatment. A record included in a block is not automatically equivalent to one considered final under another network’s conventions. Since consensus and validation rules vary, cross-network comparisons should state the status threshold used for each chain instead of treating timestamps or confirmation labels as interchangeable. The allowed evidence does not establish a universal freshness interval or finality threshold, so neither should be implied. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

## Linking activity without overstating attribution

Attribution is the process of associating a record or address with an actor, organization, or activity category. Directly observable data—such as a transaction identifier or an address recorded by a particular network—should be distinguished from an inferred connection between records. A reference standard’s draft URI proposal describes common explorer lookup objects as transactions by hash, blocks by hash or height, and addresses. These identifiers support locating records; they do not, on their own, establish that two addresses have the same owner or that a person intended a particular outcome. The proposal is a draft and does not establish universal adoption or identical explorer formats. [source](<https://bitcoin.org/bip/122/>)

A cross-chain relationship can be plausible without being uniquely determined. Two records may appear related because they occur near each other in time or have matching characteristics, but those observations alone do not establish common control, purpose, or causation. In the evidence available for this article, there is no universal attribution rule that proves identity across networks. Treat links as analytical hypotheses unless the method has independent, documented support.

A useful report makes that distinction visible. It can label links as directly observed, rule-based, or inferred; explain the criteria used; and state what evidence would change the classification. If a method uses confidence categories, define what each category means and avoid presenting a confidence label as proof. The point is not to eliminate uncertainty, but to keep readers from mistaking an analytical join for an established identity.

## Interpreting cross-chain metrics carefully

Metrics such as transaction counts or observed flows are meaningful only when their definitions and coverage are clear. A count might refer to transactions, logs, decoded events, token transfers, or another record type; these categories are not interchangeable. The documented Ethereum schema’s separation of such records is a reminder to name the unit being counted and the source fields used. [source](<https://docs.cloud.google.com/blockchain-analytics/docs/schema>)

Totals can also be affected by how related records are grouped. An event recorded on one network and a related event recorded on another may both be valid observations, but adding them together could count distinct records rather than a single underlying action. Conversely, collapsing records into one inferred activity can conceal uncertainty or exclude relevant events. The available evidence does not prescribe a general deduplication method; any deduplication rule should therefore be reported as an analytical choice, not as an inherent property of interoperable records.

Finally, observed activity is not a direct measure of user intent, economic value, or cause. A data comparison can describe what records were selected and how they relate under stated rules. Without further evidence, it cannot establish why an actor produced them or what broader consequence followed. Similarly, the BIS discussion of cross-chain risks supports a bounded observation about risks, costs, and delays in the studied context—not a conclusion about the safety or performance of every system. [source](<https://www.bis.org/publ/work1335.pdf>)

## Questions to resolve before relying on results

Before using a cross-chain comparison, ask:

- Which networks, record types, time ranges, and exclusions are represented?
- What does each normalized field mean on each source chain, and which original fields remain available for review?
- How is record status handled when networks use different consensus and finality rules? [source](<https://csrc.nist.gov/pubs/ir/8202/final>)
- Which links are directly observable, and which depend on assumptions about identity, timing, or activity?
- How are counts and flows defined, and what rules—if any—group or remove related records?
- Can another reviewer trace a reported result back to its source records and reproduce the stated method?

These checks help frame the proper use of on-chain data analytics: cross-chain comparisons can organize and examine records from interoperable networks, but their conclusions remain bounded by network-specific data, selected definitions, and the strength of the attribution method. A careful result states those limits rather than treating a normalized dataset as a complete or definitive account.

## Sources and references

- [Tokenomics and Blockchain Fragmentation](https://www.bis.org/publ/work1335.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [BIP 122: URI Scheme for Blockchain References and Exploration](https://bitcoin.org/bip/122/) — Bitcoin Improvement Proposals; retrieved 2026-10-18.
- [Blockchain Analytics Dataset Schemas](https://docs.cloud.google.com/blockchain-analytics/docs/schema) — Google Cloud; retrieved 2026-10-19.
