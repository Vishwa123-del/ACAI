def format_name(full_name):
    """
    Format a full name as "Last, First".
    
    Args:
        full_name (str): Full name in "First Last" format
        
    Returns:
        str: Formatted name as "Last, First"
    """
    # Split the full name into parts
    name_parts = full_name.strip().split()
    
    if len(name_parts) < 2:
        return "Error: Please enter both first and last name"
    
    # Get first and last name
    first_name = name_parts[0]
    last_name = name_parts[-1]
    
    # Format as "Last, First"
    formatted_name = f"{last_name}, {first_name}"
    
    return formatted_name

def main():
    """Main function to get user input and format the name."""
    print("Name Formatter - Converts 'First Last' to 'Last, First'")
    print("-" * 50)
    
    try:
        # Get input from user
        full_name = input("Enter your full name (First Last): ")
        
        # Format the name
        formatted = format_name(full_name)
        
        # Display result
        print(f"\nOriginal: {full_name}")
        print(f"Formatted: {formatted}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
