import numpy as np


def parse_input():
    with open("Day_13/input.txt", "r") as fp:
        return fp.readlines()


def part_one():
    data = parse_input()
    timestamp = int(data[0][:-1])
    bus_ids = [int(x) for x in data[1].split(",") if x.isdigit()]

    timestamps = range(timestamp-50, timestamp+50)
    valid = np.inf
    diff = np.inf
    bus_id = np.inf

    for time in timestamps:
        for bus in bus_ids:
            if time % bus == 0:
                d = abs(time-timestamp)
                if time > timestamp and d < diff:
                    valid = time
                    diff = d
                    bus_id = bus

    return bus_id*(valid-timestamp)


def part_two():
    LINES = parse_input()
    start = int(LINES[0])
    busses = ["x" if x == "x" else int(x) for x in LINES[1].split(",")]

    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    # print(mods)
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val


print("What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus? (Part 1):", part_one())
print("What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list? (Part 2):", part_two())
