set1 = {1,2,3} # unordered & unindexed 
set2 = {4,5,6}
print(set1) # {1, 2, 3}
print(type(set1)) # <class 'set'>

set1.add(4) # add one element (at any location)
print(set1) # {1, 2, 3, 4}

set1.update([5,6,7]) # add multiple elements 
print(set1) #{1, 2, 3, 4, 5, 6, 7}

set1.remove(1) # remove element 1 
print(set1) # {2, 3, 4, 5, 6, 7}

print(set1.union(set2)) # {2, 3, 4, 5, 6, 7}
print(set1.intersection(set2)) # {4, 5, 6}