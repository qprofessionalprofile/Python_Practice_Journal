"""
A nested dictionary to practice nesting multiple dicttionaries program. 
It makes a txt file, and right now, only returns the city of the rental properties when ran.
"""
rental_proprties = {
    'property_FL_001': {
        'State' : 'Florida',
        'City' : 'Miami',
        'House type' : 'Mansion',
        'Price per night: $' : 470,
        'Rating' : 4.60
    }, # The dictionary ends here and a new one opens after the comma
    'property_CA_001': { # Dictionary opens after the name
        'State' : 'California',
        'City' : 'San Diego',
        'House type' : 'Condo',
        'Price per night: $' : 220,
        'Rating' : 4.60
    }
} # The rental proferties 
get_property = rental_proprties['property_CA_001']['State']
with open('property_info_request.txt', 'w') as file: # creates a new file and names it
   for rentals in get_property: #loops over ez. set item 
       file.write(get_property + '\n')#in the file create a new line
       
"""
The list only returns the city but returns it 10 times. 
I'll find a way to update this later so it returns what is being asked of the dictionary and only once.
"""