with open('input', 'r') as f:
    yesses = set("abcdefghijklmnopqrstuvwxyz")
    summed = 0
    for line in f:
        line = line.strip()
        if line == "":
            summed += len(yesses)
            yesses = set("abcdefghijklmnopqrstuvwxyz")
            continue
        for y in yesses.copy():
            if y not in line:
                yesses.discard(y)
    summed += len(yesses)

print(summed)
