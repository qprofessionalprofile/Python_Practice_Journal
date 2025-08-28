"""
Practice with exception handeling using try, except, else, and finally. 
This is also practice from the practice journal but it got its own page!
I'll be adding more later.
"""

# #syntax error
# if True # missing the colon.
#     print("This if will return a Syntax error")


# #ZeroDivisionError
# x = 1/0 #will return a ZeroDivisionError (trieed to divide by 0)

try:
    num = int(input("Enter a number:"))
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print("thats not a valid number! {e}" )
else: 
    print(f"result is {result}")
finally: # This means the blocck will run even if no exceptions are met
    print("Execcute Complete!")
    

