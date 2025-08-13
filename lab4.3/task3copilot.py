def format_full_name():
    full_name = input("Enter your full name (First Last): ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        first = parts[0]
        last = " ".join(parts[1:])
        formatted = f"{last}, {first}"
        print("Formatted name:", formatted)
    else:
        print("Please enter both first and last names.")

format_full_name()