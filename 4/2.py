import re


def passports():
    with open("input", "r") as f:
        passport = dict()
        regex = r"(?P<key>...):(?P<value>[^\s]+)(\s|$)"
        for line in f:
            line = line.strip()
            if line == "":
                yield passport
                passport = {}
                continue
            for m in re.finditer(regex, line):
                passport[m.group("key")] = m.group("value")
        yield passport


def valid(passport):
    def _valid_hgt(x):
        m = re.fullmatch(r"(?P<i>\d+)(?P<unit>cm|in)", x)
        if not m:
            return False
        if m.group("unit") == "cm":
            return 150 <= int(m.group("i")) <= 193
        if m.group("unit") == "in":
            return 59 <= int(m.group("i")) <= 76
        return False

    fields = {
        "byr": lambda x: re.fullmatch(r"[0-9]{4}", x) and 1920 <= int(x) <= 2002,
        "iyr": lambda x: re.fullmatch(r"[0-9]{4}", x) and 2010 <= int(x) <= 2020,
        "eyr": lambda x: re.fullmatch(r"[0-9]{4}", x) and 2020 <= int(x) <= 2030,
        "hgt": _valid_hgt,
        "hcl": lambda x: re.fullmatch(r"#[0-9a-f]{6}", x),
        "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda x: re.fullmatch(r"\d{9}", x),
    }
    for field, validated in fields.items():
        if field not in passport:
            return False
        if not validated(passport[field]):
            return False
    return True


valid_count = len([passport for passport in passports() if valid(passport)])
print(valid_count)
