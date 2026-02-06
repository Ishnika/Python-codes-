""" A data analytics tool finds the maximum sales figure from multiple entries.
Implement a solution to accept ‘n’ numbers and display the largest."""
n=int(input("Enter the total no. of values you want to enter:"))
lst=[]
while(n>0):
    num=int(input("Enter the number:"))
    lst.append(num)
    n-=1
max1=max(lst)
print("The largest of all the numbers is:",max1)
