"""A student wants to swap the values of two variables for practising coding basics.
Implement a solution to swap two numbers using different techniques."""
print("""Choose:\n1.using a third variable\n2.using addition subtraction\n3.using 
multipication and division""")
num_1=int(input("Enter the 1st number:"))
num_2=int(input("Enter the 2nd number:"))
choice=int(input("Enter your choice:"))
if(choice==1):
    swap=num_1
    num_1=num_2
    num_2=swap
elif(choice==2):
    num_1=num_1+num_2
    num_2=num_1-num_2
    num_1=num_1-num_2
elif(choice==3):
    if(num_1==0 or num_2==0):
        print("This method can not be used")
    else:
        num_1=num_1*num_2
        num_2=num_1//num_2
        num_1=num_1//num_2
else:
    print("Invalid choice!")
print("value of numbers is: \nnum_1=",num_1,"\nnum_2=",num_2)
    
