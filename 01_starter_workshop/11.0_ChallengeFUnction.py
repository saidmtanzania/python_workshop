def is_password_valid(password):
    val = True
    if not len(password) >= 8:
        print("password length should be minimum of 8")
        val = False
    if not any(char.isdigit() for char in password):
        print('password should contain atleast 3 numbers')
        val = False
    if not any(char.isupper() for char in password):
        print('Password should contain atleast one uppercase')
        val = False
    if not any(char.islower() for char in password):
        print('Password should contain atleast one lowercase')
        val = False
    if val:
        return val

passwd = input("Enter your password: ")
if (is_password_valid(passwd)):
    print("Password is valid")
else:
    print("Invalid Password !!")
    
