---
title: "Proof of work crypto list: networks and inclusion criteria"
description: "Use this proof of work crypto list to identify example networks, understand the inclusion criteria, and verify whether proof of work is still current."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["proof work crypto list"]
author: "editorial_team"
primary_keyword: "proof of work crypto list"
owned_question: "Which crypto networks use proof of work, and what criteria determine whether a network belongs on a current list?"
risk_level: "medium"
---

A network belongs on a current proof-of-work crypto list only when proof of work has a documented role in its active block-production or chain-selection process. The evidence available for this article supports Bitcoin as an example and Ethereum as a former, not current, proof-of-work network. These are technical classifications, not rankings or judgments about profitability, security, or asset value.

## What qualifies a network for this list?

Proof of work is a consensus approach in which a participant searches for a computational result that is costly to find but straightforward for other network participants to verify. This article uses a narrow inclusion test: proof of work must be part of the network’s active process for producing blocks or deciding which competing history to follow. A token’s name, a mining-related service, or a network’s historical design is not enough on its own. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

The distinction between a network mechanism and an associated service matters. For example, a mining pool may use shares that meet a pool-assigned target but usually do not meet the harder network target. Pool participation therefore does not, by itself, establish that proof of work is the network’s consensus or block-selection mechanism. [source](<https://developer.bitcoin.org/devguide/mining.html>)

The permitted evidence supports a short list rather than a broad catalog. It identifies Bitcoin’s proof-of-work design and provides an explicit note that Ethereum no longer uses proof of work. It does not substantiate current classifications for additional networks. Omitting other names is an evidence limitation, not a claim that no other networks use proof of work.

A current list should state when its classifications were checked and what each entry’s evidence establishes. A source describing an older protocol state cannot automatically establish a network’s present mechanism. Where current, network-specific documentation is unavailable or unclear, the responsible choice is to leave the classification unconfirmed rather than infer it.

## Proof of work crypto list: example networks

- **Bitcoin (BTC):** Bitcoin nodes select the valid chain representing the greatest cumulative proof of work when histories compete. Nodes also enforce block and transaction validity rules; work does not make an invalid block valid. This makes Bitcoin a supported proof-of-work example, with the scope limited to the chain-selection design described by the evidence. [source](<https://bitcoin.org/bitcoin.pdf>)

- **Ethereum (ETH): not a current proof-of-work example.** Ethereum’s former proof-of-work explanation describes a probabilistic process in which simultaneous valid blocks can create temporary forks and later blocks increase confidence in one history. The evidence states that Ethereum switched to proof of stake in 2022 and no longer uses proof of work. Its past mechanism should not be used to qualify it for a current proof-of-work list. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pow>)

Ethereum’s current proof-of-stake finality provides a useful contrast. Validator votes on checkpoint blocks distinguish finalized history from blocks that are included but not finalized. This is a different documented mechanism from treating the valid chain with the greatest cumulative proof of work as the selected history. The comparison concerns the described protocols; it does not classify other proof-of-stake networks. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

This reference list is selective. It includes Bitcoin because the permitted evidence supports its proof-of-work chain-selection role, and it mentions Ethereum to prevent a historical mechanism from being mistaken for a current one. It does not assert that these are the only networks that have used or currently use proof of work. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pow>)

## How to verify a network’s current consensus

Start with documentation specific to the network, rather than a general explanation of proof of work. Look for protocol rules or technical documentation that describes how blocks are produced and how competing histories are resolved. A general consensus glossary can define a mechanism, but it cannot establish that a particular network currently uses it.

Next, identify the mechanism’s exact role. The relevant questions are whether proof of work contributes to block production, whether it helps select among competing histories, or whether the source discusses something narrower, such as a pool’s work-submission process. A pool share can measure work against a pool target without being a network-valid block, so a pool document alone may not prove the network’s consensus classification. [source](<https://developer.bitcoin.org/devguide/mining.html>)

Then check the evidence’s date and scope. A statement about a former protocol is evidence of historical use, not necessarily current use. Ethereum demonstrates this distinction: documentation about its former proof-of-work finality must be read alongside the stated change to proof of stake in 2022. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pow>)

For each entry, record the source and the date it was checked. Recheck the classification when documentation reports a protocol upgrade, migration, or other consensus change. If the material does not clearly connect proof of work to current block production or chain selection, describe the status as unverified rather than presenting an uncertain classification as fact.

Finally, keep the claim no broader than the evidence. Bitcoin’s supported description is that nodes select the valid chain representing the greatest cumulative proof of work when histories compete. That does not establish every operational detail of mining or every condition under which a node follows a chain. [source](<https://bitcoin.org/bitcoin.pdf>)

## Proof of work versus other consensus mechanisms

A network’s consensus mechanism is its rules for arriving at an agreed history or state. Proof of work and proof of stake are distinct approaches, and a classification should identify the one the active network documentation describes. A network’s name or past use of a mechanism cannot substitute for checking its current process.

The Bitcoin example centers on valid competing histories and cumulative proof of work: nodes select the valid chain with the greatest cumulative work. Validity remains essential; additional work does not turn an invalid block into a valid one. This qualification prevents the shorthand “most work wins” from being mistaken for a rule that overrides the network’s validity checks. [source](<https://bitcoin.org/bitcoin.pdf>)

The Ethereum contrast illustrates why current status matters. Its former proof-of-work explanation describes temporary forks and probabilistic finality, but the same evidence states that Ethereum switched to proof of stake in 2022. Its proof-of-stake finality uses validator votes on checkpoint blocks to distinguish finalized history from merely included blocks. These descriptions support excluding Ethereum from a current proof-of-work list; they do not establish a universal rule for every proof-of-stake network. [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pow>) [source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>)

Hybrid or multi-component systems need especially careful treatment. If a source identifies proof of work as one component but does not explain whether it produces blocks or determines the selected history, a bare classification may obscure the mechanism’s actual role. A list should state the documented function and avoid assigning a broad label beyond what the network-specific evidence supports.

## What this list does not establish

A proof-of-work classification is not evidence of mining profitability, network security, or an asset’s value. The supported claims here concern consensus and chain selection, not financial outcomes. Inclusion in a technical reference list should not be read as a recommendation or comparison of assets.

This article also makes no claims about legal status, regulation, taxes, mining availability, fees, yields, recovery, or compliance. Those topics require separate, relevant evidence and may depend on jurisdiction or operating conditions. The list is a mechanism reference only: verify each network’s current documentation, preserve the source date, and treat any unsupported classification as unresolved.

## Sources and references

- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Proof-of-Work](https://ethereum.org/developers/docs/consensus-mechanisms/pow) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
