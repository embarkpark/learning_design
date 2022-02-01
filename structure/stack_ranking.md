# Phase 1: Conceptual basics

## Setting the stage

The purposes of this learning.
What hiring managers seek, and why.
Coding vs. programming.
Professionalism.
engineering: -ilities.
Soft skills matter too.
Meta-cognition, what we know about learning. What it means to you.
Ch 1 & 8 from Make It Stick.
How to succeed.
Habits -- system over goals.
Mimetic desires -- choose your role models.

## Crash-course/refresher in an initial teaching-language 

Initial languages supported: Python, JavaScript (within Node).

Later add for lower-level coverage: C and possibly some flavor of assembly (they're very similar really).

Yet-other languages let's reserve for the later phase where we specifically treat client-side programming vs server-side programming. 

It's expected that you will come in knowing at least one language well enough to solve actual problems with it. (Not just toy problems -- actual problems).

So this module is intended to be more of a refresher.

Variables.
Types.
Operators.
Strings, formatting, interpolation.
Unicode.
Exceptions.
Functions.
Variadic arguments.
Flow control.
Function pointers.
Scope.
Iteration.
Recursion.
Collections.
Classes.
Regular expressions.
Scope.
Closures.

## Programming as structured problem-solving

Programming != typing source code.
The metaphor of construction.
Backward design from human needs and other constraints.
Problem-solving heuristics.
Well-structured programs are built from small building blocks; "place bricks to build a wall".
Some major building blocks: data, functions, modules, services.

## Basic math & logic for computing

_Reassurance: just grade school stuff, don't worry._

Number systems.
Base 2, base 10.
Bits and bytes.
Base 16.
Code: before source code was Morse code.
ASCII and Unicode. Standards and protocols.
Sound and image standards.
Floating point standard.
Boolean logic.
Bitwise operations.

## Mental model of computing: the computer itself

"Code" meaning representations.
Turing machines; computers are both physical and an abstraction.
Key takeaway: abstractions aren't just helpful, they are the core of how we understand & make things work.
CPU.
Opcodes.
Memory.
Call stack vs heap.
Stack frames.
Machine code.
Assembly.
Memory as a sequence of byte-chunks.
Addresses.
Endianness.
Memory and files.
Bus.

PB sez: In Angular or Java I usually don't think about system requirements. It's not like you're coding on an Arduino with limited RAM.

Q: Are pointers/references useful for being able to read code?
Yes: NPE's. Trouble reading error messages.

Q: Is the call stack useful for being able to read code?
Yes: To more efficiently read error messages (stack traces). To understand part of how event-driven systems work.

Q: Is knowing how the CPU works useful for being able to read code?
Yes: CPUs (in conjunction with an operating system) practically speaking are an abstraction that support time-sharing a limited, single resource. (E.g., support for the stack and saving off the stack, when interrupted). This in turn is part of understanding how event-driven systems work.

Overview of Turing machines: https://brilliant.org/wiki/turing-machines/
Turing machine simulator: http://morphett.info/turing/turing.html

## Mental model of computing: operating systems

Q: Why look at operating systems when we don't directly program them or really directly interact with them very much? Normally we use frameworks which abstract away the gory details of low-level requests for memory, and so forth. So who cares? 

Answer #1: Remember when you had trouble with debugging and you didn't really understand the error messages, the contents of the long stack traces, how Java interacts with the computer in general. Everything feels really confusing, it's hard to understand what's really happening. Although it seems like frameworks abstract away everything, in fact, our programs are running alongside other programs, managed by the operating system, and lower-level errors will bubble up to be dealt with by our programs. So when we are trying to understand errors and when we are tuning the resource usage of our programs, so they run faster or to avoid things like out-of-memory errors and so forth, we sometimes have to go at least one or two levels of abstraction below our own application source code, to root-cause what's happening and make evidence-based decisions about what to do next.

Answer #2: Operating systems are some of the most complex programs ever written, and as such, many useful patterns have been developed or applied in the context of OS's. For example, caches to improve speed, or queues to handle varying, unpredictable amounts of work that should be done sequentially, or events to handle outside input that comes at unpredictable times... or just generally separating different components of the system into logical groups that organized "horizontally" or "vertically" (hierarchically)... and so on. The general idea of reusable, practical patterns is pretty powerful to recognize and apply in our own programs. This gives you more technical design and implementation options than brute-force, or whatever pops up first when googling. You'll be able to better evaluate various options.


Manages access to system resources.
(time-sharing of the CPU, memory access, disk access etc)
Implements the concept of a "process".
Launch executable files.
Presents C/C++ APIs for all of the above to "userland" programs.
Provides a set of drivers for peripherals to interact with the core system.
Consumer OS's will provide a windowing toolkit to support GUIs.
Peripherals, interrupts, buffers.

## Functions 1

Input->processing->output.
Functions as building block of design.
Function signatures as contracts.
Functions in math.
Side effects, and avoiding them.

## Functions 2

The functional approach to program design is both an alternative and a complement to object-oriented design.

The functional approach, very broadly speaking, attempts to increase program clarity and maintainability by harnessing functions to reduce surprising side effects from code.

Functional approach to program design
Functions as first-class citizens, function pointers.
Higher-order functions.
Composing functions.
Callback functions.
Functional-style List methods. Map, filter, reduce.
Lambda expressions.

## Modeling problems as data: primitive types and arrays

Types.
Operators.
Integers.
Floats.
Booleans.
Strings.
Arrays.

## Modeling problems as data: custom types, structs and classes

Core nouns.
The power of naming.
Custom types.
Structs.
Nouns as classes.
Properties and methods.
Data hiding.
Immutability.
Inheritance to reuse functionality.

## Modeling problems as data: keyed

A primer on big-O.
O(n^2) vs O(n).
O(n) vs O(1).
Key-value is hugely useful because it is O(1).
Hashtables.
How hashtables are implemented.
Insert time.
Search time.

## Modeling problems as data: sequentially

Stacks.
Queues.
Linked lists.
Insert time and search time.
Real-world problems involving the above.

## Modeling problems as data: hierarchically

General tree.
Binary tree.
Binary search tree.
Quadtree.
Insert time and search time.
Real-world problems involving the above.

## Modeling problems as data: non-linear, networked

Graphs.
Undirected vs directed.
Cyclic vs acyclic.
Weighting.
Insert time and search time.
Real-world problems involving the above.

https://bennettgarner.medium.com/what-the-graph-a-beginners-simple-intro-to-graphs-in-computer-science-3808d542a0e5

## Clean coding

Naming.
Linters.

## Unit testing



## Debugging

approach: understand the system.
read the manual.
know what's reasonable 
know some of the fundamentals of your technical field.
have a high-level view of your system; know the components and their interfaces 
know your tools.
approach: make it fail.
repro steps that start from the beginning.
*stimulate* the failure (spray a hose on a leaky window).
approach: quit thinking and look
instrument the system ahead of time.
instrument the system when you need it.
see the failure.
see the details.
guess only to focus the search.
approach: divide and conquer.
approach: change one thing at a time.
approach: keep an audit trail.
approach: check the plug.
get a fresh view.
approach: if you didn't fix it, it ain't fixed.

https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814471684

See: 

## State and state management
 
# Phase 2: Hands-on skills for client and server

## Client language crash course 

* advanced JavaScript
* (Dart, Kotlin, Swift)

## Server language crash course

* Iniitally cover: JS (Node), Python, Go.
* (popular and can treat later but kinda want to avoid for starters): Java, C#, C++
* (kinda don't want to cover due to kitchen-sink ugliness, despite huge popularity): PHP
* (waning real-life popularity, maybe too much meta-stuff, albeit popular with bootcamps): Ruby


### Common

JSON.
File I/O.
Env vars.
Command-line args.
Regular expressions.

### JavaScript (Node)

Triple-equals.
Apply and bind.
Prototypes.
For/of.
Arrow functions.
Destructuring.
Object utility methods.
Freezing.
Let, const, var.
Getters and setters.
Modules.
Promises.
Generators.
Async iterators.

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide

### Python-specific

Docstrings.
Modules.
Namespaces.
Magic methods.
Positional vs keyword args.
Arg unpacking.
Sets.
Tuples.
Lambdas.
Comprehensions.
Generators.
Iterators.
range().
pass.
itertools.
Decorators.
Python's standard library.

Reference: https://docs.python.org/3/tutorial/

### Go-specific

Pointers.
Slices.
range.
Multiple return values.
Structs.
Methods.
Interfaces.
Embedding.
Goroutines and channels.
Channel buffering, sync, directions.
Select.
Timers & tickers.
Worker pools.
Waitgroups.
Mutexes.
Panic.
Defer.
Go's standard library.

## SQL crash course


## Networking

## Async

## OO for UI coding

Composition over inheritance. Compositional approach to building component trees or scene graphs. Intermediate O-O things like mixins.

## Client platform

(browser, iOS, Android)

## Client framework

(React, Flutter)

## Databases: relational

## Integration testing


# Phase 3: Professional, web-scale team development

## Functional approach

## Refactoring

## Databases: NoSQL

## Cloud computing

## Deployment

Continuous integration. 

## Cloud deployment

Kubernetes?

## Distributed systems design

## Architectural patterns

## Coding for reliability & observability

## Product design & UX

## Estimation and iterative development



------

* Note: this is arguable, but assuming for now that this training is focusing on client-server development (both browser and native-app clients).

So, not game programming, embedded programming, scientific programming, etc.

The reasoning, such as it is:

* (a) there are a lot more jobs out there for client-server
* (b) we want length to be manageable, and it will bloat if we throw in Unity etc 
* (c) there is enough commonality to the fundamentals that it's still useful for other types of programming

