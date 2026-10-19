---
title: "Smart Contract Examples: Escrow, Tokens, Access, and Settlement"
description: "Explore four smart contract patterns for escrow, token balances, access control, and automated settlement, including their trust assumptions and failure modes."
date: "2026-10-19"
draft: false
content_type: "analysis"
topics: ["smart-contracts-and-dapps"]
tags: ["examples of smart contracts", "smart contract use cases", "smart contract escrow", "token smart contract", "automated settlement smart contract"]
author: "editorial_team"
primary_keyword: "smart contract examples"
owned_question: "Which smart-contract patterns illustrate escrow, tokens, access control, and automated settlement?"
risk_level: "medium"
---

Useful **smart contract examples** are not lists of brand names. They are small patterns that show what state a contract stores, who may change it, which assets can move, and what happens when a condition is or is not met. Four patterns explain a large share of real applications: escrow, token ledgers, role-gated operations, and conditional settlement.

These examples are conceptual. They intentionally omit production code, chain-specific deployment details, audits, legal terms, key-management architecture, and interface design. Start with [what a smart contract is and how it executes](/articles/what-are-smart-contracts/) if terms such as state, transaction, and gas are unfamiliar.

## Read the pattern, not the product label

A product can call itself a marketplace, stablecoin, payment rail, membership pass, or settlement network while using several of the same contract patterns. Analyze each example with six questions:

1. What input starts the transition?
2. What state does the contract store before and after it?
3. Which account or role may call the function?
4. Which asset or right moves?
5. Which external fact or service does the decision depend on?
6. What path exists for failure, cancellation, dispute, or recovery?

A contract does not understand commercial intent. It evaluates encoded conditions against the state and inputs available to it. If the rule says an administrator can pause transfers, then the administrator key is part of the trust model. If release depends on an offchain delivery, the mechanism that reports delivery is part of the system even though it is not inside the contract.

## Example 1: escrow as a state machine

An escrow contract holds value while an exchange moves through explicit states. A simplified model might use:

`Created -> Funded -> Shipped -> Accepted -> Released`

It also needs exception states such as `Cancelled`, `Refunded`, or `Disputed`. The contract can reject a release call before funding, stop a second withdrawal after release, and record which address receives each amount.

Solidity's educational safe remote purchase example shows the pattern. Buyer and seller post deposits, the contract locks the value, and the buyer later confirms receipt. The contract then returns part of the deposits and releases the seller's proceeds. The example uses financial incentives to encourage completion. It does not prove that a physical shipment arrived.

That limitation is central. An onchain contract can see its own funding and calls, but not a package on a doorstep. A real design needs one or more of the following:

- mutual confirmation by the parties;
- a trusted arbitrator or multisignature decision;
- a verifiable digital event;
- an oracle that reports an external fact; or
- commercial and legal procedures outside the chain.

The contract should define timeouts, who can invoke each path, how partial performance is handled, and whether a dispute freezes or redirects funds. A production escrow must also protect withdrawals from reentrancy and failed recipients. Solidity documents the checks-effects-interactions pattern: validate first, write internal state second, and call an external address last. This ordering reduces a class of reentrancy risk but does not replace review and testing.

## Example 2: a fungible-token ledger

A token contract is a shared ledger with a standard interface. At minimum, it maps addresses to balances and applies transfer rules. ERC-20 standardizes operations such as checking a balance, transferring tokens, approving a spender, and letting the approved spender transfer up to an allowance.

A simplified direct transfer is:

`check sender balance -> subtract amount -> add amount to recipient -> emit transfer event`

An allowance flow adds a second state variable:

`owner approves spender -> allowance recorded -> spender calls transferFrom -> balance and allowance reduced`

The common interface lets wallets and applications interact with many tokens without learning a unique method for each one. That composability is the pattern's main value. It does not establish what the token represents. The same ledger mechanics can support a utility balance, governance unit, receipt, stablecoin, or [tokenized asset](/articles/what-are-tokenized-assets/).

The contract still needs policy decisions that ERC-20 does not answer:

- Who can create or destroy supply?
- Is supply capped?
- Can an administrator pause, freeze, or recover balances?
- Is the token backed by an offchain asset, and who verifies the backing?
- Which allowance and approval risks must the interface explain?
- Can the implementation be upgraded?

For a stablecoin, the ledger is only one layer. Issuance, reserve assets, redemption, banking access, compliance, and chain-specific contracts sit around it. Review [how stablecoins work](/articles/how-do-stablecoins-work/) rather than treating an ERC-20 balance as proof of redeemability.

## Example 3: role-gated operations

Access control is a pattern for deciding who may call sensitive functions. A basic contract may have one owner. A more granular system can define roles such as `MINTER`, `PAUSER`, `SETTLER`, and `UPGRADER`. The function checks the caller's role before changing state.

OpenZeppelin's access-control model separates functional roles from their administrators. An account with a minter role can be allowed to mint without being able to grant that role to others. A role's admin can grant and revoke membership. This creates a permission graph rather than a single all-powerful switch.

Consider a tokenized invoice workflow:

- an issuer role creates an invoice record;
- a verifier role marks required evidence as accepted;
- a settler role releases payment;
- a pauser role stops new settlement during an incident; and
- an admin role changes role membership.

The design is only as strong as its administration. OpenZeppelin warns that the default admin role is especially powerful. A secure system may place administration behind a multisignature account, delay sensitive changes, separate proposer and executor duties, and monitor every role event.

A common mistake is to document a role that the code does not actually check. Permission rules protect only the functions wired to them. Another is to decentralize ordinary functions while leaving one upgrade or emergency key able to replace the implementation or seize control. The complete authority map must include proxies, timelocks, guardians, signers, and external service accounts.

## Example 4: conditional automated settlement

A settlement contract applies a rule that moves value or marks an obligation complete when a condition is satisfied. A simplified flow is:

`obligation funded -> trigger submitted -> condition verified -> state marked settled -> asset transferred`

The trigger might be a user transaction, a scheduled automation service, another contract's event, or an oracle report. A deployed contract can hold onchain assets and apply programmed actions when it receives a valid call. It does not wake itself merely because a wall-clock deadline passed. Someone or some automation mechanism still submits a transaction and pays or supplies gas.

Conditions based entirely on chain state are the simplest. For example, a contract can release collateral after another onchain position is repaid. Conditions based on an exchange rate, shipment, bank confirmation, weather observation, or identity status require external input. An oracle can deliver that input, but then data selection, update frequency, outage behavior, manipulation resistance, and governance become part of the settlement design.

A robust settlement pattern defines more than the happy path:

- Which observation is authoritative?
- How fresh must it be?
- What happens if the oracle or automation service is unavailable?
- Can a condition be challenged?
- Is there a price or amount tolerance?
- Does a failed transfer leave the obligation settled or retryable?
- Who can pause, cancel, or recover funds?

The word automated means that the outcome follows encoded rules after a valid trigger. It does not mean the system has no operators, external dependencies, or judgment.

## How the patterns combine

A business workflow often composes all four patterns. Imagine an onchain invoice represented by a tokenized record:

1. An authorized issuer creates the invoice.
2. A payer deposits a supported token into escrow.
3. The contract records the funded state and prevents duplicate settlement.
4. An oracle or authorized verifier supplies evidence that a specified condition occurred.
5. The settlement function validates the evidence and caller.
6. Internal state changes to settled before the contract transfers funds.
7. Events provide an auditable trail for downstream systems.

This sequence can reduce manual reconciliation between parties that accept the same rules. It does not make the underlying invoice valid, the payer solvent, the external evidence true, or the legal obligation enforceable. Those properties come from systems outside the contract.

Composition also increases failure surfaces. The token may have transfer restrictions. The escrow may call an untrusted token contract. The oracle may be stale. An admin may pause settlement. An upgrade may change the rules after funding. Each component needs an explicit interface and failure policy.

## What the examples do not solve

Smart contracts can make rules visible and consistently executable, but they do not automatically provide:

- **correct requirements:** code can precisely enforce the wrong business rule;
- **truth about the physical world:** external facts require people, devices, institutions, or oracles;
- **safe keys:** a compromised role or signer can exercise every permission it holds;
- **economic liquidity:** a token transfer function does not guarantee a usable market or redemption route;
- **secure upgrades:** changeability solves some maintenance problems while adding administrator and governance risk;
- **privacy:** public-chain state and events may expose activity even when names are absent;
- **legal enforceability:** a technical state transition is not by itself a complete contract under every jurisdiction; or
- **bug-free execution:** audits, tests, formal reasoning, monitoring, and incident procedures reduce risk but cannot prove every deployment safe.

Interfaces can also create false confidence. A token that implements a familiar method name may still add transfer fees, block addresses, pause movement, or deviate from expected return behavior. Integrations must test the actual deployed contract and not infer safety from a standard label.

## A checklist for evaluating a smart contract example

Before adapting an example, write down:

1. **State diagram:** every valid state and transition, including cancellation and recovery.
2. **Authority map:** every account, role, admin, signer, proxy, oracle, and automation service.
3. **Asset flow:** what enters, what leaves, who can receive it, and what happens if a transfer fails.
4. **Input boundary:** which facts are onchain and which arrive from an external source.
5. **Timing model:** deadlines, confirmation rules, stale data, gas funding, and service outages.
6. **Invariant set:** properties that must always hold, such as total balances matching supply or settled funds being non-withdrawable twice.
7. **Upgrade and shutdown plan:** who can change code, pause operations, migrate state, or recover from an incident.
8. **Verification evidence:** tests, independent review, deployed bytecode, configuration, monitoring, and a current dependency inventory.

The most instructive smart contract examples are small enough to expose their assumptions. Escrow illustrates controlled state transitions, tokens illustrate shared ledgers and interfaces, access control exposes authority, and conditional settlement shows how rules connect assets to triggers. Production systems emerge by composing these patterns carefully, not by copying a short code sample.

## Sources and references

- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control) — OpenZeppelin; retrieved 2026-10-19.
- [Smart Contract Overview](https://docs.chain.link/getting-started/conceptual-overview) — Chainlink Documentation; retrieved 2026-10-19.
