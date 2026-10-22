---
title: "How to verify bitcoin message signatures and understand the result"
description: "Learn how to verify bitcoin message signatures, what a valid check shows about address control, and why it does not prove identity or authorize a transaction."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["crypto_assets_protocols"]
tags: ["Bitcoin message signing", "Bitcoin signature verification", "Bitcoin address ownership proof"]
author: "editorial_team"
primary_keyword: "verify bitcoin message"
owned_question: "How can someone verify a Bitcoin message signature, what does a successful check establish, and what does it not prove?"
risk_level: "medium"
---

To verify a Bitcoin message signature, provide the exact message, the signature, and the Bitcoin address claimed to have signed it to a verification method that supports the relevant format. A successful result means the signature is valid for those supplied inputs under that method’s rules. It supports control of the necessary signing key when the signature was created; it does not establish the signer’s real-world identity, current control, or authority to make a payment.

## What a Bitcoin message signature check evaluates

A message-signature check tests whether a signature corresponds to a particular message and claimed Bitcoin address. It is a check of those three inputs together, not a general assessment of the person making the claim or of the meaning of the message.

The message matters as supplied. If a signer produced a signature for one text, verification checks the text entered by the verifier. A paraphrase, an added sentence, or a change in formatting can mean the verifier is checking different input. This is why “the message looks the same” is not enough: the check concerns the actual text provided to the verification method.

A message signature is also distinct from a transaction. The check does not submit a Bitcoin transaction or move bitcoin. Its result concerns whether the supplied message and signature match the supplied address under the verifier’s rules. It does not show that a payment was made, is pending, or was authorized.

The key distinction is between validating a signature and interpreting what it means. A verifier can report a cryptographic match for the specified inputs. It cannot, from that match alone, determine why the message was signed or whether its contents are accurate.

## Inputs needed to verify a Bitcoin message

A verification function needs the claimed address, the message, and the signature. Bitcoin Core’s documented `verifymessage` RPC requires an address, a base64-encoded compact signature, and the exact message. It returns a boolean indicating whether the signature is valid for the supplied address and message.

**The claimed address** is the address against which the verification function checks the signature. Use the address that accompanied the signed message, not another address believed to belong to the same person or organization. The check answers a question about the address you supply; it does not resolve who controls that address in the real world.

**The message** is the text that was signed. Preserve its characters and formatting when copying it. Spaces, punctuation, line breaks, and other visible changes can affect whether the verifier receives the same message. If the message was supplied in a file or a structured format, do not silently reformat it before checking.

**The signature** is the signature string produced by the signing process. The Bitcoin Core RPC documentation specifies a base64-encoded compact signature as its input. That description applies to this documented method; it should not be treated as a universal format requirement for every wallet or verification interface.

A fourth consideration is compatibility: the verification method must support the signature format and address type involved. The available evidence here does not establish which address types or wallet-specific signing formats every tool supports. Check the documentation for the particular method before treating its output as a definitive result.

## A wallet-neutral verification workflow

1. **Choose a documented verification method.** Identify a method that says it supports the signature format and address type in question. A verification function may be part of wallet software, a command-line interface, or another application, but their input requirements and displays can differ. This guide does not endorse a particular provider.

2. **Collect the three inputs.** Obtain the claimed Bitcoin address, the exact message, and the signature string. Keep the text in its original form and avoid substituting an address or signature from a different message.

3. **Match inputs to the method’s fields.** Enter the address, message, and signature in the corresponding fields or parameters. For the Bitcoin Core `verifymessage` RPC, the documented inputs are an address, a base64-encoded compact signature, and the exact message. Other interfaces may specify different formats, so follow their own documentation rather than assuming that fields are interchangeable.

4. **Run the check and record the method and outcome.** Bitcoin Core’s documented RPC returns a boolean: whether the signature is valid for the supplied address and message. A user interface may express an outcome in different terms. Record which method was used and what it reported so that the result is not separated from the conditions under which it was obtained.

5. **If it does not validate, check exactness and compatibility.** Compare the copied message with the original, including visible spaces and line breaks. Confirm that the signature string was not changed and that the verification method supports the relevant format and address type. A negative result alone does not identify which input or compatibility issue caused the mismatch.

Verification uses the supplied message, signature, and address; it does not require handing over a private key or recovery phrase. Do not disclose secret recovery material as a troubleshooting step. If a method asks for such material to perform a verification check, that request is outside the input requirements documented for the Bitcoin Core `verifymessage` RPC described here.

## What a successful result proves—and what it does not

A successful result supports the narrow conclusion that the signature is valid for the supplied message and address under the verifier’s rules. Bitcoin signature interpretation establishes possession of the private key needed to create the checked signature. That is evidence about control of a cryptographic key associated with the signature, not proof of the identity of the person or organization that used it.

A key can be used by a person, organization, device, or service; the signature result by itself does not identify which one. A message that names an individual or company does not make that identity claim part of the cryptographic check. To establish identity, a reviewer needs other evidence that connects the address or signing key to that real-world party. This guide does not specify what evidence is sufficient for a particular identity process.

A successful result also does not prove that the signer still controls the key. The signature supports attribution to the key needed to create it, but it does not independently show present-day access or control. Nor does it establish that the signer has legal ownership rights, that the message is true, or that the signer was authorized to make a payment. Those are separate questions requiring evidence beyond this signature check.

Keep conclusions tied to the actual result: “This signature validated for this exact message and address using this method.” Avoid expanding that statement into “this person signed it,” “this person controls the address now,” or “this authorizes a payment.” The latter claims require information the verification result does not provide.

## Common verification failures and limitations

The most direct issue to investigate is whether the verifier received the exact message that was signed. Changed punctuation, spaces, line breaks, or other characters can make the supplied text differ. Compare the verifier’s input with the original message rather than relying on memory or on a visually similar copy.

Next, check whether the signature string was preserved as supplied. A method that expects a particular representation may reject an altered or incompatible string. Bitcoin Core’s documented RPC, for example, specifies a base64-encoded compact signature. That does not establish that all wallets or verification services accept that format, or that all of them use the same signing behavior.

The address type and signing format are another compatibility boundary. If a method reports that an input is unsupported, that output should be read as a limitation of the method for that input—not as proof that the message was fraudulent or that no valid signature exists. Confirm the documented scope of the method before drawing a broader conclusion.

A failed check means the supplied inputs did not produce a valid match according to the method used. It does not, by itself, say whether the message was altered, the wrong address was supplied, the signature was copied incorrectly, or the method could not handle the relevant format. Work through those possibilities separately. If exact inputs and documented compatibility still do not explain the result, the outcome remains unresolved rather than proving a particular explanation.

For legal, compliance, identity, or other high-stakes use, a technical signature match may not answer whether this evidence is suitable for the intended purpose. The result should be described with its inputs and verification method, and any assessment of its legal or institutional significance requires separate qualified review. A message-signature check is one limited form of cryptographic evidence, not a complete identity or authorization procedure.

## Sources and references

- [verifymessage (Bitcoin Core 30.0 RPC)](https://bitcoincore.org/en/doc/30.0.0/rpc/util/verifymessage/) — Bitcoin Core; retrieved 2026-10-21.
- [Wallets - Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/wallets.html) — Bitcoin Developer Documentation; retrieved 2026-10-21.
