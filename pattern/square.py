#write a code to generate a pattern n*n (forming a square)
def generate_square(n):
    lst1=[]
    for i in range(0,n):
        str1=""
        for j in range(0,n):
            str1+="*"
        lst1.append(str1)
    return lst1
n=int(input("Enter the number of rows and column:"))
print(generate_square(n))
