---
title: "How Do NFTs Work? Tokens, Metadata, Ownership, and Transfers"
description: "Learn how NFTs use smart contracts, token IDs, owner records, metadata, and transfer rules, and why owning an NFT does not automatically transfer copyright."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["nfts-digital-ownership"]
tags: ["how NFTs work", "NFT token ID", "NFT metadata", "ERC-721", "NFT ownership"]
author: "editorial_team"
primary_keyword: "how do nfts work"
owned_question: "How do NFTs represent token identifiers, ownership records, and transfer rules on a blockchain?"
risk_level: "medium"
---

An NFT, or non-fungible token, is a distinguishable token record managed by a smart contract. The contract associates a token identifier with an owner address and defines how the token can be created, approved, transferred, or destroyed. Metadata may describe an image, item, membership, ticket, game object, or other subject, but that subject is not necessarily stored in the token or on the blockchain.

Understanding an NFT therefore requires separating four layers: the onchain token, its metadata, the referenced content or asset, and any legal or application rights attached through separate terms.

## An NFT is a unique ledger record

Under ERC-721, an NFT is identified by the combination of a smart-contract address and a token ID on a particular chain. The token ID needs to be unique only within that contract. Token number 10 in one contract is unrelated to token number 10 in another.

The contract maintains a mapping from valid token IDs to owner addresses. Calling a function such as `ownerOf(tokenId)` returns the address recorded as the token's owner. This is blockchain ownership of the token record. It does not automatically identify a real-world person, prove that the minter created the referenced work, or establish ownership of a physical object.

Non-fungible means tokens are individually distinguishable. It does not mean every NFT is valuable, scarce in an economic sense, legally unique, or linked to unique media. Multiple NFTs can refer to the same image, and identical media can be referenced by tokens in different contracts.

## What minting creates

Minting is the contract operation that creates or recognizes a token ID and assigns its initial owner. In ERC-721, creation is normally represented by a `Transfer` event from the zero address to the first owner. The contract may restrict minting to an administrator, allow public minting under stated conditions, or use other application-specific rules.

Minting can also set or reveal metadata, but the token operation and content creation are different events. An artist might create a file before minting. A game might generate attributes during minting. A contract might reveal metadata later. In each case, the blockchain records what the contract did; it does not independently verify authorship, authenticity, factual claims, or rights in the referenced material.

Supply rules also come from the contract. A token ID may be one of a fixed collection, created on demand, burnable, replaceable, or governed by an upgradeable contract. Scarcity claims must be checked against the actual contracts, administrator powers, related collections, and metadata behavior.

## Metadata connects the token to content

The ERC-721 metadata extension lets a contract return a `tokenURI` for a token ID. The URI commonly points to JSON containing a name, description, attributes, and another URI for an image, video, animation, or other media. Wallets and marketplaces read this information to render the NFT.

Storage can take several forms:

- **Fully onchain:** metadata and sometimes media are encoded or generated from blockchain data.
- **Content-addressed:** the URI identifies content by a cryptographic hash through a system such as IPFS. Integrity can be checked, but continued availability still requires storage and retrieval.
- **Ordinary web hosting:** an HTTPS URL serves metadata or media from a domain. The operator may change, remove, or stop serving it.
- **Mutable contract-controlled URI:** an administrator or contract function can change where the token points. This may support reveal or correction, but it also changes persistence assumptions.

A content hash can show whether retrieved bytes match an expected file. It does not prove who created the file, whether the content is lawful, or what rights accompany the token.

## How NFT ownership and transfer work

The owner can normally transfer an ERC-721 token or approve another address to act. A per-token approval authorizes an address for one token. An operator approval can authorize an address, such as a marketplace contract, to manage all of an owner's NFTs in that collection. Broad approvals are powerful and are a common security boundary.

A transfer transaction asks the contract to replace the recorded owner. The contract checks that the sender is the owner or an authorized operator, validates the recipient and token, updates state, clears the token-specific approval, and emits a `Transfer` event. Safe transfer functions also ask a recipient smart contract to confirm that it can receive ERC-721 tokens; otherwise the transfer reverts.

A marketplace usually does not rewrite the NFT standard. It coordinates orders, signatures, payment, approvals, fees, and settlement, then calls the token contract. Custodial marketplaces may instead hold the token in their own address while tracking user entitlements offchain. The exact custody and settlement path must be identified.

## ERC-721 and ERC-1155

ERC-721 is designed around individually owned token IDs. A contract commonly represents one collection, and each valid token ID has one owner.

ERC-1155 is a multi-token standard. One contract can manage many token types, and each token ID can have balances and supply. A token type with supply one can behave as non-fungible; a token type with many interchangeable units can be fungible or semi-fungible. ERC-1155 also supports transferring multiple token IDs and quantities in one batch.

The standard affects interfaces and accounting, not the meaning of the item. Either standard can represent access, game objects, collectibles, receipts, or other application-defined interests. A wallet must inspect the contract and standard rather than infer behavior from an image or collection name.

## Token ownership is not copyright ownership

Owning an NFT means the relevant contract records an address as owner of the token. It does not automatically convey copyright, trademark rights, a licence, ownership of a physical object, or exclusivity over the referenced media.

The joint U.S. Copyright Office and USPTO report explains that transferring an NFT does not necessarily transfer the associated asset or copyright rights. Those rights depend on applicable law and on a valid agreement, licence, assignment, marketplace term, or other governing document. Buying a token that points to an artwork is therefore different from acquiring copyright in that artwork.

The same separation applies outside intellectual property. A token can represent a ticket, membership, identity credential, or claim only when the responsible application, issuer, or legal arrangement recognizes it. The blockchain can prove the token's recorded owner and history under its rules; it cannot force an external organization or court to honor an unstated right.

## What to verify before relying on an NFT

Check the complete identity and dependency chain:

- **Chain and contract:** Which network and exact contract address define the token?
- **Token standard:** Is it ERC-721, ERC-1155, another interface, or a custom implementation?
- **Token ID and supply:** Is the item individually owned, one of multiple units, burnable, or mintable again?
- **Contract control:** Who can mint, pause, upgrade, change metadata, freeze transfers, or replace implementation code?
- **Metadata:** Is the URI immutable, content-addressed, onchain, or controlled by a server?
- **Media availability:** Who stores the file, and what happens if the gateway, domain, or storage provider disappears?
- **Approvals and custody:** Which operators can transfer the token, and does a platform hold it custodially?
- **Application dependency:** Does the token's utility rely on a game, marketplace, issuer, API, or account that can change or close?
- **Rights:** What written terms grant access, redemption, commercial use, copyright licence, or a claim on an external asset?
- **Authenticity:** How is the creator, issuer, collection, or referenced object verified beyond the token's existence?

NFTs work by standardizing identifiable token records and transfer permissions on a blockchain. Their durable onchain facts may include the contract, token ID, owner, approvals, and transfer events. Metadata, media availability, authenticity, application utility, and legal rights are separate layers that must be verified rather than inferred from token ownership.

## Sources and references

- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [What Are NFTs?](https://ethereum.org/nft/) — ethereum.org; retrieved 2026-10-18.
- [Non-Fungible Tokens and Intellectual Property: A Report to Congress](https://www.copyright.gov/policy/nft-study/Joint-USPTO-USCO-Report-on-NFTs-and-Intellectual-Property.pdf) — United States Patent and Trademark Office and U.S. Copyright Office; retrieved 2026-10-18.
