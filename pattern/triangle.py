#WAP to create a pattern of triangle with a star and return a list of the pattern
def generate_triangle(n):
    lst1=[]
    for i in range(1,n+1):
        str1=""
        for j in range(0,i):
            str1+="*"
        lst1.append(str1)
    return lst1
n=int(input("Enter the no. of rows:"))
print(generate_triangle(n))
