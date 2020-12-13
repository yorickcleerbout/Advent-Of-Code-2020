def parse_input():
    with open('Day_12/input.txt') as f:
        return [(cmd, int(''.join(n))) for cmd, *n in f]


def part_one():
    d = 1
    xy = 0
    for cmd, n in parse_input():
        if cmd == 'F':
            xy += d*n
        elif cmd == 'L':
            d *= 1j**(n//90)
        elif cmd == 'R':
            d /= 1j**(n//90)
        elif cmd == 'N':
            xy += n*1j
        elif cmd == 'S':
            xy -= n*1j
        elif cmd == 'E':
            xy += n
        elif cmd == 'W':
            xy -= n

    return int(abs(xy.real) + abs(xy.imag))


def part_two():
    xy = 0
    w = 10 + 1j
    for cmd, n in parse_input():
        if cmd == 'F':
            xy += n*w
        elif cmd == 'L':
            w *= 1j**(n//90)
        elif cmd == 'R':
            w /= 1j**(n//90)
        elif cmd == 'N':
            w += n*1j
        elif cmd == 'S':
            w -= n*1j
        elif cmd == 'E':
            w += n
        elif cmd == 'W':
            w -= n
    return int(abs(xy.real) + abs(xy.imag))


print("What is the Manhattan distance between that location and the ship's starting position? (Part 1):", part_one())
print("What is the Manhattan distance between that location and the ship's starting position? (Part 2):", part_two())
