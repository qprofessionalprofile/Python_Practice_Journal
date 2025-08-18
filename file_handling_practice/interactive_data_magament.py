import re
import os


"""
Interactive Data Management Project from the file handeling practice file. Now its, its own project file.
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH3 = os.path.join(BASE_DIR, 'Interactive Data Mangament.txt')


    
if not os.path.exists(FILE_PATH3):
    with open(FILE_PATH3, 'w') as file:
        pass


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

