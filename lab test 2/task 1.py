def apply_discount(price: float, category: str) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    discounts = {"seeds": 0.10, "fertilizer": 0.15, "tools": 0.05}
    if category not in discounts:
        raise ValueError(f"Unknown product category: {category}")
    return round(price * (1 - discounts[category]), 2)

if __name__ == "__main__":
    # Tests
    assert apply_discount(100, "seeds") == 90.0
    assert apply_discount(100, "fertilizer") == 85.0
    assert apply_discount(100, "tools") == 95.0   
    assert apply_discount(0, "seeds") == 0.0
    try:
        apply_discount(100, "invalid")
    except ValueError as e:
        assert str(e) == "Unknown product category: invalid"
    
    try:
        apply_discount(-10, "seeds")
    except ValueError as e:
        assert str(e) == "Price cannot be negative"
    
    print("All tests passed!")
    
    # Interactive input
    while True:
        try:
            price_input = input("\nEnter price (or 'quit'): ").strip()
            if price_input.lower() == 'quit':
                break
            
            price = float(price_input)
            print("Categories: seeds (10%), fertilizer (15%), tools (5%)")
            category = input("Enter category: ").strip().lower()
            
            result = apply_discount(price, category)
            discount = price - result
            print(f"Original: ${price:.2f} | Discount: ${discount:.2f} | Final: ${result:.2f}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            break