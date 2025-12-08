# Take diamiter as input and calculate the area of a circle
# Area of a circle = πr² or π(d/2)² ; (for pi symbol hold alt + 227 , for squre hold alt + 0178)
#π = 3.14

diameter = int(input("Give any value as diameter:"))
radius = diameter/2

Area = 3.14 * (radius**2)

print("radius of circle is" , radius )
print("Area of circle is" , Area )


#concepts we use :-
# 1)type casting : diameter is a string by putting int ., it becomes type int,
#  2)for squring we have to give 2 astrix symbols (**) ,