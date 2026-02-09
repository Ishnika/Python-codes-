#WAP to create a function to convert farhenheit to celcius and vece versa 
def convert_temp(temp,unit):
    if unit=="c" or unit=="C":
        temp_1=(9*temp/5)+32
        return temp_1
    elif unit =="f" or unit=="F":
        temp_1=(temp-32)*5/9
        return temp_1
    else:
        return None 
temp=int(input("Enter the temprature:"))
unit=input("Enter the unit of the temprature:")
print(convert_temp(temp,unit))
