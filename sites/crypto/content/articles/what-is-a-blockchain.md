---
title: "What Is a Blockchain? How the Shared Ledger Works"
description: "Learn what a blockchain is, how transactions become blocks, why nodes use consensus, and where the technology's practical limits begin."
date: "2026-10-18"
draft: false
content_type: "definition"
topics: ["blockchain-foundations"]
tags: ["how blockchain works", "blockchain blocks", "blockchain consensus", "blockchain nodes"]
author: "editorial_team"
primary_keyword: "blockchain"
owned_question: "What is a blockchain, and how does it record and validate transactions?"
risk_level: "low"
---

A blockchain is a shared digital record maintained by a network rather than a single database administrator. Participants submit transactions, the network checks them according to its rules, and accepted records are grouped into blocks. Each new block refers cryptographically to the block before it, producing an ordered history that is difficult to alter without detection.

That short definition is useful, but it leaves out an important point: a blockchain is not one universal product. Different networks use different rules for membership, validation, consensus, privacy, and performance. The common idea is a replicated ledger whose participants agree on the order and validity of records.

## The basic idea

NIST describes blockchains as tamper-evident and tamper-resistant digital ledgers implemented in a distributed fashion. Those words are more precise than saying that blockchain data is simply immutable. Tamper-evident means an attempted change can be detected. Tamper-resistant means the design makes unauthorized changes difficult. Neither phrase means every blockchain is invulnerable or that every record placed on a chain must be correct.

The ledger is shared across participating computers. Instead of asking one central database to declare the official record, the network follows a protocol for deciding which proposed updates are valid and in what order they should appear. Once a transaction has been accepted and published under normal network operation, an individual participant cannot casually rewrite it.

This arrangement changes where trust is placed. Users do not eliminate trust altogether. They rely on the protocol, cryptography, software implementation, validators or miners, and their own key-management practices.

## How a transaction reaches the ledger

The exact process differs by network, but a typical transaction passes through six stages.

1. **A participant creates a transaction request.** The request may transfer a digital asset, call a smart contract, or propose another permitted state change.
2. **The request is signed.** A digital signature lets the network check that the request was authorized by the holder of the relevant private key. A valid signature does not prove that the person made a wise decision; it proves that the request satisfies the protocol's authorization rule.
3. **Network nodes receive and inspect the request.** They check items such as format, signature validity, available balance or state, and protocol-specific rules. Invalid requests are rejected.
4. **Accepted transactions are assembled into a proposed block.** A block is a batch of records plus metadata needed by the protocol.
5. **The network applies its consensus mechanism.** Consensus is the procedure nodes use to agree on a valid next block and the continuing canonical history. Proof of work and proof of stake are two well-known families, but their operational details are different.
6. **The accepted block is appended and replicated.** Nodes update their view of the ledger. Because the block references its parent, changing an older record would also disturb the later chain of references and conflict with the network's agreed history.

A transaction may be visible before the network treats it as sufficiently final. Applications therefore need a confirmation policy suited to the chain and the risk of the transaction. A wallet interface saying sent is not necessarily the same as an application treating settlement as complete.

## The main components

Although implementations vary, most blockchain explanations use the same core vocabulary.

**Transactions** are proposed changes to the ledger or network state. They are the individual actions users and applications submit.

**Blocks** group accepted transactions or state changes. Blocks also contain information that connects them to the existing history.

**Cryptographic references** link a block to its parent. A hash acts like a compact fingerprint of data: changing the underlying data changes the fingerprint. The chain of references helps make later tampering evident.

**Nodes** are computers running the network software. Depending on the protocol and node type, they may receive transactions, verify blocks, retain ledger data, serve applications, or participate in consensus.

**Consensus** is the set of rules and processes used to select or confirm the next valid state. It is not a general agreement about whether a transaction is fair or lawful; it is agreement under the protocol's technical rules.

**State** is the network's current recorded condition, such as balances, ownership records, or variables maintained by applications. On a programmable blockchain, a transaction can request a state change by invoking a smart contract.

**Smart contracts** are reusable programs deployed to blockchain state. They can enforce application logic when called, but they do not automatically guarantee that the logic is correct, secure, or suitable for a particular business process.

## What a blockchain does and does not guarantee

A blockchain can provide a common, inspectable history to participants who do not want one organization to maintain the only copy. It can make unauthorized historical edits difficult and visible. Public networks can also allow independent parties to verify records using their own node or an explorer.

Those properties have boundaries.

- **Bad inputs can still be recorded.** A ledger preserves what the system accepted; it does not prove that an off-chain statement was true.
- **Private keys remain a control point.** If a key is stolen or misused, the resulting transaction may still satisfy the protocol's signature rules.
- **Software can contain defects.** Node clients, wallets, bridges, smart contracts, and application interfaces all add implementation risk.
- **Consensus has assumptions.** Every mechanism depends on economic, computational, or governance conditions. The word decentralized does not by itself describe how concentrated those dependencies are.
- **Transparency is not the same as privacy.** A public ledger may expose transaction relationships even when addresses do not display legal names.
- **Performance is a design choice.** Replication and consensus create different trade-offs from a centrally administered database. Not every workload benefits from putting records on a blockchain.

For these reasons, a sound system design starts with the business requirement. If one trusted organization already controls all writers and readers, a conventional database may be simpler. A blockchain becomes more relevant when multiple parties need a shared history, independent verification, and a protocol-defined way to agree on updates.

## Why this matters for crypto infrastructure

Crypto products sit on top of this ledger process. A wallet creates and signs requests. Nodes relay and verify them. Validators or miners participate in ordering and consensus. Explorers expose ledger data in a human-readable form. Payment gateways and application services monitor confirmations and translate on-chain events into business workflows.

Understanding these layers prevents a common mistake: treating the blockchain as the entire product. A usable payment or wallet system also needs key management, user authentication, transaction monitoring, error handling, accounting, compliance controls where applicable, and a clear settlement policy. The chain supplies a shared transaction layer, while the surrounding infrastructure turns that layer into an operational service.

The practical question is therefore not only whether a project uses blockchain. It is which records need shared verification, who can submit changes, how the network reaches agreement, what finality the application requires, and which risks remain outside the ledger.

## Sources and references

- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical Introduction to Ethereum](https://ethereum.org/en/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-18.
