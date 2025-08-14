import re

"""
Practice using Pythons regular expressions. I'm practicing functions like findall(), split(), match(), etc..
"""

# text = 'Hi my name is Quinn, and I like to solve problems and I like coffee!'
# ands = re.findall(r'and', text) # Regex findall() returns a list of the occurences  also finds all matches then returns a list
# print(ands)
# print(len(ands))

# post = 'Coffee is that STUFF BOIIII! #Coffeelover and # coffeefo\'life!'
# tags = re.findall(r'#\w+', post) #using metacharacters and special sequences to narrow the search
# print(tags)

# tweets = [
#     "Loving the #sunset! So peaceful #nature #blessed",
#     "Had a great day! #happy #friends #goodvibes",
#     "Can't wait for the #weekend! #fun #relax"
# ]

# all_hashtags = []

# for tags in tweets:
#     hashTags = re.findall(r'#\w+', tags)
#     all_hashtags.extend(hashTags)

# print(all_hashtags)

# email = 'kareem1934@gmail.com'
# found = re.search(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email) # fids the first match and returns a matched object for validation \w returns a-z or A-Z or 0-9
# if found:
#     print(f'{found.group()} is a valid email! Please click continue')
  


# """
# Practice finding a phone number using re.search()
# """

# text = "contact us at 123-456-7890."
# match = re.search(r"\d{3}-\d{3}-\d{4}", text) # \d to match any digit 0-9
# if match:
#     print("Phone number is: ", match.group())



# """
# Practice with re.match()
# checks wheather the beginning of a string matches a sepcified pattern.
# It only checks the beginning of the string
# """

# #url saftey validator 

# url = "https://www.proton.org"

# secure = re.match(r"^(https|http)", url)
# if secure:
#     print("This link goes to a secure website!")
# else:
#     ("Protocol not found")

    
# """
# Practice with re.split()
# Splits strings into a list of substrings based on occurences
# of a specified pattern in  a program. 
# Similar in nature to the built in str.split() but with re.split() regex rules 
# makes for more complex splitting. Eg. splitting mulitple delimeters or 
# patterns.
# """

# info = 'Regex, in, python,s plitting, example'

# splitter = re.split(r"[,.;\s!-]+", info)
# print(splitter)



# """
# Practice with comma seperated values. CSV for short.

# Splitting based on the commas passed to the r, from CSV_info
# """

# CSV_info = "one,two,three"
# CSV_Split = re.split(r",", CSV_info) 
# print(CSV_Split)



# """
# Manipulating and subbing text with the
# re.sub(pattern, text, replacer) function.
# """

# phone_number = "(555)555-5555"
# formatted_number = re.sub(r"\D", '', phone_number) 
# #returns an empty string for everything thats not a digit.
# print(formatted_number)

# chat = '''
# @user_person1 : "This is a placeholder message!"
# @user-person2 : "Wow! another string!!"
# @user_persong-3 : "Hehehe I think im getting the hang of this!"
# '''
# anonomous_chat_creation = re.sub(r"@[\w-]+", '@anonomous_user', chat)
# print(anonomous_chat_creation)




# """
# Matching data using the () with regular expressions.
#  re.search() is used to refer to a group by index using (). 
#  It looks like re/search(pattern, text).group(index)
#  can be used in finding parts of a phone number. 
#  You can also use it to get and manipulate parts of a string.
#  URL's, Phone Numbers, dates and allows you to use them.
# """

# phone_number_text = "124-816"
# find_pattern = r"(\d+)-(\d+)"
# found_match = re.search(find_pattern, phone_number_text)
# if found_match:
#     print(f"Int_group 1: {found_match.group(1)}")
#     print(f"Int_group 2: {found_match.group(2)}")
    