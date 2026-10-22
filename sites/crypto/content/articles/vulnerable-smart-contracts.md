---
title: "Vulnerable smart contracts: common weaknesses and their risks"
description: "Learn what makes vulnerable smart contracts risky, how common coding and design weaknesses can affect dApps, and what security reviews can and cannot show."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["smart contract security risks", "smart contract vulnerabilities", "contract audit limitations"]
author: "editorial_team"
primary_keyword: "vulnerable smart contracts"
owned_question: "What makes a smart contract vulnerable, and how can common weaknesses affect its behavior and users?"
risk_level: "high"
---

A smart contract is vulnerable when its code or surrounding assumptions allow behavior that conflicts with its intended rules. For developers and dApp operators, the key is to assess the weakness, the paths that can reach it, and the contract’s dependencies—not to assume that every reported bug can be exploited or will cause the same harm.

## What makes a smart contract vulnerable?

A smart contract is code and persistent data at an on-chain address. On Ethereum, a user account can invoke a contract function by submitting a transaction to that deployed contract. This means that a weakness may matter only when particular conditions, inputs, permissions, or interactions occur; the label “vulnerability” alone does not establish that an attack has happened or that funds are at risk. [source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>) [source](<https://ethereum.org/developers/docs/smart-contracts/>)

A bug is an unintended behavior or defect in code. A vulnerability is a weakness that could undermine an intended security property under relevant conditions. A report describes a suspected or identified issue; an attempted attack is an effort to trigger harmful behavior; and a confirmed incident requires evidence that the weakness was actually used to produce an adverse effect. These are distinct stages, and a report or attempt is not by itself proof of an incident.

Risk can also come from the system around the code. A contract may call or reuse independent on-chain components through public interfaces. Each dependency adds behavior, upgrade, permission, availability, and economic assumptions to the caller’s system. A contract’s own logic can therefore be correct while its effective behavior still depends on components outside its direct control. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Whether deployed behavior can be changed depends on the contract’s design. The evidence here does not establish a universal rule about reversibility, upgrades, or repair. Review the deployed system’s actual controls and dependencies rather than assuming that an issue can be patched—or that it cannot.

## Common vulnerable smart contracts: weakness categories

**Authorization errors** occur when a sensitive function does not enforce the intended permission boundary, or when the permission check does not match the action being protected. Potential consequences depend on what the function can change and which callers can reach it. A function that changes an ordinary setting presents a different impact scenario from one that controls assets or critical system state; the code and configuration must be examined to establish that difference.

**Unsafe external interactions** arise when a contract relies on another contract or service without accounting for its behavior, availability, permissions, or economic assumptions. Composability makes reuse possible, but it also means a dependency can affect the caller’s behavior. The existence of a dependency is not proof of a defect; the important defensive question is what the calling contract assumes and what happens if those assumptions fail. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

**Flawed validation or accounting** can cause a contract to accept inputs or state transitions that do not match its intended rules. A mistake in a condition, calculation, or record of state may produce an incorrect result or disrupt expected functionality. The specific consequence cannot be inferred from the category alone: it depends on the code path, the values involved, and the state the contract maintains.

**Reentrancy** is a risk associated with interactions in which control passes to another contract before the original operation has safely completed. Such interactions can make assumptions about intermediate state important. Whether a particular pattern creates a vulnerability depends on the contract’s logic and context; identifying an external call alone is not enough to establish exploitability.

Arithmetic, logic, and configuration mistakes are likewise context-dependent. A defect may remain unreachable under the deployed configuration, or a small configuration change may alter which behavior is possible. Effective review therefore considers the contract, its permissions, its connected components, and the deployment conditions together—not merely a list of code patterns.

## How a weakness can affect a dApp

A weakness can affect contract behavior when a reachable path permits an unintended state change or prevents an intended operation. If a contract holds or manages on-chain assets, the potential consequences can include unauthorized changes to how those assets are handled. But a vulnerability category does not establish that a path is reachable, that an attacker has the necessary permissions, or that a particular asset can be affected. Those questions require analysis of the deployed code and its surrounding system.

A dApp can depend on more than its contract. Contracts may call independent on-chain components, and each component adds assumptions about behavior, upgrades, permissions, availability, and economic conditions. A failure in one dependency may therefore affect the application that relies on it, even if the application’s own code is unchanged. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Cross-chain systems illustrate why boundaries matter. Bridges coordinate activity between otherwise isolated blockchain environments, and their security depends materially on who or what verifies the source-chain event. A weakness in verification can affect the bridge’s assumptions about whether a transfer or message should be accepted. That is a risk scenario, not a claim that every bridge or transfer is vulnerable. [source](<https://ethereum.org/developers/docs/bridges>)

Keep on-chain and off-chain consequences distinct. A contract-level issue concerns deployed code and state. Interfaces, custodians, bridge operators, or other connected systems may have separate responsibilities and failure modes. An observed user problem does not, by itself, identify which component failed; trace the relevant system boundaries before attributing cause or impact.

## What security reviews can and cannot establish

A security review is evidence about the system examined, not a guarantee about every possible system state. An audit or test may identify issues within its defined scope and at the time of review, but a result does not prove that a contract is free of vulnerabilities or secure under all conditions. The evidence available here does not establish a particular review’s methods, coverage, or effectiveness, so those details should be checked in the review documentation rather than assumed.

When evaluating a review, establish what code and configuration it covered, which dependencies and privileges it considered, what assumptions it made, and whether findings remain unresolved. Also check whether the deployed code or configuration changed after the review. A review of one version cannot automatically establish the security properties of a different deployed version or of a system with changed dependencies.

Treat an issue’s status carefully. A finding may describe a confirmed defect without showing that it has been exploited; a suspected issue may require further verification; and the absence of a finding does not prove the absence of weaknesses. Separate what the report documents from what it does not establish, especially when communicating possible impacts to users or decision-makers.

## Defensive steps before and after deployment

Before deployment, map the contract’s important state, sensitive actions, permissions, and external dependencies. Check that the intended rules are represented in the code and that validation and accounting behavior match those rules. Use testing, peer review, and independent assessment appropriate to the system’s risk, while recording the scope and assumptions behind each review. These steps provide evidence for decisions; they do not establish guaranteed security.

During operation, keep track of who can perform sensitive actions and which dependencies the application relies on. Review the system when deployed code, configuration, permissions, or connected components change. Because dependencies add their own behavior and assumptions, a change outside the application’s main contract can also matter to the application’s risk profile. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

If a weakness is suspected, distinguish confirmed observations from hypotheses, preserve relevant evidence, and follow established organizational response procedures. Do not infer that funds can be recovered or that a particular response will reverse an on-chain effect. The appropriate assessment depends on the specific deployed system and what evidence is available.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
