class BMWCar:
    def show_info(self):
        print("This is a BMW car. It is fast and comfortable.\n")


class BMWMotorcycle:
    def show_info(self):
        print("This is a BMW motorcycle. It is light and agile.\n")


class BMWSUV:
    def show_info(self):
        print("This is a BMW SUV. It is powerful and spacious.\n")


# Polymorphism function
def bmw_info(vehicle):
    vehicle.show_info()


# Objects
m4 = BMWCar()
s1000rr = BMWMotorcycle()
x6 = BMWSUV()

# Same function, different classes — polymorphism!
bmw_info(m4)
bmw_info(s1000rr)
bmw_info(x6)
