---
title: "What Is an NFT Marketplace? Listings, Transfers, and Settlement"
description: "Learn how NFT marketplaces index tokens, create listings, use approvals, settle transfers, charge fees, handle royalties, and display metadata."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["nfts-and-digital-ownership"]
tags: ["NFT marketplace meaning", "how NFT marketplaces work", "NFT listing", "NFT marketplace settlement", "NFT marketplace fees"]
author: "editorial_team"
primary_keyword: "nft marketplace"
owned_question: "What is an NFT marketplace, and how do listing, transfer, fees, and settlement work?"
risk_level: "medium"
---

An NFT marketplace is a system for discovering, listing, buying, and selling non-fungible tokens. It typically combines a website or app, blockchain indexers, wallet connections, order storage, marketplace smart contracts, and transaction monitoring. The marketplace helps users coordinate a trade, while the NFT contract remains the authoritative onchain registry for token ownership.

That distinction matters. A listing displayed on a marketplace is not itself proof that a sale has occurred. A product image is not the NFT. A marketplace account is not necessarily the wallet that controls the token. To understand a transaction, a user needs the NFT contract address, token identifier, current owner, approval state, signed order terms, settlement contract, and blockchain result.

## What an NFT marketplace does

An NFT marketplace makes blockchain records usable as a catalog and trading workflow. Its indexers read token contracts, ownership changes, listings, bids, and sale events. Its interface groups that data into collection pages, search results, price displays, and wallet actions.

On the trading side, the system lets a seller state what asset is offered and what payment or other consideration is required. It may store a signed order offchain until a buyer accepts it, run an onchain auction, place the token in escrow, or combine those methods. When a trade is fulfilled, smart-contract logic coordinates payment and token transfer according to the order.

A marketplace can also apply moderation, collection verification, sanctions controls, content policies, and interface restrictions. Those choices affect what its website displays, but they do not necessarily remove a transferable token from its blockchain contract or from every other compatible interface.

## What the NFT contract records

On Ethereum, ERC-721 is a widely used non-fungible-token interface. A token is identified by the combination of its contract address and token ID. The standard includes functions for checking the owner of an ID, transferring ownership, approving one address for a token, and authorizing an operator to manage all of an owner's tokens.

These approvals are what allow many marketplaces to settle a sale without taking custody at listing time. The owner can authorize a marketplace transfer contract, sign an order, and keep the NFT in the wallet while the listing is active. At fulfillment, the settlement contract uses the approval to transfer the token under the signed terms.

Approval is powerful authority. A token-specific approval normally covers one NFT, while an operator approval can cover every compatible NFT held by that owner for that contract. Wallet interfaces should show the spender, scope, chain, and contract involved. Canceling a marketplace listing and revoking a token approval are related but not always the same action.

ERC-721 also defines an optional metadata interface. A token URI can point to a JSON document containing a name, description, image location, and attributes. The ownership record is onchain, but the media and metadata may be stored on a web server, content-addressed network, another chain, or directly in contract data.

## How an NFT listing is created

In a common non-custodial order model, the seller first connects a wallet and selects a token. The marketplace checks the token's contract, ownership, and current approval state. If necessary, the seller submits an onchain approval transaction for the marketplace's transfer or settlement contract.

The seller then signs listing terms. These can include the NFT contract and token ID, price, accepted payment asset, start and expiration times, marketplace or creator recipients, quantity for semi-fungible assets, and conditions for cancellation or partial fulfillment. A signature can authorize those terms without immediately transferring the NFT.

The marketplace may store and distribute the signed order through an offchain database or order-relay network. This makes browsing and price updates cheaper than writing every listing to the blockchain. However, an offchain order can become unfulfillable if the seller transfers the NFT, revokes approval, spends required assets, or invalidates the order.

Seaport, the marketplace protocol documented by OpenSea, illustrates this structure with an **offer** containing what one party will provide and **consideration** containing what must be received. It is one implementation, not a universal NFT marketplace specification.

## How a sale is fulfilled and settled

A buyer or another fulfiller submits a blockchain transaction referencing the order. Before transferring anything, the settlement logic checks the signature and order conditions. It also needs the seller to still own the NFT and the contract to have sufficient transfer authority. Expiration, cancellation, payment balance, token restrictions, or changed ownership can make the transaction fail.

If the checks pass, a settlement contract can move the NFT to the buyer and distribute payment among the designated recipients in one transaction. Atomic execution means the related transfers either complete under the transaction's rules or revert together. Exact behavior depends on the marketplace protocol, chain, token contracts, and order type.

After inclusion in a block, indexers observe ownership and transfer events and update the interface. A marketplace may show an item as sold before every external service considers the block final. Applications should define their own confirmation policy and handle chain reorganizations or delayed indexing.

The blockchain transaction is the settlement evidence for an onchain sale. A webpage status, email, or wallet notification is only an interpretation of that transaction and can be stale or misleading.

## Marketplace fees, gas, and royalties

Several costs can appear in one NFT trade, and they should not be combined into one unlabeled percentage.

- A **marketplace fee** pays the platform or protocol recipient under the order terms.
- A **network fee** pays for blockchain execution and can vary with transaction complexity and network conditions.
- A **creator royalty** may direct part of a sale to a creator or rights holder.
- A **payment conversion or service fee** can arise outside the NFT settlement when another provider handles cards, fiat, bridging, or asset conversion.

ERC-2981 gives compatible contracts a standard way to return a royalty recipient and royalty amount for a stated sale price. The standard is intentionally limited: it communicates royalty information, but it cannot determine that every token transfer is a sale, and payment is voluntary unless a marketplace or another mechanism enforces it. A wallet-to-wallet transfer therefore should not be assumed to generate a royalty.

Fee and royalty displays should identify the calculation basis, recipient, payment asset, and point of collection. A quoted sale price can exclude gas or external service charges.

## Custodial and non-custodial marketplace models

A non-custodial listing usually leaves the token in the seller's wallet until fulfillment. The trade still depends on signed orders, approvals, smart contracts, indexing, and an interface. Non-custodial does not mean trust-free: upgrade keys, pause controls, order validators, frontends, and metadata services can remain important.

A custodial or escrow model transfers the NFT or payment to an intermediary contract or service before final settlement. That can support auctions, delayed delivery, fiat payments, dispute processes, or managed accounts, but it changes who controls the asset and which failure modes apply.

Some systems are hybrid. A token can remain in a wallet while an operator controls which orders are published; payment can settle onchain while identity and compliance checks occur offchain. The useful question is who controls each stage, not whether a platform applies one decentralization label to the whole product.

## Metadata, media, and authenticity

Owning an NFT generally means controlling the token recorded by its smart contract. It does not automatically mean owning the copyright, trademark, physical item, domain, or every usage right associated with the referenced media. Those rights depend on the issuer's terms, applicable law, and any separate agreement.

The marketplace also has to decide which collection is authentic. A name and image can be copied into another contract, so users should verify the contract address and issuer evidence rather than relying on visual similarity. Marketplace verification badges are platform judgments, not blockchain-level proof of legal authorship.

Metadata introduces availability risk. A token URI can change when a contract permits updates, and a remote server can disappear or return different content. Content-addressed storage improves integrity checking, but persistence still depends on continued hosting or pinning. Onchain media reduces some dependencies while increasing storage cost and design constraints.

## Operational checks before using a marketplace

A neutral review should start with the exact chain, NFT contract, token ID, settlement contract, and payment asset. Then inspect the control flow:

- What permission does the wallet approval grant, and how can it be revoked?
- Is the listing an offchain signed order, an onchain record, or an escrow deposit?
- What invalidates or cancels an order?
- Which contract moves the token and distributes payment?
- Which marketplace fees, royalties, network fees, and conversion charges apply?
- Where are metadata and media stored, and can their references change?
- Which administrator, upgrade, pause, moderation, or recovery controls exist?
- What does token ownership represent under the issuer's stated terms?

These checks describe the real product boundary. An NFT marketplace is not merely an online gallery: it is an indexing, authorization, order, settlement, and presentation system built around token contracts. Understanding each layer is more reliable than assuming that one screen proves ownership, authenticity, finality, or legal rights.

## Sources and references

- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Non-fungible tokens (NFT)](https://ethereum.org/nft/) — ethereum.org; retrieved 2026-10-18.
- [Seaport](https://docs.opensea.io/docs/seaport) — OpenSea Developer Documentation; retrieved 2026-10-18.
- [ERC-2981: NFT Royalty Standard](https://eips.ethereum.org/EIPS/eip-2981) — Ethereum Improvement Proposals; retrieved 2026-10-18.
