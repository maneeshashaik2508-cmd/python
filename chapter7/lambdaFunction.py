# LAMBDA FUNCTIONS

# Syntax
# lambda arguments : expression

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# lambda function uses nested if-else logic to classify numbers as Positive, Negative or Zero.

num = lambda n : "positive " if n> 0 else "negitive" if  n < 0 else "zero"
print(num(1))
print(num(-5))
print(num(0))

# lambda checks divisibility by 2 and returns "Even" or "Odd" accordingly.

num = lambda n : "Even" if n % 2 == 0 else "odd" 
print(num(15))
print(num(20))

# creates a list of lambda functions, each multiplying its input by 10 and then executes them one by one.

num = [lambda n = x : n*10 for x in range(1,11) ]
for i in num:
    print(i())

# lambda calculates both sum and product of two numbers and returns them as a tuple.

num = lambda m,n :(m + n,m*n)
Result = num(5,5)
print(Result)

# lambda is used as a filtering condition to keep only even numbers from the list.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter(lambda x : x % 2 == 0,n)
print(list(even))

# doubles each element of the list using a lambda function and returns a new list.

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double = map(lambda x : x*2,n)
print(list(double))

# lambda multiplies two numbers at a time and reduce() applies this across the whole list to calculate the product.


from functools import reduce

n = [1,2,3,4,5]
product = reduce(lambda x,y : x*y,n)
print(product)

from functools import reduce
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
