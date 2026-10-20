---
title: "Cryptocurrency Market Makers: How It Works"
description: "Understand Cryptocurrency Market Makers, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification p."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "cryptocurrency market makers"
owned_question: "What do cryptocurrency market makers do, and how do they support liquidity and trading on crypto markets?"
risk_level: "medium"
---

# Cryptocurrency Market Makers: How It Works

Cryptocurrency market makers help trading venues connect buyers and sellers by placing or maintaining orders that can be matched. Their activity can add visible buying and selling interest, but it does not guarantee that a trade will execute at a particular price, that every asset will remain easy to trade, or that liquidity will persist as market conditions change. Understanding their role requires looking at the venue’s order system, the market-liquidity measures that matter, and the operational arrangements around funds and trading.

## What Cryptocurrency Market Makers means

A cryptocurrency market maker is a participant that supplies buy and sell interest to a market. In an order-book venue, that interest can appear as outstanding limit orders: offers to buy at specified prices and offers to sell at specified prices. When other participants submit compatible orders, the venue’s matching system may execute a trade. The market maker’s orders can therefore help create counterparties for people seeking to buy or sell.

The term describes a market function, not necessarily a particular company, contract, or venue feature. A market maker may be independent of an exchange or may operate within a broader exchange business. The accepted evidence establishes that centralized crypto exchange operators may combine functions such as third-party trading, proprietary trading, margin lending, token issuance, and custody. Not every exchange performs every function. Combining roles can create operational dependencies and conflicts, so the label “market maker” alone does not explain who controls a trading strategy, how funds are held, or how conflicts are managed.

Market making is also not synonymous with liquidity itself. Market liquidity is multidimensional: it reflects the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. These dimensions can vary with transaction size and market conditions. A market may show orders near the current price yet still impose substantial costs on a large trade, or those orders may disappear before execution. A market maker can contribute to liquidity, but cannot guarantee all of its dimensions.

## Core components of Cryptocurrency Market Makers

**The venue and matching model.** Centralized crypto exchanges commonly maintain off-chain records of outstanding buy and sell orders in a limit order book. A venue’s matching system uses its rules to process compatible orders. Individual venues can use additional matching models and order types, so an order-book description is a common model rather than a universal specification.

**Orders and market state.** The order book is a view of resting buy and sell interest at a point in time. A market maker’s quoting activity may add orders to that state; other orders can trade against them, and orders may be amended or canceled according to the venue’s rules. The exact order types, priority rules, and update behavior depend on the venue. A displayed order is not the same as a completed trade, and a snapshot does not establish that the same liquidity will remain available.

**Market-making activity.** The market maker decides what buy and sell interest to provide and interacts with the venue through its supported processes. The accepted claims do not specify a standard algorithm, required quote size, inventory policy, uptime commitment, or universal obligation to quote continuously. Those details must be verified for the specific participant and platform rather than inferred from the role’s name.

**Funds and custody.** In the high-level centralized-exchange model, users typically transfer funds or assets into the exchange’s custody before trading on its internal order book. Custody and legal ownership arrangements vary by platform and jurisdiction; some venues and products use different custody, brokerage, or settlement arrangements. The market-making function itself does not establish who holds assets, who can authorize withdrawals, or what happens during a platform outage.

**Operational dependencies.** The activity depends on the venue’s order interface and matching operation, as well as on the participant’s ability to submit and manage orders. Where an exchange combines trading with custody or other functions, those roles may be operationally connected. The available evidence supports treating these as dependencies to investigate; it does not establish a particular platform’s system design or safeguards.

## How Cryptocurrency Market Makers works

A simplified order-book workflow helps show where market makers fit:

1. **A venue records orders.** On a centralized venue using a limit order book, outstanding buy and sell orders are commonly recorded off-chain. The venue’s specific matching model and order types may add details to this basic picture.
2. **A participant supplies trading interest.** A market maker places buy and/or sell orders through the venue’s supported interface or process. The accepted evidence does not prescribe how frequently orders must be refreshed, what prices they should use, or how much inventory they must provide.
3. **Orders become part of the available market state.** The venue’s book reflects outstanding interest, including orders from market makers and other participants. The state can change as orders are matched or otherwise updated under venue rules. A displayed quote is conditional on remaining available when a compatible order arrives.
4. **Another participant seeks a trade.** A buyer or seller submits an order. If it is compatible with resting interest and the venue’s rules permit a match, the venue can execute a trade. If not, the order may remain unfilled or be handled according to the venue’s matching model; exact outcomes depend on that model and order type.
5. **Execution changes the visible interest.** A match consumes some or all of the relevant resting order. The resulting book may have different prices, quantities, or gaps. Thus, the presence of a market maker’s orders can support execution, but it does not mean that a particular order size will trade without price impact.
6. **The participant and venue continue operating under their arrangements.** Funds, custody, and settlement depend on the platform’s design and terms. In the typical centralized model described by BIS, users place assets in exchange custody before using the internal trading system, but alternative arrangements exist.

The practical effect is best assessed by looking beyond whether a market maker is present. Relevant evidence includes the spread between buy and sell interest, the transaction costs applicable to a trade, the likely price impact at the intended size, and how quickly an order can be executed. These are distinct dimensions of liquidity, and they may change with market conditions.

## Trust and control boundaries

A venue’s matching rules and order records determine how its trading system represents and processes orders. That does not, by itself, establish that a market maker will maintain quotes, that an order will execute, or that the market will remain liquid. The accepted claims describe common centralized-exchange features, not guarantees about any particular venue or participant.

Custody is a separate boundary. In the typical centralized arrangement, assets are transferred into exchange custody before internal-book trading. That means a user’s ability to trade can depend on the exchange’s custody and operational arrangements, not only on the market maker’s orders. The evidence also cautions that custody and legal ownership arrangements vary by platform and jurisdiction, and some products use other custody, brokerage, or settlement arrangements.

There can also be role overlap. A centralized exchange operator may combine third-party trading and proprietary trading with services such as margin lending, token issuance, and custody. This does not mean every exchange does so, nor does the evidence establish misconduct. It does mean that teams should identify which entity performs each function and examine the resulting operational dependencies and potential conflicts instead of assuming the market-making role is organizationally separate.

## Limitations and failure modes

Market making cannot eliminate the basic costs and constraints of trading. Spread, transaction cost, price impact, and immediacy all affect market liquidity, and their importance can differ by order size and conditions. A narrow spread alone is not a complete measure of the cost of trading, while visible orders do not prove that a large order can execute at the displayed price.

Liquidity is not a fixed property. Since it changes with transaction size and market conditions, a book observed at one time may not represent what is available later or what a larger order will encounter. A market maker’s presence also does not guarantee continuous quoting, execution, or a particular outcome; the accepted source claims do not establish such commitments.

Venue and custody dependencies create additional points to examine. A centralized-exchange customer typically transfers assets into exchange custody before using the internal trading system, but arrangements vary. If a team assumes that trading, custody, and settlement are identical across platforms, it may overlook important differences in where assets are held and how the venue’s internal trading process relates to them. Similarly, where an operator combines trading with other functions, operational dependencies and conflicts may arise, though their form and handling require platform-specific evidence.

Finally, the order-book model should not be treated as a specification for every crypto market. Centralized venues commonly use off-chain limit-order-book records, but individual venues may use additional matching models and order types. A team needs the applicable venue documentation to understand the actual workflow.

## What teams should verify

Before relying on market-making activity as part of a trading or infrastructure design, teams can use an evidence-led review:

- **Identify the venue model.** Confirm whether the market uses an internal limit order book, what matching models and order types are supported, and where official documentation describes the rules.
- **Inspect liquidity by dimension.** Evaluate spread, transaction costs, price impact, and immediacy separately. Consider the intended transaction size and the conditions under which observations were made; one metric or snapshot is not a complete liquidity assessment.
- **Establish what “market maker” means in context.** Identify the entity providing orders and obtain evidence for any claimed quoting scope or operating commitment. Do not infer a required uptime, quote size, or execution guarantee from the title alone.
- **Trace order handling.** Determine how orders are submitted, represented, matched, changed, and reflected in the venue’s book. Verify the actual venue rules rather than assuming every platform implements the same order-book workflow.
- **Map custody and settlement.** Establish where assets are held before trading, what the platform’s custody arrangement is, and how its trading process relates to custody and settlement. Check platform-specific documentation because arrangements vary, including by jurisdiction.
- **Map organizational roles.** Determine whether the exchange operator also performs proprietary or third-party trading, margin lending, token issuance, or custody. If functions are combined, document the operational dependencies and potential conflicts relevant to the system being assessed.
- **Separate documented facts from assumptions.** Treat venue documentation and verified operating terms as evidence for a specific implementation. Do not treat general descriptions of centralized exchanges as proof of a particular platform’s controls, performance, or recovery process.

Cryptocurrency market makers can contribute buy and sell interest that helps connect trades, especially on venues where outstanding orders are displayed in a limit order book. Their contribution is one part of a larger system involving venue rules, market conditions, transaction costs, and—in centralized arrangements—custody and other exchange functions. The useful technical question is therefore not simply whether a market maker exists, but what orders are available, under what rules, at what size and time, and with which operational dependencies.

## Sources and references

- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
