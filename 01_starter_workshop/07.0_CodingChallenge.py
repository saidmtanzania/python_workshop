marks = []
#taking in the input for 5 marks from the user and adding it to the list
for i in range(5):
    marks.append(int(input()))
# now that we have all the marks we can just loop over it
output = ""
for i in marks:
    if i >= 90 and i<=100:
        output += 'A'
    elif i >= 80 and i<90:
        output += 'B'
    elif i >=70 and i<80:
        output += 'C'
    elif i >= 60 and i<70:
        output +='D'
    elif i >= 50 and i < 60:
        output += 'E'
    elif i >= 0 and i<50:
        output += 'F'
    else:
        output = 'Please enter a valid number!'
#Write your code here    
#for every mark concatenate grades to the output e.g output+="A"
    #start here

#now we simply print the output
print(output)