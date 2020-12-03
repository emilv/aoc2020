from dataclasses import dataclass


class ReachedAirport(Exception):
    pass


class Tundra:
    def __init__(self, filename):
        self.slope = self.load(filename)
        self.x = 0
        self.y = 0
        self.trees = 0

    def load(self, filename):
        def _tree(c: str) -> bool:
            return c == "#"

        result = []
        with open(filename, "r") as f:
            for line in f:
                result.append([_tree(c) for c in line.strip()])
        return result

    def move(self, right: int, down: int):
        self.y += down
        if self.y >= len(self.slope):
            raise ReachedAirport
        line = self.slope[self.y]
        self.x = (self.x + right) % len(line)
        if line[self.x]:
            self.trees += 1


tundra = Tundra(filename="input")
try:
    while True:
        tundra.move(right=3, down=1)
except ReachedAirport:
    print(tundra.trees)
