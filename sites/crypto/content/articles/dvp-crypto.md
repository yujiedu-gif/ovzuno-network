---
title: "DVP Crypto: How Delivery Versus Payment Settlement Works"
description: "Learn what dvp crypto means, how delivery versus payment can coordinate asset and payment settlement, and which operational and legal dependencies matter."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["institutional_crypto_treasury"]
tags: []
author: "editorial_team"
primary_keyword: "dvp crypto"
owned_question: "What does delivery versus payment (DVP) mean in crypto settlement, and what operational conditions are needed for asset delivery and payment to occur together?"
risk_level: "medium"
---

DVP crypto settlement means linking delivery of a digital asset with payment so the two legs are intended to complete together. DVP—delivery versus payment—is a settlement arrangement, not a universal crypto protocol. Whether the legs are genuinely coordinated, and what happens if one cannot complete, depends on the transaction’s systems and arrangements.

## What DVP means in crypto settlement

Delivery versus payment describes a transaction with two obligations: one party delivers an asset, and another provides payment. The aim is to connect the outcomes so that neither side is left having completed its obligation while the other has not. The phrase identifies the intended relationship between the obligations; it does not specify one mechanism or guarantee a result.

DVP is distinct from custody, brokerage, and treasury management. It describes how asset and payment obligations are related at settlement. It does not, by itself, say who holds keys, arranges the trade, manages funds, or oversees an institution’s broader digital-asset activity. Those roles must be identified separately in the transaction arrangements.

A useful distinction is between an intended link and an enforced link. A process may rely on matching instructions or operational checks, while another may use contract or system logic to coordinate release. To assess a particular arrangement, identify what prevents either leg from completing independently, if anything, and what the parties have agreed happens when the process does not proceed as expected.

## How DVP coordinates asset delivery and payment

Map the transaction as two legs. The asset leg transfers the specified digital asset to the intended recipient; the payment leg transfers the agreed payment to the other party. The parties or their systems need to define the asset, amount, recipient, payment, and conditions for completion. These are separate obligations even when a process is designed to link them.

An illustrative contract-based arrangement can use a defined process to hold assets until a specified condition is met, with contract state transitions governing when funds are returned or released. A documented Solidity example models buyer and seller deposits held by a contract until the buyer confirms receipt. It illustrates a state-machine pattern, not a general DVP standard: the contract does not independently determine whether a physical item arrived, and the example is not a production escrow recommendation. ([source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>))

The practical question is not simply whether a smart contract is involved, but how each leg is linked. Ask whether both transfers are controlled by the same mechanism, whether that mechanism can establish that relevant conditions were met, and what happens if an instruction is missing, delayed, invalid, or disputed. If separate systems or intermediaries handle the legs, determine how their actions are coordinated and how exceptions are handled.

A transaction being sent or broadcast is not necessarily settlement under the process. For example, BTCPay operational guidance says that a merchant should not fulfill an invoice solely because an onchain payment was broadcast; the merchant’s configured settlement conditions must be met. This is a merchant-payment example, not a universal DVP rule. It shows why the parties should specify what counts as completion for each leg rather than treating submission as proof that all obligations are complete. ([source](<https://docs.btcpayserver.org/Users/invoices/>))

## What changes when crypto assets are involved

First determine whether the asset and payment use the same ledger or depend on separate systems. With separate ledgers, a bridge does not physically move an asset from one ledger to another. Depending on the bridge design, mechanisms such as locking, minting, burning, releasing, or swapping coordinate value across chains; the accounting and redemption path depends on that design. The settlement review should therefore identify what evidence or condition causes the destination-side process to act. ([source](<https://ethereum.org/developers/docs/scaling/sidechains/>))

Do not assume that a transaction’s appearance in a system is the same as completion. In Bitcoin, a transaction in a node’s mempool has no permanent ledger status until inclusion in a valid block on the accepted chain. Nodes maintain local mempools and can drop, replace, or later re-accept transactions according to their state and policies. This describes Bitcoin behavior, not a universal rule for every network. ([source](<https://developer.bitcoin.org/devguide/p2p_network.html>))

For the specific network and transaction, establish what confirmation or completion status the parties will recognize, which system reports it, and who monitors that system. Define what happens if the expected status does not arrive or if the parties’ systems report different states. The available evidence does not establish one confirmation, finality, or reversal model that applies across crypto networks, so a DVP label cannot fill in those transaction-specific details.

Also verify who controls the relevant wallets or accounts, what asset and representation the parties accept, and whether the intended recipient and payment destination are correctly specified. These are matters to resolve for the transaction. An onchain transfer or contract does not, by itself, show that a counterparty accepts the asset or that a separate payment obligation has been satisfied.

## Operational and legal dependencies to resolve

Document who initiates each leg, who checks the instructions, which system reports the relevant status, and who may act when a leg is delayed or fails. Identify the responsibilities of any provider or intermediary instead of assuming the protocol performs those functions. A protocol, wallet, application, and service provider can have distinct roles in a transaction; the parties should be clear about which component is responsible for each step.

Define the exception path before relying on the process. The parties should specify how they handle mismatched amounts or destinations, incomplete transfers, outages, delays, and disputes. Establish which instructions may be canceled or corrected, what evidence is used to assess each leg’s state, and who communicates decisions. A technical mechanism can coordinate the actions defined for it, but it does not supply undocumented procedures for every operational failure.

Review the governing documentation and applicable legal and compliance arrangements for the actual parties and jurisdictions. This explainer does not determine which law applies, whether a particular transfer is legally final, or which obligations attach to a specific institution. Those conclusions require transaction- and jurisdiction-specific review. Technical coordination does not substitute for that review, and requirements should not be assumed identical across jurisdictions.

## Limits of the DVP label

Calling a process DVP does not, by itself, establish legal finality, eliminate counterparty or operational risk, or prove that both legs will complete in every circumstance. A technical process may define how instructions and state transitions relate. The legal effect of those steps is a separate question that depends on the arrangement and its governing documentation.

A smart contract is only one possible component. A contract can execute encoded conditions, but the overall process may still depend on information or actions outside it. In the illustrative escrow model, for example, buyer confirmation is part of the process; the contract does not independently determine whether a physical item arrived. That limitation is one reason not to treat automation as proof that every underlying condition has been verified. ([source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>))

Security, recovery, availability, and control claims also need evidence specific to the system and arrangement; they do not follow from the DVP label. In a practical review, ask what links the two legs, what status counts as completion, who can intervene, and how failures and disputes are handled. Then distinguish the technical record of what happened from the legal effect assigned to it. These answers—not the acronym alone—show how asset delivery and payment are intended to occur together and where the arrangement’s dependencies remain.

## Sources and references

- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-19.
- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Sidechains](https://ethereum.org/developers/docs/scaling/sidechains/) — ethereum.org; retrieved 2026-10-18.
- [P2P Network — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
