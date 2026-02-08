#convert a binary value to decimal value 
def binary_to_decimal(binary_str):
    length=len(binary_str)
    i=0
    sum=0
    num=int(binary_str)
    while(length>0):
        rem=num%10
        sum+=rem*(2**i)
        num//=10
        i+=1
        length-=1
    return sum
binary_str=input("Enter the binary value:")
print(binary_to_decimal(binary_str))
