"""A text editor auto-detects whether an input letter is a vowel, a consonant or a number. Implement a
solution to classify the symbol."""
val=input("Enter the value:")
if(val.isdigit()):
    print("It is a digit")
else:
    if(val in ["a","e","i","o","u"]):
        print("It is a vowel")
    else:
        print("It is a consonant")
