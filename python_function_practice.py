"""
Practice using funtions, went over things like, function scope, arguments and parameters. 
"""

# def greet(): # declaration followed by name
#     print("Coding temple python practice!") # code blaock
    
# greet() #function call (will run the print inside)


#--Use of parameters 

# def parameter(param1, param2): # Both params are variables
#     print(f'This is, {param1}, {param2}!') #a use of an f string to use params in
    
# parameter('argument1', 'argument2') #No indent to call the function


#-- Use of return statements 

# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)



#-- Function scope to show local vs Global

# x = 10 # this is a Global vaiable entire program can use this

# def print_number():
#     x = 8  #This is a Local Variable. They have the same name but are different.
#     print(x) #

# print_number()    
# print(x)   

 
 
# #-- Default parameters & Variables Length

# def greet(name = "emptyContainer"):
#     print(f"Hello {name}!")
    
# greet()
# greet("Alice")

"""
Will update to go further into how function nesting works and how LEGB rules occur in python as well.
"""