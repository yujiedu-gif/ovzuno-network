---
title: "DEFI Borrowing Explained: How It Works"
description: "Understand DEFI Borrowing Explained, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification point."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: ["defi borrowing"]
author: "editorial_team"
primary_keyword: "defi borrowing explained"
owned_question: "How does borrowing work in decentralized finance (DeFi)?"
risk_level: "medium"
---

# DEFI Borrowing Explained: How It Works

## What DEFI Borrowing Explained means

DeFi borrowing is a process in which a user interacts with software deployed on a blockchain to obtain an asset under rules encoded in that software. In a common collateralized design, a user supplies one asset as collateral and borrows another, with the position and its required conditions represented in protocol state. The exact rules vary by implementation; the source material here supports a system-level explanation, not claims about any particular lending protocol, asset, or transaction.

A useful way to define the system boundary is to separate three layers: settlement, application, and interface. The settlement layer is the blockchain and its transaction history. The application layer contains the borrowing logic, such as the rules that govern the position. The interface layer is how a user or an integrating service prepares and submits actions. These layers can be distributed or combined differently in a particular system, so the labels are a reference model rather than a universal architecture. [claim_bis_defi_layers]

This distinction matters because “decentralized” does not mean that every component is equally distributed or independent. A blockchain can validate a shared transaction history and help prevent the same digital unit from being spent more than once, but the mechanism and assurance level depend on that network’s protocol and consensus design. [claim_bis_double_spend] The borrowing application, interface, and supporting services have their own dependencies and control points.

## Core components of DEFI Borrowing Explained

A borrowing arrangement can be understood through the following components. Their exact form and responsibilities are implementation-dependent.

- **Borrower and wallet:** The borrower initiates actions using a wallet or another transaction-signing setup. The wallet controls the keys used to authorize transactions; it is not the borrowing application itself.
- **Collateral and borrowed asset:** These are the assets involved in a position. Which assets are supported, how they are valued, and what rules apply must be checked in the specific application’s documentation and deployed configuration.
- **Application logic:** Smart-contract code or other on-chain software records or processes position state and applies the rules encoded in that implementation. A general description cannot establish which functions, parameters, or administrator controls a particular deployment has.
- **Blockchain settlement:** Transactions are submitted to a network and, subject to its protocol and consensus design, incorporated into its shared history. The network’s settlement behavior is a dependency, not a guarantee that every application-level outcome is beneficial or reversible.
- **User interface and integrations:** A website, wallet, API, relayer, or other service may help construct, route, display, or submit transactions. The interface is not necessarily the source of truth for the application’s on-chain state. Designs differ, and services may introduce dependencies beyond the contract and network.
- **Position state and external inputs:** A borrowing system may need state or data to evaluate whether its rules are met. The specific sources, update mechanisms, and failure behavior cannot be inferred from the general DeFi model; they require application-specific verification.

The BIS layer model helps teams avoid treating a visible interface as the whole system. It also encourages separate examination of the application’s code, the network where it settles, and the services that connect users to it. [claim_bis_defi_layers]

## How DEFI Borrowing Explained works

A typical collateralized borrowing flow can be mapped as a sequence of questions and state changes. This is a general workflow, not a claim that every DeFi borrowing application follows the same steps or uses the same terminology.

1. **Review the deployment and proposed action.** The user identifies the application, network, assets, and relevant rules. A front end may display these details, but teams should distinguish interface descriptions from the application’s deployed behavior.
2. **Authorize an asset transfer or other required action.** If the design requires collateral, the user signs the transaction that supplies or makes it available under the application’s rules. The wallet signs; the blockchain processes the submitted transaction according to its own protocol.
3. **Create or update a borrowing position.** The application records the resulting state and applies its implemented conditions. The precise meaning of the position, the permitted amount, and any ongoing requirements depend on that application’s code and configuration.
4. **Request the borrowed asset.** A subsequent action, or a combined transaction where supported, asks the application to release or account for the borrowed asset. Whether it succeeds depends on the relevant application rules and the transaction’s execution conditions.
5. **Monitor the position and applicable conditions.** A borrower or operator needs to track the state that the application uses. Monitoring tools may read or summarize that state, but teams should verify important values against the appropriate source rather than assuming a dashboard is authoritative.
6. **Repay or otherwise close the position under the system’s rules.** The user submits the action required by the implementation. The position’s final state and any remaining obligations should be checked on the relevant network and in the application’s records.

At each step, there are two different questions: what action did the user authorize, and what state change did the deployed system actually process? A wallet prompt or interface message describes a proposed interaction; transaction and application state provide evidence of what occurred. Neither should be interpreted without the relevant network and contract context.

## Trust and control boundaries

The practical trust boundary includes more than smart-contract code. It can include the blockchain’s consensus and transaction-processing design, the application’s deployed logic, the user’s key-management process, and any interface or off-chain service used to access the system. A public permissionless decentralized exchange, for example, can let users retain control of assets while trades execute or settle through smart contracts on a blockchain. But designs differ and can still depend on interfaces, relayers, administrators, or off-chain order components. [claim_bis_dex_distinction] This is an example of why asset control and system independence are separate questions; it is not evidence that every borrowing application has the same arrangement.

A system’s stated decentralization is also not sufficient evidence of how control is distributed in practice. Crypto and DeFi systems can exhibit substantial de facto centralization, and the degree and location of concentration must be assessed for a specific network, asset, application, and time window. [claim_bis_de_facto_concentration] Teams should therefore identify who can change application parameters, pause or upgrade software, control interfaces, or affect access, where those powers exist and are documented.

Operational capacity is another separate consideration. The PFMI liquidity-risk principle says payment or settlement infrastructure must manage sufficient liquid resources in relevant currencies to meet settlement obligations under normal and stressed conditions. That principle is an operational analogy when assessing crypto payment infrastructure; PFMI applies to designated financial market infrastructures, not every crypto product. [claim_payment_settlement_liquidity] It should not be presented as a rule that every DeFi borrowing application must meet, nor as proof that a given application has sufficient resources.

## Limitations and failure modes

A general workflow does not establish that a borrowing position is safe, available, or recoverable. Several dependencies can affect the result:

- **Network behavior:** Transaction processing and the assurance associated with a shared history depend on the network protocol and consensus design. A transaction’s success on one layer does not validate every assumption made by an application.
- **Application-specific rules:** Code and configuration determine what actions are accepted and how state changes. General descriptions cannot establish the precise conditions, administrative powers, or consequences for a particular deployment.
- **Interfaces and intermediaries:** A front end or integration can be a separate dependency. A system may retain on-chain components while still relying on services that affect how users discover, construct, or submit transactions.
- **Concentration of control:** A decentralization label does not reveal the actual distribution of decision-making or operational influence. Assessment requires evidence about the particular system and a defined time window. [claim_bis_de_facto_concentration]
- **Liquidity and settlement capacity:** The relevant operational question depends on the infrastructure and obligations being assessed. The PFMI analogy is limited to its stated scope and does not establish a general requirement or outcome for all DeFi products. [claim_payment_settlement_liquidity]
- **Evidence gaps:** A description of intended behavior is not the same as evidence of deployed behavior. If documentation, code, interface data, and observed transactions do not align, the discrepancy needs investigation rather than assumption.

These limitations mean that “on-chain” should not be used as a synonym for risk-free, fully decentralized, or automatically recoverable. The sources support distinctions among system layers, network validation, control distribution, and infrastructure liquidity; they do not support a guarantee of successful borrowing or repayment.

## What teams should verify

Before integrating with or operating around a borrowing application, teams can build an evidence record around the following questions:

1. **Which deployment is in scope?** Record the network, application, contract addresses or other deployment identifiers, and the date or time window for the assessment.
2. **What does each layer do?** Map settlement, application, and interface components. Note whether a service, relayer, or other off-chain component participates, and avoid assuming that the layers are organized identically across systems. [claim_bis_defi_layers]
3. **What behavior is documented, and what is deployed?** Compare official documentation with the relevant deployed code and configuration. Identify the source of each material parameter and the evidence that it applies to the deployment being assessed.
4. **What does the user authorize?** Inspect the transaction details presented for signing and determine which account, asset, and application action they concern. Compare the proposed action with the resulting transaction and state rather than relying only on interface labels.
5. **Where does control reside?** Look for documented administrative or operational roles and identify dependencies on interfaces or other services. Assess actual concentration for the specific system and time window; do not infer it from a decentralization claim alone. [claim_bis_de_facto_concentration]
6. **How is settlement evidenced?** Identify the network’s relevant transaction-history and consensus assumptions. A shared history helps address double spending, but the mechanism and assurance level depend on the network design. [claim_bis_double_spend]
7. **What operational resources or obligations are relevant?** If assessing payment or settlement infrastructure, define the obligations and relevant currencies, then evaluate the applicable evidence. Treat the PFMI liquidity principle as an analogy unless the infrastructure is a designated FMI to which PFMI applies. [claim_payment_settlement_liquidity]
8. **What remains unknown?** Record unverified assumptions, missing documentation, and differences between intended and observed behavior. Revisit the evidence when the deployment, network, service dependencies, or assessment window changes.

This process turns “How does DeFi borrowing work?” into a system map: who initiates actions, which software applies the rules, where transactions settle, what services sit in between, and which facts still need deployment-specific verification. It explains the mechanism without assuming that all protocols share the same design or that any particular outcome is assured.

## Sources and references

- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
- [Principles for Financial Market Infrastructures](https://www.bis.org/committees/cpmi/pfmi/overview) — Committee on Payments and Market Infrastructures; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
