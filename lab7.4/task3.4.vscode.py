squares = [] 

with open("NUMBERS.txt", "r") as f:
    for line in f:
        n = line.strip()
        if n.isdigit():
            squares.append(int(n) ** 2)

with open("squares.txt", "w") as f2:
    f2.write("\n".join(map(str, squares)))

print("Squares written")

