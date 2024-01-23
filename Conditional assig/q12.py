""" 
Write a program that prompts the user to input a character and determine the 
character is vowel or consonant.
"""
char = input("ENTER ANY CHARACTER ").upper()
char_list = ["A","E","I","O","U"]
if char in char_list:
    print("IT IS A VOWEL")
else:
    print("IT IS CONSONANT1")