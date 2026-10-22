---
title: "Crypto Tokens Examples: Named Assets and Their Protocol Roles"
description: "Explore crypto tokens examples by protocol role, with concise descriptions of named assets and context for understanding their functions."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "crypto tokens examples"
owned_question: "What are representative examples of crypto tokens, and what does each example illustrate about a token’s function?"
risk_level: "medium"
---

Representative crypto-token examples are easiest to understand by looking at the specific role a protocol or application documents for them: serving as pool inventory, appearing in a cross-chain transfer, or being handled as part of an application session. These examples illustrate particular mechanisms, not a complete inventory or an endorsement. The same token label does not establish identical functions, rights, or mechanics across systems.

## Crypto tokens examples, grouped by protocol role

This reference groups examples by the task they perform in a documented workflow, rather than by price, popularity, or a broad token taxonomy. A token’s function depends on its protocol or application. For each example, the useful questions are: which system is involved, what does the token do there, and which parts of the workflow are specific to that system?

The examples are deliberately narrow. A token or token representation being used in a technical process does not, by itself, establish legal ownership, enforceable claims, backing, redemption, or value. Those matters require evidence about the specific arrangement. The examples below focus on operational roles that the available documentation describes.

## Examples used for protocol access and network services

**A destination token in an onramp session.** A secure onramp integration can use a server-created session token to bind destination-wallet information to a short-lived purchase session without exposing backend API credentials in the browser. This is an example of a session mechanism in an application flow. It does not establish that the destination crypto token grants general access to a network, nor does it guarantee that a purchase will complete. The session details and security controls vary by provider and version. [source](<https://github.com/coinbase/onramp-demo-app>)

This distinction matters when reading product or integration documentation. “Token” in the session description refers to a credential-like mechanism that carries session information; it is not necessarily the same thing as the cryptocurrency being purchased or transferred. To understand either role, identify the object being described and the system that handles it. The cited example supports only the specific function of binding wallet information to a purchase session.

**ETH as a fee asset in an Ethereum-family token transfer.** In an ordinary Ethereum-family token transfer, the sender uses the same network as the recipient and holds enough native ETH to cover the transaction fee, unless a supported sponsored-fee mechanism applies. This is a limited operational example about a transfer flow. It does not establish that every token action, every application, or every blockchain uses the same fee asset or payment arrangement. [source](<https://ethereum.org/guides/how-to-use-a-wallet>)

Taken together, these cases illustrate different roles within a workflow: one mechanism binds destination information to an application session, while another involves the network’s native asset covering a transaction fee. Neither example is a general rule for all tokens. Check the relevant provider or protocol materials before assuming that an asset is required, that a fee can be sponsored, or that a session token is the asset itself.

## Examples used in governance and protocol coordination

No named governance-token example is included in this reference. The allowed evidence does not establish a particular token’s voting rights, eligible decisions, or participation rules. Naming an example without that support could suggest a wider role than the documentation demonstrates.

For any governance example, the important distinction is between a label and the documented authority. A token name alone does not specify what holders can propose or vote on, whether participation is conditional, or how a decision is carried out. Those details must be checked against the relevant protocol’s materials. This section therefore avoids treating governance tokens as a uniform category or implying that ownership of any token guarantees influence or a particular outcome.

## Examples connected to applications and digital services

**Tokens as inventory in a Uniswap v2 liquidity pool.** A Uniswap v2 pool uses deposited reserves of a token pair as the inventory from which swaps execute, while liquidity-provider shares represent contributions to that pool. This is one constant-product automated market maker (AMM) example. An AMM is a trading mechanism that uses pool assets rather than describing every possible exchange design; the example should not be generalized to all decentralized exchanges. Other AMMs can use different curves, assets, fees, and accounting. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The practical point is that the tokens in this example are assets held as pool reserves and used in swaps. The liquidity-provider share represents a contribution under this particular pool model; it should not be confused with either token in the pair. The documented pool mechanism does not, on its own, establish a universal accounting rule or any broader claim about rights associated with a token.

**A token representation in a cross-chain transfer.** Cross-chain asset transfers can use lock-and-mint, burn-and-mint, or atomic-swap and liquidity-network mechanisms. A destination-chain token may therefore be a representation coordinated with activity on another ledger, rather than an asset physically moved between ledgers. The exact accounting and redemption path depends on the bridge design. The term “bridged token” alone does not establish a uniform claim, backing arrangement, or redemption right. [source](<https://ethereum.org/developers/docs/bridges>)

A bridge coordinates activity between separate blockchain environments. That high-level description is not enough to infer which mechanism a particular transfer uses: a design may lock one representation and mint another, burn and mint, or rely on swaps and liquidity. To interpret a specific example, identify the bridge and the transfer mechanism it documents rather than assuming all destination tokens work alike.

**Destination funds advanced by a relayer.** In Across Protocol’s documented intent lifecycle, relayers can provide destination-chain funds before later reimbursement. Periodic rebalancing is used to keep chain pools sufficiently funded. This is one cross-chain liquidity model, not a description of every bridge or token transfer. [source](<https://docs.across.to/guides/concepts/intent-lifecycle>)

The relayer example helps separate the token a user receives on a destination chain from the operational path used to make funds available there. In this documented model, destination funds can be provided before reimbursement; the timing and pool coordination are part of the system’s lifecycle. Other bridges may use different patterns, so this example should be read as an implementation-specific illustration, not a universal bridge rule.

Across these application examples, tokens can serve as swap inventory, appear as representations coordinated across ledgers, or be delivered through a relayer-funded flow. Those descriptions explain specific technical roles. They do not establish that a token conveys ownership of an external asset, a redemption claim, or other rights beyond what the relevant arrangement documents.

## How to read a token example without assuming what it guarantees

Start by identifying the system and the precise object its documentation calls a token. A session token, a network fee asset, a pool reserve, a destination-chain representation, and funds advanced by a relayer are not interchangeable concepts. The name alone may not tell you which role is meant.

Then trace the described workflow. For an onramp, determine whether the documentation is discussing a session mechanism or the crypto asset involved. For a pool, distinguish the pair’s reserves from the provider’s recorded contribution. For a cross-chain transfer, check which bridge mechanism coordinates activity and how its documentation describes the destination-side asset or funds. These checks keep a narrow example from being mistaken for a general token rule.

Finally, separate technical function from conclusions about rights, backing, or redemption. A lock-and-mint description, for example, identifies a transfer pattern but does not by itself specify a holder’s legal claim or complete redemption path. Similarly, a pool or relayer mechanism describes how one application operates; it should not be projected onto unrelated tokens or protocols.

The examples here are illustrative and limited to their documented contexts. They are not a complete list or a recommendation. Where the available evidence does not establish governance rights, backing, redemption, or other guarantees for a named token, those conclusions should remain open rather than being inferred from the token’s label or its use in a technical workflow.

## Sources and references

- [Coinbase Onramp demo app](https://github.com/coinbase/onramp-demo-app) — Coinbase; retrieved 2026-10-19.
- [How to Use Ethereum Wallets](https://ethereum.org/guides/how-to-use-a-wallet) — ethereum.org; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [Intent Lifecycle in Across](https://docs.across.to/guides/concepts/intent-lifecycle) — Across Protocol; retrieved 2026-10-18.
