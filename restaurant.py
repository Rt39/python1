class Restaurant:
    def __init__(self, name: str, cusine: str):
        self.name = name
        self.cusine = cusine

    def describe_restaurant(self) -> str:
        return f'{self.name} {self.cusine}'
    
class IceCreamStand(Restaurant):
    def __init__(self, name: str, cusine: str, flavors: list[str] = []):
        super().__init__(name, cusine)
        self.flavors = flavors

    def display_flavors(self) -> None:
        print(self.flavors)

res = IceCreamStand('mc', 'american')
res.display_flavors()