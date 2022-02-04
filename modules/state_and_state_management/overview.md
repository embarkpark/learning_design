
What is "state"? Why does it matter?
What does it mean to "manage" state?
We are constantly fighting to manage infinite complexity of our creations.
One source of that complexity is change.
1) Something that never changes is completely predictable.
2) Something that changes a lot, but in the same ways, is also completely predictable.
3) Something that changes a lot, but in various ways, is harder to predict. 
4) Something that changes a lot, but in various RANDOM ways, is very hard to predict.
So... in your source code... marking the variables whose values don't ever need to change... moves your system from (4) back towards (1). Specifically, for example, languages that support a `final` keyword allow you to mark variables as frozen, once they are initialized with some value. This means you never have to worry about those values changing again, on you. This is reassuring. This is less for you to have to think about, as you are analyzing the system. 