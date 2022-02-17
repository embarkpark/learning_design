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

## Common errors and how to isolate

### Omitted Case

Ways to tell this is the problem:
Often times these errors will be the same as not catching all instances of a case.

1. Data is falling in a catch-all case. 
2. Infinite loops or time out errors. 
3. Data not changing forms resulting in type errors. 
4. Data not being altered at the end. 

Make sure all cases are accounted for and be careful about having a default catch-all
case for everything.

### Extraneous Assumption

Ways to tell this is the problem:
Often times these errors will be the same as not catching all instances of a case.

1. Resulting data or output is not in the right form.  
2. 

Never assume that something not specified in the parameters is given to you. Often
times you will need to make sure everything passed in to you, or any data you receive is
in the correct form that you expect it to be before working with it.

1. An ordered list
2. No duplicates of data
3. Correct or accurate data
4. 

### incorrect order of input 
### incorrect order of results
### off by one error 
### incorrect level of nesting 
### misnamed property 
### Incorrect Mathematical Calculation

typo or reversal in translating a formula
confusing median for mean
incorrectly assuming that there will be no exceptional cases
incorrectly consuming an api response object
blows up in the empty case 
blows up when too much data 
divide by zero -- sometimes

# Good Practices to Debug

### Testing small portions

Testing small portions at a time help make the debugging process easier. Isolating the 
error is much harder than accounting for the error 90% of the time.

### Functional Testing 
### Following data points with a Debugger

Often times your IDE will have a built in debugger that will allow you to follow your
code line by line. 

Check out the best debuggers for your code and learning to use them will save you time greatly. 
<!-- Link to debuggers for VScode, IntelliJ, Sublime, etc.  -->


https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814471684