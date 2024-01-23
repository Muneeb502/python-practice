""". Write a program that prompts the user to enter a positive integer and calculates its 
factorial. The factorial of a positive integer 'n' is denoted as 'n!' and is calculated by 
multiplying all the integers from 1 to 'n' together. For example, the factorial of 5 
(denoted as 5!) is calculated as 1 x 2 x 3 x 4 x 5.
The program should display the factorial value if the input is a positive number, or 
display a message stating that the factorial does not exist for negative numbers. 
Additionally, for an input of zero, the program should output that the factorial of 0 is 1. 
"""
print("PRINTING FACTORIAL OF GIVEN NUMBER ")
num = int(input("ENTER ANY NUMBER : "))
if num == 0 :
         print("THE FACTORIAL OF GIVEN NUMBER is : 1")
elif num > 0:
    for i in range(1,num):
               num = num * i
    print("THE FACTORIAL OF GIVEN NUMBER is :",num)
else:
    print("Oops NEGATIVE NUMBER ")
    