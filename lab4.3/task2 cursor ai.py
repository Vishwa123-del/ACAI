def cm_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Args:
        centimeters (float): Length in centimeters
        
    Returns:
        float: Length in inches
    """
    # 1 inch = 2.54 centimeters
    inches = centimeters / 2.54
    return inches

def main():
    """Main function to demonstrate the conversion."""
    # Test with the given example
    centimeters = 10
    inches = cm_to_inches(centimeters)
    
    print(f"Input: centimeters = {centimeters}")
    print(f"Output: inches = {inches:.3f}")
    
    # Additional user input functionality
    try:
        user_cm = float(input("\nEnter centimeters to convert: "))
        user_inches = cm_to_inches(user_cm)
        print(f"{user_cm} centimeters = {user_inches:.3f} inches")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
