"""
File Handling is the storing of data in a file using a program.
"""
"""
Modes of File Handling are write("w"),read("r") and append("a")
"""
#Function for writing File
def write_file(file_name,stuff):
    file = open(file_name,"w")
    file = file.write(stuff)
    file.close()
#Function for reading file 
def read_file(file_name):
    file = open(file_name,"r")
    new = file.read()
    print(new)
    file.close()
#function for append content to a file:
def append_file(file_name,stuff):
    file = open(file_name,"a")
    file = file.write(stuff)
    file.close()
#Main function
print("This is stick note system")
char = input("If you want to write new note type w and r for reading and a for appends: ")
if char == "w":
    print("Welcome to new note:")
    filex = str(input("enter your note name: "))
    if not any(filex):
        filex = str(input("Please enter your note name: "))
    else:
        stuff = str(input("enter your note: "))
        write_file(filex,stuff)
elif char == "r":
    rnote = str(input("enter your note name to read: "))
    if any(rnote):
        read_file(rnote)
    else:
        print("Your note doesnt exist")
elif char == "a":
    fileapp = str(input("enter note name to append: "))
    if not any(fileapp):
        fileapp = str(input("enter note name to append: "))
    else:
        stuff = str(input("enter your note: "))
        append_file(fileapp,stuff)







