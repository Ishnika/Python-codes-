"""A String-matching tool validates if IDs are palindromes. Implement a solution to check whether a given ID is a palindrome."""
id=int(input("Enter the ID"))
count=0
id_copy=id
while(id_copy>0):
    rem=id_copy%10
    count=(count*10)+rem
    id_copy//=10
if(count==id):
    print("yes it is a pallindrome")
else:
    print("It is not a pallindrome")
