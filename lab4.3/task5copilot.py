def read_txt_file():
    filename = input("Enter the filename (e.g., lab4.3.txt): ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
read_txt_file()