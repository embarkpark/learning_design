## Task: Debugging code  

This will focus on different debugging procedures. 

Let's say your company is trying to implement a "password validator." 

Your task is to find and solve all the bugs to get the output to pass all the tests.
Can we write a hidden test scheme. 

```python
def validatePassword(pword):

    letterCount = 0
    numCount = 0
    if len(pword) < 10:
        return False
    for letter in pword:
        #missing case error where it isn't alphabet or numeric but special character
        if letter.isalpha:
            letterCount = letterCount + 1
        else:
            numCount = numCount + 1
    # less than or equal to faults
    if letterCount < 5 or numCount < 5:
        return False

    return True


def main():
    x = 0
    while x != 1: 
        print("Passwords must have: \n1 Capital Letter\n1 Lowercase letter\n5 letters\n5 numbers\nCannot contain < or >")
        password = input("Type in your password or type 'exit' to quit\n")
        if password == 'exit':
            x = 1
        else:
            print(validatePassword(password))
    print('Finished Running')
    
        
    

main()