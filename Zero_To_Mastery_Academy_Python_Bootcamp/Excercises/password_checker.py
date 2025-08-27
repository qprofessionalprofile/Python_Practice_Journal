#Empty strings
password = input('Username: ')
username = input('Password: ')
password_length = len(password)
password_anonymizer = '**' * password_length

#User information check
print(f'{username} your password {password_anonymizer}, is {len(password)} characters long.')