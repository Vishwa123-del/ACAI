def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Args:
        text (str): The string to count vowels in
        
    Returns:
        int: Number of vowels found
    """
    # Define vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    
    # Count vowels in the string
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

def main():
    """Main function to demonstrate vowel counting."""
    print("Vowel Counter")
    print("-" * 30)
    
    # Example with "hello world"
    example = "hello world"
    count = count_vowels(example)
    print(f"Example: '{example}' -> {count} vowels")
    
    # Breakdown of vowels in "hello world"
    print(f"\nBreakdown of vowels in '{example}':")
    vowels_found = []
    for char in example:
        if char in 'aeiouAEIOU':
            vowels_found.append(char)
    print(f"Vowels found: {vowels_found}")
    
    print("\n" + "-" * 30)
    
    # Get input from user
    try:
        user_input = input("Enter a string to count vowels: ")
        vowel_count = count_vowels(user_input)
        print(f"'{user_input}' contains {vowel_count} vowels")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
