"""
3. Write a Python program that accepts a string from user. Your program should create and display a 
new string where the first and last characters have been exchanged.
    """
name = input("ENTER ANY SENTENCE : ")
new_nmae = name[-1] + name[1:-1] + name[0]
print(new_nmae)
