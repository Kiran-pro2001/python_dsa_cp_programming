"""
Built-in String Methods in Examples -


"""

# 40 methods 

#capitalize() - first character of first word in a sentence become Uppercase

str = "my name is amit"
print(str.capitalize()) # My name is amit



# casefold() - convert string into lowercase 

str = "My name is AMIT"
print(str.casefold()) # my name is amit


# center() - align a string centerly 
str = "DEMO" # length is 4
print(str.center(10,"#")) # length is 10 for the string, and at remaining place put #
#   ###DEMO###   - total length of the string is 10



# count() - use to search for the specific value, and it's count of appearance in the string 

str = "This is demo, This is another demo."
print(str.count("This")) # 2

print(str.count("demo",7,25)) #search from 7th index to 25th index - start index & end index 
# 1



# find() - search for the occurence of specific letter in a string 

str = "This is first text"
print(str.fint("text")) # 14 
# on what index we found text

str = "This is first text. This is second text"
print(str.fint("text",20,40)) # 20 - start index for searching, 40 - end index for searching
# 35 





# endswith() - check if the string ends with specific value 

str = "This is demo text. This is demo text2"
print(str.endswith("text2")) # True 

# you can also add start & end positions
print(str.endswith("text2",7,15)) #False
# from 7 to 15, unable to find the text2, so return False 




