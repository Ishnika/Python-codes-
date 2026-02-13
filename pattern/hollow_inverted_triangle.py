"""Function to return a hollow inverted right-angled triangle of '*' of side n as a 
list of strings."""
def generate_hollow_inverted_right_angled_triangle(n):
    lst1=[]
    for i in range(n,0,-1):
        str1=""
        for j in range(0,i):
            if i==n or i==1 :
                str1+="*"
            else :
                if j==0 or j==i-1 :
                    str1+="*"
                else :
                    str1+=" "
        lst1.append(str1)
    return lst1
n=int(input("Enter the number of rows:"))
print(generate_hollow_inverted_right_angled_triangle(n):)
