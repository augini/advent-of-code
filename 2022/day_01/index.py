# aoc_template.py

import pathlib
import sys


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))
    else:
        return "Freestyle"


def part1(data):
    calories = []
    temp = 0

    for x in range(len(data) - 1):
        if data[x] != "":
            temp += int(data[x])
        else:
            calories.append(int(temp))
            temp = 0

    return max(calories)


def part2(data):
    calories = []
    temp = 0

    for x in range(len(data) - 1):
        if data[x] != "":
            temp += int(data[x])
        else:
            calories.append(int(temp))
            temp = 0

    calories = sorted(calories, reverse=True)
    return sum(calories[:3])


def solve(puzzle_input):
    # Solve the puzzle for the given input.

    data = parse(puzzle_input, 2)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    print(sys.argv)
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
