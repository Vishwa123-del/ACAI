def print_multiples_while(number):
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

print("Multiples using while loop:")
print_multiples_while(5)