"""
This tuple program will create a file and return a list in a txt file with the
names of the flowers.
""" 

unique_flowers = {'Crisanthimum', 'Orchid', 'Cactus Flower'}
with open('my_garden_unique_flowers.txt', 'w') as file: # creates a new file and names it
     for flower in unique_flowers: #loops over ez. set item
         file.write(flower + '\n') #in the file create a new line