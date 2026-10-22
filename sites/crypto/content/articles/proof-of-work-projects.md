---
title: "Proof of work projects: a guide to verifying consensus"
description: "Explore proof of work projects through a concise, evidence-led list of crypto networks, with guidance on verifying consensus claims in primary documentation."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["proof work projects"]
author: "editorial_team"
primary_keyword: "proof of work projects"
owned_question: "Which crypto projects use proof of work consensus, and how can readers verify that classification?"
risk_level: "medium"
---

Proof-of-work projects are crypto networks whose documented consensus design uses proof of work to help determine accepted network history. In the evidence available for this article, Bitcoin is the only project with a supported example: its documentation describes proof-of-work block search and chain selection. To verify any project’s classification, consult its own current protocol materials and confirm that proof of work plays a role in the network’s consensus—not merely in a separate component or an informal description.

## What qualifies as a proof-of-work project?

Proof of work is a computational process in which finding a valid result is costly, while other nodes can check that result against the network’s target. That definition describes a mechanism, not a list of projects. A network qualifies for this reference list only when its own primary documentation connects proof of work to its consensus design.

Consensus is the set of processes and rules by which a network determines which blocks or history to accept. A project’s documentation may mention mining, computational work, or a proof-of-work algorithm without showing that the mechanism governs the network’s consensus. Readers should look for that direct connection before classifying the project.

Bitcoin provides the supported example here. Its original design describes miners varying a nonce in a block until the resulting hash satisfies the network’s target. When histories compete, nodes select the valid chain representing the greatest cumulative proof of work. These are Bitcoin-specific descriptions; they should not be assumed to apply to other networks.

This scope is deliberately narrower than mining operations. The article does not explain equipment, pools, profitability, or difficulty. A proof-of-work classification also does not imply that every project uses identical rules or that the label alone establishes anything about a network’s overall quality.

## Proof of work projects to verify

### Bitcoin

Bitcoin’s original network design is a supported proof-of-work example. Its documentation connects the proof-of-work search to block creation and describes cumulative work as part of selecting between competing histories. This establishes the classification for the design described in those materials, without treating the details as universal to all proof-of-work networks.

**Verification trail:** Start with the Bitcoin documentation that describes the nonce search and target condition, then check its explanation of how nodes choose between competing histories. Confirm that the source discusses the network’s consensus role. Keep the conclusion tied to the document’s scope: the evidence here describes Bitcoin’s original design and does not, by itself, establish every current implementation detail.

No additional named network is included. The allowed evidence for this article does not provide primary documentation sufficient to verify other projects’ proof-of-work classifications. That limitation is about the evidence available for this reference list; it is not a claim that Bitcoin is the only network that uses proof of work.

A careful reference list may therefore be shorter than a general catalog. Adding a project based only on a familiar name, a mining-related product, or a secondary description would go beyond the evidence supplied here. For every added entry, the documentation must support the same specific proposition: proof of work is part of that network’s consensus design.

## How to check a project’s consensus documentation

Use the following process when checking a project beyond the supported example:

1. **Locate primary documentation.** Look for the project’s protocol specification, technical documentation, or maintained source materials. Record the title and any date or version the source provides. If the documentation does not show a date or version, do not describe it as current on that basis alone.

2. **Identify the consensus function.** Find the passage explaining how the network proposes, validates, or selects blocks or history. Check whether proof of work is explicitly part of that process. A reference to mining, a work algorithm, or a component associated with the network is not enough unless the source connects it to consensus.

3. **Separate network rules from supporting components.** Ask whether the documentation describes proof of work securing the network’s consensus process or only a separate function. The distinction matters: a project-level label should reflect the role documented for the network, not an isolated tool or service.

4. **Check qualifications and dates.** Look for language indicating a hybrid design, a planned transition, or a changed consensus process. If documentation describes a change, report the relevant qualification and date or version. Older documentation may establish what a design specified then, but should not be presented as proof of a current design without checking for later primary materials.

5. **Write a limited conclusion.** Summarize only what the source supports. For example, if the source describes proof of work in a particular part of consensus, state that role rather than implying that every network function uses it. If the source is unclear, leave the classification unresolved until stronger documentation is available.

For Bitcoin, the specific verification trail is the documented nonce-and-target search and the chain-selection description based on cumulative proof of work. Do not carry those Bitcoin details over to another network unless that network’s own sources support them. The same discipline applies to claims about a transition or hybrid arrangement: verify the project-specific documentation and identify its scope rather than using a broad label without qualification.

## What this list does not establish

Classifying a network as proof of work does not establish its security, decentralization, reliability, or regulatory status. The fact that a proof-of-work result can be costly to find and straightforward to check is a definition-level property; it does not, on its own, establish the security of any particular network.

This list does not compare profitability, token value, mining costs, or investment merit. It also makes no claims about availability, fees, yields, recovery procedures, or legal and tax treatment. Those matters are outside the question of consensus classification and would require separate, current evidence specific to a project and, where relevant, jurisdiction.

Use this reference as a starting point for checking protocol documentation. Treat each project classification as a bounded statement about the consensus design its primary materials describe, not as an endorsement or a broader assessment.

## Sources and references

- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
