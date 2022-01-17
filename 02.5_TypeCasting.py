"""
Typecasting is the method to convert the variable data type 
into a certain data type in order to the operation required
to be performed by users.
"""
#example you cant concatenate integer with sring
number = 2346711 
number = str(number) #fixed by converting to string function str()
print("Total number is "+ number)
"""
also string can not converted to integer it not possible but
number in string can be converted to integer
"""
#example
temp = "23.671254"
name = "saidmtanzania" 
phone = "125_957_837"#possible
phone_converted = int(phone)
temp_converted = float(temp)
#name_converted = int(name) not possible t gives error
print(phone_converted)
print(temp_converted)
#print(name_converted) nit possible it gives error

