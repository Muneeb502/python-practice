"""
Write a program that prompts the user to enter their weight (in kilograms) and height 
(in meters). The program should calculate the Body Mass Index (BMI) using the formula: 
BMI = weight / (height * height). The program should then classify the BMI into one of 
the following categories: 
less than 18.5 - Underweight 
BMI between 18.5 and 24.9 - Normal weight 
BMI between 25 and 29.9 - Overweight 
BMI 30 or greater - Obesity 

 """
weight = float(input("ENTER YOUR WEIGHT IN Kg "))
height = float(input("ENTER YOUR HEIGHT IN METER "))
BMI = weight/height*height
if BMI < 18.5 :
    print("UNDER WEIGHT !")
elif 18.5 <= BMI <= 24.9:
    print("NORMAL WEIGHT")
elif 25<= BMI <= 29.9:
    print("OVER-WEIGHT")
else:
    print("OBESTIY!")