# Write a program that takes a sentence and prints:
# print Total characters (len()) , Uppercase version , Lowercase version 

str = input("write any sentence :- ")
print("The input :-", str,"Total characters in the input", len(str))
print("The captilized input :- ",str.capitalize())
print("The titled input :- ",str.title())
print("The uppercase of input :- ",str.upper())


# Write a Python program that takes any word or sentence as input and 
# prints the first character, The last character, The total number of characters.
  
word = input("Write an word :-")

print("The Input :- " , word)
print("The First character :-" , word[ :1])
print("The last character :-",word[-1: ])




