from math import *
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
d=b*b-4*a*c
print("d=",d)
if d==0:
    print("roots are real and equal")
    x1=x2=-b/(2*a)
    print("X1=",x1,"X2=",x2)
elif d>0:
    print("roots arr real and unequal")
    x1=(-b+sqrt(d))/(2*a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("X1=", x1, "X2=", x2)
else:
    print("Roots are imaginary")

