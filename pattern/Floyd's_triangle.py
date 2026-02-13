#Floyd's triangle
def generate_floyds_triangle(n):
    lst1=[]
    count=1
    for i in range(1,n+1):
        str1=""
        for j in range(0,i):
            str1+=str(count)
            if j+1!=i:
                str1+=" "
            count+=1 
        lst1.append(str1)
    return lst1
n=int(input("Enter the number of rows you want:"))
print(generate_floyds_triangle(n))
