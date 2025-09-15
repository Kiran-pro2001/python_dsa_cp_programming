'''
Set -

- Set is an unordered and unindexed collection of elements enclosed with {} curly braces.

- Duplicates are not allowed in set. If we put it, then set takes it only once.


unordered - 
whatever sequence you insert the element in set, that particular order doesn't remain intact.

unindexed -
you can't extract element from the set with a particular index value, because there is no proper ordering.


eg -

s1 = {1,"1",True}

'''




"""

Set Opeartions -



"""

# Add one element in Set (at any random position it gets add)
s1 = {1,"a",True,2,"b",False}
s1.add("Hello")
print(s1) # {False, 1, 2, 'a', 'Hello', 'b'}


# Add multiple elements 
# keep in mind that order is not maintained here
s1 = {1,"a",True,2,"b",False}
s1.update([10,20,30])
print(s1) #{False, 1, 2, 10, 20, 'a', 'b', 30}



# Remove an Element 
s1 = {1,"a",True,2,"b",False}
s1.remove("b") # remove the b element
print(s1) # {False, 1, 'a', 2}





'''


Set Functions - 


'''

# Uion of two sets -
s1 = {1,2,3}
s2 = {"a","b","c"}
print(s1.union(s2)) # {1, 2, 3, 'a', 'c', 'b'}



# Uion of two sets -
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
print(s1.intersection(s2)) # {5, 6}

