#WAP to create a pattern of hollow square the output should be in the form of a list 
def generate_hollow_square(n):
    lst1=[]
    for i in range(0,n):
        str1=""
        for j in range(0,n):
            if(i==0) or (i==n-1):
                str1+="*"
            else:
                if j==0 or j==n-1 :
                    str1+="*"
                else:
                    str1+=" "
        lst1.append(str1)
    return lst1
n=int(input("Enter the no. of rows or columns:"))
print( generate_hollow_square(n))
