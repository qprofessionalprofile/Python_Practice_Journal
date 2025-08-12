"""
Practice using tuples, like manipulation, slicing, unpacking, etc..
"""

# tuple1 = ('string', 1, True)

# tuple2= 'tuple packing', 222, True

# single_element_tuple = (5,)
# print(type(single_element_tuple)) #proof of a single element tuple

# empty_tuple = ()#how to do an empty tuple

# new_list = [1, 2, 3]
# my_tuple = tuple(new_list)
# print(my_tuple)

# manipulated_tuple = ("apple", "banana", "cherry")
# print(manipulated_tuple[0])  # Output: "apple"
# print(manipulated_tuple[1])  # Output: "banana"

# sliced_tuple = (1, 2, 3, 4, 5)
# print(sliced_tuple[1:4])  # Output: (2, 3, 4)

# looped_tuple = (1, 2, 3, 4, 5)

# for num in looped_tuple: 
# 	print(num) 

# my_tuple = (10, 20, 30)
# my_tuple = (40, 50, 60)  # Legal, since we're creating a new tuple

# my_tuple = ("intro")
# temp_list = list(my_tuple)
# temp_list.append("Epilogue")
# my_tuple = tuple(temp_list)

# tuple_explorer = (99, 3.45, "hello!", True)
# print("First Element: ", tuple_explorer[00000000]) #will still print
# print("Last Element: ", tuple_explorer[-1])

# tuple_explorer[1] = "world" # purposfull error

# person_info = "Alice", 30, "Developer"
# print(person_info) 


# name, age, profession = person_info
# print(name)
# print(age)
# print(profession) #tuple unpacking


# unpacked_tuple = ('More', 'Tuple', 'Practice')
# unpacked1, unpacked2, unpacked3 = unpacked_tuple
# print(unpacked1)#will print every 
# print(unpacked2)#individual element
# print(unpacked3)#as their own variable


# values = ("one", 2.22, True, 4)
# seperated, *rest = values 
# print(seperated)  
# print(rest) 
# '''*rest after the comma will print the
#  rest of the tuple in a seperate variable'''
 
# *start, last = seperated
# print(start)  
# print(last)   


# user_information = ('lenny', 25, 'Texas')
# name, _, location = user_information
# print(name)
# print(location)


# def get_user_info():
#     return "Bob", 29, "Engineer"
# name, age, profession = get_user_info()
# print(name)


# def tupleinfo(name, species, location):
#     print(f"This is {species}, his name is {name}, his location is {location}.")
    
# personInfo = ('Lenny', 'Human', "Tex-os") #needs to be global
    
# tupleinfo(*personInfo)


# my_counted_tuple = (1, 2, 3, 2, 4, 5, 2)
# print(my_counted_tuple.count(2))

# my_indexed_tuple = (1, 2, 3, 4, 5)
# print(my_indexed_tuple.index(2))

# mastered_tuples = (1, True, "three", 4.4, 5, 'six')
# print('first Element: ', mastered_tuples)
# print('forth Element: ', mastered_tuples)

# sliced_tuple = mastered_tuples[1:5]
# print("Sliced tuple: ", sliced_tuple)

# counted_tuple = mastered_tuples.count(True)
# print("The number of counted Trues: ", mastered_tuples)

"""
Will need to add the comments that explain the tuples methods and practices.
"""