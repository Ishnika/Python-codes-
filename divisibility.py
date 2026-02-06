"""A monitoring system generates a sequence of numeric event IDs from 1 to N.
To make logs easier to analyse, the system applies tags to certain events based on predefined rules:
• Events whose ID is divisible by 3 are tagged as “Buzz”
• Events whose ID is divisible by 5 are tagged as “Fuzz”
• Events divisible by both 3 and 5 receive both tags"""
id=int(input("Enter the ID :"))
if(id%3==0 and id%5==0):
    print("BUZZ FUZZ")
elif(id%3==0):
    print("BUZZ")
elif(id%5==0):
    print("FUZZ")
else:
    print("NO TAG ASSOCIATED")
