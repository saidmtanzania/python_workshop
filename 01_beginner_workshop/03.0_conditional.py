"""
Decision-making in a programming language is automated
using conditional statements, in which Python evaluates
the code to see if it meets the specified conditions.
"""
isPasswdValid = True
isAdmin = True

#When u are using if elseif only the single statement 
# that meet condition can execute 
if isPasswdValid:
    print("password is Valid")
elif isAdmin:
    print("password is valid, but not admin")
else:
    print("password is valid, but not Admin")
#