class User:
    def __init__(self, first_name: str, last_name: str, location: str):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def greet_user(self) -> None:
        print(f'Hello {self.first_name}!')

    def set_location(self, new_loc: str) -> None:
        self.location = new_loc

class Admin(User):
    def __init__(self, first_name: str, last_name: str, location: str = 'Root'):
        super().__init__(first_name, last_name, location)
        self.privileges = ["can add post", "can ban user"]

    def show_privileges(self) -> None:
        print(self.privileges)