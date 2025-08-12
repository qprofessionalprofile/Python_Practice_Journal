my_dictionary = {
    'name' : 'Eleanor',
    'age' : 69,
    'city' : 'New York'    
}


# #Adding, Finding, Removing keys and values

# my_dictionary['occupation'] = 'Developer' # Adds value to the dictionary
# my_dictionary['age'] = 70
# ol_no_name_key = my_dictionary.pop('name')# removes 'name' key
# del my_dictionary['occupation']



# #creating Errors, Printing the list, finding keys and values of the dictionary

# print(my_dictionary)#prints entire dictionary 
# #print(my_dictionary['name'])# Will throw an error when printed
# print(ol_no_name_key) # returns the popped key from key value pairs
# find_age = my_dictionary['age']
# print(find_age)



# #  Using the .get() method and .key

# print(my_dictionary.get('age')) # .get() avoids missing keys
# print(my_dictionary.get('homedesign', 'NotIntheList'))
# print(my_dictionary.get('throw_error')) #prints None becasue it doesnt exhist
#print(list(my_dictionary.keys()))


# profile = {"user": "Genisus", "age": 22, "email": "example@silly.com"}
# for value in profile.values():
#     print(value)
# for key in profile.keys():
#     print(key) #loops over all keys
    
# print(list(my_dictionary.items()))

# home_ratings = {"Miami House": 4.8, "Rouley House": 4.4}
# for location, rating in home_ratings.items():
#     print(f"{location} has a rating of {rating}") #location is key, rating is value.
    
    
    
rental_proprties = {
    'property_FL_001': {
        'State' : 'Florida',
        'City' : 'Miami',
        'House type' : 'Mansion',
        'Price per night: $' : '470',
        'Rating' : '4.60'
},
    'property_CA_001': {
        'State' : 'California',
        'City' : 'San Diego',
        'House type' : 'Condo',
        'Price per night: $' : '220',
        'Rating' : '4.60'
    }
}
rental_proprties['property_CA_001']['phone'] = '555-1234'
print(rental_proprties['property_CA_001']['phone'])

#These dont work with the 
# rental_proprties ['State'] = "Texas"
# rental_proprties ['House type'] = "Castle"

# print(list(rental_proprties.values()))


# Looping through the list of properties
for proerty_id, info in rental_proprties.items():
    print(f"Property ID: {proerty_id}, State: {proerty_id}, Rating: {proerty_id}")

user_rental = rental_proprties['property_CA_001']['City']
print(user_rental)  