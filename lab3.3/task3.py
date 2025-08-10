def calculate_power_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Example slab rates (can be adjusted as needed)
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

    print(f"Total power bill for {units} units is: ₹{bill:.2f}")

if __name__ == "__main__":
    calculate_power_bill()
    # Additional code to calculate a monthly power bill based on user input
    print("\n--- Monthly Power Bill Calculator ---")
    try:
        monthly_units = float(input("Enter the number of units consumed this month: "))
        if monthly_units < 0:
            print("Units consumed cannot be negative.")
        else:
            if monthly_units <= 100:
                monthly_bill = monthly_units * 1.5
            elif monthly_units <= 200:
                monthly_bill = (100 * 1.5) + ((monthly_units - 100) * 2.5)
            elif monthly_units <= 300:
                monthly_bill = (100 * 1.5) + (100 * 2.5) + ((monthly_units - 200) * 4)
            else:
                monthly_bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((monthly_units - 300) * 6)
            print(f"Your monthly power bill for {monthly_units} units is: ₹{monthly_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        # Calculate monthly power bill at a flat rate of $0.15 per unit
        try:
            flat_units = float(input("\nEnter units for flat rate calculation: "))
            if flat_units < 0:
                print("Units consumed cannot be negative.")
            else:
                flat_bill = flat_units * 0.15
                print(f"At a flat rate, your monthly power bill for {flat_units} units is: ${flat_bill:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            # Calculate monthly power bill based on tiered rates:
            # First 100 units at $0.10/unit, next 200 at $0.15/unit, rest at $0.20/unit
            try:
                tiered_units = float(input("\nEnter units for tiered rate calculation: "))
                if tiered_units < 0:
                    print("Units consumed cannot be negative.")
                else:
                    if tiered_units <= 100:
                        tiered_bill = tiered_units * 0.10
                    elif tiered_units <= 300:
                        tiered_bill = (100 * 0.10) + ((tiered_units - 100) * 0.15)
                    else:
                        tiered_bill = (100 * 0.10) + (200 * 0.15) + ((tiered_units - 300) * 0.20)
                    print(f"At tiered rates, your monthly power bill for {tiered_units} units is: ${tiered_bill:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                # INSERT_YOUR_CODE
                print("\n--- Tiered Power Bill Calculator with Fixed Charge and Tax ---")
                try:
                    units = float(input("Enter the number of units consumed: "))
                    if units < 0:
                        print("Units consumed cannot be negative.")
                    else:
                        if units <= 100:
                            base_amount = units * 0.10
                        elif units <= 300:
                            base_amount = (100 * 0.10) + ((units - 100) * 0.15)
                        else:
                            base_amount = (100 * 0.10) + (200 * 0.15) + ((units - 300) * 0.20)
                        fixed_charge = 5
                        subtotal = base_amount + fixed_charge
                        tax = subtotal * 0.10
                        total_bill = subtotal + tax
                        print(f"Base amount: ${base_amount:.2f}")
                        print(f"Fixed charge: ${fixed_charge:.2f}")
                        print(f"Tax (10%): ${tax:.2f}")
                        print(f"Total monthly power bill for {units} units is: ${total_bill:.2f}")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    # INSERT_YOUR_CODE
                    print("\n--- Power Bill Calculator ---")
                    try:
                        units = float(input("Enter the number of units consumed: "))
                        if units < 0:
                            print("Units consumed cannot be negative.")
                        else:
                            if units <= 100:
                                base = units * 0.10
                            elif units <= 300:
                                base = 100 * 0.10 + (units - 100) * 0.15
                            else:
                                base = 100 * 0.10 + 200 * 0.15 + (units - 300) * 0.20
                            fixed_charge = 5
                            subtotal = base + fixed_charge
                            tax = subtotal * 0.10
                            total = subtotal + tax
                            print(f"Base amount: ${base:.2f}")
                            print(f"Fixed charge: ${fixed_charge:.2f}")
                            print(f"Tax (10%): ${tax:.2f}")
                            print(f"Total monthly power bill for {units} units is: ${total:.2f}")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                        # INSERT_YOUR_CODE
                        print("\n--- Power Bill Calculator ---")
                        try:
                            units = float(input("Enter the number of units consumed: "))
                            if units < 0:
                                print("Units consumed cannot be negative.")
                            else:
                                if units <= 100:
                                    base = units * 0.10
                                elif units <= 300:
                                    base = 100 * 0.10 + (units - 100) * 0.15
                                else:
                                    base = 100 * 0.10 + 200 * 0.15 + (units - 300) * 0.20
                                fixed_charge = 5
                                subtotal = base + fixed_charge
                                tax = subtotal * 0.10
                                total = round(subtotal + tax, 2)
                                print(f"Base amount: ${base:.2f}")
                                print(f"Fixed charge: ${fixed_charge:.2f}")
                                print(f"Tax (10%): ${tax:.2f}")
                                print(f"Total monthly power bill for {units} units is: ${total:.2f}")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
