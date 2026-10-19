---
title: "How to Pay With Cryptocurrency: A Safe Step-by-Step Guide"
description: "Learn how to verify a crypto payment request, match the asset and network, review fees and addresses, authorize the transfer, and confirm settlement."
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["crypto-payments"]
tags: ["pay with crypto", "send a cryptocurrency payment", "crypto payment invoice", "pay a merchant with cryptocurrency", "verify a crypto payment"]
author: "editorial_team"
primary_keyword: "how to pay with cryptocurrency"
owned_question: "How does a user prepare, authorize, send, and verify a cryptocurrency payment safely?"
risk_level: "high"
---

To learn **how to pay with cryptocurrency**, treat the transaction as an irreversible payment instruction, not as a casual message between wallet apps. First verify the person or merchant requesting payment. Then match the exact asset and network, prepare the sending wallet and fee asset, inspect every transaction field, sign once, and verify both the blockchain result and the merchant's invoice state.

This guide covers a legitimate payment from a wallet you are authorized to use. It does not recommend an asset, wallet, exchange, or processor, and it does not provide a way to bypass identity, sanctions, tax, banking, or merchant controls. Wallet screens and finality rules vary by network.

## Confirm that the payment request is legitimate

Do not start with the QR code. Start with the commercial reason for the payment and the identity of the recipient. Open the invoice from the merchant's known website, authenticated account, or a previously verified business channel. If the request arrived through an unexpected call, direct message, pop-up, new email thread, or changed bank-style instructions, contact the organization through a channel you locate independently.

Stop when someone claims that crypto must be sent to protect funds, unlock an account, pay a government or utility demand, collect a prize, produce a certain return, or recover a previous transfer. Urgency and instructions to keep the transaction secret are reasons to verify, not reasons to hurry.

A QR code reduces typing, but it does not authenticate its creator. It can encode a scammer's address as easily as a merchant's. Check that the page or device showing the code belongs to the intended recipient. For a large or unfamiliar payment, confirm the destination through a second trusted channel and consider a small test transfer if the invoice process supports it.

## Read the payment specification

A usable crypto invoice or payment request should identify more than an amount. Record:

- the merchant or recipient;
- order or invoice ID;
- fiat amount, if the purchase is priced in fiat;
- exact crypto asset;
- blockchain network;
- token contract or other asset identifier when relevant;
- amount to send in the asset's native units;
- destination address;
- memo, tag, reference, or payment URI if required;
- quote expiry;
- who pays the network fee; and
- the merchant's confirmation and exception policy.

Asset symbols are not enough. A stablecoin may exist as different native or bridged representations on multiple networks. A provider can support one representation and reject another with the same displayed ticker. Circle's own supported-chain documentation is one concrete example of this chain-specific custody boundary.

Do not reuse an old destination merely because it previously belonged to the merchant. A modern invoice can generate a fresh address and a time-limited quote. BTCPay Server, for example, fixes an amount and exchange rate for a limited period and tracks payment and settlement states. Other checkout systems make different choices, but expiry and destination must come from the current request.

## Prepare the sending wallet

Use a wallet or withdrawal account that supports the exact asset and network on the invoice. [An exchange account and a self-controlled wallet](/articles/crypto-exchange-vs-wallet/) create different workflows: an exchange may queue a withdrawal, select from a limited network list, charge a withdrawal fee, and assign its own status; a self-controlled wallet signs and broadcasts directly through its configured network provider.

Check the available balance after reserving all fees. On Ethereum-family networks, a token transfer normally requires enough of the network's native asset to pay gas. A wallet holding USDC but no ETH on Ethereum may be unable to send until gas is available, unless the specific wallet and application support a documented sponsored-fee mechanism. Other chains use other native fee assets or fee models.

Before paying:

1. Update and open the genuine wallet application from its normal source.
2. Confirm the selected account and network.
3. Confirm the asset contract when the wallet shows multiple lookalike tokens.
4. Check the spendable amount, not only the displayed portfolio value.
5. Check the estimated network or withdrawal fee.
6. Leave enough fee asset for the transaction and any necessary follow-up.
7. Never paste a seed phrase or private key into a payment page or support chat.

If the payer must first buy or bridge an asset, that is a separate transaction with separate fees and risks. Do not improvise a bridge or substitute another token because an invoice is near expiry. Request a new invoice or another supported payment method.

## Inspect the transaction before signing

Enter or scan the current destination, then compare it with the authenticated invoice. Check more than the first and last character when possible. Clipboard malware, browser overlays, compromised websites, and human error can replace an address after copying.

Review the wallet's final authorization screen:

- sending account;
- destination address or contract;
- network;
- asset and token contract;
- amount;
- network fee and maximum fee;
- memo or destination tag; and
- any decoded contract method, approval, or warning.

A simple transfer and a contract interaction are not equivalent. An Ethereum transaction can contain a destination, value, optional input data, nonce, and fee limits. If the checkout asks for a token approval, the authorization may let a contract spend tokens later rather than sending the purchase amount immediately. Check the spender, token, allowance, and whether a second settlement transaction is expected. Do not approve an unlimited amount merely because it is the default.

A message signature may authenticate wallet control without moving funds, while a transaction signature authorizes a state change or transfer. Wallets do not always explain this distinction clearly. Reject any request whose effect you cannot identify.

## Authorize and broadcast once

When every field matches, unlock the wallet through its normal method and confirm once. The private key signs the instruction locally or within the wallet's signing system. The signed transaction is then broadcast to the network.

On Ethereum, broadcast produces a transaction hash, the transaction enters a pending pool, a validator may include it in a block, and the included block later reaches stronger consensus states. Other chains use different terms, but the general distinction remains: created, broadcast, included, and final enough for the recipient's policy are not the same moment.

Save the transaction hash immediately. If the wallet appears to wait, do not create a second payment without checking the first hash, account history, nonce, and invoice. A slow transaction can still settle later. Sending again may create a duplicate payment rather than accelerate the first one. Use only the wallet's documented replacement or fee-bump mechanism when you understand how it affects the existing transaction.

Once an ordinary Ethereum transaction is confirmed, the sender cannot simply cancel or pull it back through the wallet. A refund is a new transaction voluntarily sent by the recipient under its own policy.

## Verify both chain status and invoice status

A block explorer and a merchant checkout answer different questions. The explorer can show whether the network saw the transaction, which address and asset moved, whether contract execution succeeded, and how many confirmations or finality milestones followed. Use [a blockchain explorer](/articles/what-is-a-blockchain-explorer/) for the correct network and compare the transaction hash, destination, asset, amount, and status.

The merchant invoice decides whether that onchain result satisfies the order. A processor may treat a fully detected payment as `Processing` while it waits for settlement conditions, then mark it `Settled` when those conditions are met. It may separately classify an underpayment, overpayment, late payment, or invalid transaction. Learn the underlying lifecycle in [how a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/).

Do not rely on a screenshot supplied by either party. Open the explorer independently, and keep the invoice page or order account open until it shows the expected result. A successful transfer to the correct address may still need an invoice reference or memo to be credited automatically.

## Handle exceptions without sending again blindly

If the order does not update, collect evidence before acting:

- **Pending transaction:** check the network, hash, fee conditions, and wallet guidance. Do not pay again merely because the merchant page is slow.
- **Failed transaction:** confirm that the explorer reports failure and whether only the network fee was consumed. A failed contract execution usually does not transfer the intended token amount, but the exact result must be read from the chain.
- **Expired quote:** contact the merchant or create a fresh invoice. Do not assume the old amount will still satisfy the order.
- **Partial or excess payment:** use the merchant's documented exception route. Do not send a difference to a new address supplied by an unverified support contact.
- **Missing memo or tag:** contact the receiving service through its official support path with the hash and invoice ID.
- **Wrong asset or network:** stop. Recovery may be impossible or require the destination provider's technical and custody cooperation. Do not send more funds as a supposed recovery test.
- **Wrong address:** blockchain validators cannot determine that the destination was a mistake. Contact the known recipient and relevant provider, but do not assume reversal is available.

Anyone claiming certain recovery in exchange for an advance crypto payment or seed phrase creates a second risk. Legitimate support may request public transaction information such as a hash and invoice ID; it does not need the private key that controls the wallet.

## Keep a payment record

For support, accounting, or a commercial dispute, preserve:

- invoice or order ID and authenticated merchant URL;
- quote currency, crypto asset, network, and amount;
- destination and any memo or tag;
- quote creation and expiry times;
- transaction hash and sending account;
- network fee;
- explorer status and settlement time;
- merchant receipt or final invoice state; and
- relevant support case numbers.

Do not store seed phrases, private keys, or wallet passwords with the receipt. Those secrets authorize future activity and are not payment evidence.

The safe sequence is simple even when the infrastructure is not: verify the request, specify the asset and network, prepare the correct wallet and fee balance, inspect every authorization field, sign once, track the transaction hash, wait for both network and invoice settlement, and keep the records. If any step is ambiguous, pause and obtain a fresh request through a verified channel rather than guessing with irreversible funds.

## Sources and references

- [How to Use Ethereum Wallets](https://ethereum.org/guides/how-to-use-a-wallet) — ethereum.org; retrieved 2026-10-19.
- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-19.
- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-19.
- [Supported Chains and Currencies](https://developers.circle.com/circle-mint/supported-chains-and-currencies) — Circle Developers; retrieved 2026-10-18.
