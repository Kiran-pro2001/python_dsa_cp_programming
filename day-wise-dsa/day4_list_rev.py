l1 = [1,2,3,4,5]
# insert element 10 before 3rd index 
l1.insert(3,10)  # [1, 2, 3, 10, 4, 5]
print(l1)


# add elements from other list to the existing list
l2 = [1,2,3,4,5]
l3 = [10,20]
l2.extend(l3)
print(l2) # [1, 2, 3, 4, 5, 10, 20]


# pop() - element at particular index, if nothing add it will remove from end.

l4 = [1,2,3,4,5]
l4.pop() # remove at end
print(l4) # [1, 2, 3, 4]


l4 = [1,2,3,4,5]
l4.pop(1) # remove element at 1st index
print(l4) # [1, 3, 4, 5]


l5 = [1,2,3]
# l5.remove(10) # remove will remove the element, if that element is not their, it will give error 
print(l5) # ValueError: list.remove(x): x not in list


l1 = [1,2,3]
l1.append(10) # add element at end
print(l1)  # [1, 2, 3, 10]


l1 = [1,2,3]
l1.clear() # remove all elements, only empty list will be their
print(l1) # []


l2 = [1,2,3]
# del l2 # remove item at particulat index
print(l2) #NameError: name 'l2' is not defined. Did you mean: 'l1'?

l3 = [1,2,3,4]
del l3[1] # remove item at 1st index 
print(l3) # [1, 3, 4]


l1 = [1,2,3]
l1.sort()# ascending order
l1.sort(reverse=True) #descending order
l1.reverse() # reverse it
print(l1) # [1, 2, 3]