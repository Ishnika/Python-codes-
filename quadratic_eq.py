""" A mathematics tool computes the exact roots of a quadratic equation for teaching purposes. Implement a
solution to calculate the roots of a quadratic equation."""
import math
print("A QUADRATIC EQUATION IS IN THE FORMAT OF ax^2 +bx+c=0")
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the value of constant:"))
d=b**2-(4*a*c)
if d>0 :
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("The two roots of the quadratc equation is:", "\n1st root:",root1,"\n 2nd root",root2)
elif(d==0):
    root=-b/(2*a)
    print("The roots are:",root)
else :
    print("The roots are not real")
