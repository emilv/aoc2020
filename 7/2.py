import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Carried:
    amount: int
    color: str


contains: Dict[str, List[Carried]] = defaultdict(list)

with open("input", "r") as f:
    relation_regex = r"^(?P<container>.*) bags contain (?P<carries> ?\d+ .*? bags?)*(no other bags)?\.$"
    carries_regex = r"(?P<amount>\d+) (?P<color>.*?) bags?"
    for line in f:
        m = re.match(relation_regex, line)
        container = m.group("container")
        carries = (
            re.finditer(carries_regex, m.group("carries")) if m.group("carries") else []
        )
        for c in carries:
            contains[container].append(
                Carried(color=c.group("color"), amount=int(c.group("amount")))
            )


def bag_count(container: str) -> int:
    carries = contains[container]
    counter = 1
    for sub in carries:
        counter += sub.amount * bag_count(sub.color)
    return counter


print(bag_count("shiny gold") - 1)
