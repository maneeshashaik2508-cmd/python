# TUPLES IN PYTHON

myTuple = (78, 90, 75)
studentTuple = ("mani", "abhi", "mahi" , "abhi")

print(studentTuple[1])

# how to create empty tuples

emptyTuple = ()
singleTuple = (1,)           #HAVE TO GIVE A COMA AFTER VALUE IN SINGLETUPLE , OTHER WISE SYSTEM TAKES IT AS VALUE'S DATATYPE
singleTuple1 = ("MANI",)


print(type(singleTuple))
print(type(singleTuple1))
print(type(emptyTuple))
print(type(studentTuple))

print(studentTuple.index("mani"))
print(studentTuple.count("abhi"))

# Create a tuple of your favorite 5 fruits.
# print the total number of fruits and index of one selected fruit.

fruits = ("apple", "mango", "cherry", "pineapple", "watermelon")

print(fruits)
print(len(fruits))
print(fruits.index("pineapple"))
