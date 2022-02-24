# Debugging Module

Debugging WILL be the most time consuming process on your job. 

Everyone will do it. Nobody can avoid it. Nobody's code works the first time.

So how do you approach it?

There are many different approaches

### Approach 1: Understand the system.

The approach of always understanding everything before you debug. While it will be
easier to debug like this, it is also time consuming and hard to know most aspects of
what you are doing. 

1. Read the manual
2. Know what's reasonable
3. Know some of the fundamentals of your technical field.
4. Have a high-level view of your system; Know the components and their interfaces.
5. Know your tools.

### Approach 2: Make it fail.

The simplest and arguably most common approach.

1. Repro steps that start from the beginning.
2. *stimulate* the failure (spray a hose on a leaky window).

### Approach 3: Quit thinking and look.

Sometimes the error is very obvious by just reading through your code again.

1. Instrument the system ahead of time.
2. Instrument the system when you need it.
3. See the failure.
4. See the details.
5. Guess only to focus the search.

### Approach 4: Divide and conquer.

If you divide your code into multiple parts and make sure each works. Together
the usually will as well. 

1. Divide code into large parts.
2. Make the parts smaller and smaller until the error is on one small portion.
3. Use any other approach to fix this error. 

### Approach 5: Change one thing at a time.



<!-- ### Approach 6: Keep an audit trail.
### Approach 7: Check the plug.

1. Get a fresh view.

### approach: if you didn't fix it, it ain't fixed. -->



## In larger amounts of code how do you start the debugging phase?

### Phase 1: Fail it consistantly

If you know what the error is, then it is easy to find out why it is happening. 

How do you fail it?

Well, you obviously know something is wrong that is why you are debugging. Now just see whats unique about this input. 
Maybe try 5-10 similar inputs and now see which ones are failing. Eventually, a pattern WILL arise. Once you have found the pattern you are practically done. 

### Phase 2: Find where it fails.

Take some of your faulty inputs and run them and try finding where your code is not what it should. For some people
this means use a debugger and follow each variable making sure they are all correct. For others the simpler print statements do the trick. By isolating to the function or lines that are causing your error you now know what needs fixing. 

Note: Make sure you are working with one error. If 3 parts of your code are wrong and you test multiple inputs, some problems go away while others won't. It is important that all your errors are stemming from the same problem. 

### Phase 3: Fix your problem.

While it is easier said than done often times approaching it slowly and seeing how data is being mutated is a way 
to figure our what is the actual problem is the best way to debug your code. 

Still, there are thousands of different reasons that your code could be faulty. 

To help you out here are some tricks to find patterns that help you quickly identify the error. 


## Common errors and how to identify them

### Omitted Case

Ways to tell this is the problem:

1. Data is falling in a catch-all case.
2. Infinite loops or time out errors.
3. Data not changing forms resulting in type errors.
4. Similar data not being altered.

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
### Blows up in the empty case



### Blows up when too much or too large data

There is only a finite amount of space that can be handled by functions. This translates to all data structures
and data types. Knowing how much data your code will have to sift through should slightly change how you are coding it. 

Know you data types:

For example:
Integer - 32 bits
Range of Possible Numbers: [-2147483648, 2147483648]

If you want to represent anything over these number consider using a float. 


### Divide by zero -- Sometimes

Usually the error message will give you very explicit errors for this but 
this is a common case that you may overlook when doing lots of math in your code. 

# Good Practices to Debug

### Testing small portions

Testing small portions at a time help make the debugging process easier. Isolating the 
error is much harder than accounting for the error 90% of the time.

### Following data points with a Debugger

Often times your IDE will have a built in debugger that will allow you to follow your
code line by line. 

Check out the best debuggers for your code and learning to use them will save you time greatly. 
<!-- Link to debuggers for VScode, IntelliJ, Sublime, etc.  -->

# Test your debugging

<!-- Include module for debugging

Ideas:
Multiple functions follow data points until you can isolate the problem?
Read through code and find which case is incorrect just be viewing?

 -->


https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814471684