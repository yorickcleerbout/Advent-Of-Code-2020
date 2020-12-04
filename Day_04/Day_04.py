import re


def load_file_and_fill_dict():
    passports = []
    with open('Day_04/input.txt') as file:
        passport = {}
        for line in file:
            if line != "\n":
                items = re.split(r":| ", line.strip())
                for i in range(0, len(items), 2):
                    passport.update({items[i]: items[i+1]})
            else:
                passports.append(passport)
                passport = {}
        passports.append(passport)
    return passports


# PART 1 MATERIAL
def is_valid(passport: set):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return required.issubset(passport)


def amount_valid_part_1(passports: set):
    counter = 0
    for x in passports:
        if is_valid(x):
            counter += 1
    return counter


# PART 2 MATERIAL
def check_value(value: str, low: int, high: int):
    return low <= int(value) <= high


def check_height(height: str):
    if height[-2:] == "in":
        return check_value(height[:-2], 59, 76)
    elif height[-2:] == "cm":
        return check_value(height[:-2], 150, 193)
    return False


def check_hair_colour(color: str):
    if re.match(r"#[0-9a-f]{6}", color):
        return True
    return False


def check_eye_colour(colour: str):
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return colour in valid_colours


def check_pid(pid: str):
    return len(pid) == 9 and pid.isdigit()


def amount_valid_part_2(passports: list):
    counter = 0
    for passport in passports:
        valid = is_valid(set(passport.keys()))
        if valid:
            valid *= check_value(passport["byr"], 1920, 2002)
            valid *= check_value(passport["iyr"], 2010, 2020)
            valid *= check_value(passport["eyr"], 2020, 2030)
            valid *= check_height(passport["hgt"])
            valid *= check_hair_colour(passport["hcl"])
            valid *= check_eye_colour(passport["ecl"])
            valid *= check_pid(passport["pid"])

            counter += valid
    return counter


passports = load_file_and_fill_dict()

print("How many passports are valid? (Part 1):", amount_valid_part_1(passports))
print("How many passports are valid (With data validation)? (Part 2):", amount_valid_part_2(passports))
