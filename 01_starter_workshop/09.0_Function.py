"""
Function are "self contained" modules of code that 
accomplish a specific task. Functions usually "take in" 
data, process it, and "return" a result.
"""
def fun_name():
    print("hello mtanzania")
#call function
fun_name()
#funtion with return value
def fun_return():
    return 32

# calling function and aassigned to a variable
x = fun_return()
# printing the assigned variable
print(f"The return value is {x}")
# creating calculator function
def calculator(num1,num2):
    suM = num1+num2
    return suM
# calling calculator and assign value for it to calculate
total = calculator(12,14)
# printing the value of calculator
print(f"The total value is {total}")

#function that gives True on even number and false on other 
def isEven(num):
    if(num%2 == 0):
        return True
    else:
        return False

#assigning the number to a functions
num = int(input("Enter your number: "))
x=isEven(num)
print(f"THis number {num} is even: {x}")
#lambda expression - anonymous expression
lam = lambda arg1 : arg1*2
value = int(input("Enter number to lambda: "))
print(f"The product od value: {value} times 2 is: {lam(value)}")

#Function that calculate the length of a strings
def string_len(string):
    length = len(string)
    return length
#assigning a function to the input value for checking length of a string
String = str(input("Enter your string: "))
returned = string_len(String)
print(f"Your String length is {returned}")
