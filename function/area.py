#area of a rectangle
def area_of_rectangle(length, breadth):
    area=float(length*breadth)
    return area
l=int(input("Enter the length og the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
print(area_of_rectangle(l,b))
