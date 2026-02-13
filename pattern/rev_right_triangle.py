#write a code to create a reversed right angled triangle and add each row to a list 
def generate_right_angled_triangle(n):
    lst1=[]
    for i in range(1,n+1):
        str1=""
        for j in range(0,n):
            if j>=n-i:
                str1+="*"
            else:
                str1+=" "
        lst1.append(str1)
    return(lst1)
n=int(input("Enter the number of rows:"))
print(generate_right_angled_triangle(n))
