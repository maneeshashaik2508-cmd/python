# Ask the user for their 3 favorite movies and store them in a list. 

movie1 = input("Enter your 1st favorite movie :-")
movie2 = input("Enter your 2nd favorite movie :-")
movie3 = input("Enter your 3rd favorite movie :-")

movies = []

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies , "its datatype is ",type(movies))

#Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and 
#lowest marks using max() and min(). 

marks = (87, 64, 33, 95, 76)

print(max(marks))
print(min(marks))



#  Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks = 34

if(marks >= 95):
    print("your grade is A+")
elif(marks >= 90):
    print("your grade is A")
elif(marks >= 80):
    print("your grade is B")
elif(marks >= 70):
    print("your grade is C")
elif(marks >=35):
    print("your grade is D")
else:
    print("your are faild")

