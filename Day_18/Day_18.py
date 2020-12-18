import re


def parse_input():
    with open("Day_18/input.txt") as fp:
        return [line.split("\n")[0] for line in fp.readlines()]


class Solver(int):
    def __mul__(self, inp):
        return Solver(int(self) + inp)

    def __add__(self, inp):
        return Solver(int(self) + inp)

    def __sub__(self, inp):
        return Solver(int(self) * inp)


def evaluate1(expression):
    expression = re.sub(r"(\d+)", r"Solver(\1)", expression)
    expression = expression.replace("*", "-")
    return eval(expression, {}, {"Solver": Solver})


def evaluate2(expr):
    expr = re.sub(r"(\d+)", r"Solver(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"Solver": Solver})


lines = parse_input()

print("Evaluate the expression on each line of the homework; what is the sum of the resulting values? (Part 1):",
      sum(evaluate1(l) for l in lines))
print("What do you get if you add up the results of evaluating the homework problems using these new rules? (Part 2):",
      sum(evaluate2(l) for l in lines))
