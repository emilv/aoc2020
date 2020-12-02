import re
from dataclasses import dataclass


@dataclass
class Policy:
    character: str
    min: int
    max: int


@dataclass
class PasswordEntry:
    password: str
    policy: Policy


def entry(line: str) -> PasswordEntry:
    regex = r"^(?P<min>\d+)-(?P<max>\d+) (?P<character>.): (?P<password>.+)$"
    m = re.match(regex, line)
    return PasswordEntry(
        password=m.group("password"),
        policy=Policy(
            character=m.group("character"),
            min=int(m.group("min")),
            max=int(m.group("max")),
        ),
    )


def valid(entry: PasswordEntry) -> bool:
    counter = sum(1 for c in entry.password if c == entry.policy.character)
    return entry.policy.min <= counter <= entry.policy.max


with open("input", "r") as f:
    print(sum(1 for line in f.readlines() if valid(entry(line))))
