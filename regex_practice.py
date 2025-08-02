import re

# text = 'Hi my name is Quinn, and I like to solve problems and I like coffee!'
# ands = re.findall(r'and', text) # Regex findall() returns a list of the occurences 
# print(ands)
# print(len(ands))

# post = 'Coffee is that STUFF BOIIII! #Coffeelover and # coffeefo\'life!'
# tags = re.findall(r'#\w+', post) #using metacharacters and special sequences to narrow the search
# print(tags)

tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

all_hashtags = []

for tags in tweets:
    hashTags = re.findall(r'#\w+', tags)
    all_hashtags.extend(hashTags)

print(all_hashtags)

email = 'kareem1934@gmail.com'
found = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email)
if found:
    print(f'{found.group()} is a valid email! Please click continue')
    
'''
Finding the phone number
'''

text = "contact us at 123-456-7890."
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Phone number is: ", match.group())
    