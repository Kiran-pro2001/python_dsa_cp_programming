tup1 = (1,2,3) # ordered , immutable 
tup2 = (4,5,6)
print(tup1) # (1, 2, 3)
print(len(tup1)) #3
print(type(tup1)) # <class 'tuple'>

print(tup1+tup2)  # (1, 2, 3, 4, 5, 6) # Concatenating
print(tup1*3 + tup2) #(1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6) #Repeating & Concatenating
print(min(tup1)) # 1
print(max(tup1)) # 3