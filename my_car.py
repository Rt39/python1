from car import Car, ElectricCar

# Now we can use it as if it were defined right here
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

electric_car = ElectricCar('Tesla', 's', 2019)
print(electric_car.get_descriptive_name())
electric_car.read_odometer()