class Car:
    def __init__(
            self,
            make: str, model: str,
            year: int
        ):
        """
        Initialize attributes to describe a car.
        """
        self.make = make
        self.model = model
        self.year = year
        # Set a default value
        self.odometer_reading = 0

    def read_odometer(self) -> None:
        """
        Print a statement showing the car's mileage.
        """
        print(f"This car has {self.odometer_reading} miles on it.")
    # We are still inside the class
    def get_descriptive_name(self) -> str:
        """
        Return a neatly formatted descriptive name.
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car):
    """
    Represent aspects of a car, 
    specific to electric vehicles.
    """
    def __init__(
            self,
            make: str, model: str, year: int
        ):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(make, model, year)
        # Attributes specific to Electric Cars
        self.battery_size = 40

    def describe_battery(self) -> None:
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
