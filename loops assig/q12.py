"""
write a program that takes a positive integer N as input and calculates the sum of 
the reciprocals of all numbers from 1 up to N. The program should display the final sum. 
Output of the program should be like: 
Enter a positive integer: 5 
The sum of reciprocals from 1 to 5 is: 2.28 
"""
num = int(input("ENTER ANY NUMBER : "))
sum = 0
for i in range(1,num+1):
    sum += 1/i
print("THE SUM OF THE RECIPROCAL OF GIVEN NUMBER IS : ", sum)