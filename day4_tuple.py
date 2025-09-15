'''
Data Structures in Python -

- Tuple, List, Dictionary, Set


Tuple -
- Tuple is an ordered collection of elements enclosed within () round braces
- Tuples are immutable.
(if you create a tuple, you can't change any of the values present in the tuple) 
tuple can not be modified once it is created.

eg -
# elements of different type 
tup1 = (1,'a',True)


'''

tup1 = (1,"sparta",True)
print(tup1) #(1, 'sparta', True)
print(type(tup1)) #<class 'tuple'>




'''

Extracting Individual Elements -


'''

tup1 = (1,"a",True,"b",False)
print(tup1[0]) #1
print(tup1[-1]) #False
print(tup1[1:4]) #('a', True, 'b')




"""

Modify a Tuple -

tup1 = (1,"a",True,"b",False)
tup1[2] = "hello"

   
TypeError: 'tuple' object does not support item assignment



You cannot modify a tuple because it is immutable.

"""





"""
Tuple Basic Opearations -


"""

# Finding length of Tuple
tup1 = (1,"a",True,2,"b",False)
print(len(tup1)) #6 



# Concatenating Tuples
tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1+tup2) # (1,2,3,4,5,6)


#Repeating Tuple Elements 
tup1 = ('sparta',300)
print(tup1*3) # ('sparta',300,'sparta',300,'sparta',300)


# Repeating and Concatenating 
tup1 = ('sparta',300)
tup2 = (4,5,6)
print(tup1*3 + tup2) #('sparta',300,'sparta',300,'sparta',300,4,5,6)


# Minimum Value 
tup1 = (1,2,3,4,5)
print(min(tup1)) #1

# Maximum Value
tup1 = (1,2,3,4,5)
print(min(tup1)) #5
