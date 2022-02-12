# [module] Functions

### Some concepts we will cover

_Input->processing->output._
_Functions as building block of design._
_Function signatures as contracts._
_Functions in math._
_Side effects, and avoiding them._

### Overview

You already know how to write functions.

At a basic level, functions exist to organize code into reusable chunks. As such, functions increase program clarity and maintainability.

In addition to the reusability aspect, functions serve as a basic building block of overall program design.

## Big Ideas for this module
_What's a Big Idea? It's a concept that you'll probably remember and use years from now, because you get better results as a professional programmer by applying it._

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

## Module activities

Let's practice writing functions, focusing on problem decomposition using them.

Activity #|Activity title
---|---
1|[Breaking down an English spec](./activities/break_down_english_spec/README.md)
2|[Refactoring a big function](./activities/refactoring_a_big_function/README.md)
3|[Modeling a workflow as a sequence of functions](./activities/modeling_a_workflow/README.md)
4|[Function signatures as contracts](./activities/functions_as_contracts/README.md)
5|[Functions in math](./activities/functions_in_math/README.md)
6|[Avoiding side effects](./activities/avoiding_side_effects/README.md)

## Capstone task

