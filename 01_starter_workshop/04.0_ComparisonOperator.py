"""
Comparison operators that compare values and return true or false 
The operators include: > , < , >= , <= , === , and !== .
"""
#Example compare two numbers
n1 = 10
n2 = 10
#Greater than (>)
isN1_grt_N2 = n1 > n2 #return a boolean value that is true or fase based on condition
print(f"is {n1} Greater than {n2}: {isN1_grt_N2}")
#Less than (<)
isN1_lessThan_N2 = n1 < n2
print(f"is {n1} Less than {n2}: {isN1_lessThan_N2}")
#Greater than Equal
isN1_geaterthanEqual_N2 = n1 >= n2
print(f"is {n1} Greater than or Equal {n2}: {isN1_geaterthanEqual_N2}")
#Less than Equal
isN1_LessthanEqual_N2 = n1 <= n2
print(f"is {n1} Less than or Equal {n2}: {isN1_LessthanEqual_N2}")
#Equal to
isEqual_to = n1 == n2
print(f"is {n1} Equal to {n2}: {isEqual_to}")
#Not Equal to
isNot_Equal_to = n1 != n2
print(f"is {n1} Not Equal to {n2}: {isNot_Equal_to}")

#simple conditional with comparison operator Example
password = input("Enter Password: ")
#correct Password
correct_pass = "123456"
if password == correct_pass:
    print("correct password :)")
else:
    print("incorrect password!")
#another Example for length and short password
if(len(password)) >= 6:
    print("nice length :)")
else:
    print("too short password!")
