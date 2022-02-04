# [module] Functions

## Big Ideas for this module
_What's a Big Idea? It's a concept that you'll probably remember and use years from now, because it is harder to perform well as a professional programmer without this idea._

Programming seems like it is all about computers and programming languages. You might imagine that you are coding all day.

However, programmers also spend a lot of their time in analyzing, designing, and coordinating with other programmers and teammates in other roles, such as product managers. There are also maintenance, troubleshooting and investigative tasks.

In this sense, programming is less about "writing code", and more about problem solving. Strong programmers employ a systematic & structured problem solving approach.

[Problem decomposition](../glossary/problem_decomposition.md) is a powerful technique for systematic problem solving. Decomposing a large problem into smaller problems is how we effectively design programs. Much like a well-designed mechanical device, well-structured programs are built up from small, clearly-defined building blocks.

In programming, functions are these building blocks. Thus, functions are fundamental to program design.

### In summary
1. programming is not just coding, it's more fundamentally about problem solving
2. well-structured programs are built up from small, clearly-defined building blocks
3. functions are an important building block

## Real example: applications handling user input

Let's look at a real example of how functions help us break down ("decompose") a complex problem.

When a user taps on the keyboard (including the virtual keyboard on a phone), how do you organize your program to receive the keystroke data?

Let's review the sequence of what happens.

When first launched, every application will start up with a call to a "main" or "entrypoint" function. This function is called first, typically by the operating system.

After launching, the entrypoint function will call other functions until the application is initialized (ready for use). 

At this point, applications usually wait for an external event to occur. These events might be user input, a message from the network, etc

When an event arrives, then the program will call your custom functions, to inform your program of the event.

In our current case, a keyboard event arrives. For your program to handle keyboard input, you write a custom function to do something with the input.

```
function handleKeyEvent(event) {
    // check which key was pressed
    // possibly update something -- e.g., some data in memory
    // possibly return something, e.g., true/false was the event successfully handled
}
```

Because you write functions like this to handle events, such functions are called "handler functions", or just "handlers".

So, the hard problem of dealing with keyboard input has been greatly simplified.

As programmers, we can focus on just the handler function, and ignore the rest of the complexity. The location of taps on the phone screen, figuring out which key was pressed, getting that key data to the currently-active program, and later displaying the result, those details are handled by other functions elsewhere.

The hard problem has been _decomposed_ into many smaller problems, and we can focus on just one of those problems at a time.

## When will you use these Big Ideas? 

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

## Module activities

Let's practice writing functions, focusing on problem decomposition using them.

Activity #|Activity title
---|---
1|computation functions
2|validation functions
3|display formatting functions
4|sorting functions
5|search functions
6|data transformation functions

## Capstone task

