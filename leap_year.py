"""A calendar app calculates whether February has 29 days. Implement a solution to check if a year is a
leap year or not."""
year=int(input("Enter the year:"))
if(year%4==0):
    print("It is a leap year")
else:
    print("It is not a leap year")
