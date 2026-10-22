---
title: "Apa Itu Proof of Work? How Blockchain Consensus Uses Computation"
description: "Apa itu proof of work? Learn how miners use computation to propose blocks, how networks verify the result, and what trade-offs the design involves."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["apa itu proof work"]
author: "editorial_team"
primary_keyword: "apa itu proof of work"
owned_question: "What is proof of work, how does it let a blockchain network agree on transaction history, and what are its main trade-offs?"
risk_level: "medium"
---

Proof of work (PoW) is a block-proposal method in which participants search computationally for a result that meets a network’s rule, and other participants verify that result before considering the proposed block. It helps a network choose among competing transaction histories, but it does not replace the validity checks that determine whether blocks and transactions follow protocol rules. The details differ by blockchain; the explanation below uses Bitcoin for the core example and does not treat its rules as universal.

## What Is Proof of Work in a Blockchain?

A blockchain is a shared transaction history maintained under rules followed by network participants. When participants may produce competing versions of that history, the protocol needs a way to decide which valid history to follow. Proof of work is one way to make block proposals depend on a computational result that can be checked by others.

In Bitcoin, proof of work concerns a block header: its hash must be at or below the current target threshold. A hash is the output of a calculation applied to data; a qualifying hash is one that meets the target rule. This requirement defines what counts as sufficient work for a proposed block under Bitcoin’s current target. Other networks can use different proof-of-work rules, so Bitcoin’s specific test should not be assumed to describe every network.

The term “mining” is often used for the activity that produces candidate blocks, but proof of work is not the entire job of a blockchain. A miner can construct and propose a candidate block; network nodes independently apply block and transaction validity rules. A successful proof does not make an invalid block valid, and a proposed block is not automatically part of the history all participants follow.

This distinction is important because two questions are involved. First, does the proposal meet the proof-of-work condition? Second, does the block comply with the network’s other rules? The protocol’s agreement process depends on both. Proof of work helps determine which history is selected among valid alternatives; it is not a substitute for checking validity.

## How the Proof-of-Work Process Reaches Agreement

The basic process can be understood as a sequence of proposals, search, and independent checks:

1. **Prepare a candidate.** Mining software assembles a candidate block and header from transactions and prior block information. At this stage, the block is a proposal, not an accepted addition to the shared history.
2. **Search for a qualifying result.** The participant repeatedly computes hashes while changing candidate data. In Bitcoin’s original design, the miner varies a nonce in the block until the resulting hash meets the network target. Each attempt is another search result; most do not meet the target.
3. **Submit a qualifying proposal.** When a result meets the target, the candidate can be presented to the network. Finding the result does not itself settle whether the transactions and block structure follow all applicable rules.
4. **Verify independently.** Other nodes can check the submitted proof against the target and apply their own validity rules to the block and its transactions. A check of a supplied result is different from searching for one: verification tests whether the result qualifies rather than reproducing the search.
5. **Resolve competing histories under protocol rules.** If valid histories compete, Bitcoin nodes select the valid chain representing the greatest cumulative proof of work. “Cumulative” means the work represented across the competing history, not simply which block arrived first. The chain still has to be valid; accumulated work cannot override rule violations.

Participants may temporarily see competing block proposals. In Bitcoin’s proof-of-work model, timing and propagation can affect which branch a node sees first, while continued proof of work can resolve the branch choice under the documented rule. This is why a newly proposed block should not be described as instantly or permanently settled. The selected history is determined by the network’s rules as participants observe and validate competing work.

## Why Computation Is Used to Propose Blocks

The design relies on an asymmetry: searching for a result that satisfies a target takes repeated computation, while checking a proposed hash against the target is comparatively direct. In Bitcoin, nodes can determine whether the block-header hash is at or below the current threshold. This makes a proposal computationally costly to produce and easier for other participants to verify, without requiring every verifier to repeat the same search.

That asymmetry contributes to how Bitcoin handles competing histories. Nodes select the valid chain with the greatest cumulative proof of work. Replacing earlier history therefore requires constructing an alternative history with sufficient work and catching up with the selected one. As additional blocks build on a history, changing it requires addressing the cumulative work represented by that history, rather than merely presenting a different block.

This mechanism should not be overstated. Work is evidence that a candidate met a computational condition; it does not establish that the transactions are legitimate under the rules, that a miner acted honestly in every respect, or that a particular history can never be reorganized. Nodes must still validate blocks, and a miner’s proposal is not guaranteed to be accepted or remain in the selected chain. The protocol describes a selection rule, not an unconditional promise about every real-world outcome.

## Security Assumptions and Design Trade-offs

Proof of work’s role is bounded by the network rules and the system around them. In Bitcoin, chain selection concerns valid chains and cumulative work, while nodes separately enforce transaction and block rules. Assessing a specific security question also requires examining the relevant network and circumstances; the existence of a proof-of-work rule alone does not establish a universal level of protection.

Distribution of block-production power is one relevant consideration, but it should not be inferred from a simple count of nodes. NIST’s high-level blockchain discussion says independently operated nodes can reduce the ability of one bad actor to affect consensus as their number increases, while also cautioning that node count alone does not show operator independence, geographic diversity, implementation diversity, or block-production power. That is a general architectural observation, not evidence that every network is equally distributed or resilient.

The computational design also consumes resources. A general proof-of-work model uses time, energy, and computational cycles, but those broad characteristics do not establish a particular network’s energy use, the amount of hardware needed, or the cost of operating it. Those claims would require evidence scoped to the network, equipment, and operating conditions. Detailed hardware selection and mining operations are separate topics and are not needed to understand the consensus role.

Nor does a target-based proof alone describe all possible attacks or recovery behavior. A security assessment must stay tied to the particular protocol and threat being considered rather than converting a general design description into an assurance of safety. This explainer therefore makes no numerical energy or security estimate and no claim that proof of work eliminates attacks.

## Proof of Work Compared With Other Consensus Designs

Proof of work uses computational search to qualify block proposals. A different design, proof of stake, uses cryptocurrency committed as stake, with stake influencing a participant’s consensus weight. These labels identify different resource and participation rules; they do not, by themselves, establish which system is safer, cheaper, or more decentralized.

Specific protocols can differ in how participants are selected, how proposals are checked, how competing histories are handled, and what happens when rules are not followed. A useful comparison therefore requires looking at the rules and assumptions of the named networks rather than treating either category as a single universal implementation.

For the question “what is proof of work?”, the essential point is that computational effort helps qualify block proposals and provides a basis for choosing among competing valid histories. The network’s nodes still verify the proof and enforce the other rules. That separation—proposal through work, followed by independent validation and protocol-based history selection—is the core of the mechanism.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Proof-of-Work](https://ethereum.org/developers/docs/consensus-mechanisms/pow) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
