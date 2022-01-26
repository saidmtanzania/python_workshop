"""
Loop is a sequence of instruction s that is continually 
repeated until a certain condition is reached.
"""

"""
while loop is a control flow statement that allows code to 
be executed repeatedly based on a given Boolean condition.
"""

i = 0 #initial condition
while i < 10:
    print(f" i = {str(i)}")
    #i=i+1 or i+=1
    i+=1
#creating infinite Loop
while True:
    print(i)
    break #used to break infinite loop

"""
for loop is a control flow statement for specifying iteration, 
which allows code to be executed repeatedly
"""
for i in range(10):
    print(f" i = {str(i)}")

#changing the range from 5 to 10
for i in range(5,10):
    print(f" i = {str(i)}")
#also can be used in the list 
temperature = [255,671, 901, 90, 50, 12,73]
for n in temperature:
    print(f"List of temperature: {n}")
#Iterating Dictionary
book = {
    "title": "unkown tour guide",
    "author": "salim diwan",
    "isb": "23-134-567",
    "page_count": 356
}
for key in book:
    print(book[key])

#do while loop
