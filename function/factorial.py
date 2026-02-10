#calculate the factorial of a number using a recursive function 
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
fact=factorial(num)
print(fact)
