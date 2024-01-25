"""
3. Find and display the largest number of a list without using built-in function max(). Your program 
should ask the user to input values in list from keyboard. 

    """
num_list= [ int(i) for i in input("enter any numbers each number is separat by ( , ) :").split(",")]
max_num = 0

for a in num_list:
    if max_num < a:
        max_num = a

print("THE MAXIMUM NUMBER IS ",max_num)