"""
Practice for file handling and project creation in python.
This folder is also whwere the files that are created through out the 
program will live. 
"""


# """
# This is a program that is opening a new file and placing
# a mesage on the inside using 'w' in the open() function.
# """
# with open('user_content.txt', 'w') as file:
#     file.write('User Message Content: "Here is my message!"')
    


# """
# This a program the takes the information from an already
# exhisting file and appends new information to it.
# Its similar to the one above but this one uses 'a' to append new text to the file.
# the \n is new as well to make a new line.

# """

# with open('user_content.txt', 'a') as file:
#     file.write('\nUser Message Content: "Here is a new message!"')
    


"""
read(), readlines(), and readline() functions are used to 
read information from files that exhist, and thsoe are the  methods.
"""

with open('new_user_content.txt', 'r') as file:
    read_content = file.read()
    print(read_content)
    


