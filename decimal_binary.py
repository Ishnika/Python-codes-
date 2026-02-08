#convert a decimal number to its binary form 
def int_to_binary(n):
    if n<0:
        num=-n
    else:
        num=n
    sum=0
    while(num>0):
        rem=num%2
        sum=sum*10+rem
        num//=2
    sum_2=0
    while(sum>0):
        rem1=sum%10
        sum_2=sum_2*10+rem1
        sum//=10
    if n<0 :
        return(str(-sum_2))
    else:
        return str(sum_2)
n=int(input("Enter the number:"))
print(int_to_binary(n))
    
    
