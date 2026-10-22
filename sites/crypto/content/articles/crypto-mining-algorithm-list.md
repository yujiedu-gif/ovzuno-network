---
title: "Crypto Mining Algorithm List: Common Proof-of-Work Algorithms"
description: "Explore a crypto mining algorithm list that groups common proof-of-work algorithms, explains their basic distinctions, and clarifies what algorithm labels mean."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["proof-of-work algorithms", "hashing algorithms", "mining consensus mechanisms"]
author: "editorial_team"
primary_keyword: "crypto mining algorithm list"
owned_question: "Which algorithms are used in proof-of-work crypto mining, and how can they be grouped and distinguished?"
risk_level: "medium"
---

Proof-of-work mining algorithms are computational procedures used to search for results that satisfy a network’s proof-of-work condition. A useful crypto mining algorithm list groups documented procedures by what they do, while keeping each network’s own rules attached. The evidence available for this article supports a general proof-of-work description and a Bitcoin-specific illustration, not a verified catalog of named algorithms across multiple networks. It is therefore more accurate to explain those boundaries than to fill a list with unsupported names.

## What a mining algorithm describes

Proof of work requires computation that is costly to find but straightforward for other nodes to verify against the network’s target. This describes the broad function, not one universal implementation: the work procedure and the target belong to the protocol using them. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

A hashing function is a computational operation that produces a result from input data. In proof-of-work mining, hashing can be part of a repeated search for an output that meets a target. The term *mining algorithm* may be used informally for the hash function, the search procedure built around it, or a larger family of related procedures. Those meanings should not be treated as identical without checking how the network’s documentation uses the term.

Bitcoin provides a concrete example. Its original proof-of-work design varies a nonce in a block until the resulting hash satisfies the network’s target condition. In Bitcoin’s block-header validation, the required condition is a header hash at or below the current target threshold. This describes Bitcoin’s rules; it is not a universal specification for every proof-of-work network. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

A mining algorithm also does not, by itself, specify how all network participants validate blocks or choose between competing histories. It describes a computational part of the system. A full account needs to identify the relevant network and distinguish that work from the other rules governing block acceptance.

## Crypto mining algorithm list by family

A categorized reference should include an algorithm only when reliable protocol documentation establishes its name, function, and network association. The allowed evidence here does not verify a range of named algorithms or support a cross-network family taxonomy. The concise list below is consequently limited to the documented Bitcoin example rather than presented as exhaustive.

### Bitcoin hash-based proof of work

Bitcoin’s proof-of-work search varies a nonce in a block and checks whether the resulting hash meets the network target. In the block-header rule, a valid proof requires a hash at or below the current target threshold. This gives a narrow, protocol-specific description of Bitcoin’s mining work. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

**Family label:** “Hash-based proof of work” describes the role of hashing in the search. It is a functional description, not evidence that every network using hashes follows Bitcoin’s nonce procedure, target representation, or other consensus rules.

**Scope note:** This is one verified example, not an exhaustive crypto mining algorithm list. The evidence does not establish the names, network associations, design features, or current variants of other proof-of-work algorithms, so those entries are omitted rather than inferred.

## How common proof-of-work algorithms differ

A careful comparison starts by specifying what is being compared. At the general level, proof of work uses a computational problem that is costly to solve and straightforward for other nodes to verify. At the Bitcoin-specific level, the evidence identifies a nonce-based search and a block-header hash threshold. These descriptions establish a general purpose and one concrete implementation, but they do not support a comparative ranking of algorithm families. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>) [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

It is also useful to distinguish the work function from the workflow that supplies work to hardware. In Bitcoin’s documented workflow, mining software transforms block-template information into block-header work that hashing hardware searches and reports. That description concerns how the work is prepared and passed along; it does not turn the entire software-and-hardware workflow into the proof-of-work algorithm itself. [source](<https://developer.bitcoin.org/devguide/mining.html>)

This distinction prevents a common category error: a technical description of how a system distributes or searches for work is not necessarily a description of the underlying hash function or every consensus rule. Documentation may describe these pieces together, but readers should identify each layer separately before comparing names.

Algorithm labels alone also do not establish mining cost, security, performance, or hardware suitability. Such conclusions require evidence about a particular network and its implementation. This reference does not rank algorithms or make equipment recommendations; those questions are outside its scope.

## Algorithm, consensus mechanism, and hashing function

A hashing function is a computational building block. A proof-of-work algorithm uses computation to search for a result that satisfies protocol-defined conditions. A consensus mechanism is broader: it coordinates block production, validation, and the way participants select a history.

The Ethereum explanation of proof of work illustrates the distinction by describing proof of work as a Sybil-resistance and block-author-selection component used alongside validation, networking, incentives, and a fork-choice rule. The point here is definitional, not a claim about Ethereum’s current consensus: an algorithm or work component is not the whole mechanism. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

For the same reason, finding a proof-of-work result does not alone describe every condition a block must meet. A protocol’s validation and chain-selection rules are separate parts of the system. When reading an algorithm list, treat the algorithm name as one technical attribute of a network rather than a complete summary of how the network reaches agreement.

## How to verify an algorithm name for a network

For a specific network, use its protocol specification or maintained technical documentation. Check the wording around the algorithm name and determine whether it refers to a hash function, the search procedure that applies it, or a broader proof-of-work component. Then preserve the documentation’s network-specific scope: Bitcoin’s nonce search and header target should not be generalized to protocols whose evidence has not been checked. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

If the documentation describes mining software as well as the work, keep those layers distinct. For example, Bitcoin mining software prepares header work from block-template information, while the proof-of-work condition describes what the searched result must satisfy. The software workflow and the work condition are related, but they answer different questions. [source](<https://developer.bitcoin.org/devguide/mining.html>)

Finally, do not assume that a familiar label establishes a protocol’s current implementation or covers every variant associated with a network. Verify the exact documentation for the network and the term in question. Where the available evidence does not establish an algorithm name, family, or variant, leave that entry unclassified instead of supplying a guess.

## Sources and references

- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
