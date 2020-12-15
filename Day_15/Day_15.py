def determen_number(input, max_turn):
    last_spoken_dict = {}
    for turn, num in enumerate(input, start=1):
        last_spoken_dict[num] = turn
    spoken_now = input[-1]
    while turn != max_turn:
        last_spoken = spoken_now
        spoken_now = turn - last_spoken_dict.get(last_spoken, turn)
        last_spoken_dict[last_spoken] = turn
        turn += 1
    return spoken_now


INPUT = [0, 14, 6, 20, 1, 4]
print("What will be the 2020th number spoken? (Part 1):", determen_number(INPUT, 2020))
print("what will be the 30000000th number spoken? (Part 2):", determen_number(INPUT, 30000000))  # --> Can take some time
