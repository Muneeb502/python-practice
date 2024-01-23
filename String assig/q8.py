"""
8. Write a program that display following output: 
SHIFT 
HIFTS 
IFTSH 
FTSHI 
TSHIF 
SHIFT

    """
word = input("ENTER ANY WORD : ")
print(word)
for i in range(len(word)):
    new_word = word[1:] + word[0]
    print(new_word)
    word= new_word
