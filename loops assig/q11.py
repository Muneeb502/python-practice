"""
Write a program that asks the user for a positive integer value. The program should 
calculate the sum of all the integers from 1 up to the number entered. For example, if 
the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20. 
"""
print("PRINT SUM OF ALL NUMBER : ")
num = int(input("ENTER ANY NUMBER :"))
sum = 0
for i in range(num+1):
    sum +=i
print("the sum of given number is", sum)    
