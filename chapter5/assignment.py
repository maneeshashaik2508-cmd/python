# Create a dictionary storing meanings of 3 English words.

familymembers ={
    "father" : "Kalisha",
    "mother" : "masthan bee",
    "kids"   : "2 daughters"
}

print(familymembers)


#  Create a set of numbers and show union and intersection with another set.

set1 = {1, 2, 3, 5, "manisha", "abeeda" , "manisha" }
set2 = {1, 3, 4, 5, "maneesha" , "abeeda"}

print(set1)
print(set2)
print(set1.intersection(set2))
print(set2.intersection(set1))
print(set1.union(set2))
print(set2.union(set1))


# Try to add both integer 9 and float 9.0 to a set and observe what happens. 
# (Hint: You can convert one into a string to make both unique.) 

set = {1, 2, 3, 3.0, 4, 5, 9,}
set.add(9.0)
set.add("9.0")
print(set)