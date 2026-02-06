""" A civil engineer classifies a triangle design as equilateral, isosceles, or scalene. Implement a solution to
check the triangle type based on its sides."""
side_1=int(input("Enter the length of the 1st side:"))
side_2=int(input("Enter the length of the 2nd side:"))
side_3=int(input("enter the length of the third side:"))
if side_1==side_2 and side_2==side_3 and side_3==side_1 :
    print("It is an equilateral triangle")
elif side_1!=side_2 and side_2!=side_3 and side_3!=side_1 :
    print("It is a scelene triangle")
else:
    print("It is an isosceles triangle")
