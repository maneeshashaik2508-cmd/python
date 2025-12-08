
# Indexing of a string   {length - 1}
# Each character in a string has its position and its starts from "0"

str = "MANEESHABEE"
str1 = "MANEESHA BEE"

print(str[0])     #M           
print(str[1])     #A
print(str[2])     #N
print(str[3])     #E
print(str[4])     #E
print(str[5])     #S
print(str[6])     #H
print(str[7])     #A
print(str[8])     #B
print(str[9])     #E
print(str[10])    #E
  
print(str1[0])    #M
print(str1[1])    #A
print(str1[2])    #N
print(str1[3])    #E
print(str1[4])    #E
print(str1[5])    #S
print(str1[6])    #H
print(str1[7])    #A
print(str1[8])    #SPACE
print(str1[9])    #B 
print(str1[10])   #E
print(str1[11])   #E


#SLICING 
str = "ManiAbhi"

Mani = str[0:4]
Mani2 = str[ :4]

Abhi = str[4:8]
Abhi2 = str[ :8]

print(Mani)
print(Mani2)
print(Abhi)
print(Abhi2)

#Negitive indexing.
str = "ManiAbhi"

print(str[-8:-4])
print(str[-4:-1])  #output = abh *because last index will be excudes
print(str[-4: ])   #output = abhi   


# write a programe that takes your favorite food name as input and prints :
# the middle 3 characters
# the last 2 characters
 
Food = input("Enter your fav food :- ")
mid = len(Food)//2



print("My favorite food is ",Food)

print("Length of the food is",len(Food))
print("The middle 3 characters are",Food[mid-1:mid+2])
print("The last 2 characters are",Food[-2: ])


