FILE="input"

def found(a, b, c):
    print(f"{a} * {b} * {c} = {a*b*c}")
    exit(0)

with open(FILE, 'r') as f:
    input = sorted([int(line) for line in f.readlines()])

for ai, a in enumerate(input[:-2]):
    bs = input[ai+1:-1]
    for bi, b in enumerate(bs, start=ai+1):
        if a+b > 2020:
            break
        for c in input[bi+1:]:
            sum = a + b + c
            if sum > 2020:
                break
            elif sum == 2020:
                found(a, b, c)
