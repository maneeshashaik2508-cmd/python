# FUNCTIONS WITH PARAMETERS 

# Function defining with parameters
def average(a, b):
    averageValue = (a+b)/2
    print(averageValue)


# Function calling with Arguments
average(7,5)
average(51,25)
average(21,33)
average(5,5)


# Function defining with parameters
def average(a=5, b=5):                      # WE CAN GIVE DEFAULT VALUES TO THE PARAMETERS 
    averageValue = (a+b)/2
    print(averageValue)


# Function calling with Arguments
average(7,5)
average(51,25)
average(21,33)

average()                  # FOR THESE KIND OF CALLINGS WE USE DEFAULT VALUES TO THE PARAMETERS

# Write a function show_age(name, age) that prints: "Maneesha is 21 years old."

def show_age(name="Maneesha",age=21):
    print(f"{name} is {age} years old.")

show_age("Maneesha",21)
show_age()
show_age("Abeeda", 17)


#  Create a function add_numbers(a, b) that prints both the sum and difference.

def add_numbers(a, b):
    sum= a+b
    sub= a-b
    print("sum =",sum, "& sub =",sub)

add_numbers(10,5)
add_numbers(5,3)


# Write a function fav_food(food) that prints "Maneesha loves <food>"

def fav_food(food):
    print("Maneesha loves",food)

fav_food("panipuri.")
fav_food("Biryani.")

# Define a function message(text="Keep Learning!") and call it with and without an argument.

def msg(text="Keep learning!"):
    print(text)

msg("Good Luck!")     # OUTPUT :- Good Luck!
msg()                 # OUTPUT :- Keep Learning!

# Create a function login(username, password="1234") that prints the credentials.

def login(username, password =1234):
    print(f"USERNAME :-",username)
    print(F"PASSWORD :-",password)

login("Maneesha")
login("Abeeda", 2531)
