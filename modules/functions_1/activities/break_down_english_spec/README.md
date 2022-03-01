## Intro

Every time you are handed a plain-English specification of what a system or new feature should do, you face a problem decomposition challenge.

You must convert the fuzzy plain English problem into a set of sub-problems that are more-precisely described.

For example, let's say you are making a personal payments app.

One of the first things you'll do is decompose the large problem of "allow individuals to pay each other small amounts on their phone" into smaller problems, such as:

1. finding the person you want to pay
1. checking that this person is really who you want to pay
1. setting up the payment
1. validating the payment details
1. executing the payment
1. receiving payment confirmation

You can then imagine breaking down any of these smaller problems further into even smaller problems. Eventually the problems will be small enough that they can be converted almost mechanically into functions. E.g., `validateAccountBalance()`.

This is the problem-solving approach that seasoned programmers employ, and you will too.

## Activity

To practice translation of plain-English specs, let's continue looking at the personal payments app example, focusing on the payment execution phase.

Which of the following problem decompositions has a higher risk of an incorrect implementation, if coded as-is?

Option A:

To execute the payment:

1. transfer money from payer to payee
1. update the UI with new balance

Option B:

To execute the payment:

* begin transaction
    * check the payer's preferred accounts (in-app wallet, bank transfer, or credit card) for this transaction, in order of withdrawal preference
    * while amount remaining > 0
        * get next preferred account
        * if preferred account is valid
            * withdraw remainder from current account
                * if approved
                    * funds go into system escrow account (to fund later cash withdrawal by payee)
                    * update amount remaining
                * if not approved
                    * roll back transaction
        * else
            * roll back transaction
    * deposit amount to payee in-app wallet
* end transaction

```
Which of the two problem breakdowns has a higher delivery risk if used as the basis for implementation, A or B?

Why?
```

```
paymentMethods = payerAccount.preferredPaymentMethods
while payAmount > 0



```