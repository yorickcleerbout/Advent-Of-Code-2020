with open("Day_03/input.txt", 'r') as f:
    data = f.readlines()


def solution(right, down):
    trees = 0
    x_pos = 0
    for i in range(0, len(data), down):
        line = data[i]

        if line[x_pos % 31] == "#":
            trees += 1
        x_pos += right

    return trees


print("How many trees would you encounter when using slope of '3 right' and  '1 down' (Part 1):", solution(3, 1))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
part_two = 1
for r, d in slopes:
    part_two *= solution(r, d)
print("How many trees would you encounter when you multiply the number of trees on each slope '1r 1d', '3r 1d', '5r 1d', '7r 1d' and '1r 2d' (Part 2):", part_two)
