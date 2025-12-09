# RECURSIVE FUNCTION

def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1) 
print(factorial(5))


def fibonacci(n): 
    if n <= 1: 
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 
 
for i in range(6): 
    print(fibonacci(i), end=" ") 

# 1. Write a recursive function that prints numbers from 1 to N. 

def printnum(n):
    if n <=1:
        return 1
    print(printnum(n-1))
    return n
    
result = printnum(5)
print(result)


# 2. Write a recursive function to calculate the factorial of a number.

def facto(n):
    if n <=0:
        return 1
    return n * facto(n-1)

result = facto(6)
print(result)

   
# 3. Write a recursive function to print the Fibonacci series up to N terms.
# The next term is found by adding the previous two terms.

def fibonacci_series(n):
    if n <= 0 :
        return 1
    return fibonacci_series(n-1) + fibonacci_series(n-2)

for i in range(9):
    print(fibonacci_series(i), end=" ")

def factorial_iterative(n): 
     result = 1 
     for i in range(1, n + 1): 
         result *= i 
     return result 
print(factorial_iterative(5)) 

# 4. Write both a recursive and iterative function to find factorial - compare results.
 
def factorial(n): 
    if n == 0:
        return 1
    return n * factorial(n - 1) 
print(factorial(5))


def factorial_iterative(n): 
     result = 1 
     for i in range(1, n + 1): 
         result *= i 
     return result 
print(factorial_iterative(5)) 
