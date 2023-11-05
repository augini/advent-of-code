# aoc_template.py

import pathlib
import sys


def parse(puzzle_input, type=1, seperator="\n"):
    # Parses the input

    if type == 1:
        return list(puzzle_input.split())
    elif type == 2:
        return list(puzzle_input.split(seperator))
    elif type == 3:
        return list(puzzle_input.strip().split(seperator))


ROCKS = {
    "horizontal": [(0, 0), (1, 0), (2, 0), (3, 0)],  # horizontal line
    "plus": [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],  # plus
    "L": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # reversed L
    "vertical": [(0, 0), (0, 1), (0, 2), (0, 3)],  # vertical line
    "square": [(0, 0), (1, 0), (0, 1), (1, 0)],  # square
}

ORDER = list(ROCKS.keys())

# rock -> current rock
# side -> side to move
# rocks -> set of stopped rocks
def move_horizontal(rock, side, rocks):
    # move left
    if side == "<":
        if any([x == 0 for (x, y) in rock]) or any(
            [(x - 1, y) in rocks for (x, y) in rock]
        ):
            return rock
        return [(x - 1, y) for (x, y) in rock]

    # move right
    if side == ">":
        if any([x == 6 for (x, y) in rock]) or any(
            [(x + 1, y) in rocks for (x, y) in rock]
        ):
            return rock
        return [(x + 1, y) for (x, y) in rock]


def move_down(rock, rocks):
    if any([y == 1 for (x, y) in rock]) or any(
        [(x, y - 1) in rocks for (x, y) in rock]
    ):
        return rock

    return [(x, y - 1) for (x, y) in rock]


def get_coors(start, rock):
    return [(start[0] + x, start[1] + y) for (x, y) in rock]


def part1(data):
    """Solve part 1."""
    rocks = set()

    # get the input into a list of chars
    d, jets = data[0], []
    for i in range(len(d)):
        jets.append(d[i])

    max_y = 0
    start = (2, 4)
    curr_jet, curr_rock = 0, 0
    for i in range(2022):
        if curr_rock > 4:
            curr_rock = 0

        current = ROCKS[ORDER[curr_rock]]
        coors = get_coors(start, current)

        while True:
            if curr_jet > len(jets) - 1:
                curr_jet = 0

            # print(jets[curr_jet])
            # print(coors)
            pushed = move_horizontal(coors, jets[curr_jet], rocks)
            # print(pushed)
            fallen = move_down(pushed, rocks)
            # print(fallen)
            if pushed == fallen:
                for item in pushed:
                    rocks.add(item)
                curr_jet += 1
                # print("stopped", pushed)
                break

            coors = fallen
            curr_jet += 1

        curr_rock += 1
        temp_y = max(r[1] for r in fallen)
        if temp_y > max_y:
            max_y = temp_y

        start = (2, max_y + 4)
    return max_y


def part2(data):
    """Solve part 2."""


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
