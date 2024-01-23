"""
2. Write a program that reads a string from keyboard and display: 
* The number of uppercase letters in the string 
* The number of lowercase letters in the string 
* The number of digits in the string 
* The number of whitespace characters in the string 
    """
txt = input("ENTER ANY SENTENCE : ")
upper_case = 0
lower_case = 0
digits = 0
space = 0
other = 0
for char in txt :
    if char.isupper():
        upper_case +=1
    elif char.islower():
        lower_case +=1
    elif char.isdigit():
        digits +=1
    elif char.isspace():
        space +=1
    else :
        other +=1
print(f"the number of upper is {upper_case}")
print(f"the number of lower is {lower_case}")
print(f"the number of digits is {digits}")
print(f"the number of space is {space}")
print(f"the numbe of others is {other}")


