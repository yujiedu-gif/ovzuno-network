---
title: "Ethereum token approval: what permission does it grant?"
description: "Understand what an ethereum token approval authorizes, how an ERC-20 allowance works, and what to check before signing a token approval transaction."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["ERC-20 allowance", "token spending permission", "approve transaction"]
author: "editorial_team"
primary_keyword: "ethereum token approval"
owned_question: "What does an Ethereum token approval authorize, how does an ERC-20 allowance work, and what can a user check before granting or changing one?"
risk_level: "medium"
---

An Ethereum token approval grants a designated spender permission to use tokens up to an allowance recorded by the token contract; the approval does not itself transfer those tokens. Before signing, check the network, token contract, approving account, spender address, and requested amount, then verify the current allowance from chain data. Exact behavior depends on the token’s implementation and the transaction being authorized.

## What an Ethereum token approval authorizes

An approval is a contract-level spending permission. The ERC-20 interface defines common functions for balances, direct transfers, and approvals that let another address spend up to an authorized amount. The permission applies within the token contract’s rules; an approval transaction is distinct from a token transfer. [source](<https://eips.ethereum.org/EIPS/eip-20>)

The main parties are the **approving account**, which grants permission, and the **spender**, the address authorized to use it. The permission also relates to a particular token contract and an allowance amount. Do not assume that approval for one spender or token applies to another.

An approval does not, by itself, mean the approved tokens have moved. It records permission that the spender may use in a later interaction. Whether a particular interaction uses that permission depends on the contract and transaction involved. The ERC-20 interface describes common approval operations, but it does not establish every project-specific right, service condition, or legal treatment associated with a token. [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)

## How an ERC-20 allowance works

An allowance is the amount of token spending permission that the contract records for a particular approving account and spender. When reviewing one, identify these four elements:

- **Token contract:** the contract whose token operations are involved.
- **Approving account:** the account granting permission.
- **Spender address:** the address receiving permission.
- **Allowance:** the authorized amount recorded for that account and spender in that token contract.

This is a contract-level relationship, not a general permission over every asset in an account. The ERC-20 interface provides common operations for balances, transfers, and approvals, but the specific token contract determines its behavior. [source](<https://eips.ethereum.org/EIPS/eip-20>)

An allowance is state that can change. A spender may use permission through contract interactions under the token’s implementation, and a later approval transaction may set a different allowance. As a result, an earlier approval transaction alone does not establish the current allowance. Check the current state for the same token contract, approving account, and spender.

The interface also does not specify the complete project-specific rights or conditions connected with a token. Those require separate project documentation and terms; they cannot be inferred from the ERC-20 label alone. [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)

## What to check before signing an approval transaction

Use the following checklist to examine the permission being requested:

1. **Check the network.** Confirm the transaction is on the network you intend. Do not treat an address or balance viewed in one network context as evidence about another.
2. **Identify the token contract.** Check the contract address, not only a displayed name or symbol. The token interface does not establish all project-specific rights or conditions. [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)
3. **Identify the approving account and spender.** Confirm which account is granting permission and the exact address that will receive it. If the address does not match the interaction you intended, pause rather than relying on a label.
4. **Review the allowance amount.** Determine how much permission the transaction requests. If the interface calls it unlimited or effectively unlimited, understand that it represents a broad amount of permission; do not assume that the standard requires or recommends it. The interface defines a common approval mechanism, not a universally appropriate allowance size. [source](<https://eips.ethereum.org/EIPS/eip-20>)
5. **Distinguish approval from transfer.** Check whether the transaction is requesting an approval or a transfer. Approval records permission; it does not by itself establish that tokens have moved.
6. **Review the transaction request.** Compare the visible details with the token, spender, amount, and network you intend. A descriptive summary alone does not establish all the contract’s behavior or project conditions. [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)
7. **Verify current state afterward.** Once the transaction has been processed, check the allowance for the same token contract, account, and spender. A submitted request alone does not establish the resulting allowance.

This checklist helps distinguish what is being authorized from what the interface says about it. It is not a guarantee about the application, spender, token, or outcome.

## Changing or revoking an allowance

A later approval can change the allowance recorded for the relevant account and spender. Where the token implementation supports it, an approval can set the allowance to zero. The ERC-20 interface includes approval operations, but the actual behavior depends on the contract; check the resulting state instead of assuming a change took effect. [source](<https://eips.ethereum.org/EIPS/eip-20>)

Changing an allowance affects the permission recorded by the token contract. It does not reverse transfers that have already occurred. A zero allowance for one token-and-spender relationship also does not establish that other permissions or relationships have changed. Verify the specific token contract, approving account, and spender when checking the updated state.

## Risks, implementation differences, and evidence to verify

An approval gives the designated spender permission within the allowance and the token contract’s implementation. For that reason, the transaction’s apparent purpose or a familiar interface description is not enough to establish the full behavior of the spender or related contracts. The ERC-20 interface standardizes common operations, while the complete project-specific rights and conditions are not specified by the interface. [source](<https://eips.ethereum.org/EIPS/eip-20>) [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)

Keep three questions separate when reviewing evidence: What transaction is being requested? What allowance does the token contract currently record? What do the project’s documentation and terms say? The first concerns the proposed action, the second concerns contract state, and the third concerns conditions the interface does not define. [source](<https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text>)

The practical review remains focused: confirm the network, token contract, approving account, spender, and amount; decide whether that permission matches the intended interaction; and verify the allowance afterward. An approval alone does not show that tokens have already moved or establish project-specific rights beyond the token contract’s recorded permission.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20?trk=public_post_comment-text) — Ethereum Improvement Proposals; retrieved 2026-10-21.
