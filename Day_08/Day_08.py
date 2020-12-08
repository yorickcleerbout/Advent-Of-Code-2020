with open('Day_08/input.txt', 'r') as f:
    data = f.readlines()

with open('Day_08/test.txt', 'r') as f:
    test = f.readlines()


def part_one(data):
    accumulator = 0
    index = 0
    visited = []
    while index < len(data):
        elem = data[index].split(' ')
        action = elem[0]
        value = elem[1].replace("\n", "")

        if index not in visited:
            visited.append(index)
        else:
            return accumulator

        if action == "acc":
            if value[:1] == "+":
                accumulator += int(value[1:])
                index += 1
            else:
                accumulator -= int(value[1:])
                index += 1
        elif action == "jmp":
            if value[:1] == "+":
                index += int(value[1:])
            else:
                index -= int(value[1:])
        elif action == "nop":
            index += 1


def part_two():
    return "Did not finish this part."


print("Immediately before any instruction is executed a second time, what value is in the accumulator? (Part 1):", part_one(data))
print(part_two())
