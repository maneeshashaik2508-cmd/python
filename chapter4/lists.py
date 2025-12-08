# lists in python

food = ["biryani", "panipuri", "waffle", "ice cream", "mango" , 7]

print(len(food))

#indexing

print("First value of list :-" , food[0])
print(food[2])


# Methods in list

food[1]= "momos"          #lists are mutable
print(food)


# SLICING

print(food[1:5])

marks = [100 ,95 ,99, 20, 18, 9]

print(max(marks))
print(min(marks))



marks.append(91)      # add new value into the list

print(marks)

marks.sort()         # gives accending order in list
print(marks)
 
marks.pop(1)         # remove any value by index number
print(marks)

marks.remove(100)   # remove any value
print(marks)

marks.insert(1,100)  #add a value by particular index position
print(marks)


# write a programe that takes 3 food from the user and 
# store in list and 
# print list and its length

# FIRST METHOD

food1 = input("Enter 1st food items :- ")
food2 = input("Enter 2nd food items :- ")
food3 = input("Enter 3rd food items :- ")

foodlist = [ food1 , food2 , food3]

print(foodlist)
print(len(foodlist))

# SECOND METHOD

food1 = input("Enter 1st food items :- ")
food2 = input("Enter 2nd food items :- ")
food3 = input("Enter 3rd food items :- ")

foodlist = []

foodlist.append(food1)
foodlist.append(food2)
foodlist.append(food3)

print(foodlist)
print(len(foodlist))


