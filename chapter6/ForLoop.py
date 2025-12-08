# FOR LOOP IN PYTHON

foodList = ["cake", "mango", "pizza"]

for i in foodList:
    print(i)


nameTuple = ("mani", "abhi", "lucky", "raha")

for i in nameTuple:
    print(i)

#range (start, stop, step)

for i in range(1, 8, 1):
    print(i)


for i in range(2, 20, 2):
    print(i)


# Write a program using for and range() to print all even numbers between 1 and 20. 
for i in range(2, 21, 2):
    print(i)


# Write a program to print numbers from 1 to 50, but print "maneesha" 
# instead of numbers that are multiples of 5.
for i in range(1, 51, 1):
    if i % 5 == 0:
        print("MANEESHA")
    else:
        print(i)


# Write a program to print the square of each number from 1 to 10 using a for loop. 
for i in range(1, 11, 1):
    print(i**2)


# Write a program that prints the multiplication table of any number entered by the user using a for loop.

num = int(input("Enter any number :- "))

for i in range(1, 11, 1):
    print(num, " ""*", i, " " "=",num*i)

# Write a program that prints all numbers from 100 to 1 using for and range(). 

for i in range(100,0,-1):
    print(i)

