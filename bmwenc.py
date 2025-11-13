class BMWCar:
    def __init__(self, model, horsepower):
        self.__model = model          # private attribute
        self.__horsepower = horsepower  # private attribute

    # Getter methods
    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__horsepower

    # Setter methods
    def set_horsepower(self, new_hp):
        if new_hp > 0:
            self.__horsepower = new_hp
        else:
            print("Horsepower must be positive!")

    def show_info(self):
        print(f"Model: {self.__model}")
        print(f"Horsepower: {self.__horsepower} hp")
        print("This is a BMW car. Fast and elegant.\n")


# Using encapsulation
m4 = BMWCar("M4 Competition", 523)

# Accessing data through getters
print(m4.get_model())
print(m4.get_horsepower())

# Modifying data safely through setter
m4.set_horsepower(540)

# Showing updated info
m4.show_info()
