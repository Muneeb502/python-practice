"""
Write a program that prompts the user to input a number from 1 to 7. The program 
should display the corresponding day for the given number. For example, if the user 
types 1, the output should be Sunday. If the user types 7, the output should be 
Saturday. If the number is not between 1 to 7 user should get error message as shown 
in sample output. 
    
 """
num = int(input("ENTER ANY NUMBER BETWEEN 1 TO 7 : "))
if 1 <= num <= 7:
    if num == 1:
        print("SUNDAY!")
    elif num == 2:
        print("MONDAY!")
    elif num == 3:
        print("TUESDAY!")
    elif num == 4:
        print("WEDNESDAY!")
    elif num == 5:
        print("THURSDAY!")
    elif num == 6:
        print("FRIDAY!")
    else:
        print("SATURDAY!")
else:
    print("ERROR!! try valid number between 1 to 7")