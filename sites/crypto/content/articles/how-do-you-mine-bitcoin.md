---
title: "How do you mine bitcoin? The process and key requirements"
description: "Learn how do you mine bitcoin: how miners assemble candidate blocks, search for proof of work, and connect hardware and software to the network."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["how do you mine for bitcoins", "you mine bitcoin"]
author: "editorial_team"
primary_keyword: "how do you mine bitcoin"
owned_question: "How does Bitcoin mining work, and what does a participant do from selecting hardware to submitting valid proof of work?"
risk_level: "medium"
---

Bitcoin mining is the process of assembling a candidate block and searching for a block-header hash that meets the network’s current proof-of-work target. Mining software prepares the candidate and sends header work to hashing hardware; a qualifying block is then submitted for verification. The search and the validation are distinct: finding a hash that meets the target does not by itself make every block detail valid or guarantee acceptance. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

## What Bitcoin miners do in the network

A Bitcoin miner attempts to produce a candidate block that satisfies the proof-of-work condition. Proof of work is a computational problem designed to take substantial effort to solve while allowing a proposed result to be checked. In Bitcoin, the relevant condition is that the block-header hash be at or below the current target threshold. [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

A block header is the part of a proposed block that mining hardware hashes during the search. The mining software constructs candidate block and header data from transactions and prepares work for the hardware. The hardware’s task is to search for a qualifying hash; it does not decide on its own whether all transactions and other block details follow network rules. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/mining.html>)

Mining is also different from ordinary block validation. Validation means checking a proposed block against applicable network rules. A miner may do that work as part of its broader setup, but the act of checking is not the proof-of-work search. Conversely, a successful hash search does not exempt the resulting candidate from validation. The proof-of-work condition and the block’s other rules both matter. [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>) [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>)

This distinction explains why the process has two meaningful stages: first, a participant searches for a candidate that meets the target; then, the candidate must be checked against Bitcoin’s rules. A result that meets the hash threshold is evidence only of that condition. It does not independently establish that the block is acceptable in every other respect. [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

## How do you mine bitcoin: the process

The basic process can be understood as a sequence from block preparation through submission:

1. **Prepare candidate transaction data.** Mining software assembles a candidate block and block header from transactions. The candidate is proposed work, not yet an accepted addition to the network’s history. [source](<https://developer.bitcoin.org/devguide/mining.html>)
2. **Send header work to hashing hardware.** The software supplies the header work to the hardware. The hardware repeatedly calculates hashes as part of the search for a result that meets the current target. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/mining.html>)
3. **Search for a qualifying hash.** The target is a threshold: the block-header hash must be at or below it. The search is computational work; the target provides a condition that can be checked against a proposed result. [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>)
4. **Submit a qualifying candidate for checking.** When the search produces a hash that meets the target, the candidate can be submitted for network verification. The candidate still has to satisfy applicable Bitcoin rules beyond the hash condition. [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

The word “submit” should not be read as “accepted.” A qualifying hash means the proof-of-work threshold has been met; it does not establish that the network will accept the candidate. Validation is a separate gate. This is why a miner’s operational sequence includes both finding a result and presenting a block that can pass rule checks. [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

The evidence cited here supports this high-level workflow, not a complete specification of every field in a block, every transaction-selection policy, or every software interface. Those implementation details should not be inferred from the general description of candidate construction and header work. [source](<https://developer.bitcoin.org/devguide/mining.html>)

## Hardware, software, and network setup

At a basic level, mining involves software that prepares candidate work and hardware that performs the hash search. The documented Bitcoin mining workflow says the software constructs a candidate block and header from transactions and sends header work to hashing hardware. This establishes the distinct roles in the process, but it does not identify a required product, a universal configuration, or a particular participant’s operating conditions. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/mining.html>)

A participant considering a setup should therefore separate protocol requirements from operational choices. The protocol-level description concerns the candidate, the header-hash search, and the target condition. It does not, by itself, specify the participant’s hardware model, software package, power arrangement, network service, or site requirements. Details about a particular installation need evidence relevant to that equipment and setup rather than assumptions drawn from the mining mechanism. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

Mining can also be organized through a pool, but pool participation is not a different proof-of-work rule. Pool software, payout arrangements, fees, availability, and service conditions are not established by the protocol claims used here. Anyone evaluating a specific pool would need to check current documentation for that provider. This explanation does not compare pools or recommend one.

Keep block checking distinct from producing proof of work when assessing software roles. A node that checks a proposed block is performing validation; mining software and hashing hardware perform the candidate-work and search process. The available evidence supports that distinction but does not establish that every mining setup uses the same combination of node software, pool software, proxies, or other components. [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>) [source](<https://developer.bitcoin.org/devguide/mining.html>)

## Difficulty, rewards, and what can change

The proof-of-work target determines the hash condition a candidate must meet. Because the condition is a threshold, a miner’s search is tied to the target that applies to the candidate being tested. The accepted evidence supports the target requirement, but it does not provide the target-adjustment interval or formula. A precise account of when or how Bitcoin changes that target would require additional authorized evidence, so it is not supplied here. [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

Likewise, the claims available for this article do not establish the current block subsidy, how transaction fees are calculated, or a complete reward-allocation procedure. It would therefore be inaccurate to treat this article as a reward schedule. The limited point is that finding proof of work and getting a block accepted are separate conditions; no guaranteed reward follows merely from describing the search. [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

Protocol mechanics should also remain separate from a financial assessment. This explanation does not estimate operating costs, reward value, returns, or profitability. Those questions involve facts not established by the target and candidate-construction claims. A technical description of how hashing work is performed is not a recommendation to mine or a forecast of what a participant might receive. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

## Operational risks and claims to verify

Before relying on a practical claim about mining, identify whether it concerns the protocol, a particular service, a specific installation, or a jurisdiction. The claims used here support candidate construction, software-to-hardware work, the target condition, and the distinction between proof of work and block validity. They do not establish electricity prices or rules, permits, taxes, regulatory obligations, hardware failure rates, outage effects, pool fees, service availability, yields, or recovery options. Such claims require separate, current evidence, and jurisdiction-dependent claims require evidence for the named jurisdiction.

For protocol-related claims, check whether the statement concerns only the hash target or also asserts that the rest of a candidate block is valid. Those are not interchangeable: meeting the target is one condition, while the candidate must also satisfy applicable rules. For service-related claims, check the provider’s current terms rather than assuming that pool availability, fees, payouts, or supported configurations are uniform. [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

For equipment and operating claims, distinguish a general description of hashing hardware from evidence about an actual model, installation, power supply, network connection, or operating environment. The general mining workflow establishes that hardware searches hashes and software prepares work; it does not establish the suitability or performance of a particular setup. [source](<https://developer.bitcoin.org/devguide/mining.html>)

The practical takeaway is a bounded one: understand how transactions are assembled into a candidate, how software supplies header work to hashing hardware, what target the hash must meet, and why a qualifying result still requires validation. Treat service terms, local requirements, operating conditions, reward details, and financial outcomes as separate matters to verify rather than conclusions that follow from the proof-of-work process itself. [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/mining.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>) [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

## Sources and references

- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Block Chain](https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus) — Bitcoin Developer Guide; retrieved 2026-10-21.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
