"""
Set and Dictionary -




Dictionary -

- Dictionary is an unordered collection of key-value pairs enclosed with {} curly braces.

- Dictionary is mutable.

eg -
          key   value 
Fruit = {"Apple":10, "Orange::20}

"""

fruit = {"Mango":10, "Apple":20, "Litchi":30, "Strawberry":40}
print(type(fruit)) # <class 'dict'>


# Extracting Keys and Values 

# Extracting Keys
fruit = {"Mango":10, "Apple":20, "Litchi":30, "Strawberry":40}
print(fruit.keys()) #dict_keys(['Mango', 'Apple', 'Litchi', 'Strawberry'])



# Extracting Values 
fruit = {"Mango":10, "Apple":20, "Litchi":30, "Strawberry":40}
print(fruit.values()) #dict_values([10, 20, 30, 40])




# Adding a New Element 
fruit = {"Mango":10, "Apple":20, "Litchi":30, "Strawberry":40}
fruit["Graps"]=50  # at end
print(fruit) # {'Mango': 10, 'Apple': 20, 'Litchi': 30, 'Strawberry': 40, 'Graps': 50}





# Changing an Existing Element 
fruit = {"Mango":10, "Apple":20, "Litchi":30, "Strawberry":40}
fruit["Mango"]=100
print(fruit) # {'Mango': 100, 'Apple': 20, 'Litchi': 30, 'Strawberry': 40}


###


"""

Dictionary Functions

"""

# Update one dictionary's elements with another 
# appen the elements from the fruit2 to fruit1 or you can say, you want to conatenate values from fruit2 to fruit1, then use update method
fruit1 = {"Apple":10, "Orange":20}
fruit2 = {"Banana":30, "Guava":40}
fruit1.update(fruit2)
print(fruit1) # {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}






# Popping an element 
# .pop(key) - pass the key, which key value pair you want to remove it.
fruit = {"Apple":10, "Orange":20, "Banana":30, "Guava":40}
fruit.pop("Orange")
print(fruit) #{'Apple': 10, 'Banana': 30, 'Guava': 40}



