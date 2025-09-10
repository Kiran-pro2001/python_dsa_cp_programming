
'''

List Data Structure 


Agenda - 
1. Introduction. ✅
2. Indexing and Slicing in List. ✅
3. Changing Item Values. ✅
4. Adding List Items. ✅
5. List - Remove Iteams. ✅
6. Iteration in List. ✅
7. List Comprehension. ✅
8. Sort and Reverse Method. ✅


'''

"""

List - 
- It is denoted by [] square brackets.
- Collection of values with same or different types. 
- It allows identical values. 
- List contains ordered items. 
- It is Mutable. 
- len() function is used to give the number of items present in lists. 
- List constructor can be used to create a new list. 
x is a variable 
x = list() # list constructor 

- List is an in-built data structure which is defined as an object. 
(Tuple, Dictionary, Set defines as an Object)

"""


# Jupyter Note book  - new, python3, change the file name - List_Python


# same data type 
a = ["Kiran", "Codingmuggers","IKGPTU","Cutie"]
print(a)

# different data type
b = ["Kunal", 10, 3.4, True]
print(b)

# allows duplicate values 
# list contains duplicate values 
c = [100,200,"Kiran",100,200,100]
print(c) #[100,200,"Kiran",100,200,100]

# to get the lenght of the list - use len()
a = ['gl','tony','sachin',100.987,True]
print(len(a))

# create list constructor
x = list() #this is an empty list 
print(x)  # []
# you can put element into it 
# put elements in parenthesis 
x = list(("great learning",10,8.7))
print(x) # ['great learning', 10, 8.7]


# type() function - it returns the data type of the object. 

x = [100, 67.908, "Kiran"]
print(type(x)) # <class 'list'>



#+++++++++++++++++++++++++++++++++++++++++++++++



# Indexing and Slicing in List 



"""
Indexing and Slicing in List 

- List items can be accessed through indexing. 
- The first element present in the list has zero indexing position. 
- Negative indexing can be done in List. (-1 is the last element).
- Accessing in-between values is also possible by giving specific range of indexes. (Slicing)
- "in" Keywords is used to check if any particular value is present. 

"""

# Example - 
# list of cricketers 
# index: 0      1       2       3       4
a = ["Sachin","Dhoni","Kohli","Rohit","Yuvraj"]
print(a[1:4])  # 4th index position is excluded 
# ['Dhoni', 'Kohli', 'Rohit']

print(a[:4]) # if not putting start, by default it starts from the beginnings. 
# ['Sachin', 'Dhoni', 'Kohli', 'Rohit']

print(a[-5:-1]) #-5 to -1, and -1 index will be excluded 
#['Sachin', 'Dhoni', 'Kohli', 'Rohit']


# let's do some practical

#Indexing 
#         0            1   2       3      4
a = ["Great Learning",100,"Ram","Shyam","Tony"]
# why do we need indexing - if i need to pring only one value, then use the concept of indexing. 
print(a[2]) #Rama
print(a[4]) #Tony
print(a[-1]) #Tony




# Slicing 
#         0            1   2       3      4
a = ["Great Learning",100,"Ram","Shyam","Tony"]
print(a[1:4]) #4th index position is excluded
# [100, 'Ram', 'Shyam']

print(a[:4]) # by default it start from the first element 
#['Great Learning', 100, 'Ram', 'Shyam']


#Negative Slicing 
print(a[-5:-1]) #-1 will be excluded 
#['Great Learning', 100, 'Ram', 'Shyam']


print(a[:]) #all values will be printed
#['Great Learning', 100, 'Ram', 'Shyam', 'Tony']






# --------------------------------------------


"""

How we can use "in" Keyword in the list 

- in keyword determinte whether the specified element is present in the list or not. 

"""

a = [3,4,5,100.789,"kiran"]
#conditional statements
if "kiran" in a: # a is a list 
    print("Yes, It is True")



# --------------------------------------------





"""

Changing Item Values 

- As lists are mutable, so values can be changed.
- Values can be changed for specific range of items too.
- insert() method is used to insert an item at any specific index. 

"""

#example - 
a = ["great",100,456]
# index number, what value
a.insert(2,34) # insert before 2nd index, the element 34
print(a) #['great', 100, 34, 456]




# practical example 
a = ["Ganesh","Shriram","Gopi","Shubhash","Santosh"]
# change the value, instead of Shriram, I want Edwin
a[1] = "Edwin"
print(a) # ['Ganesh', 'Edwin', 'Gopi', 'Shubhash', 'Santosh']
# that's why list is mutable, since value can be changed.



#range of values we are changing
a = ["Ganesh","Shriram","Gopi","Shubhash","Santosh"]
a[1:4] = ["Tony","Kirtika","Edwin"]
print(a)
#['Ganesh', 'Tony', 'Kirtika', 'Edwin', 'Santosh']


# now if you want to insert an element in the list we can use insert() method

a = ["Ganesh","Shriram","Gopi","Shubhash","Santosh"]
# before index 3, insert Kiran
a.insert(3,"Kiran")
print(a)
#['Ganesh', 'Shriram', 'Gopi', 'Kiran', 'Shubhash', 'Santosh']



# --------------------------------------------



"""
Adding List Items

- append() method is used to add an item at the end position of list. 

- extend() method is used to add the element from some other list to the existing list. 

"""

a = ["great",100,456]
b = ["gl","tonny","edwin","gaurav"]
a.extend(b) # a existing list me b ke elements ko add kardo
print(a)
# ['great', 100, 456, 'gl', 'tonny', 'edwin', 'gaurav']



a = ["great",100,456]
a.append("Kiran") # add element at the end
print(a)
# ['great', 100, 456, 'Kiran']

#append()
# Let's see the practical
a = ['Kiran',"Tony",100,99]
a.append("Edwin")
print(a) #['Kiran', 'Tony', 100, 99, 'Edwin']


#extend()
x = ["gsr",987.89,True]
y = ["rsa","coder",34.56]
x.extend(y)
print(x) # ['gsr', 987.89, True, 'rsa', 'coder', 34.56]









# --------------------------------------------

# List - Remove Items 

'''
- pop() method is used to remove an item at any specified index.
By default if you are not giving any specified index, it will remove from the last element.

- remove() method is used to remove the specified element. 

- clear() method will remove all the elements from the list. 
There will be list, but there will be no item present in the list.

- del keyword is also used to remove an item at any specified index. 
By default if you are not giving any index position, then it will delete the entire list. So there will be no existing list. So if you will be printing it will show error. 

'''


"""
  
pop() vs remove()
in pop() method you are removing an item through indexing whereas in remove() method you are removing the specified element.



"""


# pop()
#square brackets
a = ["gsr","edwin","ramesh","suresh"]
a.pop() # not giving any index value - last element will be remove from the list
print(a)    # ['gsr', 'edwin', 'ramesh']


# if giving any index value
a = ["gsr","edwin","ramesh","suresh"]
# give index value
a.pop(1) # at index 1 the element will be remove 
print(a)  # ['gsr', 'ramesh', 'suresh']




# remove()
a = ["gsr","edwin","ramesh","suresh"]
# give item value that you need to remove
a.remove("ramesh")
print(a)  #['gsr', 'edwin', 'suresh']



# clear()
a = ["gsr","edwin","ramesh","suresh"]
a.clear() # all the elements will be remove, so it will be an empty list 
print(a)  # []


#del keyword 

# difference betwen del keyword and clear() method
# first of all, del is a keyword and clear is a method.
# When you are using del keyword, and you are not specifing any position, then your entire list will be deleted,  whereas in clear(), all the elements will be deleted but there is an empty list.

a = ["gsr","edwin","ramesh","suresh"]
del a[2] # at 2nd index delete that element
print(a) #['gsr', 'edwin', 'suresh']


a = ["gsr","edwin","ramesh","suresh"]
# del a     #entire list will be deleted
print(a)  #NameError: name 'a' is not defined
# because our entire list has been deleted 






 





# Iteration in List 

'''
Iteration in List - 

- List items can be looped by using while and for loop.

- Looping can be done in list items by referring index number in range function

'''

# Example - 
list1 = ["dhoni","yuvraj","sachin","kohli"]
for x in list1:
    print(x)





# practical example

a=["dhoni","yuvraj","gayle","abd","sachin"]
for x in a: 
    print(x)
'''
dhoni
yuvraj
gayle
abd
sachin
'''




a=["dhoni","yuvraj","gayle","abd","sachin"]
for x in range(0,len(a)):
    print(a[x])
"""
dhoni
yuvraj
gayle
abd
sachin
"""







'''
List Comprehension - 

- It provides a shorter syntax.
- Creating a new list from the values of current list. 


'''

# Example - 
x = ["Sachin","Sehwag","Ramesh","Rahul","Dhoni"]
y = []
for i in x:
    if "S" in i:
        y.append(i)
print(y)  # ['Sachin', 'Sehwag']



a = [2,3,5,7,8]
# I want to create a new list using this existing list - [8,12,20,28,32] 
# new list is 4 times of each element
#normal method is to create a list and using for loop we have to append element
b = []
for x in a:
    b.append(x*4)
print(b)  # [8, 12, 20, 28, 32]


# shorter way - use list comprehension
# single line logic 
l1 = [x*4 for x in a]
print(l1) # [8, 12, 20, 28, 32]


# syntax of list comprehension - 
# [expression for item in interation]







# ----------------------------------------




"""

Sort and Reverse Method in List - 

- sort() method will sort the items in an ascending order.

- reverse() method will give the sequence in reverse order. 


"""


#example -
a = ["gaurav","singh","rajput"]
a.sort()
print(a) #['gaurav', 'rajput', 'singh'] # g will come first, then r , then s.


# reverse()
a = ["gaurav","singh","rajput"]
a.reverse()
print(a) #['rajput', 'singh', 'gaurav']




a = [67,89,11,14,45,77,106]
a.sort()
print(a) #[11, 14, 45, 67, 77, 89, 106]

# if want to sort in descending order 
a = [67,89,11,14,45,77,106]
a.sort(reverse=True)
print(a) #[106, 89, 77, 67, 45, 14, 11]



#reverse()
a = ["great","learning","tony","edwin","gaurav"]
a.reverse()
print(a) #['gaurav', 'edwin', 'tony', 'learning', 'great']

