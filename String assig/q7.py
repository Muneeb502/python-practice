"""
7. A palindrome is a string that reads the same backward as forward. For example, the words dad, 
madam and radar are all palindromes. Write a programs that determines whether the string is a 
palindrome. 
Note: do not use reverse() method 
    """
word = input("ENTER ANY word!")
new_word = word[::-1]
if word == new_word:
    print("yes! it is palindrome string ")
else:
    print("no! it is not palindrome string ")