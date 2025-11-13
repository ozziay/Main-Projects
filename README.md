# WHY WOULD YOU USE GenAI SYSTEMS TO GENERATE EVERYTHING FROM START TO FINISH??? HIGHLY UNACCEPTEBLE.
# Please write your & ID?
# BMW Vehicle Project 

This project is a simple Python application that models BMW vehicles using object-oriented programming (OOP). It demonstrates inheritance with a main class (`BMW`) and three child classes: `BMWCar`, `BMWMotorcycle`, and `BMWSUV`.

### Features

- Each vehicle has basic attributes:
  - Model
  - Horsepower (HP)
  - Torque (Nm)
  - 0-100 km/h acceleration (seconds)
  - Top Speed (km/h)

- Child classes have **unique attributes**:
  - **BMWCar**: `car_type` (Sedan/Coupe) and `fuel_type` (Petrol/Diesel)
  - **BMWMotorcycle**: `bike_type` (Sport/Adventure) and `displacement` (cc)
  - **BMWSUV**: `drive_type` (FWD/RWD/AWD) and `ground_clearance` (mm)

- The `show_info()` method prints all relevant information for each vehicle, with a separator line for clarity.

### Example Vehicles

- BMW M4 Competition 2025
- BMW 320d 2025
- BMW S1000RR 2025
- BMW R1300GS 2025
- BMW X6 M60i 2025
- BMW X1 2025


### POLYMORPHISM
BMW Polymorphism Example

This Python program demonstrates the concept of polymorphism using three different BMW vehicle types:

BMWCar

BMWMotorcycle

BMWSUV

Each class defines the same method, show_info(), but with different implementations.
The bmw_info() function takes any object that has a show_info() method — regardless of its class — and calls it.

This shows polymorphism:

The same function behaves differently depending on the object that is passed to it.

Example output:

This is a BMW car. It is fast and comfortable.

This is a BMW motorcycle. It is light and agile.

This is a BMW SUV. It is powerful and spacious.



### What Is Encapsulation?

Encapsulation is one of the four main principles of Object-Oriented Programming (OOP), alongside inheritance, polymorphism, and abstraction.
It means hiding the internal data of a class and allowing access only through specific methods.

By doing this, we protect the object’s internal state from being changed accidentally or incorrectly.
Instead of accessing attributes directly, we use getters and setters to control how data is read and modified.
This makes the code safer, easier to maintain, and more predictable.

#### Our BMW Example

In this example, we used a class called BMWCar to demonstrate encapsulation.
The class contains two private attributes:

__model → stores the car’s model name.

__horsepower → stores the engine power value.

These attributes are private, meaning they can’t be accessed directly from outside the class.
To interact with them, we define getter and setter methods:

get_model() and get_horsepower() let us safely read the data.

set_horsepower() allows controlled modification, with a validation check to ensure horsepower is positive.

This structure ensures that any updates to the car’s data happen through proper logic — not random direct access.

### Summary

Encapsulation:

Protects sensitive data from outside interference.

Promotes organized and secure class design.

Ensures changes happen only through defined methods.

In our BMW example, this concept helps simulate how real-world systems protect important data — just like a BMW hides its complex inner mechanics but lets you interact safely through a dashboard.


