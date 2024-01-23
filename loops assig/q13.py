""" Write a program that prompts the user to enter a number and repeats this process 5 
times. The program should accumulate the numbers entered and then display the final 
running total. 
Sample Output: 
Enter a number: 10 
Enter a number: 15 
Enter a number: 35 
Enter a number: 40 
Enter a number: 50 
The final running total is: 150
"""
print("TAKE NUMBER WITH HELP OF LOOP")
sum = 0
for i in range(5):
    sum += int(input("ENTER A NUMBER : "))
print("THE FINAL RESULT IS : ",sum)