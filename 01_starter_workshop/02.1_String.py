# This is single comment
"""
this is multi line coment Yay!
"""
#String Data type

first_name = "John"
last_name = "Doe"

full_name = first_name + last_name
print ("Your full name: "+full_name)

#adding space betweem first name and last name
full_name = first_name + " " + last_name
print("Your full name is: "+full_name)

#measuring variable value length
passwd = "1234242112"
passwd_lenght = str(len(passwd)) #str used to typecasting (data type changing)
type(passwd_lenght)
print("Your password length is: "+passwd_lenght)

#changing character to upper case
upper_full_name = full_name.upper()
print(upper_full_name)
#changing character to lowercase
lower_full_name = upper_full_name.lower()
print(lower_full_name)
