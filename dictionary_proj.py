rental_proprties = {
    'property_FL_001': {
        'State' : 'Florida',
        'City' : 'Miami',
        'House type' : 'Mansion',
        'Price per night: $' : 470,
        'Rating' : 4.60
    },
    'property_CA_001': {
        'State' : 'California',
        'City' : 'San Diego',
        'House type' : 'Condo',
        'Price per night: $' : 220,
        'Rating' : 4.60
    }
}
get_property = rental_proprties['property_CA_001']['State']
with open('property_info_request.txt', 'w') as file: # creates a new file and names it
   for rentals in get_property: #loops over ez. set item 
       file.write(get_property + '\n')#in the file create a new line