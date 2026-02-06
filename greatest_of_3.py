"""A game compares three players' scores to find who is ahead. Implement a solution to accept three scores
and identify the winner."""
sc_1=int(input("Enter the score of the 1st player:"))
sc_2=int(input("Enter the score of the 2nd player:"))
sc_3=int(input("Enter the score of the 3rd player:"))
if(sc_1>sc_2 and sc_1>sc_3):
    print("The first player is the WINNER")
elif(sc_2>sc_1 and sc_2>sc_3):
    print("The second player is the WINNER")
else:
    print("The third player is the WINNER")
    
    
