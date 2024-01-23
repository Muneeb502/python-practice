""" 
9. Write a program in python that accepts a string to setup a passwords. Your entered password must 
meet the following requirements: 
The password must be at least eight characters long. 
It must contain at least one uppercase letter. 
It must contain at least one lowercase letter. 
It must contain at least one numeric digit. 
Your program should should perform this validation.

    """
print("ENTER YOUR PASSWORD")
print("""The password must be at least eight characters long. 
It must contain at least one uppercase letter. 
It must contain at least one lowercase letter. 
It must contain at least one numeric digit.""")

password = input("Enter your password here: ")

if len(password) >= 8:
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        print("Your password is strong and meets the criteria.")
    else:
        print("Your password does not meet the specified criteria.")
else:
    print("Your password is not at least 8 characters long!")

