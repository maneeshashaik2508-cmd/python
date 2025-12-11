# Practice Set
# 1. Write a function to calculate the factorial of a number. 
def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1) 
print(factorial(5))
# 2. Write a recursive function to print numbers from 1 to N. 

def printnum(n):
    if n <=1:
        return 1
    print(printnum(n-1))
    return n
    
result = printnum(5)
print(result)
# 3. Write a function that checks if a number is prime. 

def prime(n,d=2):
    if n == 1:
        return False
    if n == d:
        return True
    if n % d == 0:
        return False
    
    return prime(n, d+1)

print(prime(13))
print(prime(3))
print(prime(1))
print(prime(15))
print(prime(7))

# 4. Write a recursive function to find the sum of first N natural numbers.
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
n = int(input("Enter a value :-"))

print(sum(n))


# 5. Write a function greet_user(name) that prints a personalized message for 
# Saumya Singh. 
def greet(name):
    return (f"Hello",{name},"Welcome to the show!")
    

result= greet("saumya singh")
print (result)


# 6. Write a recursive program to print the reverse of a string. 
def print_reverse_recursive(s):
    if len(s) == 0:
        return
    print(s[-1], end='')
    print_reverse_recursive(s[:-1])

my_string = "Python"

print(f"Original string: {my_string}")
print("Reversed string: ", end='')
print_reverse_recursive(my_string)
print() # Prints a final newline for clean output

my_string_2 = "recursion"
print(f"Original string: {my_string_2}")
print("Reversed string: ", end='')
print_reverse_recursive(my_string_2)
print()
