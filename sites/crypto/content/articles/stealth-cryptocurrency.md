---
title: "Stealth cryptocurrency: meaning and privacy limits"
description: "Learn what stealth cryptocurrency means, how stealth-address techniques can obscure recipient addresses, and why the term does not guarantee complete anonymity."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["crypto_payments"]
tags: []
author: "editorial_team"
primary_keyword: "stealth cryptocurrency"
owned_question: "What does stealth cryptocurrency mean, and how can stealth-address techniques affect the visibility of payment recipients?"
risk_level: "medium"
---

Stealth cryptocurrency is an informal term for cryptocurrency systems or features intended to make a payment’s recipient less directly identifiable on a public ledger. A stealth address can create a one-time destination for an incoming payment, reducing the direct on-chain link to a recipient’s published address. That feature does not, by itself, establish that the payment, its amount, or the user is anonymous.

## What does stealth cryptocurrency mean?

“Stealth cryptocurrency” is not a single standardized technical category in the evidence available here. It is best understood as shorthand for privacy-oriented designs or features, including techniques that obscure the direct connection between a recipient’s usual address and a particular payment. The details depend on the protocol and transaction type.

A **stealth address** is a technique for creating a distinct destination for a payment. In Monero’s documented model, the sender can create a one-time destination address so an incoming payment is not directly linked on-chain to the recipient’s published address. This describes a particular protocol mechanism, not a rule that applies to every cryptocurrency using privacy-related language.

The distinction matters: a feature that obscures one relationship in ledger data is not proof that every detail of the transaction or the people involved is hidden. Nor does the label alone establish the protections or assumptions of a particular implementation.

## How stealth addresses can work

At a high level, the recipient provides information that lets a sender create a payment destination distinct from the recipient’s published address. The resulting one-time address is intended to reduce the direct public link between that published address and the incoming payment. In Monero’s documented design, stealth addresses serve this recipient-unlinkability function.

The mechanism is protocol-specific. A general description should not be mistaken for a complete account of how a particular wallet generates, recognizes, or handles those destinations. To understand an implementation, consult its protocol documentation and verify what the transaction records expose and what information a recipient or other party can access.

Stealth addresses also differ from other privacy techniques. For example, Monero’s ring-signature model mixes the actual spent output with decoy outputs, so an outside observer cannot directly identify which ring member authorized the spend. That is a sender-obfuscation mechanism, rather than the recipient-address mechanism described above. The presence of one technique does not establish the protections supplied by another, and neither mechanism alone supports a blanket claim of anonymity.

## What this does—and does not—hide

A stealth address addresses a specific question: whether an incoming payment is directly linked on-chain to a recipient’s published address. It does not, by itself, establish that the amount, timing, wallet activity, network information, or a person’s identity is concealed. Those details require separate, system-specific evidence.

Even for the documented Monero mechanism, privacy depends on factors beyond the address technique, including wallet behavior and information available outside the protocol. The documentation also identifies address handling and external information as relevant considerations. Therefore, describing a payment as “stealth” should not be treated as evidence that an observer cannot connect it to a person or activity.

This is a scope distinction, not a claim that a particular transaction is readily traceable. Whether a given detail is visible or can be associated with an identity depends on the specific system and circumstances; the available evidence here does not establish a universal answer for transaction amounts, timing, or network-level information.

## Questions to verify before relying on the term

For a specific cryptocurrency or wallet, begin with the relevant protocol documentation. Check what the protocol says is public, what its privacy mechanism is designed to obscure, and whether disclosure or visibility depends on address handling, wallet behavior, or other conditions. Do not transfer a description of Monero’s stealth-address model to a different system without evidence that its design works the same way.

Next, identify the exact privacy claim being made. “A payment is not directly linked on-chain to a published recipient address” is narrower than “the payment is anonymous.” Ask which data and relationships are covered by the claim, and which are outside its stated scope. A mechanism addressing recipient linkage does not, without further evidence, establish protections for sender identity, transaction amounts, timing, or activity patterns.

Finally, look for independent security evidence that evaluates the specific implementation and states its assumptions and limits. A privacy label is not a security assessment. The evidence summarized here supports a bounded description of Monero’s recipient-address mechanism and a separate description of its ring-signature mechanism; it does not establish complete anonymity or a general privacy guarantee for every cryptocurrency. For operational or jurisdiction-specific questions, seek current, authoritative information rather than inferring an answer from the term “stealth.”

## Sources and references

- [Stealth Address](https://web.getmonero.org/resources/moneropedia/stealthaddress.html) — Monero Project documentation; retrieved 2026-10-18.
- [Ring Signature](https://web.getmonero.org/resources/moneropedia/ringsignatures.html) — Monero Project documentation; retrieved 2026-10-18.
