# Debugging 1
_Introducing a recipe for debugging code._

### Defense lines against bugs
1. When we can detect a bug:
   * end user
   * testers
   * reviewers
   * automated tests
   * programmers
1. Why seasoned programmers create applications with less bugs?
   * One of the important reason: they follow clean code rules.
   * You don't need years of experience to follow them

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
    * "Rubber duck" explanations help you organize your thoughts.
    * Believe in logical reasons, not magic -- logically connect cause and effect.


### Let's practice

#### Summative task:

Learning goals:
- testing if they read delivered documentation - there should be issue that will require reading it to solve it. It can be for example how given cases should be handled.
- output warning about wrong parameter to console to test if they read it
- check if 

Description:
 * Debugging is early in the course - functions, lists, and maps are known.
 * The example app is a calorie counter app e.g. https://github.com/davidhealey/waistline. We recreate parts of business logic in Python.
 * There are given a code of the application that got bugs in it.
 * There is a description of what is expected from the application.
 * Some of the bugs are given as issues some are for them to find.
 * Some of the bugs are reported with a wrong cause: "When X happens Y bug occurs." but X is not the actual reason.
 * Their task is to fix the app.
