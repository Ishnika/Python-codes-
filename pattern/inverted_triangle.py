#WAP to create an inverted triangle and return it in the form of a list
def generate_inverted_triangle(n):
    lst1=[]
    for i in range(n,0,-1):
        str1=""
        for j in range(0,i):
            str1+="*"
        lst1.append(str1)
    return lst1
n=int(input("Enter the number of rows:"))
print(generate_inverted_triangle(n))
