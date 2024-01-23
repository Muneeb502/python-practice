"""
Write a program that prompts the user to enter their age and prints the 
corresponding age group. The program should use the following age groups: 

0-12: Child 
13-19: Teenager 
20-59: Adult 
60 and above: Senior Citizen 

"""
age = int(input("ENTER YOUR AGE : "))
if 0 <= age <=12 :
    print("CHILD")
elif 13 <= age <= 19:
    print("TEEN-AGE")
elif 20<= age <= 59:
    print("ADULT")
else :
    print("SENIOR CITIZEN!")