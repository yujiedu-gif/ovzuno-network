---
title: "How to Accept Crypto Payments: An Operating Checklist"
description: "Plan a crypto payment flow covering assets and networks, invoices, confirmations, custody, conversion, refunds, reconciliation, security, and local compliance."
date: "2026-10-18"
draft: false
content_type: "guide"
topics: ["crypto-payments"]
tags: ["accept cryptocurrency payments", "accept crypto payments on website", "merchant crypto payments", "crypto payment checkout", "crypto payment processing"]
author: "editorial_team"
primary_keyword: "how to accept crypto payments"
owned_question: "What operating decisions must a merchant make before accepting crypto payments?"
risk_level: "high"
---

To learn **how to accept crypto payments**, start with an operating model rather than a checkout button. A merchant must decide what assets and networks it will accept, how a price becomes an invoice, when a payment is final enough to fulfill, who controls the keys, how funds are converted or retained, and how refunds, accounting, security, and local compliance work.

This is a global technical guide, not legal, tax, accounting, or investment advice. Crypto payment rules vary by jurisdiction and by whether a merchant receives funds for itself, converts for others, holds customer assets, or provides transfer services. Confirm the resulting model with qualified local advisers before launch.

## Start with the settlement outcome

Define what the business wants after the customer pays:

- retain the same crypto asset;
- receive a stablecoin;
- convert to another asset;
- settle into a bank account; or
- split funds among treasury, suppliers, and fees.

That decision determines most of the architecture. Direct wallet acceptance gives the merchant control but leaves it responsible for node access, invoice monitoring, keys, liquidity, conversion, refunds, and records. A processor can manage some of those functions, but adds counterparty, account, fee, data, geographic, and withdrawal dependencies. Self-hosted software can reduce custody by the checkout system while still requiring the merchant to secure its wallet and infrastructure.

Document who is merchant of record, who quotes the rate, who receives the asset, who can sign, who converts it, and who bears volatility or depeg risk. A processor that immediately converts funds is operationally different from a tool that only detects transfers to the merchant's own wallet.

## Choose assets and networks explicitly

A token name is not a complete payment specification. Define each accepted combination by network, native asset or token contract, decimals, destination type, and supported wallet flow. USDC on one chain is not interchangeable at the deposit address with every bridged token that also uses the symbol USDC. Circle's own documentation, for example, warns that unsupported or bridged variants sent to a Circle Mint address may not be credited.

For each asset-network pair, assess:

- customer wallet availability and payment-request format;
- network fees and whether the customer needs a separate gas asset;
- expected confirmation or finality behavior;
- token contract and upgrade or freeze controls;
- liquidity for conversion into the merchant's settlement asset;
- minimum economic payment size;
- provider deposit and withdrawal support; and
- how a wrong-chain or wrong-token payment will be handled.

Use allowlisted chain and contract identifiers in the backend. Do not infer the asset from a ticker entered by a user. Checkout should show the network prominently and, when appropriate, verify it through the connected wallet.

## Create an invoice, not a static address

A static address and a fiat price leave important questions unanswered. An invoice should bind an internal order ID to the requested currency, crypto amount, exchange-rate source, quote time, expiry, allowed payment methods, destination, and current payment state.

BTCPay Server illustrates this model: an invoice fixes the requested amount and exchange rate for a limited period, then tracks states such as new, processing, settled, expired, invalid, underpaid, overpaid, and paid late. Other systems use different names, but a production flow needs equivalent states.

Generate a fresh destination or uniquely attributable payment reference where the network and wallet architecture permit it. Address reuse makes reconciliation and privacy harder. Store the exact quoted amount and rate rather than recomputing history from a later market price. The invoice expiry should match the volatility of the asset, expected wallet interaction time, and the merchant's willingness to accept late payments.

Define policies before code handles exceptions:

- Underpayment: request the difference, accept within a tolerance, or refund?
- Overpayment: automatically refund, credit the customer, or queue a review?
- Late payment: accept at the old quote, recalculate, or refund?
- Duplicate payment: attach to the same order or create a review case?
- Wrong asset or network: is recovery technically possible, and who pays the cost?

Do not silently mark these cases successful. They affect inventory, customer support, and accounting.

## Define detection and settlement

Separate at least four states: invoice created, transaction observed, transaction confirmed or finalized to policy, and order fulfilled. A transaction hash proves neither successful execution nor irreversible settlement. The chain may reject execution, reorganize a block, replace a pending transaction, or deliver a token the merchant does not support.

BTCPay's guidance explicitly distinguishes a processing invoice from a settled one and warns against fulfillment merely because a transaction was broadcast. The appropriate confirmation policy depends on the network, transaction value, product, fraud exposure, and whether delivery can be reversed. Review the underlying mechanics in [how a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/).

Use signed webhooks or authenticated event delivery to update the commerce backend. Validate the signature, enforce timestamp or replay controls if supported, and make the handler idempotent. A repeated settled event must not ship twice. Also run reconciliation independently of webhooks so a temporary outage does not lose a payment. Compare invoice records with chain or provider records and the general ledger.

Store chain ID, transaction hash, block hash or finality reference, asset contract, amount in base units, observed time, settlement time, payer data collected under policy, order ID, and any conversion or payout reference. Retain only data that the business has a lawful reason to keep.

## Separate checkout from custody

The payment page does not need unrestricted signing power. A safer design separates address derivation and payment observation from the signer that moves treasury funds. A watch-only wallet or narrowly scoped address service can receive and monitor payments while signing keys remain in hardware, a multisignature policy, a custody service, or an isolated signing system.

Define:

- who can generate receiving destinations;
- where private keys are created and backed up;
- the maximum balance kept in an online hot wallet;
- approval thresholds for sweeps and refunds;
- withdrawal allowlists and rate limits;
- administrator roles and audit logs;
- recovery if the checkout, node, provider, or signer fails; and
- incident procedures for key exposure or unsupported deposits.

Compare an exchange account and a self-controlled wallet by custody and withdrawal behavior, as explained in [cryptocurrency exchange vs wallet](/articles/crypto-exchange-vs-wallet/). Never place seed phrases in application configuration, support tickets, analytics, or a browser checkout.

## Plan conversion, payouts, and refunds

If prices are denominated in fiat but payment arrives in crypto, decide when exchange-rate risk transfers. The relevant times may be quote creation, transaction observation, required confirmation, conversion, or bank settlement. Record the chosen rule in customer terms and accounting logic.

Conversion requires executable market liquidity, not just a nominal price. Model spreads, price impact, trading and withdrawal fees, banking cutoffs, stablecoin redemption, and weekends. [Crypto liquidity](/articles/what-does-liquidity-mean-in-crypto/) can differ across a trading pair, venue, chain, and transaction size. Define fallback behavior if conversion or payout is unavailable.

Refunds need a separate workflow. Do not automatically send to the input address: it may belong to an exchange, payment router, smart contract, or wallet with a different return requirement. BTCPay's pull-payment model instead lets the recipient provide a payout destination and gives the merchant a chance to review the amount, rate, network fee, and destination before signing.

Choose whether refunds use the original fiat value, original crypto amount, or current rate, and disclose that policy. Protect refund claims from account takeover, duplicate claims, and support impersonation. A refund is a new payment with its own destination validation, approval, broadcast, confirmation, and accounting record.

## Address compliance and accounting before launch

Map the legal entities, customer locations, operating jurisdictions, assets, custody model, conversion providers, and transaction flows. Determine locally whether the activity is ordinary merchant acceptance or triggers payment, money-transmission, virtual-asset-service, consumer-protection, AML, sanctions, tax, or licensing duties. Do not assume that using a processor transfers every obligation.

For U.S. persons and businesses subject to U.S. jurisdiction, OFAC states that virtual-currency transactions are subject to sanctions obligations and recommends a tailored, risk-based compliance program. That is a U.S.-specific rule, not a global template. Other jurisdictions use different definitions, thresholds, screening, reporting, privacy, and recordkeeping requirements.

Before launch, decide what customer and transaction information is needed for fraud, sanctions, AML, tax, support, and audit purposes; who can access it; how long it is retained; and how data-subject or law-enforcement requests are handled. Obtain jurisdiction-specific advice for classification and controls.

Accounting must reconcile the sales invoice, asset and network, crypto amount, fiat value under the chosen policy, fees, exchange or processor balances, conversion trades, wallet transfers, refunds, and final bank or treasury receipt. Preserve source records rather than relying on a block explorer screenshot.

## Test the complete operating loop

Build and test in stages:

1. Write the supported asset-network matrix and settlement policy.
2. Model normal, partial, excess, late, duplicate, wrong-asset, failed, and reorganized payments.
3. Configure custody, roles, signing, backups, monitoring, and withdrawal controls.
4. Integrate invoices and signed webhooks with idempotent order updates.
5. Reconcile a test payment from invoice through chain record and ledger entry.
6. Run a small live payment using a separate customer wallet.
7. Execute a refund to a newly supplied destination with approval and confirmation.
8. Test provider, node, webhook, conversion, and banking outages.
9. Restore wallets and application data in a controlled recovery exercise.
10. Review the flow with finance, security, support, privacy, tax, and qualified legal personnel.

Only then expand assets, networks, limits, or automated refunds. The technical act of displaying a QR code is the smallest part of accepting crypto payments. A reliable merchant system connects a precise invoice to verified settlement, controlled custody, available liquidity, reversible support procedures, complete records, and the obligations of every jurisdiction in which it operates.

## Sources and references

- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-18.
- [eCommerce Integration Guide](https://docs.btcpayserver.org/Development/ecommerce-integration-guide/) — BTCPay Server; retrieved 2026-10-18.
- [Pull Payments](https://docs.btcpayserver.org/Users/pull-payments/) — BTCPay Server; retrieved 2026-10-18.
- [Supported Chains and Currencies](https://developers.circle.com/circle-mint/supported-chains-and-currencies) — Circle Developers; retrieved 2026-10-18.
- [Sanctions Compliance Guidance for the Virtual Currency Industry](https://ofac.treasury.gov/media/913571/download?inline=) — U.S. Department of the Treasury, Office of Foreign Assets Control; retrieved 2026-10-18.
