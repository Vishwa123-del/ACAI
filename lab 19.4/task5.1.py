class Car:
    def __init__(self, brand: str, model: str, year: int):
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
        if year < 1886:  # First automobile was invented in 1886
            raise ValueError("Invalid year")
            
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self) -> None:
        print("\nCar Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create and display car details
try:
    car1 = Car("Toyota", "Corolla", 2020)
    car1.display_details()
except ValueError as e:
    print(f"Error: {e}")