# aoc_template.py
import pathlib
import sys


def part1(data):
    """Solve part 1."""
    nums = []
    for line in data:
        digits = [x for x in line if x.isdigit()]
        nums.append(int(digits[0] + digits[-1]))
    return sum(nums)


def part2(data):
    """Solve part 2"""
    chardigits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    nums = []
    for line in data:
        digits = []
        for ind, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            else:
                for i, chardigit in enumerate(chardigits):
                    if line[ind:].startswith(chardigit):
                        digits.append(str(i + 1))

        nums.append(int(digits[0] + digits[-1]))
    return sum(nums)


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
