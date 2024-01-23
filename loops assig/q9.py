"""
. Write a Python program to print the first 8 terms of an arithmetic progression starting 
with 3 and having a common difference of 4. 
The program should output the following sequence: 
3 7 11 15 19 23 27 31 
"""

print("arithmetic progression first 8 terms ")
print("FOEMULA = a + (n-1)d")
for n in range(1,9):
     ans = 3+(n-1)*4
     print(ans)