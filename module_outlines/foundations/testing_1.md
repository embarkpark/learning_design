# Testing 1
_Writing unit tests for existing code._

### Professionals do not omit testing.
* High-quality construction includes verification of the work.
* Formally checking the correctness of the system obviously improves maintainability (fewer bugs).
* It can be tempting to omit testing, but doing so is a false economy -- it slows you down overall.

### Automate your testing.
* Manual verification is time-consuming and not fully reliable, because human error.
* Automated verification is less time-consuming and more reliable, because computers :)
* Thus: **write automated tests**

### Types of automated test
* There are several types of automated tests: {intro the testing pyramid}.
* We will focus on unit tests here.
* A "unit" == "the smallest piece of code that can be logically isolated in a system".
* Many consider this to be a function. (In O-O this is often considered a whole class, not just one function.)
* In this module we will focus on functions as units.

### How-to
* Consider starting with tests. That way your code structure is build upon concepts what needs to be done not how. It gives you nice indicator if you finished implementing your feature.
* Do not test parts of the frameworks or libraries/packages. If you do not trust them to work should you be using them?
* If you have trouble testing your code there high chance that architecture of your code is not right.
* Identify crucial parts of the code that need testing. Start with them.
* Each added test increase cost of future changes - tests needs to be updated. Be sure that tests that you add are not just to increase code coverage.
* Test should not only include happy paths but also other cases where things do not go as planed.
* Select test data that have regular patterns.
* Nondeterministic tests are worse then no tests.

### Let's practice

Goals:
* Building test based on specification
* Showing that making tests can help you to find bugs

