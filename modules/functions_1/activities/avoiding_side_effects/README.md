## Intro

As programmers, we are constantly creating complexity in our systems, and at the same time attempting to manage that complexity.

One key technique for managing complexity is to reduce or remove side effects from functions, when reasonable.

When functions mix together:

1. pure processing (of input -> output)
1. side effects

... then the behavior of these functions can become harder to predict.

### Examples of side effects

Here is a non-comprehensive list of side effects:

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

Note that many of these side effects are actually valuable & required for the program to actually perform any useful work. So we don't want to _completely remove_ side effects from all functions, that would be a silly goal.

Rather, we aim to improve program design by applying the principle of "separation of concerns". Generally speaking, we will get simpler functions if we separate pure processing logic from external access logic.

## Activity

Let's rewrite functions that have side effects such that the side effects are removed or minimized.

### Function #1: displaying output

> TODO: how to handle multiple languages? are these each a repo underneath this parent activity directory?

> TODO: how to automatically assess the refactoring that the learner performs? do we simply scan the code to see if there's an offending keyword?

Python
```python
def print_average_order_value(orders):
    # reduce orders to an integer of average order value in cents, rounded down to the closest cent
    # print this amount to the console
}
    pass
```

JavaScript
```javascript
function printAverageOrderValue(orders) {
    // reduce orders to an integer of average order value in cents, rounded down to the closest cent
    // print this amount to the console
}
```

Dart
```dart
void printAverageOrderValue(List<Order> orders) {
    // reduce orders to an integer of average order value in cents, rounded down to the closest cent
    // print this amount to the console
}
```

Go
```go
type Order struct {
	userID string
	amount int // in cents
}

func printAverageOrderValue(orders []Order) {
	sum := 0
	for _, o := range orders {
		sum += o.amount
	}
	fmt.Println("%v", sum/len(orders))
}
```

### Function #2: modifying a member of a passed-in array

TODO

### Function #3: modifying a property of a passed-in object

TODO

### Function #4: accessing a pseudo-random number generator

TODO
