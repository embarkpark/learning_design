## Task: Debugging code #2

This will focus on different debugging procedures. 

Let's say your company is trying to implement a "password validator." 

Your task is to find and solve all the bugs to get the output to pass all the tests.
Can we write a hidden test scheme. 

### Solution

```python
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def validatePassword(pword):

    letterCount = 0
    numCount = 0
    specialChar = False
    #Check for uppercase
    if pword == pword.lower():
        print('No Uppercase letters')
        return False
    #Check for lowercase
    if pword == pword.upper():
        print('No Lowercase letters')
        return False
    #Check for <
    if '<' in pword:
        print('Invalid <')
        return False
    #Check for >
    if '>' in pword:
        print('Invalid >')
        return False
    #Check for length
    if len(pword) < 10:
        print('Length too small')
        return False
    for letter in pword:
        if (not letter.isalpha() and not letter.isdigit()):
            specialChar = True
        if letter.isalpha():
            letterCount = letterCount + 1
        elif letter.isdigit():
            numCount = numCount + 1
    if specialChar is False:
        return False
    #Check for 5 Letters and Numbers
    if letterCount < 5 or numCount < 3:
        print('Not enough letters or numbers')
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
    