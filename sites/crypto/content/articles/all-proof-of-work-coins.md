---
title: "All proof of work coins: criteria for a scoped reference list"
description: "Explore all proof of work coins through clear inclusion criteria, scope limits, and distinctions between current, hybrid, and historical proof-of-work networks."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["all proof work coins"]
author: "editorial_team"
primary_keyword: "all proof of work coins"
owned_question: "Which cryptoassets are associated with networks that currently use proof-of-work consensus, and what criteria determine inclusion in a reference list?"
risk_level: "medium"
---

For readers seeking all proof-of-work coins, a reliable answer is a dated, criteria-based reference—not a timeless master list. Classify each candidate by the active consensus rules of its specific network, identify whether the asset is native to that network or merely associated with it, and separate current proof of work from hybrid, partial, transitioned, and historical cases. The evidence available for this article supports explaining Bitcoin’s mechanism, but does not establish a current roster of other networks. It therefore cannot substantiate an exhaustive list of all proof-of-work coins.

## What counts as a proof-of-work coin?

Proof of work (PoW) is a consensus mechanism in which a network requires computational work as part of block proposal or history selection. A cryptoasset belongs in a current-PoW reference only when the relevant network’s active rules use PoW in that role. A name, ticker, past mining activity, or broad project description does not by itself establish the current consensus design.

Bitcoin is a useful, network-specific example. Its proof of work is produced by varying a nonce in a block until the resulting hash satisfies the network’s target condition. For Bitcoin block-header validation, the hash must be at or below the current target threshold. This describes Bitcoin’s rules; other networks can use different algorithms, targets, header fields, and adjustment rules. A Bitcoin example cannot be assumed to describe every network labeled PoW. [source](<https://bitcoin.org/bitcoin.pdf>) [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

A reference also needs to define what its entries name. It might list networks, native assets, or both, but should state the relationship clearly. A network’s consensus is a property of its protocol rules, not automatically of every token that can be represented or transferred on it. The supplied evidence does not establish token-to-network relationships for a broader set of candidates, so this article does not infer them.

Proof of work is also not a complete description of every component involved in agreement. The available technical evidence supports a narrower Bitcoin-specific statement: the valid chain representing the greatest cumulative proof of work is preferred when competing histories exist. That does not mean that work alone makes an invalid block valid; the network’s validity rules still matter. A list should avoid suggesting that the words “proof of work” settle every question about block acceptance or network behavior.

## All proof of work coins: scope and inclusion criteria

A defensible reference should state three boundaries before naming entries: its research date, what counts as a network or asset entry, and the evidence threshold for inclusion. The date matters because a past description of mining does not demonstrate that the network still uses PoW. The evidence threshold matters because a project’s own broad label may not explain whether PoW remains part of active consensus.

For a current-PoW category, require maintained, attributable technical documentation that identifies PoW as part of the network’s current consensus rules. Record the source and date checked. If documentation describes only an earlier design, a limited supporting function, or a combination of consensus mechanisms, do not silently present the project as an uncomplicated current-PoW entry. If current sources are unavailable or conflict, classify the case as unverified rather than resolving the uncertainty by assumption.

The evidence available here is deliberately narrow. It supports a Bitcoin-specific explanation of PoW and a Bitcoin-specific chain-selection description. It does not supply a dated, current classification for a broad universe of networks. It therefore does not justify naming a comprehensive collection of other coins or declaring that any such collection is complete. A responsibly bounded reference can say what its evidence supports and leave unsupported candidates out.

The word “all” should be treated as a scope claim, not decoration. To support it, a reference would need a defined universe of candidates and current documentation for the entries it includes, as well as a method for handling transitions, hybrids, and uncertain cases. Without that work, a list should be called non-exhaustive and dated, rather than presented as a permanent inventory.

## How to read the reference list

A useful entry format would identify the network, the asset relationship, the consensus classification, the technical source, and the date checked. Where evidence supports it, the classification can distinguish current PoW from hybrid, partial, historical, or unverified status. These fields make it easier to see whether an entry is a statement about active protocol rules or merely a reference to a project’s earlier history.

This article does not provide named entries beyond the Bitcoin-specific mechanics because the allowed evidence does not establish a broader current roster. Bitcoin is included as an illustration of how a network-specific claim can be stated, not as a recommendation or as proof that other networks share its design.

A shared PoW label also does not establish equivalent security or operating requirements. The evidence supports that a PoW solution is computationally costly to find but straightforward for other nodes to verify against a target. It does not establish that every network uses the same target design, algorithm, or network conditions. Consequently, a reference should use the shared label for classification only and avoid turning it into a claim that all entries work alike. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

A list should also keep its purpose narrow. It can help readers identify candidate networks and find the evidence behind each classification. It cannot, on the evidence available here, establish whether a coin is profitable to mine, easy to access, or suitable as an investment. Those are different questions and require evidence that this reference does not provide.

## Networks that need separate classification

A network that changed its consensus design belongs in a different category from one that currently uses PoW. A network using PoW alongside another consensus mechanism should be labeled hybrid or partial when reliable documentation supports that description. A project with only historical proof-of-work association should not be grouped as current PoW merely because older documentation mentions mining.

Forks and similarly named assets need separate network identification. A shared name or historical association is not evidence that two networks currently follow the same consensus rules. Before listing either one, identify the specific network and check its active technical documentation. The evidence available here does not document particular forks, hybrids, or transitioned projects, so it cannot responsibly classify examples in those categories.

These distinctions also prevent a common category error: treating an asset’s history as if it were a current protocol specification. Historical use can be relevant context, but it is not sufficient evidence for a present-tense claim. If the evidence only supports past use, label it historical; if the current role is unclear, leave the case unverified.

## How to verify a network's current consensus

Begin with maintained protocol specifications or technical documentation that describes how the network currently validates or orders blocks. Check that the material refers to active rules rather than an archived design or a general explanation of mining. Record the source and date checked, then cross-check material changes against independent technical documentation where available. If sources disagree or leave the active rules unclear, state that limitation rather than choosing the stronger-sounding classification.

For a PoW claim, look for documentation connecting computational work to block proposal, block acceptance, or history selection. Bitcoin offers a specific example: a qualifying block-header hash must be at or below its current target. That condition can illustrate what a precise protocol statement looks like, but it is not a universal test that can be applied unchanged to every network. [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

Finally, match the label to the evidence. Use “current” only where documentation supports active use; distinguish a hybrid or limited role from a network whose consensus is described simply as PoW; and call a past association historical. If present rules cannot be confirmed, mark the status unverified. This approach makes a reference transparent about both its inclusions and its limits, without implying that the list is exhaustive, permanent, or a guide to mining decisions.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
