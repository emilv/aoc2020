with open('input', 'r') as f:
    yesses = set()
    summed = 0
    for line in f:
        line = line.strip()
        if line == "":
            summed += len(yesses)
            yesses.clear()
        for y in line:
            yesses.add(y)
    summed += len(yesses)

print(summed)
