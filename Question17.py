class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate, availability):
        self.vehicle_number = vehicle_number
        self.model = model
        self.__rental_rate = rental_rate       # Encapsulation
        self.__availability = availability     # Encapsulation

    def get_rental_rate(self):
        return self.__rental_rate

    def is_available(self):
        return self.__availability

    def calculate_rental_cost(self, days):
        return self.__rental_rate * days

    def display_details(self):
        print(
            self.vehicle_number,
            "-", self.model,
            "- ₹", self.__rental_rate,
            "- Available:", self.__availability
        )


class Car(Vehicle):
    def __init__(self, vehicle_number, model, rental_rate, availability, seats):
        super().__init__(vehicle_number, model, rental_rate, availability)
        self.seats = seats

    # Method overriding
    def calculate_rental_cost(self, days):
        return (self.get_rental_rate() * days) + 500


class Bike(Vehicle):
    def __init__(self, vehicle_number, model, rental_rate, availability, engine_cc):
        super().__init__(vehicle_number, model, rental_rate, availability)
        self.engine_cc = engine_cc

    # Method overriding
    def calculate_rental_cost(self, days):
        return self.get_rental_rate() * days


class Truck(Vehicle):
    def __init__(self, vehicle_number, model, rental_rate, availability, capacity):
        super().__init__(vehicle_number, model, rental_rate, availability)
        self.capacity = capacity

    # Method overriding
    def calculate_rental_cost(self, days):
        return (self.get_rental_rate() * days) + 1000


# Create vehicle objects
car1 = Car("C101", "Maruti Swift", 2000, True, 5)
car2 = Car("C102", "Hyundai Creta", 3000, False, 5)

bike1 = Bike("B101", "Honda Activa", 800, True, 110)
bike2 = Bike("B102", "Royal Enfield", 1200, True, 350)

truck1 = Truck("T101", "Tata 407", 4000, True, "2 Ton")

# Store objects in a list
vehicles = [car1, car2, bike1, bike2, truck1]

# Calculate rental cost using common interface
days = 3

print("Rental Cost for", days, "Days:")
for vehicle in vehicles:
    print(
        vehicle.vehicle_number,
        "- ₹",
        vehicle.calculate_rental_cost(days)
    )

# Find available vehicles using filter() and lambda
available_vehicles = list(
    filter(lambda vehicle: vehicle.is_available(), vehicles)
)

print("\nAvailable Vehicles:")
for vehicle in available_vehicles:
    vehicle.display_details()

# Sort available vehicles according to rental cost
sorted_available = sorted(
    available_vehicles,
    key=lambda vehicle: vehicle.calculate_rental_cost(days)
)

print("\nAvailable Vehicles Sorted by Rental Cost:")
for vehicle in sorted_available:
    print(
        vehicle.vehicle_number,
        "-",
        vehicle.model,
        "- ₹",
        vehicle.calculate_rental_cost(days)
    )

# Dictionary: vehicle type -> set of vehicle numbers
vehicle_types = {
    "Car": set(),
    "Bike": set(),
    "Truck": set()
}

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        vehicle_types["Car"].add(vehicle.vehicle_number)
    elif isinstance(vehicle, Bike):
        vehicle_types["Bike"].add(vehicle.vehicle_number)
    elif isinstance(vehicle, Truck):
        vehicle_types["Truck"].add(vehicle.vehicle_number)

print("\nVehicle Type Dictionary:")
print(vehicle_types)