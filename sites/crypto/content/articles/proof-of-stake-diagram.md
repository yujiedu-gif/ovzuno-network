---
title: "Proof of stake diagram: How validators help add blocks"
description: "Use this proof of stake diagram to follow how validators are selected, propose blocks, attest to transactions, and help a network reach agreement."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["staking_validators"]
tags: ["proof stake diagram"]
author: "editorial_team"
primary_keyword: "proof of stake diagram"
owned_question: "What does a proof-of-stake diagram show about validator selection, block proposals, attestations, and the addition of a block?"
risk_level: "medium"
---

A proof of stake diagram shows how protocol-defined validator roles can move a proposed block toward network acceptance: validators participate, one may propose a candidate, other validators check it and send attestations or votes, and the network applies its rules to the result. The exact sequence varies by protocol. The diagram below uses Ethereum’s proof-of-stake process as a specific example, not a universal template.

## Proof of stake diagram: the process at a glance

```text
Validator participation
        │
        ▼
Protocol selects or assigns validator duties
        │
        ▼
Selected validator proposes a candidate block
        │
        ▼
Other validators check the block and its transactions
        │
        ▼
Validators send attestations or other protocol messages
        │
        ▼
Protocol applies fork choice and acceptance rules
        │
        ▼
Checkpoint votes may establish finalized history
```

The boxes describe protocol roles, not a fixed schedule shared by every network. In Ethereum, validator duties include checking and attesting to blocks, and a validator proposes a block when selected by the protocol. The broader process combines attestations, a fork-choice rule, and checkpoint finality under protocol-defined conditions.

An **attestation** is a validator message that contributes to the protocol’s assessment of the chain. **Fork choice** is the rule used to select between competing candidate histories. **Finality** is a protocol-defined status for history that has met its finality conditions; it is not necessarily identical to the initial inclusion of a block. Ethereum’s finality mechanism uses validator votes on checkpoint blocks to distinguish finalized history from merely included blocks.

## What happens before a block is proposed

A **validator** is a protocol participant assigned consensus duties. The diagram starts with participation, then shows the protocol assigning or selecting duties. It does not prescribe how a participant qualifies, how stake is arranged, or what equipment or operating practices are required. Those details are network-specific and are outside this explanation.

Keep three roles distinct. Staked assets are part of the protocol’s economic arrangement; validator software performs protocol duties; and an operator manages whatever infrastructure or keys a particular implementation requires. The diagram represents the protocol’s actions, not the operator’s setup. It also does not imply that all networks select validators in the same way.

For Ethereum specifically, validator participation uses ETH deposited as slashable economic collateral. That is a network-specific design detail, not a general requirement that applies to every proof-of-stake system. This article does not cover eligibility thresholds, staking products, or instructions for operating a validator.

## How validators propose and check a block

When the protocol selects a validator to propose a block, that validator supplies a candidate for consideration. The candidate is not accepted merely because it was proposed. In Ethereum’s block-processing model, a receiving node checks the proposed block and re-executes its transactions to verify the resulting state change before accepting it. ([source](<https://ethereum.org/developers/docs/blocks/>))

Other validator roles contribute checks and attestations. These messages help the protocol evaluate the candidate and the chain history, but they should not be read as a guarantee that every network uses the same message type, ordering, or participant schedule. Ethereum’s validator duties include checking and attesting to valid blocks, while a selected validator may propose a block.

The diagram separates proposal from checking because they are different steps. A proposal supplies a candidate; validation applies network rules to it. Attestations or equivalent messages then contribute to agreement according to that network’s mechanism. The simplified arrows show the conceptual flow, not a claim that every participant observes events in one identical order.

## From validator messages to network agreement

Validation messages contribute to the protocol’s decision about which history to follow. In Ethereum, attestations work alongside a fork-choice rule, while checkpoint votes support the separate determination of finalized history. Therefore, a block may be included before it is finalized under the protocol’s finality rules.

The diagram intentionally gives no universal vote threshold or time-to-finality. Ethereum’s finality depends on protocol-defined supermajority conditions; other proof-of-stake networks may define different rules. The visual’s last two boxes—protocol acceptance and possible checkpoint finality—should therefore be read as a distinction, not as a promise that acceptance always leads to finality on a particular schedule.

## What the diagram leaves out

This is a process map, not a staking or validator-operation guide. Rewards, inactivity penalties, and slashing for specified conflicting validator messages are features of Ethereum’s validator incentive design; other protocols can use different arrangements. No reward rate or universal penalty rule is implied here. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/>))

The diagram also omits network-specific eligibility, operating, security, and recovery procedures. It does not state fees, yields, availability, regulatory or tax treatment, or compliance obligations. Those questions require current, authoritative evidence for the relevant network and jurisdiction; they cannot be inferred from the arrows in a general process diagram.

## Sources and references

- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-19.
