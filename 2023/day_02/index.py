import pathlib
import sys


def part1(data):
    """Solve part 1."""
    valid = {"red": 12, "green": 13, "blue": 14}
    invalid = set()

    for id, item in enumerate(data):
        games = item.split(":")[1].split(";")

        for each in games:
            matches = each.split(" ")
            records = {"red": 0, "green": 0, "blue": 0}

            for index, number in enumerate(matches):
                if number.isdigit():
                    color = matches[index + 1].replace(",", "")
                    records[color] += int(number)

            for values in zip(valid.values(), records.values()):
                if values[0] < values[1]:
                    invalid.add(int(id + 1))
                    break

    return sum(range(1, len(data) + 1)) - sum(invalid)


def part2(data):
    """Solve part 2."""
    total = []

    for item in data:
        pieces = item.split(":")
        games = pieces[1].split(";")
        records = {"red": 0, "green": 0, "blue": 0}

        for each in games:
            matches = each.split(" ")
            for index, number in enumerate(matches):
                if number.isdigit():
                    color = matches[index + 1].replace(",", "")
                    records[color] = max(records[color], int(number))
        mlt = 1
        for val in records.values():
            mlt = val * mlt
        total.append(mlt)

    return sum(total)


def solve(puzzle_input):
    # parse the given input
    data = list(puzzle_input.split("\n"))

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
