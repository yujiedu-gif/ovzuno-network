---
title: "What Is a Crypto ATM? Cash, Wallets, Fees, and Settlement"
description: "Learn how a crypto ATM connects cash, wallet addresses, operator liquidity, exchanges, identity checks, fees, and blockchain settlement."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["crypto-cards-and-spending-rails"]
tags: ["cryptocurrency ATM", "bitcoin ATM", "crypto ATM machine", "how does a crypto ATM work", "buy crypto with cash"]
author: "editorial_team"
primary_keyword: "crypto atm"
owned_question: "How does a crypto ATM connect cash transactions to wallets and exchanges?"
risk_level: "medium"
---

A **crypto ATM** is better understood as a cash-to-crypto exchange kiosk than as a bank cash machine. It can accept physical currency and arrange delivery of cryptocurrency to a wallet address. Some two-way machines also accept a crypto transfer and dispense cash. The terminal is only the visible part of a larger system involving identity checks, pricing, operator wallets, liquidity, an exchange or trading source, blockchain access, and transaction records.

The name can be misleading. A conventional ATM usually lets a customer access money already held in a bank account. A crypto ATM normally creates an exchange transaction between fiat currency and a digital asset. The operator, not the customer's bank, supplies or sources the crypto and decides which assets, networks, limits, fees, and settlement rules the machine supports.

## A crypto ATM is an exchange kiosk

FinCEN describes convertible virtual currency kiosks as ATM-like terminals that exchange fiat currency and virtual currency. A purchase machine takes cash and sends crypto toward a wallet destination. A two-way machine can also support the reverse direction, but that capability should never be assumed from the appearance of the terminal.

The destination may be a wallet controlled directly by the customer, an account or wallet provided by the operator, or another supported arrangement disclosed during the transaction. This difference matters. Sending to a self-controlled wallet gives the user responsibility for the receiving address and keys. Sending to a custodial account means the provider records the balance and controls withdrawal access. Review [the difference between an exchange and a wallet](/articles/crypto-exchange-vs-wallet/) before choosing a destination.

A machine may be called a Bitcoin ATM even when it supports other assets. Always verify the exact asset and network on the transaction screen. A ticker alone does not prove that the destination wallet supports the same network or token representation.

## How a cash purchase works

A typical purchase has several stages, although the exact screens and checks vary by operator and country:

1. **Choose the asset and purchase amount.** The machine checks whether the amount falls within its supported range.
2. **Complete required verification.** Depending on the transaction and local rules, this can involve a phone number, one-time code, identity document, personal information, or additional review.
3. **Provide the destination.** The customer normally scans a wallet QR code or selects an operator-provided destination flow. The address must match the chosen asset and network.
4. **Review the quote.** The screen should show how much cash will be inserted, the quoted crypto amount, applicable charges, and any warnings or expiry conditions.
5. **Insert cash and confirm.** The terminal counts the notes and presents a final transaction summary.
6. **The operator sends or allocates the crypto.** Its backend sources the asset from operator inventory or an exchange relationship and initiates delivery to the stated destination.
7. **Keep the receipt and transaction reference.** These records help distinguish the kiosk order from the later blockchain transaction and are important if support is needed.

CoinFlip Australia's published flow is one concrete example: it asks a customer to select an asset and amount, accept disclosures, complete phone and identity checks, scan a wallet QR code, insert cash, confirm, and receive the crypto. It is not a universal standard. Other operators use different verification thresholds, delivery models, timing, fees, and supported assets.

Before inserting cash, read the destination address shown by the wallet rather than scanning a QR code supplied by an unknown caller or message. A QR code is merely an encoded destination; it does not prove who controls the wallet.

## How a cash-out transaction works

At a two-way machine, the order usually begins with a sell quote. The kiosk or associated app gives the customer an address or payment request. The customer sends the exact supported asset on the stated network. The operator then observes the transaction and applies its confirmation or settlement policy before releasing cash or a redemption code.

This direction reverses both liquidity legs. The customer supplies crypto, while the operator must have enough physical cash at the terminal. A machine can therefore support purchases but temporarily lack cash-out availability, or impose different limits for each direction. The quote can also expire while the blockchain payment is pending.

Do not send until the asset, network, amount, expiry, destination, required confirmations, and refund or exception policy are clear. If the transfer arrives late, on the wrong network, or in the wrong token, automated cash redemption may fail even when a block explorer shows a transaction.

## What happens behind the screen

The terminal combines hardware with several backend services. A deployment may include a cash acceptor or dispenser, QR scanner, printer, camera or document reader, secure communications, customer-verification system, pricing engine, order database, operator wallet, blockchain node or API provider, exchange account, monitoring, and support tools.

FinCEN notes that a kiosk may connect to a separate crypto exchanger that performs the transmission, or draw on crypto held by the kiosk operator. The operator must manage both crypto and cash balances. This is an application of [crypto liquidity](/articles/what-does-liquidity-mean-in-crypto/): the machine needs enough available inventory in the correct asset and enough cash for supported redemptions, not merely a market price on a screen.

A simplified purchase path looks like this:

`cash accepted -> order and quote recorded -> compliance checks passed -> operator inventory or exchange sourced -> blockchain transaction broadcast -> destination observed -> receipt and support records retained`

The operator may batch, hedge, pre-fund, or source assets differently. The diagram is a functional model, not a promise that every terminal executes each step in real time.

## Fees are more than one line item

The amount received can differ from a public market quote for several reasons:

- an explicit operator charge;
- a spread between the operator's quoted exchange rate and a reference market price;
- a blockchain network or miner fee;
- minimum transaction economics; and
- a later wallet, exchange, or cash-out charge outside the original kiosk transaction.

The useful comparison is not just the printed fee percentage. Compare the cash inserted with the exact crypto amount expected at the destination, using a contemporaneous reference price. Also check whether a network fee is already included or will be deducted from the delivered amount.

California provides a jurisdiction-specific illustration of why both fees and spreads matter. Its kiosk rules require specified pre-transaction disclosures and receipts that identify charges and compare the customer price with a referenced licensed-exchange price. That is a California rule with stated effective dates, not a universal cap or disclosure format.

## Wallet custody and settlement still matter

The kiosk cannot correct a destination merely because it was entered through a physical machine. Before confirmation, check the first and last characters of the address, the network, the asset, and who controls the destination. Test a new wallet with a small supported transaction when practical. Never disclose a seed phrase or private key to the machine, an operator's support agent, or anyone claiming to help receive the funds.

A terminal receipt and a blockchain transaction serve different purposes. The receipt documents the order with the operator. A transaction hash identifies the onchain transfer. A broadcast transaction may still be pending, replaced, rejected, or awaiting the operator's required confirmations. Use a reputable [blockchain explorer](/articles/what-is-a-blockchain-explorer/) for the correct network and understand [how a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/).

If the destination is a custodial account, the blockchain may show that the provider received the asset before the provider credits the user's internal balance. Support will need both the kiosk receipt and the receiving platform's deposit details.

## Compliance depends on location and operator model

Identity checks are not simply a machine preference. They can support transaction limits, fraud controls, sanctions screening, anti-money-laundering duties, recordkeeping, and operator licensing. The applicable obligations depend on jurisdiction, transaction direction, operator structure, asset, amount, and customer relationship.

In the United States, FinCEN states that kiosk operators facilitating money transmission between an exchanger and a customer's wallet, or operating as exchangers themselves, are generally money services businesses under the Bank Secrecy Act. Applicable federal duties can include registration, records, reporting, and transaction monitoring. States may impose additional licensing, disclosure, fee, receipt, support, or transaction-limit rules.

That U.S. treatment should not be copied into another country's article as if it were universal. An operator or merchant must check current national, state or provincial, and local requirements before relying on a compliance design. A customer should use only a machine that clearly identifies its operator, terms, support route, quote, and receipt.

## Treat an unexpected crypto ATM instruction as a warning

FinCEN's 2025 notice describes scams in which a victim is directed under false pretenses to insert cash at a crypto kiosk and send the resulting crypto to a wallet controlled by the scammer. The machine can execute a technically valid transaction even though the reason for the payment is fraudulent.

Stop before paying when someone:

- creates urgency about an account, tax, arrest, utility cutoff, prize, refund, or computer problem;
- tells you to withdraw cash and stay on the phone while using the kiosk;
- sends a QR code and claims it is a protected, government, business, or recovery wallet;
- asks you to split transactions to avoid a limit or verification step; or
- promises that an irreversible crypto transfer can secure or restore your money.

Independently contact the real organization using a number or website you locate yourself. Do not use contact details supplied by the person demanding payment. If cash has already been inserted, retain the receipt, transaction hash, phone numbers, messages, and QR code, then contact the kiosk operator and the appropriate fraud-reporting or law-enforcement channel promptly. Recovery is not guaranteed.

A crypto ATM can provide a physical bridge between cash and a digital wallet, but the transaction is still a crypto exchange and transfer. The safe way to use one is to identify the operator, understand the quote, control or deliberately choose the destination, verify the network, preserve the records, and refuse any transaction initiated by an unverified third party.

## Sources and references

- [FinCEN Notice on the Use of Convertible Virtual Currency Kiosks for Scam Payments and Other Illicit Activity](https://www.fincen.gov/system/files/2025-08/FinCEN-Notice-CVCKIOSK.pdf) — Financial Crimes Enforcement Network; retrieved 2026-10-18.
- [Bitcoin ATM](https://coinflip.tech/en-AU/bitcoin-atm) — CoinFlip Australia; retrieved 2026-10-18.
- [Digital Financial Assets Law: Information for Kiosk Operators](https://dfpi.ca.gov/regulated-industries/digital-financial-assets/digital-financial-assets-law-information-for-kiosk-operators/) — California Department of Financial Protection and Innovation; retrieved 2026-10-18.
