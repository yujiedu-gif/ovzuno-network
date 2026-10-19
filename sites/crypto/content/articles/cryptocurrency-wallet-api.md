---
title: "Cryptocurrency Wallet API: Keys, Signing, Policies, and Events"
description: "Evaluate a cryptocurrency wallet API by key control, account creation, signing, transaction policy, balances, webhooks, recovery, and operational security."
date: "2026-10-19"
draft: false
content_type: "explainer"
topics: ["wallets-custody"]
tags: ["crypto wallet API", "wallet infrastructure API", "blockchain wallet API", "wallet signing API", "wallet transaction API"]
author: "editorial_team"
primary_keyword: "cryptocurrency wallet api"
owned_question: "What does a cryptocurrency wallet API manage across addresses, signing, policies, balances, and webhooks?"
risk_level: "high"
---

A **cryptocurrency wallet API** lets software create or reference blockchain accounts, read chain state, request signatures, send transactions, and receive lifecycle events. Those functions do not reveal who controls the assets. Some APIs only read public data. Some ask an end user to authorize every signature. Some let a developer's backend request signatures from protected key infrastructure. Others expose a custodial account whose provider controls withdrawals under an account agreement.

That control boundary is the first thing a technical buyer must document. An address-creation endpoint can look similar across products while the key owner, signing authority, recovery path, and legal relationship are completely different.

If the distinction between an account at an exchange and an independently controlled wallet is unfamiliar, start with [cryptocurrency exchange versus wallet](/articles/crypto-exchange-vs-wallet/).

## First identify the control model

Map six questions before comparing endpoints:

1. Who generates the signing key or key shares?
2. Where are they stored and used?
3. Who can authorize a signature?
4. Who constructs and broadcasts the transaction?
5. Who can recover, rotate, export, freeze, or delete access?
6. Does the API represent an onchain address or a provider's internal custodial balance?

A **data-only API** can return addresses, balances, transactions, token metadata, or fee estimates without signing anything. A **user-controlled API** requires the end user to approve signatures through credentials or a device-bound flow. A **developer-controlled API** allows the application backend to request signatures under provider and application controls. An **external-signer API** prepares payloads while a separate hardware, MPC, or key-management system signs them. A **custodial account API** instructs a regulated or commercial custodian to move assets it controls for the customer.

Provider labels are not universal custody definitions. Coinbase's current wallet documentation, for example, distinguishes end-user-owned wallets from API-key wallets controlled by a developer's server. That proves its documented product model, not how every service or jurisdiction classifies custody.

## Accounts, addresses, and network identity

A wallet API should model the account type explicitly. An externally owned account signs with a key. A smart account can add programmable authorization, batching, spending rules, or gas sponsorship. Other chains use different account and address models. Coinbase currently documents EVM externally owned accounts, EVM smart accounts, and Solana accounts, plus the ability to attach an account policy.

The object model should identify:

- network and chain ID, not only an asset ticker;
- account type and signing curve;
- address, derivation or creation context, and wallet-set relationship;
- user or business owner in the application;
- provider ID plus an immutable internal correlation ID;
- deployment status for smart accounts; and
- policy, label, and lifecycle state.

Do not assume one address means one network identity. Some EVM-compatible networks can use the same hexadecimal address while balances, contracts, nonces, fees, and transaction histories remain chain-specific. Deposit systems may require a memo or tag in addition to an address. The API contract must keep those dimensions together.

## Transaction construction, signing, and broadcast

A safe workflow separates intent from execution:

1. The application creates a transaction intent with destination, asset, amount, network, and business purpose.
2. The system resolves nonce, fees, token contract, call data, and gas requirements.
3. A simulator or policy engine evaluates the unsigned transaction where supported.
4. The required user, service, or approvers authorize it.
5. The wallet signs the exact serialized payload.
6. The application or provider broadcasts it.
7. Both record the hash and follow replacement, confirmation, failure, and finality.

Signing and broadcasting need not be the same API call. Coinbase documents interfaces that return signed messages, typed data, hashes, or transactions, including flows in which the application broadcasts separately. Circle's developer-controlled EVM tutorial similarly separates wallet creation, transaction construction through a blockchain node, and signing through its SDK. These examples show why a buyer should ask which component owns each step.

The API should expose the exact network, nonce, fee fields, destination, value, token contract, method, and call data before authorization. A human approval screen or policy service cannot evaluate a vague request such as `send transaction`. For contract calls, decoded method and parameter information should supplement, not replace, the signed bytes.

## Policies and approval controls

A policy should be enforceable at or before signing, not merely checked by application UI. Useful controls can include allowed networks, assets, destinations, contract addresses, methods, amount limits, time windows, velocity limits, and required approvers. The system should say whether a rule blocks signing, blocks broadcasting, or only raises an alert.

Roles must separate wallet administration, policy changes, transaction creation, approval, signing-service credentials, and audit access. High-value operations may require a quorum or independent approval path. A policy change should create a durable audit event and should not silently authorize a transaction already waiting in a queue unless that behavior is explicit.

The API response should include the policy decision, matched rule, approvers, timestamps, and final signed payload or transaction identifier. If a request is denied, return a stable error code rather than forcing software to parse a sentence.

## Balances, transactions, and webhooks

Balance data needs provenance. An API should identify the block height or time observed, confirmed and pending amounts, token contract, decimal precision, and whether results come from the provider's indexer, a connected node, or an internal custodial ledger. Token discovery should not automatically make every unsolicited asset safe or visible to users.

Transaction records should preserve the submitted intent, signed payload or hash, broadcast time, provider status, chain status, fee, failure reason, replacement relationship, and confirmation point. [How a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/) explains why provider submission, mempool observation, block inclusion, and application finality are separate states.

Webhooks should carry unique event IDs and resource versions. Consumers should verify signatures, reject stale or replayed events under the provider's current rules, process idempotently, and tolerate duplicates or reordered delivery. Circle, for example, documents a signature header and key ID that clients use to retrieve a public key and verify notification origin. Another provider may use HMAC or a different rotation scheme, so integrations must follow the selected API's documentation.

Polling remains necessary for recovery. A scheduled job should compare unresolved local records with current API and chain state after webhook downtime.

## Key lifecycle, backup, and recovery

Ask what the provider means by not exposing private keys. It may mean keys are generated and used inside isolated infrastructure, that shares are distributed across parties, that users hold recovery material, or simply that a custodian does not permit export. These architectures create different dependencies.

Coinbase documents its v2 Server Wallet as performing key generation, encryption, decryption, and signing inside a trusted execution environment, with requests authenticated by a developer Wallet Secret. That is a concrete provider architecture. It does not remove risk from the Wallet Secret, application authorization, policy configuration, provider availability, software updates, or recovery procedures.

A production design needs documented answers for:

- API credential and signing-secret rotation;
- employee offboarding and emergency revocation;
- user device loss or authentication recovery;
- provider outage and regional failure;
- backup format, encryption, testing, and restore authority;
- key or share export, migration, and account portability;
- smart-account owner or recovery-module replacement; and
- asset access if the vendor, customer, or application closes.

Never test recovery only on paper. Use test networks and non-production identities to run credential loss, signer loss, webhook outage, policy rollback, and provider-migration exercises.

## A production evaluation checklist

Before selecting a cryptocurrency wallet API, require an architecture diagram and threat model, then verify:

- who controls keys, policies, signatures, broadcasting, recovery, and custody;
- supported account types, networks, contracts, and transaction operations;
- exact signing payloads and a way to inspect or simulate them;
- enforceable policies, role separation, and approval evidence;
- balances and events with clear chain or ledger provenance;
- authenticated webhooks plus query endpoints for backfill;
- sandbox behavior for failures, replacement, and recovery;
- stable idempotency, pagination, error, rate-limit, and version contracts;
- audit exports and retention suitable for incident investigation; and
- an exit path that does not depend on continued access to one dashboard.

A wallet API is not defined by how quickly it returns an address. Its real boundary is the path from application intent to an authorized signature and recoverable transaction record. Make that boundary explicit before treating convenience features as security or custody guarantees.

## Sources and references

- [Create and Manage Wallets](https://docs.cdp.coinbase.com/server-wallets/v2/using-the-wallet-api/managing-accounts) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Security](https://docs.cdp.coinbase.com/wallet-api-v2/docs/security) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Sign Transactions and Messages](https://docs.cdp.coinbase.com/server-wallets/v2/evm-features/eip-712-signing) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Sign Transactions on EVM Chains](https://developers.circle.com/wallets/sign-tx-evm) — Circle; retrieved 2026-10-19.
- [Get a Notification Signature Public Key](https://developers.circle.com/api-reference/gateway/all/get-notification-signature) — Circle; retrieved 2026-10-19.
