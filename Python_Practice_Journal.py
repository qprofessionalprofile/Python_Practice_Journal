# userScoreCheck = int(input("Hi what score did you recieve?"))

# if userScoreCheck == 100:
#     print("You passed! Hunids all around!")
# elif userScoreCheck == 70:
#     print("You passed... But barely..hmmmm")
# else: 
#     print("You failed")
    
# message = "Hello World"
# print(message.upper())#uppercases letters
# print(message.lower())#lowercases letters



#-- Practice with a few methods

# text = "  Python is Cool!!    "
# print(text.strip()) # Prints the string without whitespaces Beginning or end

# message = "Hello World!" 
# print(message.replace("World", "goose"))# Prints the string with replaces string parts.

# sentence = "Python Practice is always fun with lists"
# words = sentence.split() # Will print a list with all words of the string stored inside

# words = ['Python', 'Practice', 'To', 'get', 'Noticed']
# sentence = "".join(words) # Joins the words of the list into a string

# filename = "report.pdf"
# print(filename.endswith(".pdf")) # Checks what the string ends with and returns a boolean.



#-- Further practice using strip, replace, split, and upper.

# my_String = '   Might I be an engineer?????   '

# string_Edit_One = print(my_String.strip())
# string_Edit_Two = print(my_String.replace("Might I be an engineer?????", "Coding Temple Trained!!"))
# string_Edit_Three = print(my_String.split())
# string_Edit_Four = print(my_String.upper())



#-- #Use of dynamic insertion for formating variable into strings

# name = "Q"
# age = 100000
# occupation = "Student Engineer"
# print("My name is {} and I am  {} years old!! I am a {}.".format(name, age, occupation)) # My silly use of the format method


#-- Working with a random name generator

# import random

# first_names_list = ['Jennifer', 'Lisa', 'John', 'Rakesh']
# last_name_list = ['Patel', 'Micheals', 'Gonzales', 'Smith']

# first_names_list = random.choice(first_names_list)
# last_name_list = random.choice(last_name_list)

# name_mixer = print(f"{first_names_list} {last_name_list}")



#-- String conversion to Integer
# num_str = "123"
# num = print(int(num_str))

#-- Looping Through a list

# fruits = ['apple', 'bannana', 'cherry', 'anotherFruit']
# for fruit in fruits:
#     print(fruits)
    
# # My use in range
# for i in range(12):# Count will start @ index 0 and stop at 11
#     print(i)
    
    
# # Use of a while loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1 #Incriment by 1 


# #--While Loop practice: Return positive values
    
# num = 2
# while num % 2 == 0:
#         print(num)
#         num += 2
#         if num > 20: # This is stops the block after the conditions met
#                 break
        
# num = 2
# while num <= 20: # This prints the same result
#         print(num)
#         num += 2


# For In loops & the use of the break statement 

# for i in range(10):
#         if i == 5: # Stop loop before you hit 5
#             break # Listens for a met condition then stops the loop
#         print(i)

# for i in range(5):
#         if i == 3: # When i is 3 then skip it
#            continue # Listens for the information in a the loops iteration specified then skips it
#         print(i)
        
# for i in range(31):
#         if (i % 3 == 0):
#                 continue
#         if (i > 25):
#                 break
#         else:
#                 print(i)
                
#-- Proof of knowledge of the parameters and the arguments

# def introduce_yourself(Name, Hobby):
#     print(f"Hi I'm {Name}, and my hobby is {Hobby}.")
    
# introduce_yourself("Q", "Coding")


# # --List of numbers function
# list_of_numbers = [1, 5, 10]

# def squared_nums(nums_list):
#         empty_list = []
#         for num in nums_list:
#                         squared_num = num ** 2
#                         empty_list.append(squared_num)
#         return empty_list

# print(squared_nums(list_of_numbers))


#-- Continued Practice 

# def squared_nums(new_list):
#         empty_list = []
#         for squared_num in new_list:
#                 empty_list.append(squared_num * squared_num)
#         return empty_list

# other_num_list = [10, 20, 40]
# print(squared_nums(other_num_list))



# #-- Basic Exception Handeling 
# try:
#     x = 10 / 0 
# except ZeroDivisionError:
#     print("You cant divide by zero!")
   
    
#--Anatomy of Basic Exception Haneling 
# try:
    #code that can raise an exception 
#except ExceptionType:
    #Code that runs if an exception occurs


# --Loop excercise 
# meals = ["pasta", "pizza", "salad"]

# for meal in meals:
#     print(meal.capitalize())
    
# print("Here's some dinner options for you hiring manager!")

    