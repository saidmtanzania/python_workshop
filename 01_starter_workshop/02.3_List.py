##List act as Array in python
temperature = [255,671, 901, 90, 50, 12,73]
##Printing the length of the temperature
print(f"The length of temperature list are: {len(temperature)}")
##printing list with index it start from 0
#[255,671, 901, 90, 50, 12,73]
#  0   1    2   3    4  5   6
#printing value at index 0:
index_0 = temperature[0]
print(f"The value of temperature at index 0: {index_0}")
#printing temperature at index 5
index_5 = temperature[5]
print(f"The value of temperature at index 5: {index_5}")
#printing temperature at index_3
index_3 = temperature[3]
print(f"The value of temperature at index 3: {index_3}")
#printing list without brackets or any symbolic by usinf (*)
print(*temperature)
## Two Multidimension list(Array)
temperature = [[23,43],[32,64],[45,80,70]]
#printing [specifywhich array][specifyarray value index]
value_one = temperature[0][1] #43
print(f"The value of first dimension array [23,43]of 1 index are: {value_one}")
value_two = temperature[1][0] #32
print(f"The value of second dimension array[32,64] of 0 index are: {value_two}")
value_three = temperature[2][2] #70
print(f"The value of first dimension array [45, 80, 70] of 2 index are: {value_three}")
#printing list without brackets or any symbolic by usinf (*)
print(*temperature)
#you can store value to multiple variable that specified by comma
temp1, temp2, temp3  = temperature
print(f"The value of first temp1 are: {temp1}")
print(f"The value of first temp2 are: {temp2}")
print(f"The value of first temp3 are: {temp3}")
#List also called Array
#List is the collection of similar items.
tempav1_temperature = [234,55,456.0,3451,34,901]

#printing the length of the tempav1_temperature
print(f"The lenght of temperature value is :{len(tempav1_temperature)}")

#printing value in the list
#[234,55,456.0,3451,34,901]
#  0  1   2     3   4   5

v1_temperature = tempav1_temperature[0]
print(f"the value of first temperature is: {v1_temperature}")
v2_temperature = tempav1_temperature[1]
print(f"the value of second temperature is: {v2_temperature}")
v3_temperature = tempav1_temperature[2]
print(f"the value of third temperature is: {v3_temperature}")