---
title: "How Do Stablecoins Work? Issuance, Pegs, and Redemption"
description: "Learn how stablecoins are issued, transferred, and redeemed, how fiat-backed, crypto-collateralized, and algorithmic models differ, and why pegs can fail."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["stablecoins-settlement"]
tags: ["how stablecoins work", "stablecoin mechanism", "fiat backed stablecoin", "crypto collateralized stablecoin", "algorithmic stablecoin"]
author: "editorial_team"
primary_keyword: "how do stablecoins work"
owned_question: "How do stablecoins issue, circulate, maintain a reference value, and support redemption?"
risk_level: "high"
---

Stablecoins are crypto assets designed to track a reference value, commonly a national currency such as the US dollar. They circulate as blockchain tokens, but their stability comes from mechanisms outside ordinary token transfer: reserves and redemption, collateral and liquidation, or rules intended to change supply and demand.

The word *stable* describes an objective, not a guarantee. A stablecoin can trade above or below its reference, redemption can be restricted or delayed, and a mechanism can fail. Understanding a stablecoin therefore requires tracing both the token and the arrangement that supports it.

## Stable is a design objective

Three values should be kept separate:

1. **Reference value:** the unit the stablecoin is intended to track, such as one US dollar.
2. **Redemption value:** what an eligible holder can claim from an issuer, smart contract, reserve, or collateral system.
3. **Market price:** the price available on exchanges, decentralized pools, or peer-to-peer markets.

These values may be close without being identical. Direct redemption can anchor the market price when it is credible and accessible. When redemption is uncertain, slow, expensive, or unavailable, secondary-market supply and demand can move the token away from its reference.

## The stablecoin operating cycle

A common issuer-backed cycle begins when an approved customer sends money to an issuer. The issuer adds the funds to its reserve arrangement and authorizes stablecoins to be minted to the customer's blockchain address. The customer can transfer the tokens to wallets, merchants, exchanges, or applications. Those transfers are settled under the rules of the blockchain on which the tokens exist.

The token may trade many times without any reserve asset moving. A holder who can access the issuer's redemption process returns tokens and requests the reference asset. Once accepted, the tokens are normally burned and the issuer pays out under its terms. Minting and burning should cause circulating token supply to expand and contract with primary-market demand.

Many retail holders never transact directly with the issuer. They acquire or sell tokens through exchanges, brokers, wallets, or liquidity pools. Their effective price and exit path can therefore depend on intermediaries as well as the issuer.

## Fiat-reserve-backed stablecoins

A fiat-reserve-backed stablecoin relies on an identifiable issuer and assets held offchain. Reserves may include cash, bank deposits, short-term government instruments, repurchase agreements, or other permitted assets. The composition matters because reserve credit risk, market risk, maturity, and liquidity affect the issuer's ability to meet redemptions.

The basic mechanism is:

- the issuer receives eligible funds and mints tokens;
- reserve assets are held or invested under the arrangement's custody rules;
- tokens circulate on one or more blockchains;
- eligible holders redeem according to the issuer's procedures; and
- redeemed tokens are burned or otherwise removed from circulation.

A statement that a token is backed one-for-one is incomplete. Users still need to know which assets back it, who owns and safeguards them, whether they are segregated, who has a legal claim, how frequently balances are reported, and what happens during issuer, custodian, or bank insolvency. An attestation, audit, regulatory filing, and real-time proof-of-reserves dashboard answer different questions and should not be treated as interchangeable.

## Crypto-collateralized stablecoins

A crypto-collateralized system uses digital assets locked in smart contracts. Because the collateral can be volatile, systems commonly require more collateral value than the stablecoins created against it. A user deposits an accepted asset into a vault, borrows or mints stablecoins within a collateral-ratio limit, and later repays the stablecoins to unlock the collateral.

The system needs price information to determine collateral value. If the ratio falls below a threshold, liquidation mechanisms sell or transfer collateral to reduce the debt. Stability therefore depends on smart contracts, price oracles, collateral liquidity, liquidator participation, parameter governance, and the ability to manage rapid market moves.

Overcollateralization is a buffer, not a guarantee. A price gap, oracle failure, congested network, illiquid auction, contract defect, or governance failure can leave insufficient collateral or bad debt. Some systems add emergency shutdowns, reserves, fees, or multiple collateral types, each introducing further rules and dependencies.

## Algorithmic and hybrid models

Algorithmic stablecoins attempt to influence price through programmed supply changes and economic incentives. A system might let users exchange the stablecoin for a companion token, issue incentives when price is below the reference, or expand supply when price is above it.

Such mechanisms depend on continued demand and credible conversion. If the asset offered during contraction is itself supported by expectations about future stablecoin demand, declining confidence can become reflexive: redemptions increase supply of the companion asset, its value falls, and the promised conversion becomes less credible. An automatic rule cannot create solvent backing merely by changing token quantities.

Hybrid designs combine reserves, crypto collateral, algorithmic controls, derivatives, or external liquidity. The label does not determine risk. Each component and the order in which losses are absorbed must be evaluated.

## Why the market price can stay near the reference

When eligible participants can mint at approximately the reference value, a market price above the reference can create an incentive to mint and sell. Additional supply can push the market price downward. When participants can buy below the reference and redeem near the reference, buying and redemption can reduce circulating supply and pull the price upward.

This arbitrage channel is only as strong as its access. Identity requirements, banking hours, redemption minimums, fees, settlement delays, chain congestion, exchange withdrawal limits, reserve concerns, or temporary suspensions can create a band around the reference or break the link. Market makers may narrow that band, but they also manage inventory, credit, liquidity, and operational risk.

The IMF notes that issuers may promise par redemption while actual access is constrained. The FSB therefore emphasizes clear legal claims, effective stabilization, transparent reserve information, and timely redemption in its recommendations for global stablecoin arrangements. Those recommendations are evaluation criteria, not evidence that every stablecoin meets them.

## How stablecoins move and settle

An onchain transfer changes ownership or control of the token according to the blockchain and contract. It does not itself move bank deposits, government securities, or other reserve assets. Final redemption adds an offchain payment, asset delivery, or collateral release step.

A token can exist natively on several blockchains under one issuer. It can also appear as a wrapped or bridged representation created by a third-party bridge. Those are different structures. Users should verify the contract address, issuer support, bridge or custodian, redemption path, and whether the received token is native or wrapped.

Stablecoin contracts may include administrator powers to mint, burn, pause, upgrade, freeze, or block addresses. These controls may support recovery or compliance but also create governance, key-management, censorship, and operational dependencies. Blockchain settlement finality does not eliminate issuer, reserve, legal, or banking risk.

## What to verify in a stablecoin arrangement

Before relying on a stablecoin for payment, treasury, settlement, or application logic, ask:

- **Reference:** What asset, currency, or basket is being tracked?
- **Issuer and claim:** Who owes the holder, and what legal right does the token provide?
- **Stabilization:** Is value supported by fiat reserves, crypto collateral, an algorithm, or a hybrid?
- **Reserves:** What assets are held, by whom, with what liquidity, segregation, reporting, and assurance?
- **Redemption:** Who is eligible, at what value, minimum, fee, timetable, and under which suspension conditions?
- **Supply controls:** Who can mint and burn, and how is cross-chain supply reconciled?
- **Collateral:** What ratios, oracles, liquidations, auctions, and backstops apply?
- **Technology:** Which contracts, administrators, upgrade keys, bridges, chains, and service providers are required?
- **Governance:** Who can change parameters, reserve policy, eligible collateral, or redemption terms?
- **Failure handling:** What happens after a depeg, reserve loss, custodian failure, chain outage, oracle fault, or contract exploit?
- **Jurisdiction:** Which laws and regulators apply to issuance, custody, payments, disclosures, sanctions, and user rights?

Stablecoins work by combining a transferable blockchain record with a stabilization and redemption arrangement. The token shows what moved onchain; reserves, collateral, contracts, incentives, governance, and legal rights determine whether its reference value remains credible and whether a holder can ultimately exit at that value.

## Sources and references

- [Understanding Stablecoins](https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf) — International Monetary Fund; retrieved 2026-10-18.
- [Understanding Stablecoin Technology and Related Security Considerations](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8408.pdf) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements](https://www.fsb.org/uploads/P170723-3.pdf) — Financial Stability Board; retrieved 2026-10-18.
