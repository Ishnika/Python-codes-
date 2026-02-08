#check if the given number is even or not 
def is_even(n):
    if n%2==0 :
        return True 
    else :
        return False 
n=int(input("Enter the number:"))
print(is_even(n))
