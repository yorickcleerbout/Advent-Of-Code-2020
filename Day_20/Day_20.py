from functools import reduce


def turn(lines, turns):
    for x in range(turns):
        turn = []
        for y in range(len(lines)):
            turn.append(''.join([z[y] for z in reversed(lines)]))
        lines = [y for y in turn]
    return lines


with open("Day_20/input.txt", 'r') as file:
    data = {int(x.split(':\n')[0].split(' ')[1]): x.split(':\n')[
        1] for x in file.read().strip('\n').split('\n\n')}
    borders, flips = {}, {}
    for k, v in data.items():
        lines = v.split('\n')
        flips[k] = [lines, turn(lines, 1), turn(lines, 2), turn(lines, 3), [x[::-1] for x in lines], turn(
            [x[::-1] for x in lines], 1), turn([x[::-1] for x in lines], 2), turn([x[::-1] for x in lines], 3)]
        borders[k] = [x[0] for x in flips[k]]
    amt_borders = {k: len([z for z in v if any(
        [z in w for q, w in borders.items() if k != q])]) for k, v in borders.items()}
    print('Part 1: {}'.format(reduce(lambda x, y: x*y,
                                     [a for a, b in amt_borders.items() if b == min(amt_borders.values())])))
    picture = [[[] for x in range(int(len(data.keys())**0.5))]
               for y in range(int(len(data.keys())**0.5))]
    for k, v in flips.items():
        if amt_borders[k] == min(amt_borders.values()):
            others = sum([w for q, w in borders.items() if k != q], [])
            for x in flips[k]:
                if ''.join([d[-1] for d in x]) in others and x[-1] in others:
                    picture[0][0], used = x, [k]
                    break
    for y in range(len(picture)):
        if y == 0:
            for x in range(1, len(picture)):
                for key in flips.keys():
                    if key not in used:
                        for i in range(len(flips[key])):
                            if ''.join([t[0] for t in flips[key][i]]) == ''.join([j[-1] for j in picture[y][x-1]]):
                                picture[y][x] = flips[key][i]
                                used.append(key)

        else:
            for x in range(len(picture[0])):
                for key in flips.keys():
                    if key not in used:
                        for i in range(len(flips[key])):
                            if flips[key][i][0] == picture[y-1][x][-1]:
                                picture[y][x] = flips[key][i]
                                used.append(key)
    for y in range(len(picture)):
        for x in range(len(picture)):
            picture[y][x] = [f[1:-1] for f in picture[y][x][1:-1]]
    final = []
    for y in picture:
        for x in range(len(y[0])):
            final.append(''.join([z[x] for z in y]))
    dragon = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.strip('\n').split('\n')
    idx = []
    for y in range(len(dragon)):
        for x in range(len(dragon[0])):
            if dragon[y][x] == '#':
                idx.append([x, y])
    tot = 0
    for rot in [final, turn(final, 1), turn(final, 2), turn(final, 3), [x[::-1] for x in final], turn([x[::-1] for x in final], 1), turn([x[::-1] for x in final], 2), turn([x[::-1] for x in final], 3)]:
        for y in range(len(final)-len(dragon)):
            for x in range(len(rot[y])-len(dragon[0])):
                if all([rot[y+j][x+i] == '#' for i, j in idx]):
                    tot += len([z for z in ''.join(dragon) if z == '#'])
    print('Part 2: {}'.format(
        len([z for z in ''.join(final) if z == '#'])-tot))
