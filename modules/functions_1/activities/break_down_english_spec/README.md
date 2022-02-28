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

To practice translation of plain-English specs, let's continue looking at the personal payments app example.

For payment execution, which of the following problem decompositions is better?

Option A:

To execute the payment:

1. request a transfer from the bank
1. update the UI

Option B:

To execute the payment:

* begin a transaction
* check the payer's preferred payment method (in-app balance or bank transfer)
* if using in-app balance
    * request drawdown from in-app balance
        * wait for approval
        * if approved
            * update balance to pay
        * else
            roll back transaction
* if a balance remains to be paid...
    * request a transfer from the account's bank for the balance
        * wait for approval
        * if approved
            * log the success
        * else
            * roll back transaction


```
Which of the two problem breakdowns has a higher delivery risk if used as the basis for implementation, A or B?

Why?
```