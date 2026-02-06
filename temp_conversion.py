"""A weather app developer needs to provide both Celsius and Fahrenheit readings. Implement a solution to
convert Fahrenheit temperature into Centigrade or vice versa."""
print("Choose:\n1.to covert from celius to fahrenheit\n2.to convert from fahrenhiet to celcius")
choice=int(input("\nEnter your choice:"))
if(choice>2 or choice<1):
    print("\nInvalid choice")
else:
    temp=int(input("\nEnter the temprature:"))
    if(choice==1):
        temp_1=(1.8*temp)+32
        print("\nThe temprature in fahrenheit:",temp_1)
    elif(choice==2):
        temp_1=(temp-32)/1.8
        print("\nThe temprature in celcius:",temp_1)
