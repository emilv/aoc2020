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

    def climb(self):
        self.x = 0
        self.y = 0
        self.trees = 0

    def ride(self, right: int, down: int) -> int:
        self.climb()
        try:
            while True:
                self.move(right=right, down=down)
        except ReachedAirport:
            return self.trees

    def move(self, right: int, down: int):
        self.y += down
        if self.y >= len(self.slope):
            raise ReachedAirport
        line = self.slope[self.y]
        self.x = (self.x + right) % len(line)
        if line[self.x]:
            self.trees += 1


tundra = Tundra(filename="input")
crashes = [
    tundra.ride(right=1, down=1),
    tundra.ride(right=3, down=1),
    tundra.ride(right=5, down=1),
    tundra.ride(right=7, down=1),
    tundra.ride(right=1, down=2),
]
result = 1
for trees in crashes:
    result *= trees
print(result)
