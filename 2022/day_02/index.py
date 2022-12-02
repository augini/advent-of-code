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
    mapping = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    gamemapping = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    scores = {"X": 1, "Y": 2, "Z": 3}

    total_score = 0
    for item in data:
        items = item.split(" ")

        if gamemapping[mapping[items[0]]] == mapping[items[1]]:
            total_score = total_score + scores[items[1]]

        elif gamemapping[mapping[items[1]]] == mapping[items[0]]:
            total_score = total_score + 6 + scores[items[1]]
        else:
            total_score = total_score + 3 + scores[items[1]]
    return total_score


def part2(data):

    lose_mapping = {"A": "Z", "C": "Y", "B": "X"}
    win_mapping = {"A": "Y", "B": "Z", "C": "X"}

    scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

    total_score = 0
    for item in data:
        items = item.split(" ")
        if items[1] == "X":
            total_score = total_score + scores[lose_mapping[items[0]]]

        elif items[1] == "Z":
            total_score = total_score + 6 + scores[win_mapping[items[0]]]
        else:
            total_score = total_score + 3 + scores[items[0]]
    return total_score


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
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
