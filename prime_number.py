"""A cybersecurity tool verifies prime numbers used in encryption keys. Implement a solution to accept a
number and check whether it is prime."""
num=int(input("Enter the number:"))
if num==0:
    print("neither prime nor composite")
elif num==1:
    print("It is a unique number")
elif num==2:
    print("It is prime")
else:
    for i in range(2,num//2+1):
        if num%i==0:
            flag=0
            break
        else:
            flag=1
    if(flag==0):
        print("The number is composite")
    else:
        print("The number is prime")   
