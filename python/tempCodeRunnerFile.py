password= input("Enter a password: ")
if len(password) == 8 and password[:4].isalpha() and password[4:].isdigit():
    print("Password is valid.")