#WAP to create a rectangle of n rows and m columns make sure tha the output should be the the form of a list
def generate_rectangle(n, m):
    lst1=[]
    for i in range(0,n):
        str1=""
        for j in range(0,m):
            str1+="*"
        lst1.append(str1)
    return lst1
n=int(input("Enter the number of rows:"))
m=int(input("Enter the number of columns:"))
print(generate_rectangle(n, m))
