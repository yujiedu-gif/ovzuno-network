---
title: "Synthetic asset crypto: how reference-based tokens work"
description: "Learn how synthetic asset crypto can represent exposure to an underlying reference, how tracking mechanisms work, and which design risks to assess."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["tokenization_rwa"]
tags: []
author: "editorial_team"
primary_keyword: "synthetic asset crypto"
owned_question: "How do crypto-based synthetic assets represent the value or behavior of an underlying reference, and what mechanisms and risks are involved?"
risk_level: "high"
---

Crypto-based synthetic assets are tokens or arrangements designed to provide exposure to a reference—such as an asset’s value—without necessarily conveying ownership of that asset. How the exposure is created, maintained, and backed depends on the specific design; a token’s existence alone does not establish a holder’s ownership, redemption rights, or claim against an issuer or collateral.

## What makes a crypto asset synthetic?

A synthetic asset is best understood by asking what it tracks, rather than assuming what it owns. The reference might be a price or another measurable exposure. The token or arrangement is intended to reflect that reference under its own rules, but that intent is not proof that the reference itself has been transferred to the holder.

This distinction separates synthetic exposure from a token that records ownership under a particular system. For example, an ERC-721 contract standardizes owner lookup, approvals, and transfer behavior for distinct tokens. That technical ownership record concerns the token; it does not establish that the token holder owns an asset named by the token or has rights against an issuer. The relevant rights depend on the system and its governing terms. (ERC-721 interface claim: `claim_erc721_owner_transfer`.)

Likewise, a common fungible-token interface does not settle what a token represents. ERC-20 defines functions and events for balances, transfers, approvals, and related token operations, but the interface does not determine backing, issuance policy, market value, or implementation safety. (ERC-20 interface claim: `claim_erc20_interface`.) A synthetic token can therefore be technically transferable while its connection to a reference depends on other mechanisms and arrangements.

## How synthetic asset crypto can track a reference

There is no single tracking mechanism implied by the label “synthetic.” A design may rely on collateral, pricing inputs, and protocol rules, or on contractual arrangements that provide reference-linked exposure. Those components do not necessarily transfer the referenced asset. Their roles and dependencies must be established from the particular system’s documentation and governing terms.

One documented collateralized model uses overcollateralized smart-contract positions, price oracles, collateral-ratio rules, and liquidation processes. An oracle is a mechanism that supplies price information to the contract; the contract uses that input within its rules. This model has specific dependencies, and it is not a description of every synthetic asset. Its documented failure risks include problems with the oracle, contract, governance, liquidity, collateral price, or bad-debt handling. (Collateral-model claim: `claim_crypto_collateral_model`.)

Other arrangements may provide exposure through a third party rather than a collateralized onchain position. In a U.S. federal securities-law context, SEC staff describe third-party tokenized-security models that may represent a custodial entitlement or synthetic instrument rather than direct ownership of the referenced security. That statement concerns those described models; it should not be generalized to every crypto synthetic asset or treated as a legal determination for a particular token. (Third-party-model claim: `claim_sec_third_party_models`.)

For any design, separate the reference from the method used to track it. A reference is what the arrangement aims to follow; the tracking mechanism is the set of rules, inputs, assets, and counterparties intended to maintain that relationship. A token’s interface or transfer capability cannot, by itself, verify that the mechanism works as intended.

## Where tracking can fail

Tracking depends on the mechanism’s inputs and operating conditions. In a collateralized design, the cited model depends on an oracle, collateral valuation, contract rules, and liquidation processes. If an essential dependency fails or the collateral is insufficient under the system’s rules, the design may not maintain the intended exposure. These are model-specific risks, not a conclusion that every synthetic asset uses the same structure. (Collateral-model claim: `claim_crypto_collateral_model`.)

Governance is another dependency in that same model: the claim identifies governance failure among the possible risks. Readers therefore need to establish which rules govern the arrangement and how changes or failures are handled. The allowed evidence does not specify a universal governance process, recovery procedure, or method for resolving a tracking interruption; those details must be verified for the particular design.

Third-party arrangements raise a different question: what does the holder’s position represent? A token may stand for an indirect entitlement or synthetic exposure rather than direct ownership of the reference. The precise rights and exposure depend on the structure and governing documents. (Third-party-model claim: `claim_sec_third_party_models`.) Do not infer that a reference price, collateral pool, or token balance automatically guarantees redemption or a particular outcome.

## What a token holder may—and may not—be entitled to

Technical exposure, ownership, and a contractual claim are distinct concepts. A token can be designed to track a reference without transferring that reference to its holder. In the cited third-party model, a token may represent a custodial entitlement or synthetic instrument rather than direct ownership of the referenced security; the claim is limited to the models described by SEC staff in a U.S. federal securities-law context. It does not determine the rights attached to another arrangement. (Third-party-model claim: `claim_sec_third_party_models`.)

Before treating a token as redeemable or as a claim on an issuer or collateral, examine the governing documents and identify who, if anyone, owes an obligation to the holder. Verify any stated redemption conditions, relevant custody arrangements, and the process for enforcing the described rights. The allowed evidence does not establish universal redemption rights, ownership, legal classification, regulatory treatment, or tax consequences for synthetic assets. Those conclusions require authoritative, jurisdiction-specific evidence and should not be inferred from token mechanics alone.

A wallet does not resolve this rights question. SEC staff explain, in U.S. educational material, that a crypto wallet generally stores private keys or passcodes used to access and authorize crypto assets rather than storing the assets themselves. This technical point does not establish what a particular token represents or what rights its holder has. (Wallet claim: `claim_sec_wallet_not_assets`.)

## A practical framework for evaluating a design

For a particular synthetic asset, gather evidence in a sequence that keeps the mechanism separate from the rights:

1. **Identify the reference.** Determine exactly what value or behavior the arrangement says it tracks. Do not treat the token name or interface as proof of that relationship.
2. **Map the tracking mechanism.** Establish whether the design relies on collateral and price inputs, a third-party arrangement, or another documented method. The collateralized model described above is one design, not a universal template. (Collateral-model claim: `claim_crypto_collateral_model`.)
3. **List dependencies and failure modes.** For a collateralized position, check the documented oracle, contract, governance, liquidity, collateral-price, and bad-debt dependencies. For another structure, verify its own documented dependencies rather than borrowing assumptions from this model. (Collateral-model claim: `claim_crypto_collateral_model`.)
4. **Read for rights, not just technical behavior.** Establish whether documents describe ownership, redemption, a custodial entitlement, or synthetic exposure, and who is responsible for any promised performance. A token standard’s interface does not establish backing or legal rights. (ERC-20 interface claim: `claim_erc20_interface`; third-party-model claim: `claim_sec_third_party_models`.)
5. **Keep unsupported conclusions open.** The evidence available here does not establish a universal audit standard, upgrade-control framework, recovery process, current availability, fee, yield, or compliance status. Verify such details with current, authoritative documentation for the specific arrangement, and do not assume they apply across designs.

The central distinction is simple: a synthetic asset is about designed exposure to a reference, while ownership and enforceable rights depend on the specific arrangement. Understanding its tracking mechanism and dependencies helps explain how that exposure is intended to work, but does not by itself prove that tracking will hold or that the holder can claim the referenced asset.

## Sources and references

- [Statement on Tokenized Securities](https://www.sec.gov/newsroom/speeches-statements/corp-fin-statement-tokenized-securities-012826-statement-tokenized-securities) — U.S. Securities and Exchange Commission staff divisions; retrieved 2026-10-19.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
