# #-- Storing list elements

# my_list = [1, 2, 3, 4, 5]
# mixed_list = [1, "apple", 3.14, True]



# #-- Accessing list elements

# my_list = ["apple", "bannana", "cherry"]
# print(my_list[0])

# my_list.append("orange")# adding to the list 
# my_list.insert(1, "blueberry")# 1 specifies where to put blueberry
# my_list.remove("apple") # removes a value from the list

# del my_list[0] # removes the first item 
# my_list.pop(1) # removes and returns the item at index 1

# my_list = [1, 2, 3, 4, 5, 6]
# subset = my_list[1:4] # will return a list of accessed elements starting from index 1 and stopping at index 4

# print(my_list[:3]) # will print the list as normal since the beginning isnt specified. It will stop at 3 since the last index isnt printed.
# print(my_list[3:]) # similar as above, the sequence thats posted will start as 4 and complete to the end of the list



#-- List manipulation on their functionality and operations

# fruits = ["apple", "bannana", "cherry", "date"]
# citrus_fruits = fruits[1:3]

# print(fruits[0]) 
# print(fruits[3])

# fruits.append("elderberry")
# fruits.insert(1, "blueberry")
# fruits.remove("bannana")
# del fruits[0]

# print(fruits)
# print(citrus_fruits)



#-- List functions and methods 

# len([1, 2, 3, 4])

# min([5, 3, 8])
# max([5, 3, 8])

# numbers = [3, 6, 3, 9]
# print(numbers.sort())
# print(numbers.reverse())

# list1 = ["I", "Want", "Numbers"]
# list2 = [1, 2, 3]

# print(list1.extend(list2))