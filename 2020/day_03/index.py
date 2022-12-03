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
    l, row = len(data), len(data[0])
    trees, y = 0, 0

    for i in range(0, l):
        if data[i][y] == "#":
            trees += 1

        if y + 3 >= row:
            y = (y + 3) % row
        else:
            y += 3
    return trees


def part2(data):
    """Solve part 2."""
    l, row = len(data), len(data[0])
    trees, y = 0, 0

    steps = [1, 3, 5, 7, 1]
    down = [1, 1, 1, 1, 2]
    results = []

    for step, d in zip(steps, down):
        for i in range(0, l, d):
            if data[i][y] == "#":
                trees += 1

            if y + step >= row:
                y = (y + step) % row
            else:
                y += step
        results.append(trees)
        trees = 0
        y = 0

    total = 1
    print(results)
    for r in results:
        total *= r
    return total


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
