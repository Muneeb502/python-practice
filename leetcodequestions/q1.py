"""
write a function that take a integer list from user and a target number
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 
    """
    
list = [1,3,5,7,8,9,13]
num = 6

def inset_option(num,list):
    for i in range(len(list)):
        if list[i] == num:
            return i 
        elif list[i] > num :
            return i 
    return len(list)
insert_index = inset_option(num,list)
print(insert_index)