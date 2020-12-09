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
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    fields.remove("cid")
    return len(passport.keys() & fields) == len(fields)


valid_count = len([passport for passport in passports() if valid(passport)])
print(valid_count)
