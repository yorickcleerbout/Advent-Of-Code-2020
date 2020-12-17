def parse_input():
    with open("Day_16/input.txt", 'r') as f:
        return f.readlines()


rules = []
my_ticket = []
nearby_ticket = []
tickets = []
lines = parse_input()
temp = []
for i, line in enumerate(lines):

    if line != "\n":
        temp.append(line.rstrip())
    elif line == "\n":
        if len(rules) == 0:
            rules = temp
            rule = {v.split(": ")[0]: v.split(
                ": ")[1].split(" or ") for v in rules}
            rules = {}
            for k, v in rule.items():
                v = [list(range(int(i.split("-")[0]), int(i.split("-")[1])+1))
                     for i in v]
                v = [i for k in v for i in k]
                rules[k] = v

            temp = []
        if len(my_ticket) == 0:
            my_ticket = temp
            temp = []
if len(nearby_ticket) == 0:
    nearby_ticket = temp
    nt = [v.split(",") for v in nearby_ticket[1:]]
    nt = [int(i) for j in nt for i in j]
    nearby_ticket = nt
    def mint(l): return [int(i) for i in l.split(",")]
    tickets = [mint(j) for j in temp[1:]]


error_counts = 0
valid_tickets = []
for values in tickets:
    for v in values:
        valid = False
        for rv in rules.values():
            if v in rv:
                valid = True
                break
        if not valid:
            error_counts += v
            break
    if valid:
        valid_tickets.append(values)

# a dictionary to hold possible fields for each col
possible_fields = {i: set(rules.keys()) for i in range(len(valid_tickets[0]))}
for ticket in valid_tickets:
    for i, value in enumerate(ticket):
        for field in rules:
            possible = False
            if value in rules[field]:
                possible = True
            if not possible:
                possible_fields[i].discard(field)

# remove repeated fields
for i in sorted(possible_fields, key=lambda k: len(possible_fields[k])):
    this_field = next(iter(possible_fields[i]))
    for j in possible_fields:
        if i != j:
            possible_fields[j].discard(this_field)

mt = [int(x) for x in lines[22].split(",")]

ans = 1
for i in possible_fields:
    if possible_fields[i].pop().startswith("departure"):
        ans *= mt[i]

print("What is your ticket scanning error rate? (Part 1):", error_counts)
print("What do you get if you multiply those six values together? (Part 2):", ans)
