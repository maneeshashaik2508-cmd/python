
# Write a program to print all even numbers between 1 and 50 using a while loop.

num = 1

while (num<=50):
    if(num%2 == 0):
        print(num)
    num=num+1

# Write a program that prints the sum of first n natural numbers. 
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15. 

n = int(input("Enter any number :- "))
sum =0

while (n>=1):
    sum = sum+n 
    n=n-1
print(sum)
print(n)
    

# Write a program to print this pattern using a while loop: 
# * 
# * * 
# * * * 
# * * * *

n=1

while n<=4:
    print("*" " "*n)
    n+=1


# print a name 5 times, but each time with a number in 
# front of it. Write a program using a while loop that prints:

n =1

while n<=5:
    print("MANEESHA SHAIK",n)
    n=n+1

# Write a program to print the multiplication table of any number using a while loop. 

n = int(input("Enter any number :-"))
i = 1

while i<=10:
    print(n ," " "*" " ",i," " "=" " ",n*i)
    i=i+1
      
    