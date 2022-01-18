#A dictionary is an unordered and mutable Python container
#that stores mappings of unique keys to values.

book = {
    "title": "unkown tour guide",
    "author": "salim diwan",
    "isb": "23-134-567",
    "page_count": 356
}

#Accessing Dictionary
book_title = book['title']
#printing assigned varaible of book title
print(book_title)
#changingi title of the book in Dictionary
book["title"] = "How to become you"
book_title = book["title"]
#printing updated title of the dictionary
print(book_title)
#printing the whole dictionary book
print(book)
#if you dont know any keys you can use this function key() 
keys = book.keys()
print(keys)
#list of dictionary
users=[{
    "name":"saied",
    "username":"mtanzania",
    "age": 24,
    "passwd":12345
},{
    "name":"Bright",
    "username":"XO",
    "age": 22,
    "passwd":12424 
},{
    "name":"Jackson",
    "username":"Ndege",
    "age": 26,
    "passwd":12091
}]

print(users)
#Bag of Dictionary Book, Stationary, size, color
bags = {
    #declaring books
    'books':[{
    "title": "unkown tour guide",
    "author": "salim diwan",
    "isb": "23-134-567",
    "page_count": 356  
    },{
    "title": "How to be you",
    "author": "saidmtanzania",
    "isb": "23-134-131",
    "page_count": 534}],
    #declaring stationary
    'Stationary':[{
     "name": "mtanzaniatech",
     "location":"Ubungo terminal",
     "availability":"24/7",
     "weekend": "10AM to 06PM"
    },{
        'name': 'pen',
        'quantity': 120,
        'price': 200
    },{
        'name':"exercise_book",
        'quantity':200,
        'price': 500
    }],
    #declaring size
    'size': 25,
    #declaring color
    'color': 'blue'
}
#printing the bags
print(bags)

###sample example using for loop
#PRINTING KEYS OF DICTIONARY
print("\n Printing Keys of Dictionary(BAG) \n")
for i in bags.keys():
    print(i)
#PRINTING VALUE OF Dictionary
print("\n Printing values of Dictionary(BAG) \n")
for j in bags.values():
    print(j)
#PRINTING ITEMS OF Dictionary
print("\n Printing items of Dictionary(BAG) \n")
for n in bags.items():
    print(n)