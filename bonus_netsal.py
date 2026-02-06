"""An HR system needs to calculate employees’ net salaries, including a fixed 12% bonus for each worker.
Implement a solution to accept the number of employees and their basic salary. Compute bonus, net salary, and
display results."""
num=int(input("Enter the number of employies:"))
sum=0
count=0
for i in range(0,num):
    sal=int(input("Enter the salary of the emplyee:"))
    bonus=0.12*sal
    print("The bonus of the employee is:",bonus)
    sum+=sal
    count+=1
net=sal/count
print("The net slary of the emplies is:",net)
    
    
