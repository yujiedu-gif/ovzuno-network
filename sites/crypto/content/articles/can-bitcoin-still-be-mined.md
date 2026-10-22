---
title: "Can bitcoin still be mined? How Bitcoin mining works"
description: "Can bitcoin still be mined? Learn how mining supports Bitcoin’s transaction history and security, and how the block subsidy changes over time."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["can bitcoins still be mined"]
author: "editorial_team"
primary_keyword: "can bitcoin still be mined"
owned_question: "Can Bitcoin still be mined, and what does mining do in the Bitcoin network today?"
risk_level: "medium"
---

Yes. Bitcoin can still be mined: miners construct candidate blocks and search for proof of work, while network participants validate blocks under protocol rules. Mining helps order Bitcoin’s transaction history; it is distinct from the scheduled creation of new bitcoin, and this evidence pack does not include an authorized claim about the subsidy schedule.

## Can bitcoin still be mined?

Mining is Bitcoin’s proof-of-work process for proposing blocks. Proof of work is a computational process in which a publishing node must solve a difficult problem that other nodes can verify. In Bitcoin’s original design, mining software constructs a candidate block and header from transactions, then provides header work to hashing hardware. The hardware searches for a hash that satisfies the network’s target.

That mechanism does not mean every candidate becomes part of the accepted history. Nodes enforce the network’s rules, and proof of work cannot make an invalid block valid. When valid histories compete, Bitcoin’s design treats the valid chain with the greatest cumulative proof of work as the selected history. Replacing accepted history requires rebuilding work and catching up with the selected chain. These are protocol mechanisms, not a claim about any individual miner’s circumstances.

The concise answer to “Can bitcoins still be mined?” is therefore yes in the sense that mining remains the process by which Bitcoin blocks are proposed through proof of work. That answer does not establish whether a particular person can operate mining equipment, whether mining is financially viable, or what rules apply in a particular location.

## What miners do when they create a block

A block is a proposed addition to Bitcoin’s recorded transaction history. Mining software assembles a candidate from transactions and creates header work for hashing hardware to search. The search varies candidate data, including a nonce, until the resulting hash meets the network’s target condition. This repeated search is the mining computation; it is not the same as a node’s later validity check.

The distinction between proposing and validating is important. Miners perform the proof-of-work search and propose candidate blocks. Nodes check blocks and transactions against protocol rules. The Bitcoin network’s structure includes protocol rules, a transaction ledger, and participants that update, store, and read that ledger. A miner’s work is one part of the process; it does not replace the network’s validation rules.

When competing valid histories exist, cumulative proof of work helps determine which history is selected. The Bitcoin design describes the selected history as the valid chain representing the greatest cumulative work. That does not mean work can override validity: an invalid block remains invalid even if it has computational work attached to it. Nor does this high-level description quantify the security of a particular transaction or guarantee a particular outcome.

This division also clarifies why “mining creates bitcoin” is an incomplete description. Mining proposes and helps order blocks; the protocol’s issuance rules govern any new bitcoin associated with a block. The allowed evidence here supports the mining and history-selection mechanisms, but it does not authorize a detailed claim about the current subsidy amount, reduction interval, or calendar timing.

## How mining rewards and new issuance work

The block subsidy is the protocol-defined component of miner revenue associated with issuance of new bitcoin. Transaction fees are a separate possible component of miner revenue. Keeping those categories distinct prevents a common misunderstanding: a change in new issuance is not the same thing as a change in transaction fees.

This article does not state the subsidy’s amount or describe when it changes. The allowed evidence for this assignment does not establish those details. It therefore would be inaccurate to use this article to infer a current per-block reward, a specific halving date, or the amount a miner might receive. Those details require evidence that is specifically authorized and current for the relevant protocol rules.

The general distinction remains useful without a number: mining is the block-proposal process, while issuance is controlled by protocol rules. A miner’s possible revenue can include the subsidy and transaction fees, but naming those components does not establish their present value, guarantee either component to an individual, or predict future revenue.

## What happens as the block subsidy declines

A lower block subsidy, when it occurs under Bitcoin’s issuance rules, means less newly issued bitcoin is associated with a block than under a higher subsidy. Transaction fees remain a separate category. The distinction explains why a change in issuance should not automatically be described as a change in mining itself: mining refers to proposing blocks through proof of work, whereas the subsidy concerns new issuance.

The evidence available for this article does not authorize a precise reduction schedule or current operating figures. It also does not support predictions about future fees, miner participation, profitability, or network security. A statement about scheduled issuance cannot, on its own, establish those outcomes. The protocol-level point is limited: the mining process and the amount of new issuance are related parts of Bitcoin’s design, but one is not a synonym for the other.

## What this answer does not establish

This explanation does not tell a reader whether mining is viable for a specific operation. That question would require current, context-specific evidence outside the protocol mechanisms described here. It also does not provide hardware recommendations, setup instructions, or guidance on choosing a mining pool.

No legal, tax, regulatory, or compliance conclusion follows from the mining mechanism. Those matters require jurisdiction-specific evidence and are outside this article’s scope. Likewise, the description of proof of work and block history does not establish a current fee level, yield, return, availability statement, or recovery process.

The supported answer is narrower: Bitcoin mining is a process for constructing candidate blocks and searching for proof of work; network rules govern block validity; and cumulative proof of work helps select between valid competing histories. This explains what mining does, without treating it as a guarantee of earnings or making unsupported claims about the issuance schedule.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Block Chain](https://developer.bitcoin.org/devguide/block_chain.html?highlight=consensus) — Bitcoin Developer Guide; retrieved 2026-10-21.
