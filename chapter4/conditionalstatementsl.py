#conditional statements

marks = 95

if(marks >= 90):                 # In case of multiple conditions then we use if & elif
    print("Your grade is A")
elif(marks >=80):
    print("Your grade is B")




age = 22
 
if(age > 18):                    # In case of one condition we use if & else 
    print("you are eligible to vote")
else:
    print("you are not eligibile to vote")


# write a python programe that takes a number as input and prints :
# "positive" if number>0
# "zero"  if number == 0
# "negative" if number < 0

num = int(input("Enter a number :- "))

if(num > 0):
    print("POSITIVE")
elif(num == 0):
    print("ZERO")
else:
    print("NEGATIVE")


