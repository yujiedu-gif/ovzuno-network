---
title: "Simple explanation of cryptocurrency mining: how proof of work works"
description: "A simple explanation of cryptocurrency mining: learn how proof-of-work miners propose blocks, compete to meet network rules, and support consensus."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["simple explanation cryptocurrency mining"]
author: "editorial_team"
primary_keyword: "simple explanation of cryptocurrency mining"
owned_question: "How does cryptocurrency mining work in a proof-of-work blockchain, and how does it help the network agree on new blocks?"
risk_level: "medium"
---

For beginners, cryptocurrency mining is the block-proposal process used by proof-of-work networks: miners assemble candidate blocks and search for a result that meets a protocol-defined condition. Other network participants check the proposed block against the rules, and the network’s consensus process determines how valid blocks fit into its shared history. Mining supports agreement about block order, but it does not make an invalid block valid or guarantee absolute security.

## What cryptocurrency mining means in proof-of-work networks

Mining is specific to proof-of-work systems; it is not a universal process used by every cryptocurrency network. In a general proof-of-work model, a participant searches for a computational result that is costly to find but comparatively straightforward for others to verify. The precise algorithm and rules depend on the protocol. **[source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>)**

The word “mining” can sound as if miners process every transaction or decide on their own what the network accepts. A more accurate starting point is that mining proposes candidate blocks. The network’s rules determine whether a candidate is valid, while its consensus process determines how valid proposals contribute to the accepted history.

Proof of work is also distinct from other consensus approaches. This article focuses on the proof-of-work model and uses Bitcoin for a specific workflow example where needed. Bitcoin’s details illustrate one protocol; they should not be treated as rules that every cryptocurrency follows.

## How miners turn pending transactions into a candidate block

A candidate block is a proposed package of transactions together with information that connects it to earlier blockchain history. The transactions provide the activity the candidate would record; the block structure provides the proposed place for that activity in the chain.

In Bitcoin’s mining workflow, software constructs a candidate block and block header from transactions, then sends header work to hashing hardware. **[source](<https://developer.bitcoin.org/devguide/mining.html>)** This is a Bitcoin-specific description. Other networks may define their blocks, transaction selection, and mining software differently.

The candidate is a proposal, not a final record. A miner’s choice to include a transaction does not by itself establish that the transaction is valid or that it has become part of the accepted history. The proposal must be checked under the network’s rules. This is why it is useful to separate the miner’s work of assembling and proposing a block from the network’s work of checking it.

The same distinction applies to the block as a whole. A qualifying proof of work does not excuse a candidate from other protocol requirements. Work and validity answer different questions: the proof shows that the required computational condition was met, while validation checks whether the block and its contents follow the network’s rules.

## How proof of work makes miners compete

After a candidate has been prepared, proof-of-work mining searches for a result that meets a condition defined by the protocol. The general proof-of-work model uses a computational problem that is hard to solve but easy for other participants to verify. **[source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>)** “Easy to verify” is relative to the search: checking a submitted result does not require performing the same open-ended search that produced it.

A simple way to picture the process is as repeated attempts. The miner changes data used in the candidate’s proof-of-work calculation and checks whether the resulting value qualifies under the protocol’s condition. If it does not qualify, the attempt does not provide an acceptable proof. If it does, the miner has a result to submit with the proposed block—but the block still needs to meet the network’s other rules.

This search is not a vote in which a miner can simply declare a preferred transaction history. The network defines what counts as a qualifying result and what makes a block valid. A proposal that fails those checks cannot become valid merely because work was expended on it.

The model also explains why no single mining description covers all networks. Protocols can set different proof conditions and define their block and validation rules differently. The useful general idea is the relationship between a computationally demanding search and a result that other participants can check; the exact implementation belongs to each protocol.

## What happens when a miner proposes a valid block

Once a miner has a candidate with a qualifying proof, the proposal can be considered by the network. Participants check whether the proof meets the relevant condition and whether the block follows the protocol’s validity rules. Acceptance is therefore conditional: a miner’s submission is not enough on its own, and proof of work is only one part of the checks.

If a valid candidate fits the network’s current history, it can become part of the history the network follows. But networks may face competing histories, so a protocol also needs rules for deciding which valid history to treat as preferred. In Bitcoin’s design, nodes select the valid chain representing the greatest cumulative proof of work when histories compete. **[source](<https://bitcoin.org/bitcoin.pdf>)** This chain-selection description is Bitcoin-specific; other protocols may resolve competing proposals differently.

That example separates several stages that are easy to conflate. A miner first proposes a block. The network checks it for validity. If valid histories compete, the protocol’s selection rules determine which history is preferred. Calling a block “mined” describes the proposal and proof-of-work process; it does not by itself mean the block has passed every validity check or become part of the selected history.

For readers thinking about transaction confirmation, the practical distinction is that inclusion in a proposed block is not the same as a network-wide conclusion about the history. The protocol’s validation and consensus rules govern that conclusion. The details of confirmation and finality are network-specific, so this general explanation does not assign one universal level of assurance to all mined blocks.

## Why mining supports consensus—and what it does not guarantee

Consensus is the process by which network participants coordinate on an accepted history. In Bitcoin’s proof-of-work design, the selected valid chain represents accumulated work, and replacing accepted history requires rebuilding work and catching up. **[source](<https://bitcoin.org/bitcoin.pdf>)** This helps explain how proof of work supports agreement about block order: changing the history is not simply a matter of proposing a different version; the competing history must satisfy the system’s selection rules.

That mechanism is not an absolute security guarantee. The cited Bitcoin description explains the chain-selection model, not a promise that every possible attack or operational failure is impossible. Nor does computational work override validity: nodes still apply protocol rules, and an invalid block does not become acceptable just because it is associated with work.

Mining also should not be used as a catch-all term for every task in a blockchain. Here it means proposing candidate blocks through proof of work. Validation means checking proposed transactions and blocks against rules. Consensus concerns how participants coordinate on the history they accept. These functions relate to one another, but keeping them distinct prevents the mistaken impression that miners can unilaterally decide what the network records.

The short version is: miners assemble candidate blocks, search for a proof that meets the network’s condition, and propose the result; participants check the proof and block; and protocol-specific consensus rules determine how valid proposals become part of the shared history. Bitcoin provides a concrete example of this model, but the details vary across proof-of-work protocols, and mining is not a universal process for all cryptocurrency networks.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
