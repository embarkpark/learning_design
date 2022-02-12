## Intro

Every time you are handed a plain-English specification of what a system or new feature should do, you face a problem decomposition challenge. You can use the technique described above to convert the fuzzy plain English problem into a set of more-precisely-described sub-problems.

For example, if your team is asked to make a personal payments app, then one of the first things you'll do is decompose the large problem of "allow individuals to pay each other small amounts on their phone" into smaller problems, such as:

1. finding the person you want to pay
1. checking that this person is really who you want to pay
1. setting up the payment
1. validating the payment details
1. executing the payment
1. receiving payment confirmation

You can imagine then breaking down any of these smaller problems further into even smaller problems. Eventually the problems will be small enough that they can be converted almost mechanically into functions. E.g., "validateAccountBalance()".

This is the problem-solving approach that seasoned programmers employ, and you will too.

## Activity

TODO:

```
supply a spec

offer at least two possible ways to break it down

ask which one is better

supply a reason why
```

