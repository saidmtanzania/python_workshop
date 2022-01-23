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
    file = input("enter your note name:")
    if not any(file):
        file = input("Please enter your note name:")
    else:
        stuff = input("enter your note")
        file = file.append(".txt")
        write_file(file,stuff)




