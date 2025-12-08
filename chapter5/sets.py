# SETS IN PYTHON

# sets donot entertain duplicasy
food = {"biryani", "panipuri", "paneer", "iceCream", "biryani"}

print(type(food))
print(food)

empty = set()            # creating empty set   
print(type(empty))

food.add("GulabJamun") 
print(food)

food.remove("biryani")
print(food)


# you are given a list of programming languages:
# ["python", "java", "C++", "python", "java", "C"]
# Convert it into a set and print how many unique languages maneesha knows.

programmingList = ["python", "java", "C++", "python", "java", "C"]

# convert list into set

programmingSet = set(programmingList)
print(type(programmingList))
print(type(programmingSet))
print(programmingSet)

print("maneesha knows these many languages :-",len(programmingSet) , "languages")