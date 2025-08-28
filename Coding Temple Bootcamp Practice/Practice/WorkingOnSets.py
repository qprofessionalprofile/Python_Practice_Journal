# empty_set = set()
# print(type(empty_set))

# new_set = {'one', 'two', 'three'}
# print(new_set) # creating a set 

# alist = ['item', 'stuff', 'thing', 'oddity']
# set_list = set(alist)
# print(set_list) #will print not in order

# hobbies = ['reading', 'gaming', 'hiking', 'axe throwing', 'reading']
# hobbies_set = set(hobbies)
# print('First list: ', hobbies)
# print('Set with Duplicates Removed: ', hobbies_set)

# aset = ['Germany', 'Sweden', 'USA', 'UAE']
# for country in aset:
#     print(country)# Becausse its a list it will print going down.
    
# favourite_movies = {'Incredibles', 'Tarzan', 'Hush Puppy'}
# for movie in favourite_movies:
#     print(movie)
    
# unique_flowers = {'Crisanthimum', 'Orchid', 'Cactus Flower'}
# with open('my_garden_unique_flowers.txt', 'w') as file: # creates a new file and names it
#     for flower in unique_flowers: #loops over ez. set item
#         file.write(flower + '\n')#in the file create a new line
        
# my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
# print('superman' in my_set)  # Prints True
# print('spiderman' in my_set)  # Prints False
# my_set.add('green lantern')
# print(my_set)  # Output: Green lantern is at the end

# guests = {'Charles', 'Robert', 'Alexandra'}
# if 'Alexandra' in guests:
#     print('Alexandra is present')
# else:
#     print('Alexandra is abscent.')
    
# foods = {'pizza', 'suchi', 'pasta'}
# foods.add('peppers')
# print('peppers' in foods)
# print(foods) 

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}

# print(set1.issubset(set2))  # Output: True -also issubseet check if all of one set are in anotehr
# print(set2.issuperset(set1))  # Output: True -also superset checks if one set contains all elements of another


# set1 = {'basketball', 'soccer', 'tennis'}
# set2 = {'basketball', 'soccer'}

# print(set2.issubset(set1))  # Is set2 a subset of set1?
# print(set1.issuperset(set2))  # Is set1 a superset of set2?

# set1 = {'information', 'data'}
# set2 = {'moreinformation', 'data'} #both datas will print as one
# unified_data = set1.union(set2)
# print(unified_data)

# set1 = {'Alice', 'Bob', 'Charlie'}
# set2 = {'David', 'Emma', 'Charlie'}
# mutual_freinds = set1.symmetric_difference(set2) # 
# print(mutual_freinds)

# def clean_username_lists(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
    
#     # Remove duplicates and merge
#     all_unique = set1.union(set2)
#     print("All unique usernames:",'\n', all_unique,'\n')
    
#     # Common emails
#     common_usernames = set1.intersection(set2)
#     print("usernames in both lists:",'\n', common_usernames,'\n')
    
#     # Emails unique to each list
#     unique_usernames = set1.symmetric_difference(set2)
#     print("usernames unique to each list:",'\n', unique_usernames, '\n')

# username_list1 = ['username1', 'username2', 'username3', 'username5']
# username_list2 = ['username4', 'username5', 'username6']

# clean_username_lists(username_list1, username_list2)

# magical_library = ("magical Tome", ["Ancient Scolls", ("Spell", "Bless")], "Wizard's Guide")

# print(magical_library[1][1][1]) #prints bless

attacks = ("Infinite Age", ["Thanos Snap", ("Spell", "Bless")], "Wizard's Guide")

print(attacks[1][1][1]) #prints bless

