"""A shopkeeper wants to calculate the total bill amount after applying a 20% 
discount on the purchase.Implement a solution to accept item no., quantity, and unit 
price. Compute the amount and apply 20% discount."""
it_no=int(input("Enter the item number:"))
quan=int(input("Enter the quantity:"))
unit_pr=int(input("Enter the price of one unit:"))
dis=0.80*(quan*unit_pr)
print("The total amount after discount is:",dis)
