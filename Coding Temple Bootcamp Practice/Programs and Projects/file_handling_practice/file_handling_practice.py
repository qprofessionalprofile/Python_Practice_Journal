import re
import os


"""
Practice for file handling and project creation in python.
This folder is also whwere the files that are created through out the 
program will live. 
"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'home list.txt')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH2 = os.path.join(BASE_DIR, 'home list dicttionary.txt')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH3 = os.path.join(BASE_DIR, 'Interactive Data Mangament.txt')


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as file:
        pass
if not os.path.exists(FILE_PATH2):
    with open(FILE_PATH2, 'w') as file:
        pass
    
if not os.path.exists(FILE_PATH3):
    with open(FILE_PATH3, 'w') as file:
        pass
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
    


# """
# read(), readlines(), and readline() functions are used to 
# read information from files that exhist, and thsoe are the  methods.
# """

# with open('new_user_content.txt', 'r') as file:
#     read_content = file.read()
#     print(read_content)
    


# """
# List storage and extraction (dictionary and lists)
# """

# # Storage of lists
# homes = ["One story", "Stilt House", "Condo"]

# with open(FILE_PATH, 'w') as file:
#     for home in homes:
#         file.write(home + '\n')
        
# # List Extraction
# homes = []
# if os.path.exists(FILE_PATH):

#     with open(FILE_PATH, 'r') as file:
#         for home in homes:
#             homes.append(home.strip())
#         print(homes)

# #Extracting from stroed dictionaries
# homes = {
#     'Mansion': '1000000',
#     'Condo': '250000',
#     'Stilt Home': '450000',
#     'Dome Home': '200000'    
# }

# with open(FILE_PATH2, 'w') as f:
#     for home, types in homes.items():
#         f.write(f"{home}: {types}\n")

# # Dictionary data extraction
# home_info = {} #empty list for homes extracted information to live

# with open(FILE_PATH2, 'r') as file:
#     for line in file:
#         home, types = line.strip().split(': ')
#         home_info[home] = types
# print(home_info)



"""
Interactive Data Management
"""

def homes_list(homes):
    with open(FILE_PATH3, 'w') as f:
        for home in homes: 
            f.write(f"{home['Home Type']}-:-{home['Home Price']}-:-{home['Home State']}\n")
#uses a delimiter to structure and seperate information. Makes reading parsed information easier.

def add_home(homes):
    Home_Type = input("What is the house type? ")
    Home_Price = input("How much is the house? ")
    Home_State = input("Where is the house? ")
    homes.append({'Home Type' : Home_Type, 'Home Price' : Home_Price, 'Home State' : Home_State})
    homes_list(homes) #Adds the home information to the file.
    
def read_homes():
    home_list = []
    with open(FILE_PATH3, 'r') as f:
        for line in f:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            if data: 
                home_list.append({'Home Type' : data.group(1),
                              'Home Price' : data.group(2),
                              'Home State' : data.group(3).strip() })
    return home_list 

def view(homes):
    print('Homes List')
    print('---------------------')
    for id, home in enumerate(homes):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if home['Home Type'][0].lower() in vowels else 'a'
        print(f"{id + 1}.) {home['Home Type']} is {a_or_an} {home['Home Price']} home on {home['Home State']}")
        
def sell_home(homes):
    view(homes)
    home = int(input("\n\nSelect the number of the house taht youd like to sell.: "))
    home = homes.pop(home - 1) # delete homes from the first index
    print(f"\n{home['Home Type']} was sold! Congratulations!")
    homes_list(homes)
    
def main():
    while True:
        homes = read_homes() 
        action = input('''
Your "investment" choice
-----------------------
1 - Add a "bought" home
2 - "Sell" a home
3 - Review all house "investments"
4 - Quit
''')
        if action == '1':
            add_home(homes)  # "Buy" a new house
        elif action == '2':
            sell_home(homes)  # "sell" a house
        elif action == '3':
            view(homes)  # Shows all homes
        elif action == '4':
            print("Lets keep investing together!")
            break

main()

