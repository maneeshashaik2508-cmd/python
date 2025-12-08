# DICTIONARY IN PYTHON 

student = {
    "name" : "maneesha",
    "age" : 22,
    "city" : "ongole",
    "roll number" : 43 ,
    "name" : "abeeda"
}

print(type(student))           # <class 'dict'>
print(student["name"])         # if we give dupilicate keys system will takes the last occurrence
print(student)
print(student["city"])

student["city"] = "Hyderabad"        # updating the dict's values
print(student)

student["favSubject"] = "maths"        # to add new key
print(student)

student.pop("favSubject")
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))



# create a dictinary named marks to store marks of 3 subjects.
# add the subjects one by one and print the final dictionary.

marks = {}

marks["Maths"] = 99
marks["Chemistry"] = 98
marks["Physics"] = 91

print(marks)

