
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