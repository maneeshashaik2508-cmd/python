#Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.
#Fahrenheit = (C × 9/5) + 32  and  Kelvin = C + 273.15 

celsius = float(input("Enter temperature in Celsius :- "))
print("Temperature in Celsius =" , celsius)

Fahrenheit = (celsius*9/5) + 32
print("Temperature in Fahrenheit =" , Fahrenheit)

kelvin = celsius + 273.15
print("Temperature in kelvin =" , kelvin)


#2⃣ Bill Split Calculator 
#Write a program that takes total bill amount and number of friends as input. 
#Calculate how much each person will pay. 
#Also print the data type of each variable used. 

Totalbill = float(input("Enter total bill amount here :- "))
print("Total bill amount is =" , Totalbill , "and It's datatype is" , type(Totalbill))

Friends = int(input("Enter number of friends :- " ))
print("Number of friends are" , Friends , "and It's datatype is" ,type(Friends))

Eachwillpay = Totalbill/Friends
print("Each friend will pay ", Eachwillpay, "rupees and It's datatype is"  , type(Eachwillpay))

