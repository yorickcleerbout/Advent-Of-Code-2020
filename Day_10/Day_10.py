def parse_input():
    with open("Day_10/input.txt", "r") as fp:
        return [int(line.rstrip()) for line in fp.readlines()]


def part_one():
    one_jolt = 0
    two_jolt = 0
    three_jolt = 0
    outlet_rating = 0

    data = parse_input()
    data.append(max(data)+3)

    while True:
        if (outlet_rating + 1) in data:
            one_jolt += 1
            outlet_rating += 1
        elif outlet_rating+2 in data:
            two_jolt += 1
        elif (outlet_rating + 3) in data:
            three_jolt += 1
            outlet_rating += 3
        else:
            break
    return (one_jolt * three_jolt)


def part_two():
    data = parse_input()
    data.append(max(data)+3)
    sol = {0: 1}
    for line in sorted(data):
        sol[line] = 0
        if line - 1 in sol:
            sol[line] += sol[line-1]
        if line - 2 in sol:
            sol[line] += sol[line-2]
        if line - 3 in sol:
            sol[line] += sol[line-3]

    return sol[max(data)]


print("What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?", part_one())
print("What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?", part_two())
