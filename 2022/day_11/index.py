# aoc_template.py

import pathlib
import sys
import math
from collections import defaultdict
from functools import reduce


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data, checker, part, round):
    """Solve part 1."""
    monkeys = {}
    divisible = []
    length = len(data)

    for i in range(0, length, 7):
        curr = data[i : i + 7]

        # get monkey number
        num = curr[0].split(" ")[1].replace(":", "")

        # get starting items
        starting = list(
            map(lambda x: int(x), curr[1].split(":")[1].replace(" ", "").split(","))
        )

        # get operation
        operation = curr[2].replace(" ", "").split("=")[1][3:]
        symbol, value = operation[0], "old" if operation[1:] == "old" else int(
            operation[1:]
        )

        # get test effect values
        test_value = int(curr[3].split(" ")[-1])
        if_true = int(curr[4].split(" ")[-1])
        if_false = int(curr[5].split(" ")[-1])

        divisible.append(test_value)

        monkeys[num] = {
            "starting": starting,
            "operation": [symbol, value],
            "test": [test_value, if_true, if_false],
        }

    count = defaultdict(int)
    lcm = reduce(lambda x, y: x * y, divisible)

    for i in range(round):
        for key in monkeys.keys():
            monkey = monkeys[key]

            for item in monkey["starting"]:
                count[key] += 1
                if monkey["operation"][1] == "old":
                    item *= item
                elif monkey["operation"][0] == "*":
                    item *= monkey["operation"][1]
                elif monkey["operation"][0] == "+":
                    item += monkey["operation"][1]

                # print(lcm)
                # item = checker(item, 3) if part == 1 else checker(item, lcm)
                print(item)

                if item % monkey["test"][0] == 0:
                    monkeys[str(monkey["test"][1])]["starting"].append(item)
                else:
                    monkeys[str(monkey["test"][2])]["starting"].append(item)

            monkey["starting"] = []

    res = sorted(list(count.values()))
    return res[-1] * res[-2]


# Time complexity: O(n*m)
# Space complexity: O(n)


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    def p_1(input, a):
        return math.floor(input // a)

    def p_2(input, a):
        return input % a

    # get the solutions for each problem
    solution1 = part1(data, p_1, 1, 20)
    solution2 = part1(data, p_2, 2, 148)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
