---
title: "Blockchain graphic: What to show in a payment-flow diagram"
description: "Learn what a blockchain graphic should show about payment initiation, network validation, recording, and settlement—and where a simplified visual may mislead."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["blockchain_payment_foundations"]
tags: ["blockchain diagram", "blockchain payment flow"]
author: "editorial_team"
primary_keyword: "blockchain graphic"
owned_question: "What should a blockchain payment graphic show to explain how a payment moves from initiation through network validation to recorded settlement?"
risk_level: "medium"
---

A useful blockchain payment graphic should show who initiates and authorizes a payment, how its request reaches the relevant network, how the network validates and records it, and whether a separate application or merchant confirmation follows. Label the diagram as conceptual unless it depicts a documented transaction, and do not equate a recorded transaction with every form of business settlement or confirmation.

## What a blockchain graphic can explain about payments

A blockchain payment graphic is a visual model of selected steps in a payment flow. It can help readers see the order of actions and the roles involved, but the drawing is not itself proof that a transaction happened. A conceptual diagram describes a process; it should not be represented as a transaction record or evidence that a particular payment settled.

The flow depends on the network and the application around it. For example, an Ethereum state-changing contract interaction is described as a signed transaction that is broadcast, selected for a block, executed, and later gains stronger confirmation or finality. This is a documented network-specific lifecycle, not a universal template for every blockchain or payment service. **[source](<https://ethereum.org/developers/docs/transactions/>)**

A diagram should state what it covers and name the network when it relies on specific network mechanics. If it leaves out a stage, groups actions into one box, or uses simplified arrows, explain that choice in a note. A generic visual should not imply that all networks validate, record, or confirm payments in the same way.

Treat each box as a claim about the process. “The customer submits a request” describes an action by a participant; “the network records a transaction” describes a network event; and “the merchant accepts the payment” describes a decision that may belong to an application or business process. Keeping these claims separate helps a reader avoid assuming that one automatically establishes the others.

A useful graphic also identifies its intended level of detail. A high-level diagram may show only initiation, network processing, and a receiving application. A more detailed one may distinguish construction, authorization, broadcast, inclusion, execution, and later confirmation. Either can be useful if the captions make clear what has been condensed or left out. Avoid adding technical-looking boxes merely to make the visual appear complete when the evidence does not support their meaning.

## Show the payment flow from initiation to recording

A left-to-right sequence is one way to make the flow readable. At each stage, label the actor and action rather than relying on unexplained arrows.

1. **Initiation:** Show the sender or initiating system preparing a payment request. If the graphic is about a specific implementation, it may distinguish wallet creation, transaction construction, and signing. One documented developer-wallet tutorial separates those activities, with transaction construction involving a blockchain node and signing handled through a server-side SDK. That is an implementation example, not a required architecture for all payments. **[source](<https://developers.circle.com/wallets/sign-tx-evm>)**
2. **Authorization and submission:** Show the relevant authorization step and the request being sent toward the network. Use a labeled arrow for the transaction request; do not make it appear that an asset travels through a physical pipeline.
3. **Validation and recording:** Identify the network step that checks and records activity, using terminology supported for the named network. For the cited Ethereum state-changing interaction, the lifecycle includes broadcast, selection for a block, execution, and stronger confirmation or finality later. Do not add a guaranteed time to any stage unless the evidence for the specific context supports it. **[source](<https://ethereum.org/developers/docs/transactions/>)**
4. **Application or merchant response:** If an application or merchant reacts to network activity, represent that as a separate stage. A payment integration may distinguish statuses such as processing and settled, as well as partial, overpaid, expired, invalid, or late. These are documented BTCPay invoice states, not universal labels or protocol states. **[source](<https://docs.btcpayserver.org/Users/invoices/>)**

The distinction between network recording and application confirmation matters because the two can represent different checks. A merchant may apply its own configured acceptance conditions in addition to observing network activity. If the diagram does not model those conditions, say so rather than showing network recording as automatic business approval.

The sequence should also show where the diagram stops. For example, it may end at a network record, at an application notification, or at a merchant’s own acceptance decision. These endpoints answer different questions. A graphic ending at network inclusion should not imply that it has also depicted the receiving application’s status handling or the merchant’s business decision.

## Label participants, messages, and value movement

Include only the participants needed to explain the chosen flow. Depending on the example, labels may include a sender, recipient, wallet or initiating service, network, and merchant or receiving application. Do not place an application, wallet, merchant, or provider inside a “protocol” box unless the depicted design actually makes it part of that protocol.

A clear legend can distinguish three kinds of movement:

- **Instructions or transaction data:** A request asking the network to process an action.
- **Asset or value accounting:** A visual representation of what changes in the payment flow. The arrow is a diagram convention; it is not evidence of physical movement.
- **Status messages:** Signals such as submitted, included, processing, or confirmed. Define these labels for the depicted context instead of treating them as interchangeable.

The arrows need not all mean the same thing. A request sent to a network, an accounting change represented in a network record, and a status returned to an application are different relationships. Give them different line styles, colors, or labels, and explain the visual key. If the graphic uses one arrow style for every relationship, captions should still distinguish what each arrow represents.

When illustrating Bitcoin transaction structure, a diagram can show an input referring to a specific prior output by the prior transaction hash and output index. This can explain how the transaction connects to earlier recorded activity. It is a Bitcoin-specific structural detail and should not be generalized to account-based networks or treated as a complete account of wallet ownership. **[source](<https://developer.bitcoin.org/reference/transactions.html>)**

For a network-specific graphic, identify the network and asset representation when known. Do not imply that assets with the same name or symbol necessarily have identical transfer mechanics across networks. If the available evidence does not establish a detail, omit it or mark it as an assumption rather than filling the gap with a generic blockchain icon.

Keep participant identity distinct from the address or key shown in a visual. A diagram may represent a sender and recipient as roles in a process, but an address label alone should not be presented as proof of a person’s identity. If identity is outside the graphic’s scope, state that rather than letting a person-shaped icon imply verification.

## Make validation and settlement limits visible

Use stage labels carefully. “Submitted” can describe an action by a wallet or service; “recorded” can refer to a network-history event; and “confirmed” or “final” should be used only when the relevant network’s definition supports that meaning. If evidence says a transaction gains stronger confirmation or finality later, show that as a distinct stage rather than implying that it happens at broadcast. **[source](<https://ethereum.org/developers/docs/transactions/>)**

Settlement can mean different things in different contexts. In the documented BTCPay invoice example, an invoice records a requested amount and a time-limited exchange rate while distinguishing awaiting payment, processing, settled, expired, invalid, partial, overpaid, and late states. A diagram that uses those terms should identify them as that implementation’s labels, not universal protocol states. **[source](<https://docs.btcpayserver.org/Users/invoices/>)**

If the diagram depicts a rollup, name the architecture and preserve the scope of its documented flow. The cited Ethereum optimistic-rollup pattern describes execution and state storage off Ethereum, transaction data and results published to Ethereum, and a challenge process for disputed state transitions. A simplified visual should not present this as a flow shared by all networks or suggest that including a challenge process establishes the safety or outcome of a particular payment. **[source](<https://ethereum.org/developers/docs/scaling/optimistic-rollups/>)**

A graphic should mark any confirmation or settlement condition it omits. For instance, a box labeled “recorded” does not tell the reader what confirmation policy a merchant uses. If a diagram shows only one network event, use a note such as “application acceptance conditions not shown” rather than suggesting that the visual resolves those conditions.

A flow diagram also cannot establish who controls a key, the legal identity of a participant, whether an off-chain obligation has been fulfilled, or whether a recorded action can be recovered. These questions are outside what the pictured payment sequence alone can demonstrate. Do not use a final-looking check mark or “complete” label unless the graphic defines what completion means and supports that meaning for its context.

## Use blockchain payment graphics responsibly

Before publishing, check that each network-specific stage is supported by documentation for the depicted system. Label an example “illustrative” unless it is based on a documented transaction, and explain the basis for any actual transaction shown. Do not invent a transaction, test result, confirmation time, fee, or outcome to make the diagram look concrete.

Review arrows and symbols as carefully as captions. A single arrow labeled “payment” may blur a signed instruction, a network record, an asset-accounting change, and an application status. Separate them when the distinction affects interpretation. Add a note when stages are omitted, combined, or shown only at a conceptual level.

Make the graphic’s assumptions explicit. Name the network when the mechanics are network-specific, identify whether a status label belongs to a protocol or an application, and describe any implementation example as such. If a caption includes a fee, timing, security, availability, recovery, or compliance statement, check that it is supported for the relevant network, service, or context. Do not present variable or context-dependent outcomes as universal facts.

Finally, keep the conclusion proportional to the visual. A diagram can explain a selected payment flow, but it cannot by itself prove that the flow occurred, that a merchant accepted the payment, or that a transaction satisfies an organization’s settlement conditions. A concise scope note helps readers understand both what the graphic shows and what it leaves unresolved.

## Sources and references

- [Transactions Reference](https://developer.bitcoin.org/reference/transactions.html) — Bitcoin Developer Reference; retrieved 2026-10-19.
- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-19.
- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-19.
- [Optimistic rollups](https://ethereum.org/developers/docs/scaling/optimistic-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Sign Transactions on EVM Chains](https://developers.circle.com/wallets/sign-tx-evm) — Circle; retrieved 2026-10-19.
