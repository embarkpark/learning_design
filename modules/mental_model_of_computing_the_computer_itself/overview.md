
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
