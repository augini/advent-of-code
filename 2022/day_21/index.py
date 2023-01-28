# aoc_template.py

import pathlib
import sys
from collections import defaultdict
from copy import deepcopy


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1_recursive(data):
    M = defaultdict(str)

    for item in data:
        words = item.split()
        name = words[0][:-1]
        expr = item.split(":")[1]
        M[name] = expr.split()

    def e(name, h):
        expr = M[name]

        if name == "humn" and h >= 0:
            return h

        try:
            return int(expr[0])
        except:
            assert len(expr) == 3

            e1 = e(expr[0], h)
            e2 = e(expr[2], h)

            if expr[1] == "+":
                return e1 + e2
            elif expr[1] == "*":
                return e1 * e2
            elif expr[1] == "-":
                return e1 - e2
            elif expr[1] == "/":
                return e1 // e2
            else:
                assert False, expr

    print(e("root", -1))

    p1 = M["root"][0]
    p2 = M["root"][2]

    if e(p2, 0) != e(p2, 1):
        p1, p2 = p2, p1
    assert e(p1, 0) != e(p1, 1)
    assert e(p2, 0) == e(p2, 1)

    target = e(p2, 0)

    lo = 0
    hi = int(1e128)
    while lo < hi:
        mid = (lo + hi) // 2
        score = target - e(p1, mid)
        if score < 0:
            lo = mid
        elif score == 0:
            print(mid)
            break
        else:
            hi = mid


def part1(data):
    """Solve part 1."""

    num_yelling = defaultdict(int)
    math_operation = defaultdict(str)

    for item in data:
        parts = item.split(": ")
        if parts[1].isdigit():
            num_yelling[parts[0]] = int(parts[1])
        else:
            math_operation[parts[0]] = parts[1]

    while len(math_operation) > 0:
        for key in math_operation.copy():
            keys = list(num_yelling.keys())
            ops = math_operation[key].split(" ")

            if ops[0] in keys and ops[2] in keys:

                num_1 = num_yelling[ops[0]]
                num_2 = num_yelling[ops[2]]

                if ops[1] == "+":
                    num_yelling[key] = num_1 + num_2
                elif ops[1] == "-":
                    num_yelling[key] = num_1 - num_2
                elif ops[1] == "*":
                    num_yelling[key] = num_1 * num_2
                elif ops[1] == "/":
                    num_yelling[key] = num_1 // num_2

                del math_operation[key]

    return num_yelling["root"]


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1_ = part1_recursive(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2, solution1_


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
