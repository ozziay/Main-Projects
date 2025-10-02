class BMW:
    def __init__(self, model, horsepower, torque, zero_to_hundred, top_speed):
        self.brand = "BMW"
        self.model = model
        self.horsepower = horsepower
        self.torque = torque
        self.zero_to_hundred = zero_to_hundred
        self.top_speed = top_speed
        
    def show_info(self):
        print (f"{self.brand} {self.model}")
        print (f"Horsepower: {self.horsepower} hp")
        print (f"Torque: {self.torque} Nm")
        print (f"0-100 km/h: {self.zero_to_hundred} seconds")
        print (f"Top Speed: {self.top_speed} km/h")

class BMWCar (BMW):
    def __init__(self, model, horsepower, torque, zero_to_hundred, top_speed, car_type, fuel_type):
        super().__init__(model, horsepower, torque, zero_to_hundred, top_speed,)
        self.car_type = car_type
        self.fuel_type = fuel_type

    def show_info (self):
           super().show_info()
           print(f"Car Type: {self.car_type}")
           print(f"Fuel Type: {self.fuel_type}") 
           print("-"*40)


class BMWMotorcycle (BMW):
    def __init__(self, model, horsepower, torque, zero_to_hundred, top_speed, displacement, bike_type):
        super().__init__(model, horsepower, torque, zero_to_hundred, top_speed,)
        self.displacement = displacement
        self.bike_type = bike_type

    def show_info(self):
        super().show_info()
        print(f"Engine Displacement: {self.displacement} cc")
        print(f"Bike Type: {self.bike_type}")
        print("-"*40)


class BMWSUV (BMW):
    def __init__ (self, model, horsepower, torque, zero_to_hundred, top_speed, drive_type, ground_clearance):
        super().__init__(model, horsepower, torque, zero_to_hundred, top_speed)
        self.drive_type = drive_type
        self.ground_clearance = ground_clearance

    def show_info(self): 
        super().show_info()
        print(f"Drive Type: {self.drive_type}")
        print(f"Groune Clearance: {self.ground_clearance} mm")
        print("-"*40)


m4 = BMWCar("M4 Competition 2025", 523, 650, 3.5, 290, "Coupe", "Petrol")
ser320d = BMWCar("320d 2025", 190, 400, 6.9, 235, "Sedan", "Diesel")
s1000rr = BMWMotorcycle("S1000RR 2025", 210, 113, 3.2, 303, 999, "Sport")
r1300gs = BMWMotorcycle("R1300GS 2025", 145, 149, 3.4, 210, 1300, "Adventure")
x6 = BMWSUV("X6 M60i 2025", 540, 750, 4.3, 250,"AWD", 210) 
x1 = BMWSUV("X1 2025", 201, 230, 7.4, 220, "FWD", 190)

vehicles = [m4, ser320d, s1000rr, r1300gs, x6, x1]

for vehicle in vehicles:
    vehicle.show_info()


