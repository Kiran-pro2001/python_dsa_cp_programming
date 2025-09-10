
myList = [1,2,3] #same type, different type and duplicate values
print(myList) # [1, 2, 3]
print(type(myList)) #<class 'list'>

#list constructor 
x = list((1,2,3))
print(x) #[1, 2, 3]

# Slicing
b = [10,20,30]
print(b[:8]) # no error - it will print till the last elements #[10, 20, 30] #by default it start from first element 
print(b[0:1]) # [10]
print(b[-3:-1]) #-1 is excluded   #[10, 20]
print(b[-5:-2])  #-2 is excluded # -5 is not their..so it will start from the first element.    # [10]
print(b[-2:-2]) #start from -2 index, exclude -2 index, so empty list    # []


#Indexing 
c = [1,2,3,"kiran"]
print(c[3]) # "kiran"
# print(c[5]) #IndexError: list index out of range
print(c[-1]) # "kiran"
print(c[:]) # full list gets printed 




# in keyword 
d = [1,2,3,4,5]
if 10 in d:
    print("Yes")
else:
    print("No")



# change value - mutability 
a = [10,20,30]
a.insert(0,100) # at 0th index, insert 100
print(a) #[100, 10, 20, 30]

b = ["Kiran","Kunal"]
b.insert(10,"Kajal") # before 10th index, insert "Kajal"
print(b) #['Kiran', 'Kunal', 'Kajal']
# 10th index is very big...so come to last index.

c = [20,3.5,"kiran"]
c.insert(-5,"kajal") #-5 matlab sabse pehle index pe insert karna hai value 
print(c) # ['kajal', 20, 3.5, 'kiran']

d = [1,2,3,4,5]
d.insert(-1,"kiran") #-1 index se pehle insert "kiran"
print(d) #[1, 2, 3, 4, 'kiran', 5]


# .insert(index,value) - insert value before the given index.

# d.insert(-1, "kiran") means → insert "kiran" before the element at index -1 (which is 5).

# That’s why "kiran" comes just before the last element.






#practice 
d = [10,20,30,40,50]
# insert element at end 
d.insert(len(d),100) #before 5th index, insert 100
print(d) #[10, 20, 30, 40, 50, 100]

# OR

# to insert at end, I can use .append
d.append(200)
print(d) #10, 20, 30, 40, 50, 100, 200]


a = [10,20,30]
# a[3] = 10 #IndexError: list assignment index out of range
#3rd index is not their
print(a)


b = [20,40,60]
b[1] = 50
print(b) # [20, 50, 60]


c = [10,20,30,40]
c[1:2] = [50]
print(c) #[10, 50, 30, 40]


d = [1,2,3,4,4,5]
d[0:3] = [10,20,30] #[10, 20, 30, 4, 4, 5]
print(d)


d = [1,2,3,4,4,5]
d[0:3] = [10,20,30,50]  #it will push all values
print(d) #[10, 20, 30, 50, 4, 4, 5]



d = [1,2,3,4,4,5]
d[0:3] = [10,20]  #it will push all values whether it is less or more
print(d) # [10, 20, 4, 4, 5]




# Adding items in list

#.append(element) - add element at the end of the list.
f = [1,2,3]
f.append(100)
print(f) # [1, 2, 3, 100]


# .extend() - add elements from other list to the existing list 

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6]





# remove elements from the list 

# .pop() - it removes the element at particular index, if not giving index by default it remove an element from the end index. 

y = [10,20,30]
y.pop() # no index given, it will remove element from the end
print(y) #[10, 20]

x = [1,2,3]
# x.pop(5) #5th index is not their, so indexerror
#IndexError: pop index out of range
print(x)



x = [1,2,3]
x.pop(-1)
print(x) #[1,2]




# .remove(element) - it is used to remove an element
i = [1,2,3]
i.remove(3) #remove the element 3
print(i) #[1, 2]
# to remove the 1st index value - use pop method
i.pop(1) # at 1st index remove element
print(i) #[1]



j = [10,20,40,50,60]
j.append(70) # add at end
print(j) #[10, 20, 40, 50, 60, 70]
# insert 30 element before 40 element 
j.insert(2,30) #before 2nd index, insert 30
print(j) #[10, 20, 30, 40, 50, 60, 70]

# to remove the last element 
j.pop() # remove specific to index, if nothing pass, remvoe the last element
print(j) #[10, 20, 30, 40, 50, 60]
j.insert(len(j),70)
print(j) #[10, 20, 30, 40, 50, 60, 70]

# remove the 40 element
j.remove(40)
print(j) #[10, 20, 30, 50, 60, 70]

# j.remove(100) # element 100 is not their, then how it can remove 
# #ValueError: list.remove(x): x not in list
print(j)

# .clear() - remove all elements, empty list will be their

j.clear()
print(j) # []


# del keyword is used to remove an item at any index 
k = [10,20,30]
del k[0]
print(k)
#[20, 30]

m = [1,2,3]
# del m # it delete the complete list, so nothing is their
#NameError: name 'm' is not defined
print(m)



l1 = [1,2,3,4,5]
l2 = [value**2 for value in l1]
print(l2)  #[1, 4, 9, 16, 25]


l3 = [1,20,-1]
l3.sort() #ascending order
print(l3) # [-1, 1, 20]

l5 = [1,-1,0]
l5.sort(reverse=True)
print(l5) # [1, 0, -1]


l4 = ["kiran", "kunal"]
l4.reverse()
print(l4) # ['kunal', 'kiran'] 



