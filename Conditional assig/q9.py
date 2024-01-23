"""
The roots of the quadratic equation ax2
 + bx + c = 0, a ≠ 0 are given by the following 
formula: 
In this formula, the term b2
 - 4ac is called the discriminant. If b2
 - 4ac = 0, then the 
equation has two equal roots. 
If b2
 - 4ac > 0, the equation has two real roots. If b2
 - 4ac < 0, the equation has two 
complex roots. 
Write a program that prompts the user to input the value of a (the coefficient of x2
), b 
(the coefficient of x), and c (the constant term) and outputs the roots of the quadratic 
equation. 

"""
print("ax2+ bx + c = 0")
a = int(input("ENTER THE A VALUE : "))
b = int(input("ENTER THR B VALUE : "))
c = int(input("ENTER THE B VLAUE : "))

discriminant = (b**2) - (4*a*c)

if discriminant == 0 :
    root = -b / (2*a)
    print(f"the equation has two equal roots. {root}")
elif discriminant < 0:
    root1 = -(b - discriminant) / (2*a)
    root2 = -(b + discriminant) / (2*a)
    print(f"the equation has two complex roots.{root1} and {root2} ")
else:
    root1 = -(b - discriminant) / (2*a)
    root2 = -(b + discriminant) / (2*a)
    print(f"the equation has two real roots.{root1} and {root2}")
