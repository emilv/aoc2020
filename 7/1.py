import re
from collections import defaultdict
from typing import Dict, Set

contains: Dict[str, Set[str]] = defaultdict(set)

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
            contains[container].add(c.group("color"))


def contains_shiny_gold(container):
    carries = contains[container]
    for sub in carries:
        if sub == "shiny gold" or contains_shiny_gold(sub):
            return True
    return False


result = 0
for container in list(contains.keys()):
    if contains_shiny_gold(container):
        result += 1

print(result)
