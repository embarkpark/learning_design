Debugging WILL be the most time consuming process in coding. 

Everyone will do it. Nobody can avoid it. Nobody's code works the first time...

So how do you approach it?

Approach 1: Understand the system.
1. Read the manual.
2. Know what's reasonable 
3. Know some of the fundamentals of your technical field.
4. Have a high-level view of your system; Know the components and their interfaces.
5. know your tools.
Approach 2: Make it fail.
1. repro steps that start from the beginning.
2. *stimulate* the failure (spray a hose on a leaky window).

Approach 3: quit thinking and look
1 instrument the system ahead of time.
2. instrument the system when you need it.
3. see the failure.
4. see the details.
5. guess only to focus the search.

Approach 4: divide and conquer.
Approach 5: change one thing at a time.
Approach 6: keep an audit trail.
Approach 7: check the plug.

get a fresh view.
approach: if you didn't fix it, it ain't fixed.


In short how do you start the debugging phase. 

Phase 1: Fail it consistantly

If you know what the error is, then it is easy to find out why it is happening. 

How do you fail it?

Well, you obviously know something is wrong that is why you are debugging. Now just see whats unique about this input. 
Maybe try 5-10 similar inputs and now see which ones are failing. Eventually, a pattern WILL arise. Once you have found the pattern you are practically done. 

Phase 2: Find where it fails.

Take some of your faulty inputs and run them and try finding where your code is not what it should. For some people
this means use a debugger and follow each variable making sure they are all correct. For others the simpler print statements do the trick. By isolating to the function or lines that are causing your error you now know what needs fixing. 

Note: Make sure you are working with one error. If 3 parts of your code are wrong and you test multiple inputs, some problems go away while others won't. It is important that all your errors are stemming from the same problem. 

Phase 3: Fix your problem.

While it is easier said than done often times approaching it slowly and seeing how data is being mutated is a way 
to figure our what is the actual problem is the best way to debug your code. 

Still, there are thousands of different reasons that your code could be faulty. 

To help you out here are some tricks to find patterns that help you quickly identify the error. 


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

### Incorrect order of Input 

Ways to tell this is the problem:

1. Type Errors in statically typed languages. 
2. Data has not been changed from original form.

Make sure all cases are accounted for and be careful about having a default catch-all
case for everything.

### incorrect order of results
### Off by one error 
These are usually very easy to spot.

Generally there is an edge case that is missed or an index that is not being accounted for.
If there is a patter of always being off by one in your result that means you are probably missing the first
or last case. 

### Incorrect level of Nesting 

This usually means in a n dimensional object exactly an (n-1) amount of data is being changed or 
used. This would mean that if you are working with a 3D array then 

[0, 0, 0]
[0, 0, ]
[]
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