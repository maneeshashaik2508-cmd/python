# OOPS IN PYTHON
# CLASSES AND OBJECTS

# class creation
class vehicle:
    color ="black"                  # attributes
    petrolOrDiesel ="petrol"        # attributes
    mileage="10kmph"                # attributes

# object creation
car = vehicle() 
print(car.color)  

bike = vehicle()
print(bike.petrolOrDiesel)

aeroplane = vehicle()
print(aeroplane.mileage)
print(aeroplane.color)

# we created one class and 3 objects of thet class

# Create a class Car with attribute brand = "Scorpio".

class car:
    brand = "Scorpio"

object = car()
print("Brand name",car.brand)

# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects with different values.

class laptop:
    brand = "default"
    Ram = "default 8GB"
    price ="default 1 lakh"

laptop1 = laptop()
laptop1.brand="Macbook"
laptop1.Ram="16GB"
print("laptop1 brand :-" ,laptop1.brand)
print("laptop1 price :-" ,laptop1.price)
print("laptop1 ram :-" ,laptop1.Ram)

laptop2 = laptop()
laptop2.brand="lenovo"
print("laptop2 brand :-",laptop2.brand)
