# INSERT_YOUR_CODE
def temperature_conversion():
    print("=== Temperature Conversion ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Select conversion (1 or 2): ").strip()
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    temperature_conversion()
    # INSERT_YOUR_CODE
    def temperature_menu():
        while True:
            print("\n=== Temperature Conversion Menu ===")
            print("1. Convert temperature")
            print("2. Exit")
            menu_choice = input("Select an option (1 or 2): ").strip()
            if menu_choice == "1":
                temperature_conversion()
            elif menu_choice == "2":
                print("Exiting temperature conversion menu.")
                break
            else:
                print("Invalid option. Please try again.")

    temperature_menu()
