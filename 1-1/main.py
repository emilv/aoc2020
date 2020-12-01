FILE="input"
GOAL=2020

def found(a, b):
    print(f"{a} * {b} = {a*b}")
    exit(0)

with open(FILE, 'r') as f:
    input = [int(line) for line in f.readlines()]

less = set()
exact = []
more = set()

for n in input:
    if n < 1010:
        less.add(n)
    elif n == 1010:
        exact.append(n)
    else:
        more.add(n)

if len(exact) >= 2:
    found(1010, 1010)

for a in less:
    b = 2020 - a
    if b in more:
        found(a, b)

exit(1)
