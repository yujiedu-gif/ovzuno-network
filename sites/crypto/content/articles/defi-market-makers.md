---
title: "DeFi Market Makers: How Liquidity Mechanisms Work"
description: "Learn how DeFi market makers support trading, how automated market makers differ from professional firms, and what risks shape decentralized liquidity."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["automated market makers", "decentralized exchange liquidity", "AMM"]
author: "editorial_team"
primary_keyword: "defi market makers"
owned_question: "How do market-making mechanisms provide liquidity in DeFi, and how do automated market makers differ from market-making firms operating in decentralized markets?"
risk_level: "medium"
---

In decentralized finance (DeFi), market-making can mean either an automated protocol that prices swaps against pooled assets or a professional firm that trades in decentralized markets. The protocol provides execution rules; liquidity providers contribute assets; and a firm makes trading decisions. These roles can overlap, but they are not interchangeable, and none guarantees a particular price or easy execution.

## What “market maker” means in DeFi

In general, market-making describes activity that helps make trading possible by supplying tradable liquidity. In DeFi, the phrase can refer to a protocol mechanism, the participants who supply assets to it, or a professional trading operation. Those are distinct roles, even when the same organization participates in more than one.

An automated market maker (AMM) is a protocol mechanism. In one example, a Uniswap liquidity pool is a pairing of tokens held in a smart contract for swaps on a decentralized exchange. A liquidity provider (LP) contributes assets to a pool and can receive a share of trading fees while bearing inventory and adverse-selection risk. The LP supplies capital; the protocol's rules govern how swaps interact with the pool. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://www.bis.org/publ/work1227.pdf>)

A professional market-making firm is a human or algorithmic trading operation, not a pool formula. It may make trading decisions and manage positions in decentralized markets. Its activity can interact with AMM pools, but it remains separate from the protocol's programmed execution rules. Conversely, a pool can provide swap liquidity without a professional firm choosing each trade. The label “market maker” alone does not establish which role an organization performs.

## How automated market makers price and execute trades

A pool-based AMM can quote and execute swaps through a smart contract and a pricing rule, rather than requiring a conventional central limit order book for that pool. The contract's reserves supply the inventory from which swaps execute. In the Uniswap v2 example, liquidity-provider shares represent contributions to a token pair's reserves. This is a particular constant-product design, not a universal AMM template: pool formulas, assets, fees, and accounting can differ. [source](<https://www.bis.org/publ/work1227.pdf>)

Because a swap uses the pool's available inventory, the pool state and the proposed trade size affect execution. A pool's quoted output is not a guarantee that every transaction will execute at that amount. In particular, the relationship between trade size and available liquidity matters when evaluating an expected swap result. There is no single pricing rule or execution behavior that can be assumed across all AMMs.

A decentralized application may also have distinct settlement, application, and interface layers, each with its own technical dependencies. A pool's pricing and execution rules belong to the application mechanism, while an interface is a separate way to interact with it. These layers can be distributed or combined differently across systems. Knowing the interface does not, by itself, describe the pool's pricing design. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

## How professional market makers interact with decentralized venues

A professional firm may trade against AMM pools or participate through other market structures, depending on the venue. It can make its own decisions about trading and inventory rather than relying solely on the pool's automatic pricing rule. The firm's activity may contribute to trading liquidity, but it does not turn the firm into the AMM protocol or make the protocol a discretionary trading desk.

One possible cross-market activity is arbitrage: trading in response to price differences between markets. In the specific case of an issuer-backed stablecoin, issuance and redemption near a reference value can provide an arbitrage path between the primary market and the secondary-market price. That path is conditional: fees, minimums, eligibility, delays, market liquidity, banking access, or redemption suspensions can weaken or block it. This example does not mean all DeFi prices are aligned through arbitrage, or that a firm can always trade or redeem at a reference value. [source](<https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf>)

A firm may also contribute assets to a pool, making it an LP as well as an active trader. The functions remain conceptually distinct: supplying assets exposes the provider to pool-related inventory risks, while discretionary trading involves the firm's decisions about its activity. Whether a particular firm performs either function requires evidence about that firm; the general AMM model cannot answer that question.

## Liquidity, execution, and the trade-offs for participants

Liquidity in a pool is not a promise of low slippage, a fixed execution price, or continuous availability. The pool supplies inventory for swaps, but the relevant pricing rule and pool state govern how a particular trade interacts with that inventory. A reader assessing an execution mechanism should therefore separate the existence of pooled assets from what the protocol's rules imply for a trade of a given size.

LPs may receive a share of trading fees, but they also bear risks. One potential exposure, commonly called impermanent loss, is an inventory-value loss relative to holding the assets when pool prices move. Fees may or may not offset it. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state; the term does not mean that a loss always occurs or necessarily reverses. [source](<https://www.bis.org/publ/work1227.pdf>) [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

Adverse selection is another potential LP risk. The evidence identifies it as an exposure associated with liquidity provision, but does not establish a universal size or outcome. The relevant risk depends on the pool and market conditions. A professional firm trading in a venue and an LP contributing assets can therefore have different exposures, even when both activities support trading.

## Risks and due diligence for DeFi market-making systems

Start with the actual mechanism rather than the broad label “DeFi.” For a pool, determine which pricing and accounting design applies and how it handles the assets being traded. For a firm, distinguish discretionary trading from any pool assets it supplies. A description of one role should not be treated as a complete account of the other.

Risks also depend on a system's specific architecture. The DeFi layers of settlement, application, and interface can have distinct dependencies, and their distribution varies by system. The accepted evidence here does not establish that every AMM has the same oracle, bridge, governance, or operational dependencies, so those risks should be assessed only where the design uses the relevant components. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

For a specific system, consult its current protocol documentation and relevant disclosures. Treat claims about audits, incidents, recovery, fees, yields, availability, or compliance as system-specific questions that require current, attributable evidence. General descriptions of AMMs and liquidity provision do not verify those claims, establish the status of a particular firm, or support legal or tax conclusions.

The key distinction is who or what performs each function: the AMM rules price and execute pool swaps, LPs contribute assets, and professional firms make trading decisions. A firm can participate in a pool, but that overlap does not erase the difference between automated protocol mechanics and professional market-making activity.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
- [Understanding Stablecoins](https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf) — International Monetary Fund; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
