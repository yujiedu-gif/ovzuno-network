---
title: "L2 blockchain list: Networks and inclusion criteria"
description: "Explore an L2 blockchain list with inclusion criteria, network classifications, and settlement context. Check evidence and scope before comparing networks."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["2 blockchain list"]
author: "editorial_team"
primary_keyword: "l2 blockchain list"
owned_question: "Which networks belong on a current, evidence-based list of Layer 2 blockchains, and what criteria distinguish them from other scaling systems?"
risk_level: "medium"
---

A current, evidence-based L2 blockchain list should include only networks whose documented architecture executes transactions outside an underlying Layer 1 and identifies a specific function—such as security, consensus, data availability, or settlement—that depends on that Layer 1. The evidence available for this reference does not establish current classifications for individual networks, so it cannot support naming any as a verified entry. The table therefore records that limitation and provides criteria for evaluating candidate networks without treating a project label as proof.

## What qualifies for this L2 blockchain list?

Layer 2 (L2) is used here as an architectural classification, not as a label that confirms a particular level of security. An Ethereum L2 derives some security from Ethereum’s Layer 1, but the exact guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. To qualify for this list, a candidate’s documentation must identify both the underlying chain and the function it relies on that chain to perform. [source](<https://ethereum.org/developers/docs/scaling/>)

The underlying-chain relationship matters more than the mere fact that a system processes activity elsewhere. One modular architecture model separates execution, settlement, consensus, and data availability into distinct functions that can be assigned to specialized layers. This is a useful way to organize the questions for a candidate, but it is not a universal definition of every blockchain architecture. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A system should not be included just because it connects to another blockchain, uses a bridge, or describes itself as a scaling network. Separate ledgers do not physically transfer assets between themselves: bridge designs coordinate value through mechanisms such as locking, releasing, minting, burning, or swapping. The accounting and redemption path depends on the bridge design, and the existence of a bridge alone does not establish that the connected system is an L2. [source](<https://ethereum.org/developers/docs/scaling/sidechains/>)

This is a limited reference, not a complete census. The allowed evidence does not provide current, network-specific documentation to verify named systems’ architecture, status, or settlement arrangements. It therefore cannot support a dated roster of confirmed network entries. The criteria below show what would be needed to add one responsibly.

## Layer 2 networks in the reference list

| Network | Design category | Underlying chain | Settlement relationship | Evidence status |
|---|---|---|---|---|
| No network-specific entry verified | Not established | Not established | Not established | The available evidence supports general L2 criteria, but does not confirm a current network’s classification or relationship to an underlying chain. |

An empty roster is more accurate than filling the table with names based on familiarity or an unverified label. The evidence supplied for this article does not establish whether any specific candidate currently executes outside a Layer 1, what it publishes to that chain, or what security or settlement role the chain performs. Without those details, a network cannot be marked as a verified L2 entry.

A future entry should give the network name and the date of the documentation checked, then state its documented design category and underlying chain. It should describe the relevant settlement or data-handling relationship in the documentation’s own scope. The entry should also distinguish confirmed details from unresolved points—for example, where documentation identifies an underlying chain but does not explain exactly which security function depends on it.

This approach avoids implying that the table is comprehensive or that inclusion is an endorsement. It also avoids assigning a network a design category that the available evidence cannot substantiate. For the same reason, this reference does not treat a candidate’s self-description as sufficient verification.

## How the listed networks differ

No named network can be compared on the supplied evidence. For a supported comparison, use the same questions for each candidate: where does transaction execution occur; which chain handles settlement or consensus; where is transaction data made available; and what documented mechanism supports the proposed state transition? The modular model’s separation of execution, settlement, consensus, and data availability helps organize these questions, but each answer must come from evidence about the specific system. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

Keep the limits of an underlying-chain relationship explicit. An L2’s security relationship is not a blanket transfer of every property of its Layer 1: the exact guarantee depends on system-specific proofs, data availability, settlement, governance, and exit mechanisms. If documentation supports only a narrow statement—for example, that a system posts certain data to a chain—do not expand that into an unsupported claim that the chain provides all of the system’s security. [source](<https://ethereum.org/developers/docs/scaling/>)

Also separate settlement from cross-chain asset coordination. A bridge can coordinate value between ledgers without physically moving an asset from one ledger to another. Its accounting and redemption path depends on its design. Consequently, a bridge connection does not, by itself, show that a system is an L2 or that its transactions settle on the connected chain in the relevant architectural sense. [source](<https://ethereum.org/developers/docs/scaling/sidechains/>)

Some comparison fields may remain unresolved or not directly comparable. A system’s documentation may describe its architecture at a high level without specifying all relevant data-handling or exit details. Record that uncertainty rather than inferring an answer from another project’s design or from a category name.

## How to verify a network’s Layer 2 status

For each candidate, consult the candidate’s current technical documentation and documentation for the underlying chain. Check the publication or update dates and look for descriptions of execution, settlement, data availability, and the mechanism used to support or dispute state changes. The available evidence here does not supply those network-specific details; they must be established before adding an entry.

Next, identify the actual dependency the candidate claims. Does the documentation say what function the underlying chain performs, or does it only use a broad phrase such as “secured by” a chain? An L2 derives some security from its Layer 1, but the exact guarantee is conditional on design details including proofs, data availability, settlement, governance, and exits. Preserve those conditions in any summary instead of turning a qualified relationship into a universal security claim. [source](<https://ethereum.org/developers/docs/scaling/>)

If documentation describes a bridge or a separate ledger, investigate that relationship as a distinct question. Bridged assets are not physically moved between ledgers; bridge mechanisms coordinate value, and the particular accounting or redemption path depends on the design. That fact can clarify how assets are represented across systems, but it does not establish L2 status. [source](<https://ethereum.org/developers/docs/scaling/sidechains/>)

Finally, record unresolved terminology openly. If a project calls itself an L2 but its documentation does not establish the underlying-chain relationship, mark the classification unverified. If the design or published documentation changes, revisit the entry rather than assuming that an earlier classification remains current.

## Scope and limitations of the list

This reference cannot claim to be exhaustive, to establish network operational status, or to confirm current classifications for individual systems. Its scope is limited to the criteria that can be stated from the available evidence. No specific network can be added as verified without current, network-specific documentation supporting its classification and its relationship to an underlying chain.

The list also makes no conclusions about performance, security rankings, fees, availability, or suitability. Those are separate questions and cannot be inferred from inclusion in an L2 category. A reader checking a candidate should verify its own documentation and the underlying chain’s documentation, distinguish established facts from open questions, and note when the cited material was published or updated. Because network designs and descriptions can change, the reference should be revised when new evidence supports a different or more complete classification.

The practical result is a deliberately narrow list: at present, no named network is verified by the evidence available for this article. That is not a claim that no Layer 2 networks exist. It is a statement about the limits of this evidence and the standard required before a network belongs on a current, evidence-based reference list.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Sidechains](https://ethereum.org/developers/docs/scaling/sidechains/) — ethereum.org; retrieved 2026-10-18.
