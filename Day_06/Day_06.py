with open('Day_06/input.txt') as f:
    data = f.readlines()


def clean_up_data(data):
    cleaned = []
    for line in data:
        cleaned.append(line.replace('\n', ''))
    return cleaned

# PART 1 MATERIAL


def how_many_yes(data):
    temp = []
    counter = 0
    for i in range(0, len(data)):
        if data[i] == '':
            temp = []

        for x in data[i]:
            if x not in temp:
                counter += 1
                temp.append(x)
    return counter


def how_many_everyone_yes():
    file = open("Day_06/input.txt", "r")
    peopleInGroup = 0
    currentGroup = ""
    numCommonYes = 0

    for line in file.readlines():
        if line == "\n":
            for char in set(currentGroup):
                if currentGroup.count(char) == peopleInGroup:
                    numCommonYes += 1
            peopleInGroup = 0
            currentGroup = ""
        else:
            peopleInGroup += 1
            currentGroup += line.strip()

    for char in set(currentGroup):
        if currentGroup.count(char) == peopleInGroup:
            numCommonYes += 1

    return numCommonYes


print("For each group, count the number of questions to which anyone answered 'yes'. What is the sum of those counts? (Part 1):",
      how_many_yes(clean_up_data(data)))

# Had to read the file again, did not know how to fix without
print("For each group, count the number of questions to which everyone answered 'yes'. What is the sum of those counts? (Part 2):", how_many_everyone_yes())
