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
    """Solve part 1."""
    count = 0
    for item in data:
        one, two = item.split(",")
        # print(one, two)
        _one, one_two = one.split("-")
        _two, two_two = two.split("-")
        if int(_one) <= int(_two) and int(one_two) >= int(two_two):
            count += 1
        elif int(_two) <= int(_one) and int(two_two) >= int(one_two):
            count += 1

    return count


def part2(data):
    """Solve part 2."""
    count = 0

    for item in data:
        one, two = item.split(",")
        # print(one, two)
        _one, one_two = one.split("-")
        _two, two_two = two.split("-")

        if (int(_one) <= int(_two) and int(one_two) >= int(_two)) or (
            int(_one) <= int(two_two) and int(one_two) >= int(two_two)
        ):
            count += 1
            # print(item)
        elif (int(_two) <= int(_one) and int(two_two) >= int(_one)) or (
            int(_two) <= int(one_two) and int(two_two) >= int(one_two)
        ):
            count += 1

    return count


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
