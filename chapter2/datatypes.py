food = "biryani"
age = 22
name ="maneesha"
height =143.5

print(type(food))     #string
print(type(age))      #integer
print(type(name))     #string
print(type(height))   #float

#programe to take age as input and print value entered and its datatype

age = int(input("Enter your age :-"))
print("value Entered is" , age , "as age")

print("Age datatype is" ,type(age))

#input two numbers and print sum

input1 = int(input("enter first number :- "))     #input() takes user input as a string , 
input2 = int(input("enter second number :- "))

sum = input1 + input2

print("sum of two values is" ,sum)


# TYPE CONVERSION
#implicit 

x = 5 
y = 2.5
z = x+y

print(z)
print(type(z))

#explicit ; 
# take num as input convert to float and print both original and converted value with data types

num = int(input("Give some value :- "))
print("original value is" , num , "and data type is" ,type(num))

convertedvalue = float(num)

print("converted value is", convertedvalue , "and converted datatype is" ,type(convertedvalue))



