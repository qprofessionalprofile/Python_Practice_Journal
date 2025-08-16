import os
""""
Program that allows the user to add owned houses to a list in an external
file. Allows the user to view and manipulate the data.
"""
# This gets the path to the folder that contains the information from the program
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'homes.txt')

# file creation
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as file:
        pass

# Function to create the file for holding items from the next function.
def create_homes(homes):
    with open(FILE_PATH, 'w') as file:
        for home in homes:
            file.write(home + '\n')

# funstion to view the created file and read its contents.
def view_homes():
    homes_list = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            for line in file:
                homes_list.append(line.strip())
    return homes_list

# This function holds the conditions to add, remove, view, and quit.
def main():
    while True:
        action = input("\n1 - Add house, 2 - View Home, 3 - Sell home, 4 - Quit\n")
        
        if action == '1':
            homes = view_homes()
            add_home = input("Enter your new home: ")
            homes.append(add_home)
            create_homes(homes)
            print(f"'{add_home}' added!")
            
        elif action == '2':
            homes = view_homes()
            if homes:
                print("Here are your owned homes: ")
                for i, home in enumerate(homes, start=1):
                    print(f"{i}. {home}")
                
        elif action == '3':
            homes = view_homes()
            if homes:
                try:
                    home_id = int(input("Which home are you selling? (integer)"))
                    if 1 <= len(homes):
                        homes.pop(home_id - 1)
                    create_homes(homes)
                except ValueError:
                    print("you must enter a valid number")
                except:
                    print("There isnt a home by that number.")
                else:
                    print("Home Sold! Congrats!")
        elif action == '4':
            print("Thank you, goodbye!")
            break
        elif action == 'help':
            show_help()
        else:
            print("Invalid input please retry.")
def show_help():
    print("""
==================== HELP MENU ====================
1 - Add house
    Lets you type in a new home name and adds it to your list.
    
2 - View Home
    Shows all homes you currently own, numbered for easy reference.
    
3 - Remove home
    Lets you type in the number of a home from your list to remove it.
    
4 - Quit
    Closes the program.
    
help
    Shows this help menu.
====================================================
""")
    
main()
            
            