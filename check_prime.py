#check if the number is prime or not
def is_prime(n):
    flag=1
    if n==2 :
        return True 
    else:
        for i in range(2,n//2+1):
            if n%i==0 :
                flag =0 
                break
            else :
                continue
    if flag==0:
        return False 
    else :
        return True 
n=int(input("Enter the number:"))
print(is_prime(n))
