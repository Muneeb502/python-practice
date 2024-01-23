"""
5. Write a Python program that accepts a string from user. Your program should create a new string by 
shifting one position to left. 
For example if the user enters the string 'examination 2021' then new string would be 'xamination 
2021e' 
    """
    
txt = input("ENTER ANY SENTENCE : ")

new_txt = txt[1:]+txt[0]

print(f"THE NEW STRING IS THIS : {new_txt}")



