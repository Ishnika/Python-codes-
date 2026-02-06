"""A wholesale supplier applies 10% discount if the order > 1000 items. Implement a solution to compute total
expenses and apply a discount accordingly."""
no=int(input("Enter the number of items:"))
price=int(input("Enter the price of the item:"))
if(no>1000):
    tot=(no*price)*0.90
else:
    tot=no*price
print("Total amount to be paid is:",tot)
