---
title: "Decentralised Exchanges for Crypto: How It Works"
description: "Understand Decentralised Exchanges for Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verifica."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: ["decentralised exchanges crypto"]
author: "editorial_team"
primary_keyword: "decentralised exchanges for crypto"
owned_question: "How do decentralized exchanges for crypto work, and what infrastructure enables them?"
risk_level: "medium"
---

# Decentralised Exchanges for Crypto: How It Works

Decentralised exchanges for crypto are applications that coordinate digital-asset trades using blockchain-based components. The label does not describe one uniform architecture: an automated market maker (AMM), an on-chain order book, an auction, and an intent-based system can follow different paths from a user’s request to execution and settlement. Understanding the design means identifying where trade logic runs, where assets are held, how orders or liquidity are supplied, and which services sit between a user and the blockchain.

A useful starting point is the public permissionless DEX model discussed in Bank for International Settlements (BIS) research. In that model, a user can retain control of assets while trades execute or settle through smart contracts on a blockchain. This is a distinction from the common centralized-exchange model, where assets are deposited and trading can occur internally. It is not a claim that every DEX has the same custody arrangement or that every component is decentralized.

## What Decentralised Exchanges for Crypto means

A decentralized exchange (DEX) is a crypto-trading application whose execution or settlement relies, at least in part, on blockchain-based mechanisms rather than only on an exchange operator’s internal ledger. The system boundary can include a user’s wallet, an interface, smart contracts, liquidity or order-management mechanisms, blockchain validators, and sometimes additional services such as relayers or off-chain order components.

The boundary matters because the word “decentralized” can refer to different properties. It may describe who controls assets, where trade rules are enforced, how transactions are ordered, or who can change the software. Those properties do not necessarily move together. BIS research notes that DEX designs can still depend on interfaces, relayers, administrators, or off-chain order components, even where users retain asset control during execution or settlement.

The AMM model is one documented example, not a definition of every DEX. In the AMM model discussed in BIS Working Paper 1227, smart contracts and liquidity pools implement trading, and transactions settle when included in a blockchain block. Order-book, auction, intent-based, cross-chain, and hybrid designs can use different execution paths. Therefore, a description of one AMM should not be generalized to the entire category.

## Core components of Decentralised Exchanges for Crypto

A practical architecture map separates the following components and asks what each one does:

- **User and wallet:** The user chooses an action and authorizes a transaction through a wallet or another signing mechanism. The wallet’s role and custody arrangement depend on the specific implementation; the general DEX label does not establish them.
- **Interface:** A website or application may display markets, balances, quotes, and transaction controls. An interface can help construct or submit a request without being the component that enforces settlement. Interfaces may also be a dependency, so teams should identify who operates them and whether another route to the contracts exists.
- **Trade mechanism:** An AMM may use smart contracts and liquidity pools. Other designs may use order books, auctions, intents, or hybrid arrangements. The mechanism determines how a request is matched or priced, but the source pack does not establish a single universal algorithm or quote guarantee.
- **Smart contracts:** In an AMM model, contracts implement the trading mechanism. Their exact responsibilities, upgrade controls, and dependencies are implementation-specific and need direct verification.
- **Liquidity or orders:** A pool-based design depends on liquidity being available to execute trades. An order-based design depends on orders and the systems that submit, match, or relay them. These are different operational dependencies, not interchangeable descriptions.
- **Blockchain and block inclusion:** In the cited AMM model, settlement occurs when a transaction is included in a blockchain block. The chain therefore forms part of the execution environment; a request submitted to an interface is not, by itself, proof of completed settlement.
- **Supporting operators and governance:** Relayers, administrators, interface operators, or other actors may influence parts of a design. Changes to the underlying network can also require coordination. For Ethereum, protocol changes involve proposal, technical review, implementation, coordination, and adoption across network stakeholders; other networks may use different processes.

This map is a set of questions, not an assertion that every DEX contains every component. A team should document the actual system it is evaluating rather than infer architecture from a product label.

## How Decentralised Exchanges for Crypto works

A typical AMM-oriented path can be described at a high level, with an important limit: the precise steps and responsibilities depend on the implementation.

1. **The user prepares a trade request.** The user selects the relevant assets and action in an interface or other client. The client may obtain information from on-chain state or additional services; the source pack does not establish one standard data path for all DEXs.
2. **The request is authorized and submitted.** A wallet or signing mechanism may authorize the transaction, which is then submitted toward the relevant blockchain contract. Teams should verify which component constructs the transaction, which party submits it, and whether any relayer or off-chain order component is involved.
3. **The trading mechanism processes the request.** For the AMM model discussed by BIS, smart contracts and liquidity pools implement trading. This differs from an order-book, auction, intent-based, cross-chain, or hybrid design, where the execution path may be different.
4. **The transaction is included in a block.** In the cited AMM model, the trade settles when its transaction is included in a blockchain block. Submission and settlement are therefore distinct events: a request can be pending before inclusion, and a displayed interface status should be checked against the relevant transaction and chain state.
5. **The resulting state can be checked.** Verification should identify the transaction and the relevant contract or chain state, rather than rely solely on an interface message. The exact evidence available and its interpretation depend on the chain and implementation.

The steps clarify what “on-chain” can and cannot mean. A trade may use on-chain smart contracts for execution or settlement while discovery, order formation, interface access, or other parts rely on off-chain services. Conversely, the existence of a blockchain transaction does not independently establish that every surrounding service is decentralized or operated without privileged control.

## Trust and control boundaries

The central trust question is not simply “Is this a DEX?” It is “Which actor or component can affect each stage?” Separate asset control, transaction authorization, trade execution, settlement, interface access, and software changes.

In the public permissionless DEX model compared by BIS, users can retain control of assets while trades execute or settle through smart contracts. That statement is scoped to the model; it should not be expanded into a guarantee about all DEXs, all assets, or every operational path. BIS also notes dependencies that may include interfaces, relayers, administrators, or off-chain order components. A user may interact with a blockchain-based contract through a service whose availability or behavior is controlled elsewhere.

The broader crypto ecosystem can exhibit substantial de facto centralization even when its stated architecture or ethos emphasizes decentralization, according to BIS. The degree and location of concentration must be assessed for a specific network, asset, application, and time window. For a DEX review, that means tracing control rather than relying on branding: who can alter a contract, operate the main interface, relay or filter requests, provide critical data, or coordinate upgrades? The source pack does not answer those questions for any particular application.

Network-level change is another boundary. On Ethereum, a protocol change requires proposal, technical review, implementation, coordination, and adoption across network stakeholders. This describes Ethereum’s EIP and network-upgrade process, not a universal governance template. Other cryptocurrency networks may use formal voting, foundation or company control, or informal coordination. An application’s own administration and the underlying network’s governance should therefore be evaluated separately.

## Limitations and failure modes

A DEX label does not guarantee uninterrupted access, successful execution, a particular level of liquidity, or uniform control over all components. The accepted evidence establishes variation in design and potential dependencies, but it does not provide product-specific security, performance, fee, or recovery guarantees.

Potential points of operational failure follow from the architecture. An interface may be unavailable even if contracts remain on a blockchain. A relayer or off-chain order component may be a dependency where the design uses one. In an AMM model, the mechanism relies on liquidity pools; a request’s outcome is not established merely by the existence of a pool. At the chain layer, the cited model ties settlement to block inclusion, so a submitted request and a settled transaction must not be treated as the same state. These are dependency checks, not predictions that a particular failure will occur.

There is also a performance distinction between centralized and decentralized models. BIS describes centralized exchanges as able to provide near-real-time trading, liquid order books, and advanced order functionality after assets are deposited. Performance and liquidity vary by venue, asset pair, and market conditions. This comparison does not establish that every centralized exchange has those qualities or that every DEX lacks them; it identifies differences in common operating models, not a universal ranking.

Finally, the degree of decentralization cannot be inferred from the stated ethos alone. BIS’s systemic assessment warns of possible de facto concentration, with the degree and location varying by network, asset, application, and time window. A responsible evaluation records the date and scope of observations instead of treating a one-time architecture diagram as permanent evidence.

## What teams should verify

For an operational or technical review, build an evidence record around the specific DEX, network, asset, and time period under consideration:

1. **Identify the design.** Determine whether the application uses an AMM, order book, auction, intent-based, cross-chain, or hybrid path. Do not assume an AMM workflow applies to other models.
2. **Trace the transaction.** Document how a user request is formed, authorized, submitted, processed, and settled. Identify the point at which the system treats a trade as settled and what evidence confirms that state.
3. **Map custody and control.** Establish where assets are held before, during, and after execution, and which actors can affect them. Do not infer custody from the word “decentralized.”
4. **List external dependencies.** Check for interfaces, relayers, administrators, off-chain order components, or other services. Record what happens to the user path if each dependency is unavailable; do not assume an alternative route exists without evidence.
5. **Inspect liquidity or order dependencies.** For a pool-based AMM, verify which pools the workflow uses. For other models, identify the relevant order, matching, or auction mechanisms. The source pack does not support a universal liquidity measure or execution guarantee.
6. **Separate application and network governance.** Record who can change application components and how the underlying network handles protocol changes. For Ethereum, account for proposal, technical review, implementation, coordination, and adoption; do not transfer that process to other networks without evidence.
7. **Assess concentration in context.** Specify the network, asset, application, and time window for any claim about operational concentration. Revisit the assessment when the system changes.
8. **Use primary evidence for current specifics.** Confirm current contract behavior, interfaces, supported assets, fees, availability, and recovery procedures in relevant official documentation or other suitable primary evidence. The accepted claims here do not establish those product-specific facts.

The result should be an architecture and dependency map, not a blanket verdict. Decentralised exchanges for crypto can use blockchain-based contracts to execute or settle trades while relying on different combinations of wallets, interfaces, pools, orders, relayers, administrators, and network processes. The useful technical question is which component performs each function, what evidence shows that it did so, and which assumptions remain outside the protocol’s documented behavior.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
