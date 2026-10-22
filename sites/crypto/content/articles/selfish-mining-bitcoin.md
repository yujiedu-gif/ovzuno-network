---
title: "Selfish mining bitcoin: how withheld blocks affect consensus"
description: "Learn how selfish mining bitcoin involves withholding and selectively publishing blocks, and why its effects depend on network conditions and assumptions."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["Bitcoin proof-of-work consensus", "withheld blocks", "block propagation"]
author: "editorial_team"
primary_keyword: "selfish mining bitcoin"
owned_question: "How does selfish mining work in Bitcoin, and how can withholding blocks affect the public chain and mining incentives?"
risk_level: "medium"
---

Selfish mining in Bitcoin is a theoretical strategy in which a miner or coordinated group withholds valid blocks and publishes them selectively, attempting to affect which competing branch becomes the public history. Its consequences depend on proof-of-work competition and network conditions. Withholding does not bypass Bitcoin’s validity rules or guarantee that the private branch will be accepted.

## What selfish mining means in Bitcoin

Bitcoin uses proof of work to produce candidate blocks and to order competing histories. In a general proof-of-work model, participants search for a computational result that is costly to find but straightforward for others to verify. Bitcoin’s chain-selection design represents the selected history as the valid chain with the greatest cumulative proof of work. A block’s work alone does not make it valid: the chain must also satisfy Bitcoin’s rules. [source](<https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model>) [source](<https://bitcoin.org/bitcoin.pdf>)

Selfish mining concerns when valid blocks are published. A miner following the strategy keeps some found blocks private while extending a branch that other participants cannot yet see. The rest of the network continues building on the publicly visible branch. The strategy is therefore about managing a competition between branches, not creating a separate consensus rule or making invalid blocks acceptable.

“Public chain” here means the history that network participants are following under Bitcoin’s rules, rather than every block any miner has produced. A miner’s proposal is not guaranteed to be accepted by every node or to remain in the selected chain. Nodes apply their validation rules, and competing blocks or chains can affect which history is followed. [source](<https://bitcoin.org/bitcoin.pdf>)

This differs from an ordinary temporary fork. Bitcoin participants may temporarily observe competing block proposals, including when blocks are produced at roughly the same time. Timing and propagation can influence which branch a node sees first, while continued proof of work can resolve the branch choice under Bitcoin’s documented rule. Such a temporary competition does not, by itself, show that any miner deliberately withheld a block. [source](<https://bitcoin.org/bitcoin.pdf>)

## How withheld blocks can change the public chain

Imagine two branches: a visible branch that other miners are extending and a private branch that one miner is extending without immediately announcing it. While the private blocks remain undisclosed, other participants cannot build on those blocks based on the network’s public view. If the miner later publishes its branch, the additional proof of work can change the competition between the histories.

That possibility is conditional. Bitcoin’s chain-selection design favors the valid history with the greatest cumulative proof of work when histories compete; publication order alone does not determine the result. If the public branch has gained work, or if the private branch is not valid, disclosure does not ensure that the private branch becomes the selected history. The relevant comparison is between valid branches and their accumulated work, as evaluated by nodes. [source](<https://bitcoin.org/bitcoin.pdf>)

Different participants may receive a block at different times. Timing and propagation can affect which competing proposal an individual node first observes, so a branch contest is not necessarily experienced identically at every point in the network. The evidence here supports treating propagation as relevant; it does not establish that any particular publication schedule will produce a winning branch. [source](<https://bitcoin.org/bitcoin.pdf>)

If the selected history changes, some previously visible blocks may no longer be part of that history. That is a consequence of competing valid branches and chain selection, not evidence that a miner has made a rule-breaking block valid. Bitcoin’s proof-of-work design makes changing earlier history more costly as additional blocks build on it, because an alternative history must provide sufficient cumulative work. This describes the design’s mechanism, not a guarantee that reorganization is impossible. [source](<https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus>)

## When selfish mining can affect incentives

The incentive question is whether selectively publishing blocks changes the expected outcome for the withholding group relative to other miners. To assess that question, an analysis needs to specify at least the group’s share of mining work, how quickly blocks propagate, whether miners coordinate, and how other miners respond to competing branches. These are inputs to an analysis, not conditions that can be replaced by a simple claim that secrecy is always advantageous.

Hash-power share matters to the branch competition because the strategy depends on accumulating proof of work while another branch is also being extended. But the allowed evidence does not establish a fixed hash-power threshold at which selfish mining becomes profitable, nor does it give a reward advantage that applies across network conditions. A numerical threshold or payoff would need evidence tied to a particular model and its assumptions.

Propagation and response matter as well. Because participants may temporarily see competing proposals, the timing of block delivery can affect the branch each participant initially follows. A model must account for its communication assumptions and the behavior it assigns to other miners; a result built on one assumed response should not be treated as a protocol guarantee. [source](<https://bitcoin.org/bitcoin.pdf>)

Bitcoin’s chain-selection rule remains the protocol backdrop: when histories compete, nodes select a valid chain with the greatest cumulative proof of work. The rule does not itself promise that a miner’s withholding strategy will earn more, or that other miners will react in a particular way. The evidence used here does not establish a current expected payoff or profitability under actual network conditions. [source](<https://bitcoin.org/bitcoin.pdf>)

## What the strategy does—and does not—imply for Bitcoin security

Selfish mining should be distinguished from violating Bitcoin’s consensus rules. Work cannot turn an invalid block into a valid one. At the same time, valid competing branches may affect which history nodes follow. This is a chain-selection concern: the question is which valid history has the greatest cumulative proof of work, not whether a miner can simply declare its preferred history canonical. [source](<https://bitcoin.org/bitcoin.pdf>)

The mechanism alone does not demonstrate a successful double-spend or control of the network. Those conclusions require more than the existence of withheld blocks. Practical analysis of a proof-of-work attack also depends on factors such as network topology, concentration of mining, software behavior, confirmations, and the transaction being targeted. The available evidence does not quantify the outcome for a particular attack or establish that selfish mining automatically produces one. [source](<https://bitcoin.org/bitcoin.pdf>)

Possible effects on incentives or confidence in fair competition should likewise be presented as conditional concerns, not as inevitable results. The claims available here do not measure how often blocks become stale because of selfish mining, quantify any broader security impact, or establish the strategy’s prevalence. A theoretical branch-competition mechanism is not, on its own, evidence of observed frequency.

## How to assess claims about selfish mining

When reading a study or explanation, identify what evidence it uses. A theoretical analysis, a simulation, and observations of network behavior are distinct kinds of support. Check whether it states assumptions about hash-power share, propagation, coordination, and other miners’ responses. If those assumptions change, the result may not carry over; the evidence presented here does not supply a universal threshold or a measured account of real-world prevalence.

Next, separate protocol rules from claims about incentives. Bitcoin’s proof-of-work chain-selection design explains how valid histories compete. A claim that a particular withholding strategy changes rewards needs separate analysis and should state the conditions under which the result holds. Do not turn an analytical result into a rule of Bitcoin’s protocol, or treat a model’s assumptions as a description of every network condition. [source](<https://bitcoin.org/bitcoin.pdf>)

Finally, be precise about what “affects the public chain” means. Selective publication may influence a contest between valid branches, but influence is not certainty: nodes apply validity rules, accumulated work matters, and propagation and participant responses affect the competition. The supported conclusion is limited. Selfish mining is a way to analyze strategic block publication in Bitcoin; the available evidence does not establish a guaranteed reward advantage, a universal threshold, current profitability, or real-world prevalence.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-21.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Block Chain](https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus) — Bitcoin Developer Guide; retrieved 2026-10-21.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
