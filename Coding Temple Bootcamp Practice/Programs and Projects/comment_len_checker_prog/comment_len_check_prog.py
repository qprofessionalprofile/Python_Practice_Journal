"""# This is a micro program to print the length of comments to keep them pep-8 range per line.
--white spaces count!--"""

comment = ""# <--paste your code here
com_len = len(comment)

if com_len <= 78 | 80:
    print(f"Your comment length is: {com_len}, you're in the safe range")
else:
    print("Your comments too long! Try a multi line comment or reduce your words to 78 - 80 characters.")