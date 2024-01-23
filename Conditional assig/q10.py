"""
 Write a program that prompts the user to enter three numbers and sorts them in 
ascending order. The program should print the sorted numbers. 

    """
num1 = int(input("ENTER ANY 1 NUMBER : "))
num2 = int(input("ENTER ANY 2 NUMBER : "))
num3 = int(input("ENTER ANY 3 NUMBER : "))

num_list = [num1,num2,num3]
print("before",num_list)

print("after",sorted(num_list))