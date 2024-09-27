class Car:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year
    def printDesc(self):
        print(f"Your selected Car is a {self.year} {self.make} {self.model}")


class Truck(Car):
    def __init__(self, model, make, year, TowCap):
        super().init(model, make, year)
        self.TowCap = TowCap
    def printDesc(self):
        super().printDesc()
        print(f"Your selected Car is a {self.year} {self.make} {self.model} with a towing\
            capacity of {self.TowCap}")

class SUV(Car):
    def __init__(self, model, make, year, SeatingCap):
        super().init(model, make, year)
        self.SeatingCap = SeatingCap
    def printDesc(self):
        super().printDesc()
        print(f"Your selected Car is a {self.year} {self.make} {self.model} with a seating\
            capacity of {self.SeatingCap} seats")

choice = input("""What type of car are you looking for? Type the number according to the car \n \

        1. Sedan \n \
        2. Truck \n \
        3. SUV \n""")

if (choice == "1"):
    make1 = input("Enter the make of the car: ")
    year1 = input("Enter the year of the car: ")
    model1 = input("Enter the model of the car: ") 
    Sedan = Car(model1, make1, year1)
    Sedan.printDesc()
elif (choice == "2"):
    make2 = input("Enter the make of the car: ")
    year2 = input("Enter the year of the car: ")
    model2 = input("Enter the model of the car: ") 
    TowCapacity = input("Enter the Tow Capacity you are looking for in the vehicle: ")
    Pickup = Truck(model2, make2, year2, TowCapacity)
    Pickup.printDesc()
elif (choice == "3"):
    make3 = input("Enter the make of the car: ")
    year3 = input("Enter the year of the car: ")
    model3 = input("Enter the model of the car: ") 
    SeatCap = input("Enter the amount of Seats in the vehicle")
    SportsUtilityVehicle = SUV(model3, make3, year3, SeatCap)
    SportsUtilityVehicle.printDesc()

