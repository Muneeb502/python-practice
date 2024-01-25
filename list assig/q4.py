""" 
4. Write a program that rotates the element of a list so that the element at the first index moves to the 
second index, the element in the second index moves to the third index, etc., and the element in the last 
index moves to the first index. 
    """

element_list = input("ENTER ANY NUMBERS OR WORDS : ").split()
new_list = [element_list[-1]] + element_list[0:-1]
print("so the new list is ", new_list)

