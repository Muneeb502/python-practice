"""
. Write a py program that input a list and ask user to delete a given word from a list. 
   
 """
 
list = input("ENETR ANY ELEMENT :").split()
print("YOR LIST :",list)
dele_word = input("ENTER THE WORD YOUWANT TO DELET : ")
if dele_word in list:
    list.remove(dele_word)
    print("WORD HAS BEEN DELELTED")
else:
    print("WORD NOT FOUND")
print("your new list is ",list)
