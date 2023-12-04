import pathlib
import sys
from collections import defaultdict


def parse(puzzle_input, type=1, seperator="\n"):
    #  print(puzzle_input)
    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


def part1(data):
    """Solve part 1."""
    res = 0

    for ind, line in enumerate(data):
        line = line.split(":")[1:]
        playing, winning = line[0].split("|")[0], line[0].split("|")[1]

        playing = [int(x) for x in playing.split()]
        winning = [int(x) for x in winning.split()]

        val = len(set(playing) & set(winning))

        if val > 0:
            res += pow(2, val - 1)

    return res


def part2(data):
    """Solve part 2."""
    cards = defaultdict(int)
    res = 0

    for ind, line in enumerate(data):
        line = line.split(":")[1:]
        playing, winning = line[0].split("|")[0], line[0].split("|")[1]

        playing = [int(x) for x in playing.split()]
        winning = [int(x) for x in winning.split()]

        cards[ind] += 1

        val = len(set(playing) & set(winning))

        if val > 0:
            res += pow(2, val - 1)

        for j in range(val):
            cards[ind + 1 + j] += cards[ind]

    return sum(cards.values())


def solve(puzzle_input):
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
