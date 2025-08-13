def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    A year is a leap year if:
    1. It is divisible by 4
    2. If it is divisible by 100, it must also be divisible by 400
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if it's a leap year, False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    """Main function to get user input and check if it's a leap year."""
    try:
        # Get input from user
        year = int(input("Enter a year to check if it's a leap year: "))
        
        # Check if it's a leap year
        if is_leap_year(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
            
    except ValueError:
        print("Please enter a valid integer for the year.")

if __name__ == "__main__":
    main()
