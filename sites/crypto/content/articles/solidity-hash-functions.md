---
title: "Solidity hash functions: available primitives, encoding, and risks"
description: "Learn how Solidity hash functions process encoded inputs, how keccak256 differs from other built-in options, and what collision risks matter."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["keccak256 Solidity", "abi.encodePacked", "hash collision"]
author: "editorial_team"
primary_keyword: "solidity hash functions"
owned_question: "What hash functions does Solidity expose, how are their inputs encoded, and what security limits should developers understand when using them?"
risk_level: "medium"
---

Solidity developers should treat a hash as the digest of the exact bytes supplied to it: first decide how values will be encoded, then hash those bytes, and make sure the encoding cannot confuse distinct inputs. The available evidence here does not establish Solidity’s built-in function names, return types, or encoding rules, so those implementation details must be checked against the official documentation for the compiler version in use rather than assumed.

## What Solidity hash functions do

A hash function transforms input data into a digest. Hashing is not encryption: it does not provide a reversible way to recover the input, and a digest by itself does not establish who produced the data or whether it is secret. Cryptography is a broader discipline covering security goals such as confidentiality, data integrity, source authentication, and non-repudiation; a particular primitive generally serves only some of these goals. ([source](<https://csrc.nist.gov/glossary/term/cryptography>))

For Solidity code, the practical point is that the digest depends on the bytes actually passed to the function. If an application intends to hash structured values, the encoding that turns those values into bytes is part of the design—not a harmless formatting step.

## Which hash functions Solidity provides

This article cannot verify the exact Solidity built-in hash-function list, their names, output types, or version-specific behavior from the evidence available. Before choosing a primitive, consult the official Solidity documentation matching the compiler version and confirm the supported functions and expected input and output types. Do not infer Solidity support from a different language’s libraries: for example, Python’s `hashlib` exposes named hash algorithms, but that does not establish Solidity’s built-in interface. ([source](<https://docs.python.org/3/library/hashlib.html>))

Nor should multiple hash algorithms be treated as interchangeable merely because they all produce digests. Their names and availability alone do not establish suitability for a particular contract operation. The intended application, its inputs, and the required security properties must be evaluated separately.

## How Solidity hash functions handle input encoding

A hash function consumes bytes. Solidity programs therefore need an encoding step when the inputs are values such as integers, addresses, or strings. The encoding determines the byte sequence being hashed, so two different-looking sets of values can be ambiguous if their encodings concatenate into the same bytes.

The evidence available for this article does not establish the precise behavior of Solidity’s `abi.encode` or `abi.encodePacked`, including how either handles dynamic values. Verify those rules in the version-matched ABI documentation before relying on them. In particular, do not assume that a packed encoding is safe for multiple variable-length inputs merely because the source-level values appear distinct. Consider whether explicit lengths, delimiters, or another unambiguous representation is needed, and validate the complete encoding design.

The key review question is not just “Which hash function is called?” It is also “Can the exact bytes supplied to it be parsed back into only the intended input tuple?” If that cannot be answered clearly, the encoding deserves further review before it is used in contract logic.

## Preventing ambiguous hashes and misuse

A collision can arise at two different levels. A cryptographic hash collision means distinct byte strings produce the same digest. Encoding ambiguity is different: distinct input tuples may first be encoded as the same byte string, after which any hash function necessarily receives identical input. Changing hash algorithms cannot fix an ambiguous encoding.

Use an encoding whose boundaries are unambiguous for the values involved. Check how dynamic data is represented, whether lengths or separators are needed, and whether the intended decoding is unique. Then review how the resulting digest is used. A digest alone does not prove authenticity, keep the input confidential, or provide secure randomness; those properties require appropriate mechanisms and assumptions beyond hashing. ([source](<https://csrc.nist.gov/glossary/term/cryptography>))

Keep the claim precise when describing a collision. If two structured inputs produce identical encoded bytes, that is an encoding collision, not evidence that the underlying hash algorithm has been broken. Conversely, even a well-formed encoding does not establish every security property of the larger application.

## When to verify implementation details

Check the official Solidity documentation that matches the compiler version for built-in function availability, input and output types, and ABI encoding behavior. The evidence available here does not support a general statement about Solidity hash-function gas costs, comparative collision resistance, or a recommended algorithm for every use case; avoid treating any such statement as universal without suitable, version-specific and cryptographic evidence.

Finally, separate the hash operation from the surrounding application logic. Ask what exact bytes are committed to, whether the encoding is unambiguous, and what the application concludes from a matching digest. These checks explain the role of a Solidity hash without implying that hashing alone makes a contract or protocol secure.

## Sources and references

- [hashlib — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html) — Python Software Foundation; retrieved 2026-10-19.
- [Cryptography](https://csrc.nist.gov/glossary/term/cryptography) — National Institute of Standards and Technology; retrieved 2026-10-19.
