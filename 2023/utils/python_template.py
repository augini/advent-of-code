# aoc_template.py
import pathlib
import sys


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 1."""


def solve(puzzle_input):
    # parse the given input
    data = list(puzzle_input.split())

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
