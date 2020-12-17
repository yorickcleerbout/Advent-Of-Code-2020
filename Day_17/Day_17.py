def parse_input():
    with open("Day_17/input.txt") as fp:
        return [fline.rstrip() for fline in fp.readlines()]


def simulate(cubes):
    new_cube = {}
    for c in cubes:
        x = checkNeighbors(c, cubes)
        if cubes[c] == '#':
            if x == 2 or x == 3:
                new_cube[c] = '#'
            else:
                new_cube[c] = '.'
            n = findNeighbors(c)
            for x in n:
                if x not in cubes:
                    k = checkNeighbors(x, cubes)
                    if k == 3:
                        new_cube[x] = '#'
        elif cubes[c] == '.':
            if x == 3:
                new_cube[c] = '#'
            else:
                new_cube[c] = '.'
    return new_cube


def findNeighbors(c):
    neighbors = [(c[0]+i, c[1]+j, c[2]+k)
                 for i in range(-1, 2)
                 for j in range(-1, 2)
                 for k in range(-1, 2)
                 if not (i == 0 and j == 0 and k == 0)]
    return neighbors


def checkNeighbors(c, cubes):
    n = findNeighbors(c)
    neighbors_count = len([x for x in n if cubes.get(x) == "#"])
    return neighbors_count


def simulate4d(cubes):
    new = {}
    for c in cubes:
        x = checkNeighbors4d(c, cubes)
        if cubes[c] == '#':
            if x == 2 or x == 3:
                new[c] = '#'
            else:
                new[c] = '.'
            n = findNeighbors4d(c)
            for x in n:
                if x not in cubes:
                    k = checkNeighbors4d(x, cubes)
                    if k == 3:
                        new[x] = '#'
        elif cubes[c] == '.':
            if x == 3:
                new[c] = '#'
            else:
                new[c] = '.'
    return new


def findNeighbors4d(c):
    neighbors = [(c[0]+i, c[1]+j, c[2]+k, c[3]+w)
                 for i in range(-1, 2)
                 for j in range(-1, 2)
                 for k in range(-1, 2)
                 for w in range(-1, 2)
                 if not (i == 0 and j == 0 and k == 0 and w == 0)]
    return neighbors


def checkNeighbors4d(c, cubes):
    n = findNeighbors4d(c)
    neighbors_count = len([x for x in n if cubes.get(x) == "#"])
    return neighbors_count


def part_one():
    lines = parse_input()
    cubes = {(i, j, 0): lines[i][j]
             for i in range(len(lines))
             for j in range(len(lines[0]))}
    for i in range(6):
        cubes = simulate(cubes)

    return list(cubes.values()).count('#')


def part_two():
    lines = parse_input()
    cubes = {(i, j, 0, 0): lines[i][j]
             for i in range(len(lines))
             for j in range(len(lines[0]))}
    for i in range(6):
        cubes = simulate4d(cubes)

    return list(cubes.values()).count('#')


print("How many cubes are left in the active state after the sixth cycle?", part_one())
print("How many cubes are left in the active state after the sixth cycle?", part_two())  # Can take some time :D
