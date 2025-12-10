# Instance Attribute 

class Student:
    college = "XYZ Institute" 


    def __init__(self, name, course):
        self.name = name
        self.course = course

  
s1 = Student("Saumya", "Btech") 
print("student 1 name :-",s1.name)
print("Student 1 course :-",s1.course)


s2 = Student("Aman","B.com")
print("student 2 name :-",s2.name)
print("student 2 course :-", s2.course)





