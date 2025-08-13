def read_txt_file(filename):
    """
    Read a .txt file and return its contents.
    
    Args:
        filename (str): Name of the .txt file to read
        
    Returns:
        str: Contents of the file, or error message if file not found
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'."
    except Exception as e:
        return f"Error reading file: {str(e)}"

def main():
    """Main function to get filename from user and read the file."""
    print("Text File Reader")
    print("-" * 30)
    
    # Get filename from user
    filename = input("Enter the name of the .txt file to read: ")
    
    # Add .txt extension if not provided
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    print(f"\nReading file: {filename}")
    print("-" * 30)
    
    # Read and display file contents
    content = read_txt_file(filename)
    print(content)
    
    # Additional functionality - show file statistics
    if not content.startswith("Error"):
        lines = content.split('\n')
        words = content.split()
        characters = len(content)
        
        print("\n" + "-" * 30)
        print("File Statistics:")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")

if __name__ == "__main__":
    main()
