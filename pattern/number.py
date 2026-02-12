#generate a pattern of right triangle with the number of row as the value in it 
def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    lst1=[]
    for i in range(1,n+1):
        str1=""
        for j in range(0,i):
            str1+=str(i);
        lst1.append(str1)
    return lst1
