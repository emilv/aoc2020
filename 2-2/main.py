import re
from dataclasses import dataclass


@dataclass
class Policy:
    character: str
    a: int
    b: int


@dataclass
class PasswordEntry:
    password: str
    policy: Policy


def entry(line: str) -> PasswordEntry:
    regex = r"^(?P<a>\d+)-(?P<b>\d+) (?P<character>.): (?P<password>.+)$"
    m = re.match(regex, line)
    return PasswordEntry(
        password=m.group("password"),
        policy=Policy(
            character=m.group("character"), a=int(m.group("a")), b=int(m.group("b"))
        ),
    )


def valid(entry: PasswordEntry) -> bool:
    password, policy = entry.password, entry.policy
    counter = 0
    if len(password) >= policy.a and password[policy.a - 1] == policy.character:
        counter += 1
    if len(password) >= policy.b and password[policy.b - 1] == policy.character:
        counter += 1
    return counter == 1


with open("input", "r") as f:
    print(sum(1 for line in f if valid(entry(line))))
