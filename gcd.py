#calculate the greatest common divisor of two numbers
def gcd(n, m):
    div=1
    if n<m:
        num=n
    else:
        num=m
    for i in range (2,num+1):
        if(n%i==0 and m%i==0):
            if i>div:
                div=i 
            else:
                continue 
    return div 
n=int(input("Enter the 1st number:"))
m=int(input("Enter the 2nd number:"))  
print(gcd(n, m))
        
