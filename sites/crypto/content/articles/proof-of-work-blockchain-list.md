---
title: "Proof of work blockchain list: notable networks and verification"
description: "Explore a proof of work blockchain list with clear inclusion criteria and checks for consensus use, current status, and historical or hybrid designs."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["proof of work blockchains list"]
author: "editorial_team"
primary_keyword: "proof of work blockchain list"
owned_question: "Which notable blockchain networks currently use proof of work for consensus, and how can their status be verified?"
risk_level: "medium"
---

Bitcoin is the only network this evidence set supports listing as a current proof-of-work example; Ethereum belongs in a historical category because it switched to proof of stake in 2022. This is a scoped, non-exhaustive reference, not a claim that only Bitcoin currently uses proof of work. To add another network, verify its active consensus design in current, maintained documentation and record when you checked it.

## What qualifies for this proof of work blockchain list?

Proof of work (PoW) is a consensus design in which participants perform computational work under network rules. A consensus mechanism is the set of processes used to determine which proposed blocks and history the network accepts. The phrase “proof of work” can also refer to one component within a larger mechanism, rather than describing every part of consensus.

For Bitcoin, the proof-of-work search varies a nonce in a candidate block until the resulting hash satisfies the network’s target condition. Bitcoin’s proof-of-work chain selection treats the valid chain with the most accumulated work as the preferred history. These descriptions support classifying Bitcoin’s design as proof of work. They do not, by themselves, provide a live status check for every Bitcoin network operation; a current classification should still be checked against maintained documentation.

This list uses a conservative inclusion rule: include a network as current only when the evidence identifies its active consensus mechanism. Keep historical use separate, and do not assume that related networks, forks, or projects share the same status. The available evidence supports one current example and one historical example. It does not establish a broader catalog of current networks.

A network’s status is also distinct from how participants implement or interact with it. The classification concerns the network’s consensus design, not a wallet, mining service, exchange, application, or individual user. A token listing or a service’s use of the word “mining” is not enough to establish that the associated blockchain currently uses proof of work.

## Notable networks that use proof of work

| Network | Classification in this reference | Evidence and qualification |
|---|---|---|
| Bitcoin | Current proof-of-work example supported by this evidence set | Bitcoin’s design uses a nonce search to produce proof of work meeting the network target. Its chain-selection design prefers the valid history with the most accumulated proof of work. The supplied evidence describes the protocol design but does not constitute a separate, real-time operational status check. |
| Ethereum | Historical proof-of-work use; not current | Ethereum’s documentation says it switched to proof of stake in 2022 and no longer uses proof of work. Include it only as a historical example, not as a currently proof-of-work network. |

“Current” in this table means that the entry is supported as a current example by the permitted evidence. The evidence for Bitcoin describes its original network design and does not independently confirm present operation on a particular date. Therefore, readers should confirm current status in maintained Bitcoin documentation before relying on the entry as a dated status record. Ethereum’s historical classification is limited to the documented transition and statement that it no longer uses proof of work.

This narrow table is deliberate. The available evidence does not establish current proof-of-work status for other named networks, so it would be misleading to add them merely to make the list look more comprehensive. It also does not establish that any fork or related blockchain follows Bitcoin’s design. Each network needs its own evidence and status check.

## How to verify consensus and current status

Start with technical documentation maintained for the network: a protocol description, consensus documentation, or an official developer guide. Check that the source names the blockchain itself, explains the role proof of work plays, and makes clear whether that role is active or historical. Record the source and date checked so a later reader can distinguish a current verification from an old description.

Then test the classification against the source’s exact wording. Does it say that proof of work currently participates in block production or chain selection? Or does it describe an earlier version, an optional component, a test environment, or a related project? If it only establishes a historical design, classify the network as historical. If it does not establish current status, leave it unverified or omit it rather than inferring the answer.

Bitcoin offers a useful example of checking both mechanism and scope. Its documented nonce search and accumulated-work chain-selection rule provide evidence for the PoW classification. Those mechanism details should not be confused with independent proof that a particular service, mining operation, or connected application is working as expected. The source supports a protocol-level description, not claims about every participant or service.

Ethereum illustrates why a current-status check matters. Its proof-of-work material identifies the mechanism as part of a broader consensus design, while also stating that Ethereum switched to proof of stake in 2022 and no longer uses proof of work. A search result that mentions Ethereum and proof of work can therefore be accurate about its history while being misleading if presented as a current classification.

Do not treat an explorer, token page, or mining-related service as sufficient evidence on its own. Such material may describe an asset or service without establishing the network’s active consensus rules. If maintained technical sources are unclear or conflict, report that the status is unresolved rather than choosing the interpretation that produces a longer list.

## How to label historical and hybrid designs

A historical label applies when a network used proof of work in an earlier design but the available evidence says it has since moved to another consensus approach. Ethereum is the supported example here: the documentation states that it switched to proof of stake in 2022 and no longer uses proof of work. It should not appear in a table of current proof-of-work networks merely because older materials describe its former mechanism.

A hybrid or auxiliary arrangement needs a more specific explanation. In this context, “hybrid” means proof of work plays a defined role alongside another consensus component; “auxiliary” means it supports one part of the process rather than describing the whole mechanism. Ethereum’s conceptual explanation makes the general distinction that proof of work can provide Sybil resistance and block-author selection alongside validation, networking, incentives, and a fork-choice rule. However, that description is not evidence that Ethereum currently uses proof of work, nor does it establish the status of any other hybrid network.

For a proposed hybrid entry, verify three points in documentation for that particular network: which component uses proof of work, what consensus responsibility it performs, and whether the documentation describes that arrangement as active. State the role in the table instead of using an unqualified label. If the evidence documents only historical or auxiliary use, preserve that limitation and do not present the network as a straightforward current PoW example.

Recheck classifications after protocol changes or upgrades. The evidence here does not specify a universal review interval, and an older description cannot establish the current role of a consensus component. The practical standard is to date each check and rely on maintained documentation that addresses the named network’s active design.

## What the list does not establish

A proof-of-work label is a description of consensus design, not a complete assessment of security, decentralization, or attack resistance. Bitcoin’s chain-selection description says valid histories are compared by accumulated proof of work; it does not establish an absolute guarantee against every possible reorganization or attack. Ethereum’s former proof-of-work description characterizes finality as probabilistic because simultaneous valid blocks can create temporary forks and later blocks increase confidence in one history. That historical observation should not be generalized into a security judgment about current Ethereum, which the evidence says no longer uses proof of work.

This reference also says nothing about whether mining a network is profitable or suitable, what rewards or fees apply, or whether an asset or service is available. Those are separate questions and require evidence specific to the network, service, date, and operating conditions. No conclusion about jurisdiction, regulation, tax treatment, or compliance follows from the consensus classification.

The useful result is deliberately modest: Bitcoin is the current proof-of-work example supported here, with a verification caveat about the date and scope of the underlying design evidence; Ethereum is a historical example, not a current one. For any additional candidate, check maintained, network-specific documentation, distinguish active use from historical or hybrid roles, and record the date before expanding the list.

## Sources and references

- [Proof-of-Work](https://ethereum.org/developers/docs/consensus-mechanisms/pow) — ethereum.org; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
