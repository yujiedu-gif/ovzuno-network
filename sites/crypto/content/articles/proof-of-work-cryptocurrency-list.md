---
title: "Proof of work cryptocurrency list: networks and verification criteria"
description: "Use this proof of work cryptocurrency list to identify candidate networks, check consensus classifications, and note hybrid or changed mechanisms."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["mining_consensus"]
tags: ["proof work cryptocurrency list"]
author: "editorial_team"
primary_keyword: "proof of work cryptocurrency list"
owned_question: "Which cryptocurrencies use proof-of-work consensus, and what criteria should be used to verify that classification?"
risk_level: "medium"
---

The evidence authorized for this reference supports one named hybrid example, Decred, but does not support a comprehensive list of cryptocurrencies that use proof of work alone. To classify a network, check its own consensus documentation, distinguish block production from other consensus roles, and record the network, documented design, and review date. Do not treat a hybrid example or a historical description as proof of a network’s current, proof-of-work-only status.

## What qualifies for a proof-of-work cryptocurrency list?

A proof-of-work cryptocurrency list should identify networks by their consensus mechanisms, not by a token’s name, ticker, branding, or association with mining. The relevant question is what the network’s protocol asks participants to do when blocks are proposed, checked, and incorporated into its accepted history.

Proof of work is a component of a broader consensus process, not necessarily a complete description of that process. In the Ethereum proof-of-work explanation, for example, it is described as a Sybil-resistance and block-author-selection component that operates alongside validation, networking, incentives, and a fork-choice rule. That explanation illustrates why a single label can leave out important protocol roles; it does not establish Ethereum’s current consensus classification. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

For a reference list, an entry should identify the network and state whether the evidence supports proof of work alone or a combination of mechanisms. A hybrid design must be labeled as hybrid, not silently included in a list that implies proof-of-work-only consensus. Where documentation is historical, version-specific, or unclear about present status, the entry should say so rather than generalize.

The evidence available for this article supports a concise, limited catalog rather than a broad directory. That limit reflects the allowed evidence, not a claim that no other cryptocurrencies use proof of work.

## Proof of work cryptocurrency list: entries and consensus notes

| Network | Classification supported by the evidence | Qualification |
|---|---|---|
| Decred | Hybrid proof of work and proof of stake | The documented design combines proof-of-work block production with proof-of-stake ticket voting. Ticket voters approve blocks and participate in rule-change governance. [source](<https://docs.decred.org/proof-of-stake/overview/>) |

This is a hybrid entry, not an example of proof-of-work-only consensus. Its two roles matter: proof of work produces blocks, while proof-of-stake ticket voting has approval and governance functions. The description is specific to Decred’s documented architecture; it should not be treated as a template for how every hybrid network divides responsibilities. [source](<https://docs.decred.org/proof-of-stake/overview/>)

No additional network belongs in this evidence-bounded list because the permitted claims do not establish another network-specific classification. Adding familiar names from memory would not meet the verification standard. A reader looking for a more extensive catalog would need current, network-specific evidence for each additional entry.

The table also does not imply that Decred’s protocol has remained unchanged indefinitely. The available claim identifies an architecture, but it does not supply a review date or establish a current protocol version. For that reason, this article cannot present the entry as a date-verified statement of present network operation. A publication-ready, current directory would need to attach a review date to evidence that actually supports that temporal scope.

## How to verify a network’s current consensus

Begin with material that describes the network’s own protocol. The documentation should name the network and explain the function proof of work performs. A general explanation of proof of work can clarify terminology, but it cannot by itself prove that a particular cryptocurrency currently uses that mechanism.

Then identify whether the description is current, historical, or tied to a particular protocol version or fork. Record the document’s stated scope and the date it was reviewed. If the evidence does not say whether the described mechanism remains in force, mark the classification as unverified for current status. Avoid converting a statement about an earlier design into a present-tense claim.

Next, look for other mechanisms with consensus responsibilities. A network may use proof of work for block production while another mechanism contributes to block approval, chain selection, or governance. Decred’s documented combination of proof-of-work block production and proof-of-stake ticket voting demonstrates why a verification note should describe roles as well as labels. [source](<https://docs.decred.org/proof-of-stake/overview/>)

Finally, distinguish proposing a block from checking whether it is valid. In Ethereum’s proof-of-stake block-processing description, a node receiving a proposed block checks the block and re-executes its transactions to verify the resulting state change before accepting it. This is a specific Ethereum example of a verification role; it is not a rule that can be assumed for every network. [source](<https://ethereum.org/developers/docs/blocks/>)

A useful record for each candidate should include the network name, the primary documentation consulted, what proof of work does in the described design, any additional consensus mechanism, the relevant version or historical qualification, and the review date. If a source does not establish one of those details, state that gap. A dated note is a way to make the scope visible, not a substitute for evidence that the classification is correct.

## What this list does not establish

A proof-of-work label does not establish an asset’s profitability, price, investment merits, or suitability for a particular person. This reference is a technical classification aid, not a financial assessment or recommendation.

Consensus classification alone also does not establish a network’s security, decentralization, transaction performance, or recovery options. Those are separate questions requiring evidence about the specific network and the property being assessed. A consensus label should not be expanded into a broader claim about how a system performs or responds to adverse conditions.

This list is not a mining setup guide. It does not compare or recommend hardware, pools, software, or services, and it does not provide instructions for mining. Those subjects require separate, appropriately scoped evidence and are outside the classification task here.

## Jurisdiction, compliance, and other claims to verify separately

A consensus mechanism does not establish legal status, regulatory treatment, tax consequences, or whether an asset or service is available in a jurisdiction. This article makes no such jurisdiction-specific claims. Any claim of that kind would need current, authoritative evidence tied to the relevant jurisdiction and activity; consensus terminology is not a substitute.

The same boundary applies to fees, yields, security, and recovery. None follows automatically from a proof-of-work classification, and the evidence used for the Decred entry does not establish those characteristics. Verify each separately from suitable evidence or omit it when that evidence is unavailable.

For accurate publication, keep the list’s scope visible: identify the network, distinguish a sole mechanism from a hybrid design, state the evidentiary and temporal limits, and date a current-status review only when it has actually been performed. With the permitted evidence here, Decred can be described as a documented hybrid example, while a comprehensive, date-stamped list of current proof-of-work networks cannot be responsibly supplied.

## Sources and references

- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
- [PoS Voting Overview](https://docs.decred.org/proof-of-stake/overview/) — Decred Documentation; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
