"""
The marks obtained by a student in 3 different subjects are input by the user. Your 
program should calculate the average of subjects and display the grade. The student 
gets a grade as per the following rules: 
Average Grade 

90-100 A 
80-89 B 
70-79 C 
60-69 D 
0-59 F 

"""
subject1 = int(input("ENTER SUBJECT 1 MARKS :"))
subject2 = int(input("ENTER SUBJECT 2 MARKS :"))
subject3 = int(input("ENTER SUBJECT 3 MARKS :"))

if 0<= subject1 <=100 and 0<= subject2 <=100 and 0<= subject3 <=100 :
    avg= (subject1+subject2+subject3)//3
    print(avg)
    if 90<= avg <=100:
        print("A")
    elif 80 <= avg  <= 89 :
        print("B")
    elif 70 <= avg  <= 79 :
        print("B")
    elif 60 <= avg  <= 69 :
        print("B")
    elif 0 <= avg  <= 59 :
        print("F")
else:
    print("ENTERA VELID MARKS!")

