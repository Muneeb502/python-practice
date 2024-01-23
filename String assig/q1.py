"""
1. Write a program that accepts a string from user. Your program should count and display number of 
vowels in that string. 
 """
text = input("ENTER ANY SENTENCE : ").lower()
vowel = ["a","e","i","o","u"]
count = 0
for char in text:
    if char in vowel:
        count +=1
print(f"the total number of vowel is : {count}")