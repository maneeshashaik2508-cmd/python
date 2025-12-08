# RETURN STATEMENTS
# The return statement is used to send a value back from a function. 
# After return, the function stops execution. 

def multiply(a=10, b=10):
    return a*b

print(multiply(2,2))
result=multiply()
print(result)

result=multiply(5,2)
print(result)

# Write a function square(num) that returns the square of a number.

def squre(num):
    return num**2

print(squre(5))
result= squre(2)
print(result)

# Write a function that takes a string and returns the count of vowels and consonants separately.

def func(userInput):
    vowel= "aeiouAEIOU"

    countVowel =0
    countconsonants =0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowel:
                countVowel+=1
            else:
                countconsonants+=1
        
    return countVowel,countconsonants


result = func("maneesha bee")
print(result)

vowels , consonants = func("abeeda")
print(vowels,consonants)


# Write a function that takes a <class list> of integers and returns the count of even numbers, odd numbers and zeros separately.
def evenOdd(userInput):
    countEven = 0
    countOdd = 0
    countZero = 0

    for num in userInput:
        # Check if the input is an integer before proceeding
        if isinstance(num, int):
            if num == 0:
                countZero += 1
            elif num % 2 == 0:
                countEven += 1
            else:
                countOdd += 1

    return countEven, countOdd, countZero

# Example usage with a list of integers
result = evenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(result)
   
numbers =evenOdd([1,2,3,5,5,8,2,0,0,0,2])
print(numbers)

# Define a function convert_to_upper(word) that returns the uppercase version of the string. 

def convert_to_upper(uesrInput):
    return uesrInput.upper()

result= convert_to_upper("maneesha")
print(result)

print(convert_to_upper("maneesha abeeda"))


# Create a function full_name(fname, lname) that returns the full name joined with a space.

def full_name(fname, lname):
    return f"{fname} {lname}"

result = full_name("maneesha","shaik")
print(result)

print(convert_to_upper(full_name("maneesha","shaik")))

