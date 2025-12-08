str1 ="maneesha shaik"

print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.find("e"))           
print(str1.replace(" ","_"))
print(str1.count("e"))          #count the occurence


#writhe a programe that takes a sentence as input , 
#converts it to uppercase , replace all spaces with underscores "_" 
# and print the new string

str = input("Write any sentence :- ")
print("The old string is",str)
str1 = str.upper()

print("The new string is",str1.replace(" ","_"))

#escape sequence

print("hello world")
print("hello\nworld")   #to print in next line
print("hello\tworld")   #to print with extra space



#Formatted strings (f-strings)
# f-Strings make it easy to include variables inside strings.

name = "maneesha shaik"
age = 21


print(f"My name is {name.upper()} and I am {age} year old.")