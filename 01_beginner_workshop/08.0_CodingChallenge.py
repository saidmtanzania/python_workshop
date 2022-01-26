##for checking vowel and printing result if all vowel appear

string = input("Enter any Strings: ")
sentence = string.lower()
store = []
list = ["a","e","i","o","u"]
for letters in sentence:
    if letters in list:
            if letters in store:
                sorry = " "            
            else:
                store.append(letters)
if len(store) == len(list):
    result = "YES"
else:
    result = "NO"
print(result)
