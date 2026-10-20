---
title: "Python Blockchain Implementation: A Minimal Hash-Linked Example"
description: "Create and validate a small chain of hash-linked blocks in Python, then see why the example does not provide consensus, networking, persistence, identity, or payment"
date: "2026-10-20"
draft: false
content_type: "guide"
topics: ["blockchain_payment_foundations"]
tags: ["Python blockchain example", "blockchain data structure in Python", "hash-linked blocks", "validate a blockchain in Python"]
author: "editorial_team"
primary_keyword: "python blockchain implementation"
owned_question: "How can a learner implement a minimal blockchain data structure in Python, and which production properties will it not provide?"
risk_level: "medium"
---

# Build a Minimal Blockchain in Python

This guide builds a small, local chain of hash-linked blocks. It demonstrates how to include block contents and the preceding block’s hash in each block hash, append entries, and check the resulting links and hashes. It is a data-structure exercise, not a production blockchain or payment system.

The key distinction is between **checking consistency in one local copy** and **maintaining a shared history among independent participants**. The code performs the first task only. It does not establish who submitted data, whether a network accepts it, or which of two conflicting histories should be followed.

## What this Python blockchain example demonstrates

Each block stores three values: data, a previous-block hash, and a hash computed from the data and previous hash. The first block uses a chosen starting value because it has no earlier block in this chain. Each later block points to the hash of the block immediately before it.

That arrangement creates a checkable relationship between blocks. If block data changes but its stored hash is left untouched, recomputing the hash can reveal the mismatch. If a later block points to a value other than the preceding block’s stored hash, a link check can reveal that break.

These checks have a deliberately narrow meaning: they report whether the current in-memory objects satisfy this program’s hash and link rules. They do not make the data impossible to alter. Someone who can edit a block and recompute its hash can also update later links; this example has no independent participant or conflict-resolution rule to judge the rebuilt chain.

Python’s standard-library `hashlib` module provides interfaces to named cryptographic hash algorithms that accept bytes and produce fixed digest values. The module supplies a hashing interface, not consensus, networking, persistence, signatures, or a complete blockchain. See the Python [`hashlib` documentation](https://docs.python.org/3/library/hashlib.html). [claim_python_hashlib_digest]

## Define a block and compute its hash

This example uses SHA-256 through `hashlib`. It encodes a deliberately simple text representation of the fields being hashed as UTF-8 bytes. The hash input includes both `data` and `previous_hash`, so the validator can later recompute the block hash from those same values.

```python
import hashlib


def hash_fields(data, previous_hash):
    payload = f"{data}|{previous_hash}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash_fields(self.data, self.previous_hash)
```

The `hash_fields` function forms a string from the two selected values, encodes it as bytes, and passes those bytes to SHA-256. The digest is represented as text and stored in the block’s `hash` attribute. This minimal encoding is intended for the illustrative string values used below, not as a general-purpose serialization format. For example, the code does not define how arbitrary structured data should be represented, nor does it check whether different inputs could produce the same text representation. Keep the example’s data simple and treat the hash input format as part of the program’s rules.

A practical review question is: **Can every value that the application intends to protect be traced into the bytes passed to the hash function?** Here, the answer is limited to `data` and `previous_hash`. If the block structure changes, the creation and validation code must use the corresponding fields and encoding procedure.

A hash also does not establish authorship. The example accepts ordinary Python values as data and has no identity, authorization, or transaction-signature system. The computed digest is useful for comparing a stored result with a newly computed result; it is not proof that a particular person approved the contents.

## Create a chain and append blocks

The chain below begins with a block whose previous hash is the literal string `"0"`. That value is a simple starting convention for this exercise, not a digest computed from another block. The `append` method reads the hash of the current final block and supplies it to the next block as `previous_hash`.

```python
class Blockchain:
    def __init__(self):
        self.blocks = [Block("Starting entry", "0")]

    def append(self, data):
        previous_hash = self.blocks[-1].hash
        self.blocks.append(Block(data, previous_hash))

    def is_valid(self):
        if not self.blocks:
            return False

        if self.blocks[0].previous_hash != "0":
            return False

        for index, block in enumerate(self.blocks):
            if block.hash != hash_fields(block.data, block.previous_hash):
                return False

            if index > 0:
                previous_block = self.blocks[index - 1]
                if block.previous_hash != previous_block.hash:
                    return False

        return True


chain = Blockchain()
chain.append("Illustrative entry one")
chain.append("Illustrative entry two")

print(chain.is_valid())  # True
```

The call sequence is small enough to inspect directly:

1. `Blockchain()` creates one initial block.
2. The first `append` reads that block’s hash and creates a second block linked to it.
3. The next `append` reads the second block’s hash and creates a third block linked to it.
4. `is_valid()` checks that the chain is nonempty and that the initial block follows this example’s `"0"` convention. It then recomputes every block hash and checks each later block’s link to its predecessor.

The entries are illustrative strings, not payment records or identity details. To run the example, put the code in one Python file and run it with Python. The final print statement should display `True` for the chain as created. That output means only that this in-memory chain passes the checks implemented here at that moment.

The validator includes two extra checks so its stated rules are explicit: it rejects an empty list and rejects a first block that does not use the chosen starting value. Those are conventions of this program, not rules that every blockchain must use.

The append operation trusts the current last block: it does not ask other participants whether that block is acceptable, or whether a competing history exists. It also only changes the Python list in memory. Closing the process loses this example’s chain unless additional storage code is written; adding storage would not supply the other properties missing from the demonstration.

## Validate links and block contents

The validator performs two related checks. First, it recomputes a block’s hash from its current data and previous-hash field, then compares the result with the hash stored on that block. This checks whether those fields and the stored digest agree under this program’s hashing procedure.

Second, for every block after the first, it compares that block’s `previous_hash` with the preceding block’s stored `hash`. This checks whether the blocks are connected in the expected order according to the current objects.

Try changing a block’s data without updating its stored hash:

```python
chain.blocks[1].data = "Changed entry"
print(chain.is_valid())  # False
```

The recomputed digest no longer matches the stored hash, so validation returns `False`. This demonstrates detection of an inconsistency in the current objects. It does not show that a separate copy exists, that an outside party witnessed the original value, or that the data cannot be changed.

To demonstrate the link check independently, recreate the chain, change the third block’s previous hash, and recompute that block’s stored hash using the modified fields:

```python
chain = Blockchain()
chain.append("Illustrative entry one")
chain.append("Illustrative entry two")

chain.blocks[2].previous_hash = "not the preceding block hash"
chain.blocks[2].hash = hash_fields(
    chain.blocks[2].data,
    chain.blocks[2].previous_hash,
)
print(chain.is_valid())  # False
```

The third block’s stored hash now agrees with its own data and modified previous-hash field. The validator should nevertheless return `False` because that previous hash does not match the second block’s hash. This isolates the link rule from the recomputation check. These tests help a learner verify what the code checks, but they do not broaden what a successful result means.

When reading or modifying `is_valid()`, check that it:

- Rejects an empty chain and applies the example’s stated starting-value convention.
- Recomputes each block’s hash from the same fields and encoding used when the block was created.
- Compares each recomputed value with the stored hash.
- Checks the previous-hash relationship for every block after the initial block.
- Treats `True` as a result about this local chain, not as evidence of agreement among participants.

A local validation routine can find certain inconsistencies in the data it examines. It cannot, by itself, decide which history a network should accept.

## What the example does not provide

At a high level, NIST describes a blockchain as using cryptographically linked transactions, distributed ledger copies, validation, and established conflict-resolution rules to maintain a tamper-evident shared history. Participation, consensus, privacy, finality, and governance vary across blockchain systems. This Python example has hash links and local checks, but no distributed copies or conflict-resolution machinery. [claim_blockchain_replication]

The distinction matters because adding a `hash` attribute does not turn a program into a shared ledger. This example does not provide:

- **Consensus or conflict resolution.** It has no participants maintaining separate copies, no network rules for accepting entries, and no mechanism for choosing between conflicting histories. Its `is_valid()` method tests objects in one process; it does not establish agreement among independent participants.
- **Networking or peer verification.** There is no peer discovery, message exchange, or verification of messages from another system.
- **Durable persistence or recovery.** The chain is held in a Python list in memory. The sample does not save it to durable storage, reload it, recover from an interrupted process, or create operational backups.
- **Identity, authorization, or transaction signatures.** A string placed in `data` is simply data in this program; there is no mechanism to identify an author or check cryptographic authorization. In NIST’s high-level description of a blockchain transaction lifecycle, a transaction becomes part of the shared ledger after cryptographic authorization, validation under network rules, grouping into a block, and a consensus decision. Specific checks, block structures, consensus, and finality rules differ by network. [claim_nist_transaction_consensus]
- **Comprehensive security or protection against a chain editor.** The example has not undergone a comprehensive security review. An editor who can alter data and recompute the affected hashes and links can create a locally consistent chain. Hashing supports the stated consistency checks; it does not alone supply consensus, networking, persistence, or signatures.
- **Payment processing.** The sample has no transaction model, payment authorization flow, or network-specific validation rules. Its illustrative strings should not be treated as real payment records, and the code should not be used to hold funds or record real payments.

These are separate responsibilities, not properties enabled simply by changing the hash function. The exercise focuses on local data representation and checking. Shared history, authorization, communication, persistence, and operational security require mechanisms not present here.

## When to use this exercise

Use this Python blockchain implementation as a compact way to study a data structure, encoding, hashing, and validation. Try changing block data, changing a previous-hash field, and reading which check catches each inconsistency. Before relying on a result, ask what exact fields enter the hash, how each later block links to its predecessor, and what the validator has—and has not—observed.

Do not use the toy implementation to hold funds, record real payments, or make security guarantees. A successful local check does not establish distributed agreement, authorship, or a production security property. For adjacent background, see [What is a blockchain?](/articles/what-is-a-blockchain/) and [What is proof of work?](/articles/what-is-proof-of-work-in-blockchain/).

## Sources and references

- [hashlib — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html) — Python Software Foundation; retrieved 2026-10-19.
- [NIST IR 8202: Blockchain Technology Overview](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
