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