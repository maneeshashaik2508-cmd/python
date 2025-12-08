
# maneesha wants to print her username five times in uppercase letters.

name ="maneesha"

for i in range(1,6,1):
    print(name.upper())

# You are given a list of Saumya’s favorite foods. Write a Python program to print each food item using a for loop.

favfood=["cake", "panipuri", "dosa", "biryani", "idly", "pongal"]

for i in favfood :
    print(i)

# Saumya has created a tuple of countries she has already traveled to. Write a 
# Python program to print each country using a for loop. 


countries_traveled = ("Malaysia", "Vietnam", "Switzerland", "Italy", "Bhutan") 

for i in countries_traveled:
    print(i)


# Write a program that prints numbers 1 to 10, but skips the number 7 using the continue statement.

for i in range(1, 11, 1):
    if i == 7:
        continue
    print(i)


#Print all numbers between 1 and 50 except multiples of 5.

for i in range(1, 51, 1):
    if i % 5 == 0:
        continue
    print(i)

# Create a program that asks the user for 5 favorite foods and prints them one by one. 

food1 = input("Enter your 1st fav food :-")
food2 = input("Enter your 2nd fav food :-")
food3 = input("Enter your 3rd fav food :-")
food4 = input("Enter your 4th fav food :-")
food5 = input("Enter your 5th fav food :-")

food = [food1, food2, food3, food4, food5]

for i in food:
    print(i)

