"""A learning application analyzes numbers for mathematical properties.
Design a solution to check whether a given number is a Perfect number or an Armstrong number."""
import math
num=int(input("Enter the number:"))
count=0
flag=0
num_copy=num
while(num_copy>0):
    count+=1
    num_copy//=10
num_copy=num
num_arm=0
while(num_copy>0):
    rem=num_copy%10
    num_arm+=math.pow(rem,count)
    num_copy//=10
num_p=0
for i in range(1,num):
    if(num%i==0):
        num_p+=i
if(num_arm==num and num_p==num):
    print("The number is both perfect and an armstrong number")
elif(num_arm==num):
    print("The number is an armstrong number")
elif(num_p==num):
    print("The number is a perfect number")
else:
    print("The number is neither perfect not armstrong")
    
