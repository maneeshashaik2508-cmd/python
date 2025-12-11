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



# ARBITARY ARGUMENTS

def num(*numbers):
    """Sums an arbitrary number of positional arguments."""
    return (f"Arguments packed into a tuple: {numbers}")


# Call the function with different numbers of arguments
numtuple1 = num(10, 20)                   # Output:- Arguments packed into a tuple: (10, 20)
numtuple2 = num(1, 5, 10, 15, 20)         # Output:- Arguments packed into a tuple: (1, 5, 10, 15, 20)

print(numtuple1)
print(numtuple2)


def create_profile(name, **details):
    """Creates a profile with a required name and arbitrary details."""
    profile = {'name': name}
    profile.update(details)
    return profile

# Call the function with different keyword arguments
user1 = create_profile("Maneesha", age=21, city="New York")
# user1: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(user1)

user2 = create_profile("Abeeda", occupation="Engineer", phone="555-1234", country="USA")
# user2: {'name': 'Bob', 'occupation': 'Engineer', 'phone': '555-1234', 'country': 'USA'}
print(user2)

# Write a Python function called calculate_average :
# that can accept any number of scores (integers or floats) as input. 
# The function should return the arithmetic mean (average) of those scores.

def average(*num):
    if not num:
        return 0
    
    total = sum(num)
    length = len(num)
    return total/length

result = average(20,10,20,30)
print(result)


def my_flexible_function(fixed_arg, *args, **kwargs):
    
    # 1. Fixed Argument
    print(f"Required Argument: {fixed_arg}")
    
    # 2. Arbitrary Positional Arguments (*args)
    print(f"Positional Arguments (Tuple): {args}")
    
    # 3. Arbitrary Keyword Arguments (**kwargs)
    print(f"Keyword Arguments (Dict): {kwargs}")

# --- Example Call ---
my_flexible_function(
    "Hello",            # fixed_arg
    10, 20, 30,         # *args
    name="Alice",       # **kwargs
    location="Mars"     # **kwargs
)
