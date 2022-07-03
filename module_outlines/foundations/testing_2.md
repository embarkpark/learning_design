# Testing 2
_Reorganizing code to make it more testable._

### Unit tests are another client of the code
* Unit tests verify the *contract* of the unit under test.
* Whoever calls a piece of code can be considered a "client" of that code.
* An automated test is _another client_ of the code under test.

### Better design through testing
* Having another client forces the design to be less coupled to one client.
    * Less coupling means less breakage when one component changes.
        * This increases maintainability.
* Conversely, when code is difficult to test, its contracts and behavior tend to be more tightly-coupled to other code.
    * Tight coupling increases the risk of breakage when one component changes.
        * This reduces maintainability.

### "Testable code is cleaner code."
* Especially as systems get larger, loosely coupled, well-tested code becomes extremely important for maintainability.

### How-to
{TODO: small examples reorganizing to make code more testable}

### Let's practice

Review goals:

* Reorganize a small amount of code to make it more testable, as shown in examples.
* Add tests of the now-testable code.



