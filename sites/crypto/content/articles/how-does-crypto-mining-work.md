---
title: "How does crypto mining work: the proof-of-work process"
description: "Learn how does crypto mining work in proof-of-work networks, from transaction selection and block proposals to verification, consensus, and rewards."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["crypto mining work"]
author: "editorial_team"
primary_keyword: "how does crypto mining work"
owned_question: "How does crypto mining work in a proof-of-work blockchain, from transaction selection through block validation and reward, and what does mining contribute to consensus?"
risk_level: "medium"
---

In a proof-of-work blockchain, mining is the process of preparing a candidate block and repeatedly searching for a block-header hash that meets the network’s target. Miners propose blocks; nodes independently check them under that network’s rules. Bitcoin provides a documented example, but its particular mining steps are not a universal specification for every blockchain.

## What mining does in a proof-of-work blockchain

Proof of work is a mechanism in which a participant performs computational work to produce a result that other participants can check. In Bitcoin’s original design, miners vary a nonce in the block until the resulting hash satisfies the network’s target condition. A nonce is a value included in the data being searched; changing it gives the miner another candidate input to hash. The exact fields and rules are protocol-specific, so this explanation uses Bitcoin only where it says so.

Mining constructs and proposes candidate blocks. It does not independently decide that every proposed block is valid or that it will remain in the selected history. A miner’s work is one part of a network process: nodes apply their own validation rules, and the network’s consensus design governs how competing valid proposals are handled.

Keep the roles distinct. Mining software prepares block work and hashing hardware searches for a qualifying result. Nodes check the proposal against applicable rules. These activities may be performed by the same operator, but the functions are conceptually separate. In Ethereum’s block-processing model, for example, a receiving node checks a proposed block and re-executes its transactions to verify the resulting state change. That is an illustration of independent checking, not an example of Ethereum mining: it should not be mistaken for Bitcoin’s proof-of-work mechanism or a universal process.

## How crypto mining work moves transactions into a candidate block

A mining workflow begins with data that can be considered for a block. In Bitcoin, mining software constructs a candidate block and header from transactions and sends header work to hashing hardware. The header is the data searched for a qualifying hash, while the candidate block represents the proposed block and its transactions.

This description does not mean that every transaction known to a miner must be included, or that one transaction-selection policy applies across networks. Which transactions can be proposed, how a candidate is assembled, and what block data may be used are matters of the particular protocol and software. The miner creates a proposal; the network’s validation rules determine whether the proposal is acceptable.

This distinction also prevents a common misunderstanding about “putting transactions on the blockchain.” A miner’s candidate is not yet an accepted ledger update merely because it has been assembled or sent for hashing. The candidate still needs a qualifying proof and must pass the network’s checks. Even then, the block’s place in the selected history depends on the network’s consensus rules.

## How miners search for proof of work

In Bitcoin, software turns candidate-block information into header work that hashing hardware searches. The hardware repeatedly computes hashes while permitted data is varied. The protocol’s target sets the qualifying condition: Bitcoin proof of work requires a block-header hash at or below the current target threshold. This search is not a general-purpose calculation intended to solve arbitrary scientific problems; it is a search for an output that meets the protocol condition.

The search takes computational effort, while another node can check a proposed hash against the target. That is the basic distinction between finding and verifying proof of work: finding involves repeated attempts, while checking asks whether the reported result satisfies the rule. The exact hash function, target representation, and allowed inputs depend on the network. Bitcoin’s nonce-search description should not be generalized to a different protocol without evidence about that protocol.

A qualifying result is a proposal, not a guarantee of acceptance. Mining establishes that the candidate meets the proof-of-work condition, but it cannot substitute for the other requirements that nodes apply. A block that fails an applicable rule does not become valid simply because its hash meets the target.

## How the network checks a mined block

Once a miner has a candidate with qualifying proof, the block can be proposed to the network. Nodes check the proof and apply their relevant block and transaction rules independently. The miner’s announcement therefore asks the network to consider a block; it does not compel nodes to accept it.

For Bitcoin, when histories compete, nodes select the valid chain representing the greatest cumulative proof of work. Both parts of that description matter: the chain must be valid under node rules, and cumulative work is used when valid histories compete. Work alone does not make an invalid block valid.

This can produce a practical distinction between a block being found and a block remaining in the selected history. Bitcoin network participants may temporarily observe competing block proposals; timing and propagation can affect which branch an individual node sees first. Continued proof of work can resolve the branch choice under Bitcoin’s documented rule. The exact handling of competing proposals and the meaning of finality depend on the particular network, so “mined” should not be read as “irreversible” or as a promise that every node will accept the block.

## When miners receive rewards—and what the process does not guarantee

Rewards are determined by the protocol and its rules. The evidence supporting this explanation establishes the Bitcoin proof-of-work search and candidate-block workflow, but it does not establish a specific reward amount, payout schedule, or reward formula. Those details cannot be inferred from the act of finding a qualifying hash, and they should not be treated as the same across networks.

Mining by itself also does not establish profitability, guaranteed income, or a particular security outcome. A miner may propose a block without every node accepting it, and an accepted block’s status in a competing-history situation depends on the network’s consensus rules. For a reader tracing the lifecycle, the useful sequence is: candidate work is constructed, hashing searches for a qualifying result, a block is proposed, nodes check it, and the protocol determines how it fits into the selected history. Mining contributes candidate blocks and proof of work; independent validation and network-specific consensus rules determine what the network accepts.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
