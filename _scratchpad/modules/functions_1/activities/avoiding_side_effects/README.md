## Intro

As programmers, we are constantly creating complexity in our systems, and at the same time attempting to manage that complexity.

One key technique for managing complexity is to reduce or remove side effects from functions, when reasonable.

### Examples of side effects

Here is a non-comprehensive list of common "side effects".

* displaying output (e.g., to a terminal)
* reading/writing from/to a database
* transmitting data over the network
* logging
* modifying a variable outside the function
* modifying a member of a passed-in array (mutating argument)
* modifying a property of a passed-in object (mutating argument)
* calling another function which itself has a side effect
* accessing system time or other global values
* generating a random number using a system library

Obviously, many of these side effects are actually valuable & required for the program to actually perform any useful work.

So we don't want to _completely remove_ side effects from all functions, that would be a silly goal.

Rather, we aim to improve program design by applying the principle of "separation of concerns". Generally speaking, we will get simpler functions if we separate pure processing logic from external access logic.

I.e., when functions unnecessarily mixes these two aspects together...

1. pure processing (inputs -> return value)
1. hidden side effects

... then the behavior of these functions can become harder to predict.

## Activity

Let's rewrite functions that have side effects such that the side effects are removed or minimized.


