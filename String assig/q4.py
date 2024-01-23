"""
4. Write a Python program that accepts a string from user. Your program should create a new string in 
reverse of first string and display it. 
For example if the user enters the string 'EXAM' then new string would be 'MAXE' 
    """
   
txt = input("ENTER ANY SENTENCE : ")
new_txt = txt[::-1]
print(new_txt)