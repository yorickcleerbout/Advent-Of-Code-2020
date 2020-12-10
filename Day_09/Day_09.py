import itertools


def parse_input():
    with open("Day_09/input.txt", 'r') as f:
        data = f.readlines()
    return [int(i) for i in data]


def validate_value(preamble, value):
    results = [(x + y) for x, y in itertools.combinations(preamble, 2)]
    return value in results


def part_one(data, preamble):
    for i, d in enumerate(data[preamble:]):
        truthy = validate_value(data[i:i+preamble], d)

        if not truthy:
            return d


def find_range(data, search_value):
    for n in range(len(data)):
        accumulator = 0
        for p, i in enumerate(data[n:]):
            accumulator += i

            if accumulator == search_value:
                data_range = data[n:n+p+1]
                if not len(data_range) == 0:
                    return data_range

            if accumulator > search_value:
                continue


def part_two():
    data_range = find_range(data, part_one(data, 25))
    result = min(data_range) + max(data_range)
    return result


data = parse_input()


print("What is the first number that does not have this property? (Part 1):", part_one(data, 25))


print("What is the encryption weakness in your XMAS-encrypted list of numbers? (Part 2):", part_two())
