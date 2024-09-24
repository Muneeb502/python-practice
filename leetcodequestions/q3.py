"""

write a program that find a number in list which is not in repeated in list
Example :
     input = [2,4,5,7,3,7,5,2,1,3,4]
     output= 1
     
    """
    
list = [ 2,4,5,7,0,0,7,1,5,3,7,2,2,3,4,5,7,9,9,3,5]


dic = {}

for i  in list:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] =1 
        
for num , rep in dic.items():
    if rep == 1:
        print(num)
     return

print(dic)