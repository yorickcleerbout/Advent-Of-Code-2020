import re


with open("day_07/input.txt") as f:
    raw = f.read()


def parse_raw():
    bags = re.findall(r"([a-z]+ [a-z]+) bags contain (.+)", raw)
    formula = re.compile(r"(\d+) ([a-z]+ [a-z]+) bag")
    return {bag: {inner: int(n) for n, inner in formula.findall(contents)} for bag, contents in bags}


formulas = parse_raw()


def has_shiny(bag):
    return "shiny gold" in formulas[bag] or any(map(has_shiny, formulas[bag]))


def count(bag):
    return 1 + sum(n * count(inner) for inner, n in formulas[bag].items())


def part_one():
    return sum(map(has_shiny, formulas))


def part_two():
    # -1 since we don't count the shiny gold bag itself!
    return count("shiny gold") - 1


print("How many bag colors can eventually contain at least one shiny gold bag? (Part 1):", part_one())
print("How many individual bags are required inside your single shiny gold bag? (Part 2):", part_two())
