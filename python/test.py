text = "siva vanga selfdrive"
testlength = len(text)
print("Length of the text:", testlength)
parts = text.split()
result= parts[0] + " " + " ".join(parts[1:])
uppercase = result.upper()
print("Uppercase:", uppercase)
lowercase = result.lower()
print("Lowercase:", lowercase)

print(bool(testlength))     # True (non-zero value)


password= "aaAa4321"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
if not len(password) < 8: 
    errors.append("Password must be at least 8 characters long.")
if not any(a.isupper() for a in password):
    errors.apppend("Password must contain at least one uppercase letter.")
if not any(a.islower() for a in password):
    errors.append("Password must contain at least one lowercase letter.")
if not any(a.isdigit() for a in password):
    errors.append("Password must contain at least one digit.")
if not any(a in symbols for a in password):
    errors.append("Password must contain at least one symbol.")
if not errors:
    print("Password is valid. = True")
else:
    print("Password is invalid. = False")