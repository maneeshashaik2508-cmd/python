#arithemetic operators

x = 10
y = 7

print(x + y)   #add
print(x - y)   #sub
print(x*y)     #multiplication
print(x/y)     #division
print(x%y)     #modulus
print(x**y)    #power

#comparision operators

print(x==y)
print(x>=y)
print(x<=y)
print(x<y)
print(x>y)
print(x!=y)     #not equal 

#Logical operators


print(x==y)     #false
print(x>y)     #true
print(x<y)     #false
print(x!=y)     #true

print(x==y and x!=y)   #false nd true    ans = false
print(x==y and x<y)    #false nd false   ans = false
print(x!=y and x>y)    #true nd true     ans = true
print(x>y  and x<y)    #true nd false    ans = false

print(x==y or x<y)    #false nd false   ans = false
print(x!=y or x>y)    #true nd true     ans = true
print(x==y or x!=y)   #false nd true    ans = true
print(x>y  or x<y)    #true nd false    ans = true


# not operator will change the true value into false and false value into true

print(not(x==y and x!=y))   #false nd true    ans = true
print(not(x==y and x<y) )   #false nd false   ans = true
print(not(x!=y and x>y) )   #true nd true     ans =false 
print(not(x>y  and x<y) )   #true nd false    ans = true


print(not(x==y or x<y)  )  #false nd false   ans = true 
print(not(x!=y or x>y)  )  #true nd true     ans = false 
print(not(x==y or x!=y) )  #false nd true    ans = false 
print(not(x>y  or x<y)  )  #true nd false    ans = false 


# Assignment operator

a = 2
b = 3

a = a+6
a+=6

a = a-1
a-=1

a = a*2
a*=2

a = a/2
a/=2