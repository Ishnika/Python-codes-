"""Develop a menu-driven calculator program to perform basic arithmetic operations.
The program should continue executing based on the user's choice and display the result of each operation."""
print("CHOOSE:\n1.for addition \n2. for subtraction \n3.for multiplication \n 4. for division")
choice=int(input("Enter your choice:"))
if choice<1 or choice>4:
    print("INVALID CHOICE!")
else:
    num_1=int(input("Enter the 1st number:"))
    num_2=int(input("Enter the 2nd number:"))
    if choice==1:
        add=num_1+num_2
        print("The sum of the numbers is:",add)
    elif choice==2:
        if(num_1>num_2):
            sub=num_1-num_2
            print("The difference of the numbers is:",sub)
        else:
            sub=num_2-num_1
            print("The difference of the numbers is:",sub)
    elif choice==3:
        mul=num_1*num_2
        print("The product of the numbers is:",mul)
    else:
        if(num_2==0):
            print("The denominator can't be zero")
        else:
            d=num_1/num_2
            print("The answer after division is:",d)
