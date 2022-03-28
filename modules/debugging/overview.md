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

The premise of this is very simple. Keep changing things until you realize 



<!-- ### Approach 6: Keep an audit trail. NOT SURE HOW TO MAKE THIS AN APPROACH AGAIN FEEL LIKE ITS MORE OF A PRACTICE
FOLLOWING WHAT YOURE DOING CLOSESLY
### Approach 7: Check the plug. NOT REALLY A PROCESS BUT GIVING IT A BREAK IS MORE OF A PRACTICE

1. Get a fresh view.

### approach: if you didn't fix it, it ain't fixed.  YEAH BUT HOW DOES IT HELP-->



## In larger amounts of code how do you start the debugging phase?

### Phase 1: Fail it consistently

If you know what the error is, then it is easy to find out why it is happening. 

How do you fail it?

Well, you obviously know something is wrong that is why you are debugging. Now just see whats unique about this input. 
Maybe try 5-10 similar inputs and now see which ones are failing. Eventually, a pattern WILL arise. Once you have found the pattern you are practically done. 

### Phase 2: Find where it fails.

Take some of your faulty inputs and run them and try finding where your code is not what it should be. For some people
this means use a debugger and follow each variable making sure they are all correct. For others the simpler print statements do the trick. By isolating to the function or lines that are causing your error you now know what needs fixing. 

Note: Make sure you are working with one error. If 3 parts of your code are wrong and you test multiple inputs, some problems go away while others won't. It is important that all your errors are stemming from the same problem. 

### Phase 3: Fix your problem.

While it is easier said than done often times approaching it slowly and seeing how data is being mutated is a way 
to figure our what is the actual problem is the best way to debug your code. 

Still, there are thousands of different reasons that your code could be faulty. 

To help you out here are some tricks to find patterns that help you quickly identify the error. 


## Common errors and how to identify them

### Omitted Case
Description:
Ommitted case is when you fail to account for one of the cases that data might come in as. 


Ways to tell this is the problem:
1. Data is falling in a catch-all case.
2. Infinite loops or time out errors.
3. Data not changing forms resulting in type errors.
4. Similar data not being altered.

Note:
Make sure all cases are accounted for and be careful about having a default catch-all
case for everything.

Note 2: If it blows up in the empty case
This is often the most overlooked case, but make sure something happens if it's empty
it will be accounted for. 

Note 3: Incorrectly assuming that there will be no exceptional cases
There can be anything inputted. Either limit what you are getting inputted OR account 
for it in your code. Anything that can be accepted as a data point should be accounted for.


### Extraneous Assumption
Description:
This is when you assume certain things about the input data that may not be true. It 
usually means you have to change or account for certain things in your data and maybe even
*clean* your data to make sure it can and will run properly. 

Ways to tell this is the problem:
1. Resulting data or output is not in the right form.  

Note:
Never assume that something not specified in the parameters is given to you. Often
times you will need to make sure everything passed in to you, or any data you receive is
in the correct form that you expect it to be before working with it.

1. An ordered list
2. No duplicates of data
3. Correct or accurate data

### Incorrect order of Input 
Description:
The input of the data is not in the order you expected. This could be in many forms
such as items in a list, order of data in a string, etc.

Ways to tell this is the problem:
1. Type errors usually inform you of this.
2. Data has not been changed from original form.

Note:
Make sure you reorder your input to make sure if fits what you are excpecting before
you proceed with working with it. 

### Incorrect order of Results 
Description:
This usually means your output isn't what is expected in terms of ordering. 
Expecting: Sorted Ascending Array
Actual: [1, 2, 6, 34, 26, 10]

Ways to tell this is the problem:
1. Other functions break despite this function appearing to be correct. 
2. Only partially running your outputted data and either erroring or not running the rest properly. 

Note: Usually a simple printing of your output should show you if it is in the order it wants. Sometimes it is even worth 
having a helper function do the sorting for you. 


### Off by one error
Description:
These are usually very easy to spot but you are consistantly off by one in your 
measure or test in something.

Note:
Generally there is an edge case that is missed or an index that is not being accounted for.
If there is a patter of always being off by one in your result that means you are probably missing the first
or last case.


### Nesting Logic 
Description:
This can mean a bunch of things but always relates to your code running a loop or conditional at a 
point that it shouldn't be. You have to be aware of what can be changed where you are in code.  


Example (With Conditionals):
```python
if isAnimal is False:
    if animal == "Dog":
        
```
Obviously at this point in the code you shouldn't be checking if animal is Dog since you know its
not an animal. 

Ways to tell:
1. (In Loops) Only a part of your data (usually the first row or column) has been changed.
2. (In Conditionals) One part of your conditional always returns either false or true, or it never gets reached. 
3. (Across Functions) When you are calling helper functions unneccessarily or not at all. 


### Misnamed Property
Description: It is a simple but overlooked error. You're searching for something and it doesn't seem to be there. 

This can be in a variety of ways: Accessing database, JSON request, object properties, etc.

Almost always you should print out your data and make sure you are getting something that makes sense. 
Before trying to work with that data more, if you know what you get and if everything is working until a certain point
you should print your data, ensure it is correct, and then continue from there. 

Ways to tell: 
1. You are working with no data.
2. You are working with incorrect data. 
3. In certain languaged failed request of some sort. 



### Incorrect Mathematical Calculation
Description:
This is a common mistake that can step from many things, but you should always make sure it 
works for all possible inputs.

Ways to tell:
1. Your math doesn't output the right number.

Note: This can be from:
1. Confusing median for mean. 
2. Divide by zero.
3. Error on negative numbers, or 0.

### Typo or Reversal in translating a formula 
Description:
This is when you are using a formula given to you and trying to rewrite it or change it slightly. 

Ways to tell:
1. Output wrong or unit tests are failing. 

Note: Pretty much just be careful here. Look through your formula slowly and take a few inputs and slowly 
work through them while observing the output. 



<!-- ### incorrectly consuming an api response object WON'T YOUR FETCH/GET REQUEST TELL YOU WHAT YOU GET AND 
STATICALLY TYPED LANGUAGES TELL YOU WHATS WRONG HERE -->

### Blows up when too much or too large data
Description:
There is only a finite amount of space that can be handled by functions. This translates to all data structures
and data types. Knowing how much data your code will have to sift through should slightly change how you are coding it. 

Note:
Know you data types:
For example:
Integer - 32 bits
Range of Possible Numbers: [-2147483648, 2147483648]

If you want to represent anything over these number consider using a float. 

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

# Want to learn more on debugging?
Read more [here](/../..//blob/master/resources/Debugging_The_9_Indispensable_Rules.pdf)  
Support the author and buy the book [here](https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814471684)
