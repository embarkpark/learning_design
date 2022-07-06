# Debugging 1
_Introducing a recipe for debugging code._

### Don't go into battle with no plan
* A logical, step-by-step debugging process is more likely to succeed than disorganized/random "spray-and-pray" debugging.
* If you don't have a good process, you can fall into "tunnel vision", trying the same things over and over, not advancing.

### What is a good debugging process?

1. Identify exactly how to reproduce the problem.
1. Identify which parts of the code are related to the problem.
    * Really read the stacktraces.
    * Really read the console output.
1. Understand the flow of control and data in those parts.
    * Really read the code.
    * Really read the documentation.
1. Programmatically reproduce the problem.
    * Write a test case that fails at first.
    * Write the fix.
    * The test case should now pass.
1. Proceed scientifically - formulate and test hypotheses.
1. Don't just look for quick workarounds, aim to understand what is happening.
    * [Rubber duck](https://github.com/embarkpark/learning_design/blob/master/meta/glossary.md#rubber-duck-debugging) explanations help you organize your thoughts.
    * Believe in logical reasons, not magic -- logically connect cause and effect.
      * See [Cargo Cult](https://github.com/embarkpark/learning_design/blob/master/meta/glossary.md#cargo-cult-mentality) 


### Let's practice

#### Summative task:

Review goals:

* Really read the documentation.
* Really read the console output.
