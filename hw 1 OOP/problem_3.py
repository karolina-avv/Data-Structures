class Vehicle:
    def __init__(self, power, brand, owner):
        self._power = power
        self._brand = brand
        self._owner = owner

    def drive(self):
        return "Driving"

    def sell(self, new_owner):
        if isinstance(new_owner, Person):
            self._owner = new_owner
            return self._owner
        else:
            raise ValueError("Invalid owner type. Must be a Person instance.")
        

    def __add__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(self._power + other._power, self._brand, self._owner)
        else:
            raise ValueError("Invalid operand. Must be a Vehicle instance.")

    def __iadd__(self, other):
        if isinstance(other, Vehicle):
            self._power += other._power
            return self
        else:
            raise ValueError("Invalid operand. Must be a Vehicle instance.")

    def __str__(self):
        return f"Brand: {self._brand}, Power: {self._power}, Owner: {self._owner.__repr__()}"


class Person:
    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname

    def change_name(self, first, last):
        self._firstname = first
        self._lastname = last

    def sell_vehic(self, v, new_owner):
        if v._owner == self:
            v.sell(new_owner)  
    
    def __repr__(self):
        return f"Person({self._firstname}, {self._lastname})"


class Car(Vehicle):
    def __repr__(self):
        return f"Car({self._brand}, {self._power}, {self._owner._firstname}, {self._owner._lastname})"


class Truck(Vehicle):
    def __init__(self, power, brand, owner, max_cargo):
        super().__init__(power, brand, owner)
        self._max_cargo = max_cargo

    def __add__(self, other):
        if isinstance(other, Truck):
            return Truck(self._power + other._power, self._brand, self._owner, self._max_cargo + other._max_cargo)
        else:
            raise ValueError("Invalid operand. Must be a Truck instance.")

    def __iadd__(self, other):
        if isinstance(other, Truck):
            self._power += other._power
            self._max_cargo += other._max_cargo
            return self
        else:
            raise ValueError("Invalid operand. Must be a Truck instance.")

    def __sub__(self, other):
        if isinstance(other, Truck):
            return Truck(self._power - other._power, self._brand, self._owner, self._max_cargo - other._max_cargo)
        else:
            raise ValueError("Invalid operand. Must be a Truck instance.")

    def __isub__(self, other):
        if isinstance(other, Truck):
            self._power -= other._power
            self._max_cargo -= other._max_cargo
            return self
        else:
            raise ValueError("Invalid operand. Must be a Truck instance.")

    def __str__(self):
        return f"Brand: {self._brand}, Power: {self._power}, Owner: {self._owner.__repr__()}, c: {self._max_cargo}"



def main():
    # Create a Person
    person1 = Person("John", "Doe")

    # Create Vehicles
    car1 = Car(200, "Toyota", person1)
    truck1 = Truck(300, "Ford", person1, 1000)
    car2 = Car(150, "Honda", person1)
    truck2 = Truck(250, "Chevrolet", person1, 800)

    # Display initial vehicle details
    print("Initial Vehicle Details:")
    print(car1)  # should print Brand: Toyota, Power: 200, Owner: Person(John, Doe)
    print(truck1)  # should print Brand: Ford, Power: 300, Owner: Person(John, Doe), c: 1000
    print(car2)  # should print Brand: Honda, Power: 150, Owner: Person(John, Doe)
    print(truck2)  # should print Brand: Chevrolet, Power: 250, Owner: Person(John, Doe), c: 800

    print("\nRepresentation Details:")
    print(car2.__repr__())  # should print Car(Honda, 150, John, Doe)
    print(person1.__repr__())  # should print Person(John, Doe)

    # Change the name of the person
    person1.change_name("Jane", "Smith")

    # Sell vehicles to a new owner
    person2 = Person("Peter", "Moldan")
    person1.sell_vehic(car1, person2)
    person2.sell_vehic(truck2, person1)

    # Perform vehicle addition and subtraction
    print("\nVehicle Addition and Subtraction:")
    result_add = car1 + car2
    result_sub = truck1 - truck2
    print("Result of car1 + car2:", result_add._power)  # should print 350
    print("Result of truck1 - truck2:", result_sub._max_cargo)  # should print 200

    # Display updated vehicle details
    print("\nUpdated Vehicle Details:")
    print(car1)  # should print Brand: Toyota, Power: 200, Owner: Person(Peter, Moldan)
    print(truck1)  # should print Brand: Ford, Power: 300, Owner: Person(Jane, Smith), c: 1000
    print(car2)  # should print Brand: Honda, Power: 150, Owner: Person(Jane, Smith)
    print(truck2)  # should print Brand: Chevrolet, Power: 250, Owner: Person(Jane, Smith), c: 800


if __name__ == '__main__':
    main()
