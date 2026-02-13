# Function to calculate the value of y using the slope-intercept form of a line.
def calculate_y(slope, intercept, x):
    y=float(slope*x+intercept)
    return y
s=int(input("Enter the slpoe:"))
i=int(input("ENter the intercept:"))
x=int(input("Enter value of x:"))
print(calculate_y(s, i, x))
