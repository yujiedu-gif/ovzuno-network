---
title: "Proof of work coin list: networks and verification criteria"
description: "Use this proof of work coin list to review networks that use proof-of-work consensus, understand inclusion criteria, and verify classifications against current"
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["mining_consensus"]
tags: ["proof work coin list"]
author: "editorial_team"
primary_keyword: "proof of work coin list"
owned_question: "Which crypto networks use proof-of-work consensus, and what criteria should readers use to verify that classification?"
risk_level: "medium"
---

A useful proof-of-work coin list identifies the network whose block production uses proof of work, then verifies separately which asset is native to that network. The evidence available for this guide supports a verification method but does not establish named networks and native-asset pairings, so it cannot responsibly supply confirmed coin entries. Readers can use the criteria below to assess a list without treating an unsupported example as fact.

## What qualifies for this proof of work coin list?

Proof of work (PoW) is a consensus model that uses a hard-to-solve but easy-to-verify computational problem to select a participant for block publication. It consumes time, energy, and computational resources. Concrete network rules—including algorithms, difficulty adjustments, and hardware requirements—vary, so the general label alone does not describe a particular network’s implementation. [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>) [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>)

For classification, the primary unit is the **network**, not a coin’s ticker or a token name. A network’s consensus mechanism describes how it selects or authorizes block publication. The asset relationship is a separate question: a proposed list should include an asset as native only when evidence confirms that relationship to the same network being classified. Evidence that a token exists on a network does not establish that the token has a separate PoW consensus.

Use four checks before including an entry:

- **Identify the specific network.** Record its name and the protocol documentation or version being reviewed. Avoid carrying a classification over from another network with a similar name.
- **Confirm PoW’s role.** Find technical documentation that describes computational work as part of block publication or consensus. A mention of mining, hashing, or compatible equipment alone is not enough to establish that role.
- **Verify the asset separately.** Include a coin or native-asset name only if a source establishes its relationship to the network. If the relationship is unclear, omit it or mark it unverified.
- **Resolve design qualifications.** Check whether the source describes a hybrid design, an auxiliary role, a migration, or a prior protocol version. Explain uncertainty rather than flattening a qualified design into an unambiguous label.

This approach separates mechanism from identity. It does not treat PoW as proof of performance, reliability, or any other property beyond the documented consensus design. Nor does a classification imply that a network’s settings will remain unchanged.

## Examples of networks using proof of work

No network can be presented as a verified entry using the allowed evidence for this guide. The permitted claims describe PoW generally and include a Bitcoin-specific chain-selection example, but they do not establish a current network-and-native-asset pairing that would support a named list entry. Leaving the list unpopulated is more accurate than adding familiar names without authorized evidence.

A researcher assembling a list can use a table like this as a recordkeeping format. The fields are criteria to fill, not confirmed entries:

| Field | What to record |
|---|---|
| Network | The specific network and, where relevant, the protocol version checked |
| Consensus basis | A technical source that explains PoW’s role in block publication or consensus |
| Native asset | The asset name only if a source confirms its relationship to that network |
| Source date or version | Enough information for another reader to identify the documentation reviewed |
| Qualification | Any hybrid role, migration, uncertainty, or conflict between sources |

A list’s scope should be visible alongside its entries. If it contains selected examples, call it illustrative. If it claims to be exhaustive, the researcher needs a defensible way to identify the population reviewed and show that every included entry meets the same criteria. The available evidence here does not support a completeness claim.

A source that establishes a network’s PoW design does not, by itself, establish the network’s native asset. Likewise, an asset relationship does not independently prove that the network currently uses PoW. Treat those as two separate findings and retain the supporting source for each.

## How to verify a network’s consensus mechanism

Begin with the network’s own technical documentation or another authoritative technical specification. Locate the explanation of how blocks are proposed, selected, or accepted. Check whether computational work participates in that process, and record the source’s title and date or version. A general explanation of PoW can help define the term, but it cannot substitute for network-specific evidence.

Then distinguish consensus from neighboring technical details. A **hashing algorithm** is a computational method; its presence alone does not establish that a network uses PoW to produce blocks. **Mining hardware compatibility** indicates that equipment can perform a type of work, not that the network currently depends on that work for block production. A token standard concerns token behavior and does not, by itself, establish the host network’s consensus. The classification question is about the specific network’s block-publication rules, not a tool, algorithm, or asset label in isolation.

For hybrid or multi-role designs, describe what the documented mechanism does. If PoW contributes to only one role, or another mechanism shares responsibility, say so instead of implying that the network relies on PoW alone. If sources do not make the roles clear, mark the classification as uncertain and identify the missing information. An unqualified label is not a substitute for resolving an ambiguity.

Next, confirm the asset relationship independently. Make sure the source identifies the asset as native to the same network whose consensus you checked. Similar names, a shared ticker, or a token deployed on a network do not establish that relationship. If the documentation does not settle it, leave the asset field blank or explicitly unverified.

Finally, compare source dates and versions. If one source describes an earlier design and another describes a later one, do not combine them into a single current claim. Record the discrepancy and the protocol versions involved. Where the sources conflict or a relevant upgrade is not documented, mark the entry for further review rather than choosing the more convenient classification.

## Scope limits, changes, and reader checks

This guide is a verification method, not a verified or exhaustive inventory of PoW networks. The authorized evidence does not substantiate named entries and their native-asset relationships. That limitation does not mean that no networks qualify; it means that this article cannot responsibly name them on the evidence supplied. Any separately researched list should state its as-of date and whether it presents examples or claims completeness.

Classifications can become outdated when network documentation changes, an upgrade alters block-production rules, or a migration changes the system being described. Rechecking should therefore be tied to the exact network and the source’s date or version. Difficulty adjustment is one example of a network-specific rule: adjustment intervals and formulas differ across networks, so a general PoW description cannot establish those details for a particular entry. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

The classification has narrow meaning. It does not establish a coin’s safety, legitimacy, liquidity, availability, suitability for mining or investment, or expected future performance. It also does not establish a universal rule for choosing among competing histories. In Bitcoin’s design, nodes select the valid chain with the greatest cumulative proof of work when histories compete, while still enforcing validity rules. That is a Bitcoin-specific example, not a rule to attribute automatically to every network described as PoW. [source](<https://bitcoin.org/bitcoin.pdf>)

Before relying on an entry, ask:

1. Does the source refer to the exact network and protocol version?
2. Does it describe PoW’s role in block publication, rather than merely mention hashing, mining, or hardware?
3. Is the native-asset relationship independently supported?
4. Are hybrid roles, upgrades, source dates, and unresolved conflicts disclosed?
5. Is the list clearly labeled as illustrative or supported by a method for claiming completeness?

If any answer is unclear, label the entry unverified instead of filling the gap with an inference. This consensus check also does not establish jurisdictional, tax, regulatory, fee, yield, availability, security, recovery, or compliance conclusions. Those subjects are outside this reference method and require separate, current evidence specific to the relevant subject and jurisdiction.

## Sources and references

- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
