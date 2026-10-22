---
title: "How to mine ethereum: what changed after proof of stake"
description: "Learn how to mine ethereum historically, why Ethereum ended proof-of-work mining, and how its current consensus mechanism differs from mining."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["crypto_assets_protocols"]
tags: ["mine ethereum"]
author: "editorial_team"
primary_keyword: "how to mine ethereum"
owned_question: "Can Ethereum be mined today, and what did mining require before Ethereum moved to proof of stake?"
risk_level: "medium"
---

Ethereum’s main network cannot be mined today: its move from proof of work to proof of stake ended mining as the process for producing blocks on that network. Before that change, mining used computing power to search for work that met network rules. The distinction matters when reading older tutorials: they describe a historical mechanism, not a current way to participate in Ethereum’s main network.

## Can you mine Ethereum today?

No. On Ethereum’s main network, proof-of-work mining is no longer the block-production process. Mining hardware and pool arrangements cannot restore that former process; the network’s protocol rules determine which participation and blocks it accepts.

This answer is specific to Ethereum’s main network. The name “Ethereum” may appear in discussions of other networks or technologies, but a similar name does not establish that a network uses the same protocol or consensus mechanism. Verify the precise network before applying a tutorial or interpreting claims about mining. This guide does not explain how to mine another network.

It is also useful to distinguish a network’s rules from the tools once used to work within them. Hardware performs computation, while software can prepare work for that hardware. Neither tool category defines the network’s current consensus rules. A device that was suitable for a historical workload, or software that once prepared mining work, does not by itself make that work valid under a different protocol.

## How Ethereum mining worked before proof of stake

Proof of work is a consensus model in which participants use computation to search for a result that satisfies a network target. In a typical proof-of-work process, mining hardware performs repeated hash computations. Software prepares candidate work and passes suitable work to the hardware to search. Network-specific rules determine the candidate data, target, and other conditions for acceptable work; those details should not be assumed to be identical across blockchains.

A documented Bitcoin mining workflow offers a bounded illustration of the software-hardware division: software constructs a candidate block and header from transactions, then sends header work to hashing hardware. This is an example from Bitcoin, not a complete account of Ethereum’s former implementation. It helps explain the general idea of preparing work and searching for a qualifying result, but it cannot establish Ethereum-specific details such as its exact historical software, algorithm, parameters, or operating requirements.

Mining software and mining hardware had different roles. Software supplied or organized the work to be searched; hardware carried out repeated computations. A mining setup therefore depended on more than the presence of a computer: the software had to produce work that matched the network and hardware had to perform the required computation. The exact design varied by network and protocol period. No present-day hardware specification follows from this high-level description.

Mining pools were an additional operational arrangement in proof-of-work ecosystems. A pool can assign devices portions of a search space and receive submitted shares. A share is evidence of work measured against the pool’s assigned target; meeting that target does not necessarily mean the share is a network-valid block. This distinction helps explain how pool software can track contributed work without every submitted share becoming a block accepted by the network.

The pool mechanism is not itself a consensus rule. The network’s rules decide whether a proposed block is valid, while a pool’s software and terms govern its own work assignment and accounting. Pool arrangements can differ, and a description of this general division should not be taken as proof that every historical Ethereum miner used a pool or that all pool systems operated the same way.

Rewards and fees also need a time and network attached to them. In the documented Bitcoin model, miner revenue can include a block subsidy and transaction fees. That example illustrates why protocol rewards and transaction fees are separate components, but it does not supply Ethereum’s historical reward amounts or establish current economics. Any claim about what Ethereum miners received must be tied to the relevant historical protocol rules. A remembered reward figure is not a present-day earning expectation.

## What replaced mining on Ethereum

Ethereum’s main network changed from proof of work to proof of stake. Under the former model, miners searched computationally for acceptable work. Under the current model, validators participate according to proof-of-stake protocol rules. This is a change in the network’s consensus approach, not simply a new name for the former mining workflow.

The change also shows why hardware, software, and network rules should be discussed separately. A miner’s hardware performs hashing, and mining software organizes work for that hardware. Those functions belong to the former proof-of-work process. Validator participation is a different protocol role, so historical mining tools and pool instructions do not describe it.

A protocol change is also distinct from an individual operator changing equipment or installing software. Ethereum protocol changes involve proposal, technical review, implementation, coordination, and adoption across network stakeholders. The transition therefore cannot be reversed by a user choosing a different mining configuration.

This distinction is not an invitation to treat staking as mining under another label. The two terms refer here to different consensus mechanisms and participant roles. This guide does not provide staking instructions, compare providers, or make claims about returns. A change in how a network reaches consensus does not, by itself, establish a particular financial outcome for an individual participant.

## What to check before acting on mining advice

Start by identifying the exact network and the protocol period the material covers. Does it explicitly refer to Ethereum’s main network, or to another blockchain? Does it describe proof of work as a historical process, or imply that it remains Ethereum’s current process? These questions prevent a technically accurate old explanation from being mistaken for current operating guidance.

Next, check whether the claim concerns protocol behavior or an operational tool. Protocol rules determine what work and blocks the network accepts. Hardware searches; software can prepare and pass work; pools can assign search space and track shares. Those mechanisms describe how mining operations can be organized, not whether mining is a current participation method on Ethereum’s main network.

Then check the scope of examples. A Bitcoin workflow may illustrate a general pattern, but it does not prove Ethereum used identical rules or tools. A generic account of pools does not establish the terms or operation of any particular pool. Historical reward or fee examples should be treated as claims about a defined protocol period, not converted into estimates of current earnings.

Finally, verify status and technical details against current primary documentation for the network in question. Look for clear identification of the network, the consensus mechanism, and the date or protocol version covered by a tutorial. If a source does not establish those points, do not infer that its instructions apply today. In particular, do not infer profitability, hardware suitability, service safety, or asset recovery from a historical description of mining.

## Risks and jurisdiction-dependent considerations

The protocol history explained here does not establish whether any particular hardware, pool, software, or related service is currently available or suitable. Nor does it establish service fees, security, or recovery conditions. Those are separate claims about specific arrangements and require current, relevant evidence. A historical description of mining is not an assessment of a provider.

The same boundary applies to financial claims. Past protocol rewards do not guarantee future outcomes, and this guide does not estimate returns or recommend an activity. Any statement about expected earnings would require evidence beyond the fact that mining once formed part of Ethereum’s protocol.

Regulatory, tax, and compliance conclusions are also outside this guide. They require jurisdiction-specific evidence and circumstances not supplied by the protocol mechanics described here. Do not use an old mining tutorial, a general explanation of proof of work, or this historical account as a substitute for current jurisdiction-specific guidance.

The practical conclusion is narrow: Ethereum’s main network no longer uses mining, while its former proof-of-work process involved computational search organized through software and hardware, sometimes with pools. To assess a claim about mining, identify the network and time period first, then verify the applicable protocol rules. That keeps historical explanation separate from current network operation and from claims about services or financial outcomes.

## Sources and references

- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
