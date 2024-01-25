"""
. Write a program that accepts a list from user. Your program should reverse the content of list and 
display it. Do not use reverse() method
 """
random_list = input("ENTER ANY LIST ELEMENT SEPARAT BY (:) ").split(":")
print("original list :",random_list)
print("reversed list",random_list[::-1])