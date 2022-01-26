"""
Logical Operators Simply PLay with Truth value{True/False}
Main Logical Operator are AND,OR and NOT
NOTE: Must have basic idea of Algebra
"""
#Logical AND
print("____LOGICAL___AND____")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("___________________\n")
#Logical OR
print("|_______LOGICAL_____OR______|")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("|________________________|\n")
#Logical NOT
print("|_______LOGICAL_____NOT______|")
print(not(True))
print(not(False))
print("|________________________|\n")

#Simple Example printing Even Numbers
num = int(input("input an integers: "))
if(num > 200):
    print(f"Number is Greater than 200 ")
    if(num % 2 == 0):
        print("Number is Even")
    else:
        print("number is not even")
elif(num == 200):
    print(f"Number is Equal to 200 ")
    if(num % 2 == 0):
        print("Number is Even")
    else:
        print("number is not even")
else:
    print("Number is less than 200")
    if(num % 2 == 0):
        print("and is even")
    else:
        print("not even")



