---
title: "Blockchain dApp Architecture: Wallets, RPC, Contracts, and Indexers"
description: "See how a dApp connects its front end, wallet, RPC node, smart contracts, indexer, storage, oracles, and off-chain services, including key trust boundaries."
date: "2026-10-19"
draft: false
content_type: "explainer"
topics: ["smart-contracts-dapps"]
tags: ["dApp architecture", "Web3 application architecture", "decentralized application architecture", "dApp frontend architecture", "blockchain application stack"]
author: "editorial_team"
primary_keyword: "blockchain dapp architecture"
owned_question: "How do wallets, front ends, RPC providers, indexers, smart contracts, and off-chain services fit into a dApp architecture?"
risk_level: "medium"
---

A **blockchain dApp architecture** is the full system that lets a user interface read decentralized state, request an account authorization, submit a transaction, and present the resulting application state. The smart contract is central, but it is only one component. A production dApp commonly includes a web or mobile front end, a wallet-facing provider, an RPC node, one or more contracts, an indexer, and off-chain services for work that does not belong on-chain.

The useful architectural question is not whether every component is decentralized. It is which component has authority over each fact or action, what can fail independently, and how the application proves the result it shows. That map prevents an RPC response, indexer record, browser configuration, or backend assertion from being treated as equivalent to finalized chain state.

## A dApp is a system, not only a smart contract

Ethereum's technical definition combines a smart contract with a frontend user interface. The contract supplies shared rules and on-chain state. The frontend gives people a usable way to inspect that state and form actions. Supporting components connect the two.

A typical stack has these roles:

- **Frontend:** renders pages, validates input, and composes read or write requests.
- **Wallet and provider:** exposes authorized accounts, reports chain and account changes, and asks the user to approve signatures.
- **RPC node or gateway:** reads chain data, simulates calls, and broadcasts signed transactions.
- **Smart contracts:** execute deterministic rules and update on-chain state.
- **Indexer:** converts blocks, transactions, receipts, and logs into query-friendly entities.
- **Off-chain services:** handle private data, notifications, scheduled work, file delivery, analytics, or integrations.
- **Oracle:** delivers external facts to a contract through a defined trust and update model.

Calling the whole stack a dApp does not make every layer trustless. A frontend served from one domain, a single RPC account, or a proprietary indexer can be an availability or censorship dependency even when the contract remains accessible through another interface. Architecture documentation should state those dependencies instead of hiding them behind a Web3 label.

## The front end presents state and composes intent

The browser or mobile client is the user's control surface. It knows presentation rules, supported networks, contract addresses, ABIs, token metadata, and feature configuration. It may combine direct RPC reads with indexed history and off-chain profile data to render one page.

That convenience creates a responsibility: label the provenance of material values. A wallet balance read at block 20,000,000, an indexer's transaction list synced to block 19,999,980, and a backend's cached price do not share one consistency boundary. The UI should not merge them into a single apparently atomic state without accounting for their timestamps and block references.

Frontend code is also replaceable. A user could call the same public contract through another interface, but only if the contract address, network, and functions are discoverable. Publishing verified addresses and interface versions reduces dependence on the original website. It does not remove phishing risk; the application still needs an authenticated delivery path and clear transaction previews.

## The wallet controls identity and authorization

The wallet is not merely an RPC transport. It manages account keys or delegates access to a signing system, applies permissions, and presents requests for user approval. The EIP-1193 provider is the interface exposed to an application. It offers a minimal `request` method plus events such as `accountsChanged` and `chainChanged`.

This separation matters. The frontend can ask for accounts or request a signature, but it should not receive the private key. The provider passes messages between the application, wallet, and client. Because a webpage is an untrusted environment, the wallet must validate requests, isolate key material, limit exposed account data, and make chain changes visible.

The application must react when the selected account or network changes. Cached allowances, balances, and contract addresses can become wrong immediately after either event. Before a write, bind the displayed action to the current chain ID, sender, destination, method, arguments, value, and fee policy. [A cryptocurrency wallet API](/articles/cryptocurrency-wallet-api/) explains the account, signing, and transaction boundary in more detail.

## RPC connects the application to chain state

An RPC endpoint is the network path to a node. Ethereum clients implement JSON-RPC methods so applications can read blocks, query contract state, estimate or simulate execution, obtain transaction receipts, and broadcast signed transactions. A library may hide the raw JSON, but the trust boundary remains.

The endpoint determines which chain view the application sees. It may be behind the head, lack archive state, impose log-range limits, or return an error during reorganization or overload. Two providers can briefly disagree without either being malicious. For high-value operations, record the chain ID, block number or hash, endpoint, request, and response; use explicit state contexts; and compare independent paths where the risk justifies it.

Failover needs semantic checks, not only another URL. A backup endpoint should point to the intended chain, support the required methods and history, and meet the same finality policy. Otherwise an automatic retry can silently change the meaning of a read. [What a blockchain API is](/articles/what-is-a-blockchain-api/) describes the broader family of node and data interfaces.

## Smart contracts own deterministic on-chain rules

Contracts are the shared execution layer. Their code and current state decide whether a call succeeds, which storage changes occur, and which events are emitted. A contract can own balances, permissions, settlement rules, or protocol state in a way that multiple frontends can independently access. [What smart contracts are](/articles/what-are-smart-contracts/) covers this execution model.

A contract is not a general backend. On-chain computation and storage cost resources, public state is visible, and a contract cannot make an ordinary HTTP request during execution. Bugs, privileged upgrade paths, paused states, and external contract dependencies belong in the architecture diagram. So do proxy and governance controls, because the address a frontend calls may not uniquely identify immutable logic.

Events are useful integration outputs, but the contract's state and receipt are authoritative for execution. An event can be omitted, renamed after an upgrade, or misunderstood by an indexer. Business acceptance should check the exact contract, chain, transaction status, event identity, and any required state rather than trusting a human-readable notification alone.

## Indexers turn chain history into application queries

Nodes expose protocol-shaped data, not necessarily the product query a user wants. Asking for every position owned by an account or every payment associated with an order may require scanning many blocks and decoding many logs. An indexer performs that work ahead of time.

The Graph describes a Subgraph as an open API that extracts blockchain data, processes it, stores entities, and exposes them through GraphQL. Its manifest identifies contracts and events; mappings transform those events into a schema designed for application queries. Other indexing systems use different technology but fill the same architectural role.

An indexed record is a derived view, not new chain authority. It can lag the head, miss an event because of a mapping error, or need rollback after a reorganization. Production consumers should know the indexer's latest processed block, retain block and transaction provenance, make writes idempotent, and provide a recovery or backfill path. [A blockchain data API](/articles/blockchain-data-api/) explains how derived data differs from direct node state.

## Off-chain services handle work the chain should not

Most useful dApps still have conventional services. A backend may keep encrypted user preferences, issue notifications, coordinate a transaction queue, calculate non-authoritative analytics, protect an API key, or integrate with email and payment systems. Object storage or content-addressed storage can hold files that are too large or unsuitable for contract storage.

These services should not quietly become the only enforcer of a rule advertised as on-chain. If a backend decides whether an action is allowed before a contract call, document whether the contract independently enforces the same condition. If a frontend asset or metadata file is referenced by a content hash, availability still requires a host or pinning strategy; integrity and availability are separate properties.

Oracles occupy a specific bridge position. They make external information available on-chain through contracts and an update process. They are not the same as an RPC provider, which exposes chain data, or an indexer, which reorganizes chain history. Oracle source quality, update frequency, fallback behavior, and governance become part of the dApp's on-chain risk model.

## Trace reads and writes through different paths

A **read path** might begin when the frontend asks an indexer for a user's positions, then verifies a critical balance through RPC at a named block. The frontend combines those results with local display metadata and shows the indexer's sync height. No signature is required unless the application needs proof of account control.

A **write path** begins with user intent. The frontend encodes a contract call and asks the wallet to approve it. The wallet confirms the account, chain, destination, arguments, and value, then signs. RPC broadcasts the signed transaction. The application tracks the hash until a receipt reports execution and the required confirmation policy is met. Afterward, the indexer observes the canonical log and refreshes the query model.

These paths converge only after chain execution. A successful frontend request is not a successful transaction. A returned hash is not inclusion. Inclusion is not necessarily successful execution, and a newly observed block may not meet the application's finality threshold. [How a smart contracts API works](/articles/smart-contracts-api/) follows this lower-level request lifecycle.

## Design around trust and failure boundaries

Before launch, an architecture review should answer:

- Which chain, contract address, ABI, and implementation version does each environment use?
- Which facts come directly from contract state, receipts, logs, indexed entities, or off-chain databases?
- Where are private keys, API credentials, personal data, and administrative permissions held?
- What happens if the wallet, RPC endpoint, indexer, oracle, storage host, or backend is unavailable?
- How does the system detect stale blocks, indexer lag, chain reorganization, duplicate events, and failed execution?
- Can users reach the contracts through another interface, and can they verify the addresses?
- Which components can change rules or software, and how are upgrades disclosed and monitored?
- What identifiers connect a UI action to its account, chain, transaction, receipt, log, and derived record?

The concise model is: the frontend composes intent, the wallet authorizes it, RPC connects to a node, contracts execute shared rules, indexers organize history, and off-chain services supply capabilities that are private, expensive, or impossible on-chain. A sound blockchain dApp architecture makes those responsibilities and failure modes visible. It does not pretend that using a smart contract erases the trust placed in every surrounding component.

## Sources and references

- [Technical introduction to dapps](https://ethereum.org/developers/docs/dapps/) — ethereum.org; retrieved 2026-10-19.
- [EIP-1193: Ethereum Provider JavaScript API](https://eips.ethereum.org/EIPS/eip-1193) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [JSON-RPC API](https://ethereum.org/developers/docs/apis/json-rpc/) — ethereum.org; retrieved 2026-10-19.
- [Subgraphs](https://thegraph.com/docs/en/subgraphs/overview/) — The Graph Documentation; retrieved 2026-10-19.
- [Smart Contract Overview](https://docs.chain.link/getting-started/conceptual-overview) — Chainlink Documentation; retrieved 2026-10-19.
