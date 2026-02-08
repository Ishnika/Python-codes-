#function to chck if the number is a perfect square or not
import math
def is_perfect_square(num):
    if num<0:
        return False 
    else:
        root=int(math.sqrt(num))
        if (root**2)==num :
            return True
        else :
            return False
num=int(input("Enter the number:"))
print(is_perfect_square(num))
