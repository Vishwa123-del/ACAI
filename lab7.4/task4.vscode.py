def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i, len(values)):
            denominator = values[j] - values[i]
            if denominator != 0:
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            else:
                results.append((i, j, None))  
    return results
values = []
with open("INPUT.txt", "r") as infile:
    for line in infile:
        for token in line.strip().split():
            try:
                values.append(float(token))
            except ValueError:
                pass

results = compute_ratios(values)
with open("output.txt", "w") as outfile:
    for i, j, r in results:
        outfile.write(f"{i} {j} {r if r is not None else 'None'}\n")

print("Ratios written")
