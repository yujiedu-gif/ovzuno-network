---
title: "Ethereum unit converter: convert wei, gwei, and ether"
description: "Use an ethereum unit converter to translate wei, gwei, and ether with clear conversion factors, worked examples, and checks for decimal-place errors."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["crypto_assets_protocols"]
tags: ["wei to ether", "gwei to ether", "ether denominations"]
author: "editorial_team"
primary_keyword: "ethereum unit converter"
owned_question: "How can you convert between wei, gwei, and ether, and how should you interpret the result?"
risk_level: "low"
---

An Ethereum unit converter expresses the same ETH amount in wei, gwei, or ether. Use the conversion factors—1 ETH equals 10¹⁸ wei, and 1 gwei equals 10⁹ wei—to multiply when converting to a smaller denomination and divide when converting to a larger one. The number changes with the unit; the underlying quantity does not.

## Ethereum unit converter: the denominations it handles

Ether, often written as ETH, can be represented in different denominations. **Wei** is the base denomination used to express an Ethereum account balance. **Gwei** is a larger denomination, and **ether** is larger still. These names describe different scales for expressing an amount; converting between them changes the displayed number, not the amount’s account ownership or network.

An Ethereum unit converter applies a scale factor to express a quantity in another denomination. It is useful when a value appears in a unit different from the one you need. For instance, a quantity shown in wei can be converted to ETH by dividing by the number of wei in one ETH. The result is still an ETH-denominated representation of the same quantity, rather than a transfer or change to an account balance.

Keep the unit attached to every number you write down or copy. The number “42” alone does not say whether it means wei, gwei, or ETH. Writing “42 gwei” makes the quantity interpretable and gives you a starting point for choosing the correct conversion factor.

A denomination conversion is also distinct from changing the network associated with an amount. The amount must be understood in the context of a particular Ethereum network because balances do not carry between independent networks. Changing from wei to ETH changes the unit notation; it does not move a balance between networks. [source](<https://ethereum.org/en/developers/docs/accounts/>)

## The conversion factors between wei, gwei, and ether

The core relationships are:

- **1 ETH = 10¹⁸ wei**
- **1 gwei = 10⁹ wei**
- **1 ETH = 10⁹ gwei**

The relationship between ETH and gwei follows from their shared wei scale: one ETH contains 10¹⁸ wei, while one gwei contains 10⁹ wei, so one ETH corresponds to 10⁹ gwei. [source](<https://ethereum.org/en/developers/docs/accounts/>) [source](<https://ethereum.org/en/developers/docs/accounts/>)

These factors work in either direction. To convert to a **smaller denomination**, multiply by the number of smaller units in the larger unit. To convert to a **larger denomination**, divide by that number. Therefore:

- ETH to wei: multiply by 10¹⁸; wei to ETH: divide by 10¹⁸.
- Gwei to wei: multiply by 10⁹; wei to gwei: divide by 10⁹.
- ETH to gwei: multiply by 10⁹; gwei to ETH: divide by 10⁹.

“Smaller denomination” refers to the size of each unit, not the amount being represented. The same quantity requires a larger numerical count when expressed in smaller units. That direction check is useful before doing the arithmetic: the number should grow when converting ETH to gwei or wei, and shrink when converting wei or gwei to ETH.

## Convert an amount step by step

First identify the input amount and its unit. Next identify the destination unit and the factor connecting the two. Multiply or divide according to the direction, then label the answer. Keeping the units visible helps prevent applying a correct factor to the wrong pair of denominations.

**Example: ETH to gwei and wei**

For **0.25 ETH**:

- To convert to gwei, multiply by 10⁹: 0.25 × 1,000,000,000 = **250,000,000 gwei**.
- To convert to wei, multiply by 10¹⁸: 0.25 × 1,000,000,000,000,000,000 = **250,000,000,000,000,000 wei**.

Both outputs represent the same input quantity in different denominations. A reverse check confirms the first result: 250,000,000 gwei ÷ 10⁹ = 0.25 ETH. The second can be checked by dividing the wei result by 10¹⁸, which also returns 0.25 ETH.

**Example: wei to ETH**

For **3,000,000,000,000,000,000 wei**, divide by 10¹⁸. The result is **3 ETH**. Multiplying 3 ETH by 10¹⁸ returns the original wei amount.

**Example: gwei to ETH**

For **42,000,000 gwei**, divide by 10⁹. The result is **0.042 ETH**. To check it, multiply 0.042 by 10⁹; the result is 42,000,000 gwei.

These examples are arithmetic demonstrations, not rules about how a particular wallet or application must format a value. When recording a conversion, include both the source and destination units—for example, “42,000,000 gwei = 0.042 ETH”—so the result can be reviewed without guessing what the numbers mean.

## Check decimal placement and precision

The conversion factor determines the decimal shift. Multiplying ETH by 10¹⁸ to obtain wei shifts the decimal 18 places to the right; dividing wei by 10¹⁸ to obtain ETH shifts it 18 places to the left. The shift between gwei and wei is nine places because their factor is 10⁹. These shifts are another way to understand the multiplication and division rules, but writing out the factor can make a check easier when the input contains many digits.

When the result is a wei amount, preserve its full integer value. Do not remove zeros or round the integer merely to make it shorter. If you convert a value into a larger denomination and choose to round the displayed decimal, make clear that the displayed result is rounded; a shortened representation may not retain the exact original quantity. The unit relationship itself does not prescribe how much precision a particular interface displays. [source](<https://ethereum.org/en/developers/docs/accounts/>) [source](<https://ethereum.org/en/developers/docs/accounts/>)

Use a short verification routine before relying on a copied value:

1. **Check the labels.** Confirm that the input and output units are stated and that the output is labeled with the unit you intended.
2. **Check the factor.** Use 10¹⁸ for ETH and wei, and 10⁹ for gwei and wei or ETH and gwei.
3. **Check the direction.** Multiply when converting to the smaller denomination; divide when converting to the larger denomination.
4. **Check the scale.** The numeric value should become larger toward smaller units and smaller toward larger units.
5. **Reverse the calculation.** Where practical, convert the result back and compare it with the starting quantity.

A reverse calculation is particularly helpful with values containing long strings of zeros. If converting back does not reproduce the input, check for a missing zero, an incorrect factor, a misplaced decimal, or a unit-label error. Do not treat matching-looking digits as sufficient: the units and the arithmetic direction must match as well.

## Where denomination conversion ends

Converting wei, gwei, and ETH answers a unit question: how can the same quantity be written at another scale? It does not calculate a transaction’s gas usage or total fee, and it does not tell you an amount’s market value in another currency. Those are separate calculations and are outside the scope of denomination conversion.

For software or operational use, verify unit handling against the documentation for the relevant implementation. The conversion factors establish the relationships among the units, but do not specify a particular wallet or application’s accepted inputs, limits, rounding, or display behavior. Avoid assuming that two interfaces display a value the same way unless their documentation confirms it.

The essential check is simple: identify the starting unit, choose the corresponding factor, multiply toward smaller denominations or divide toward larger ones, and keep the output label attached. A reverse conversion can then confirm that the answer represents the same quantity. An Ethereum unit converter should make those steps easier to follow, not obscure the unit or precision of the result.

## Sources and references

- [Ethereum accounts](https://ethereum.org/en/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-21.
