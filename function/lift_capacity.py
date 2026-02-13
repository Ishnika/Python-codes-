#Function to calculate the number of rounds the lift needs to cover.
def calculate_lift_rounds(n, capacity):
    if n%capacity==0:
        return n//capacity
    else:
        return (n//capacity)+1
n=int(input("Enter the number of people:"))
cap=int(input("Entr the capacity of the lift:"))
print(calculate_lift_rounds(n, cap))
