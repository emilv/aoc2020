import dataclasses


@dataclasses.dataclass
class BoardingPass:
    chars: str
    row: int
    col: int
    seat_id: int


def parse(line: str) -> BoardingPass:
    def num(chars: str, lower: int, upper: int) -> int:
        if not chars:
            return upper
        middle = (upper - lower) // 2 + lower
        if chars[0] in ("F", "L"):
            return num(chars[1:], lower, middle)
        else:
            return num(chars[1:], middle + 1, upper)

    row = num(line[:7], 0, 127)
    col = num(line[7:], 0, 7)
    seat_id = row * 8 + col
    return BoardingPass(chars=line, row=row, col=col, seat_id=seat_id)


with open("input", "r") as f:
    boarding_passes = [parse(line.strip()) for line in f]

print(max([bp.seat_id for bp in boarding_passes]))

boarding_passes.sort(key=lambda bp: bp.seat_id)
last = boarding_passes.pop().seat_id
while boarding_passes:
    curr = boarding_passes.pop().seat_id
    if curr < last - 1:
        print(curr + 1)
        break
    last = curr
