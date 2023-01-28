# aoc_template.py

import pathlib
import sys
from collections import defaultdict, deque


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    holding = defaultdict(deque)
    operations = []
    tests = {}
    counts = defaultdict(int)

    temp = 0
    for item in data:
        # print(item)
        if "Monkey" in item:
            parts = item.split(" ")
            temp = int(parts[1][0])
        elif "Starting items" in item:
            parts = item.split(":")
            # print(parts[1])
            digits = parts[1].strip().split(",")

            for d in digits:
                holding[temp].append(int(d))

        elif "Operation" in item:
            parts = item.strip().split(":")
            # print(parts[1])
            ops = parts[1].split(" ")
            if "+" in item:
                operations.append(("add", ops[-1]))
            else:
                operations.append(("multiply", ops[-1]))
        elif "Test" in item:
            parts = item.split(" ")
            tests[temp] = {
                "divisible_by": int(parts[-1]),
                "true": int(data[data.index(item) + 1].split(" ")[-1]),
                "false": int(data[data.index(item) + 2].split(" ")[-1]),
            }

    # print(holding)
    # print(operations)
    # print(tests)

    curr = 0
    _max = len(holding)

    for i in range(20):
        for curr in range(_max):
            while holding[curr]:
                counts[curr] += 1
                item = holding[curr].popleft()

                if operations[curr][0] == "multiply":
                    if operations[curr][1] == "old":
                        item = item * item
                    else:
                        item = item * int(operations[curr][1])
                else:
                    if operations[curr][1] == "old":
                        item = item + item
                    else:
                        item = item + int(operations[curr][1])

                item //= 3

                if item % tests[curr]["divisible_by"] == 0:
                    holding[tests[curr]["true"]].append(item)
                else:
                    holding[tests[curr]["false"]].append(item)

        curr = 0

    res = list(counts.values())
    res.sort()

    return res[-1] * res[-2]


def part2(data):
    """Solve part 2."""
    holding = defaultdict(deque)
    operations = []
    tests = {}
    counts = defaultdict(int)

    temp = 0
    for item in data:
        # print(item)
        if "Monkey" in item:
            parts = item.split(" ")
            temp = int(parts[1][0])
        elif "Starting items" in item:
            parts = item.split(":")
            # print(parts[1])
            digits = parts[1].strip().split(",")

            for d in digits:
                holding[temp].append(int(d))

        elif "Operation" in item:
            parts = item.strip().split(":")
            # print(parts[1])
            ops = parts[1].split(" ")
            if "+" in item:
                operations.append(("add", ops[-1]))
            else:
                operations.append(("multiply", ops[-1]))
        elif "Test" in item:
            parts = item.split(" ")
            tests[temp] = {
                "divisible_by": int(parts[-1]),
                "true": int(data[data.index(item) + 1].split(" ")[-1]),
                "false": int(data[data.index(item) + 2].split(" ")[-1]),
            }

    # print(holding)
    # print(operations)
    # print(tests)

    curr = 0
    _max = len(holding)

    for i in range(20):
        for curr in range(_max):
            while holding[curr]:
                counts[curr] += 1
                item = holding[curr].popleft()

                # if operations[curr][0] == "multiply":
                #     if operations[curr][1] == "old":
                #         item = item * item
                #     else:
                #         item = item * int(operations[curr][1])
                # else:
                #     if operations[curr][1] == "old":
                #         item = item + item
                #     else:
                #         item = item + int(operations[curr][1])

                # item //= 3

                if item % tests[curr]["divisible_by"] == 0:
                    holding[tests[curr]["true"]].append(item)
                else:
                    holding[tests[curr]["false"]].append(item)

        curr = 0

    res = list(counts.values())
    res.sort()
    print(res)
    return res[-1] * res[-2]


def solve(puzzle_input):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    #  print(sys.argv)
    for path in sys.argv[1:]:
        #   print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
