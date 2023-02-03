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

def create_graph(lines):
    grid = []
    for l in lines:
        grid.append([int(x) for x in l])
    return grid

def part1(data):
    """Solve part 1."""
    g = create_graph(data)
    row = len(g)
    col = len(g[0])

    # visible = 0

    top = [[-1]*col for _ in range(row)]
    left = [[-1]*col for _ in range(row)]
    right = [[-1]*col for _ in range(row)]
    bottom = [[-1]*col for _ in range(row)]

    for r in range(row-1):
        cur_max_left = -1
        cur_max_right = -1
        cur_max_top = -1
        cur_max_bottom = -1
        for c in range(col-1):
            # left to right
            val = g[r][c]
            if val > cur_max_left:
                cur_max_left = val
            left[r][c] = cur_max_left

            # right to left
            val = g[r][col - c - 1]
            if val > cur_max_right:
                cur_max_right = val
            right[r][col - c - 1] = cur_max_right

            # top to bottom
            val = g[c][r]
            if val > cur_max_top:
                cur_max_top = val
            top[c][r] = cur_max_top

            #bottom to top
            val = g[col - c - 1][r]
            if val > cur_max_bottom:
                cur_max_bottom = val
            bottom[col - c - 1][r] = cur_max_bottom

    counter=0

    for r in range(row):
        for c in range(col):
            if r == 0 or c == 0 or r == row-1 or c == col-1:
                # visible += [(r, c)]
                counter+=1
            else:
                val = g[r][c]
                if val > left[r][c-1] or val > right[r][c+1] or val > top[r-1][c] or val > bottom[r+1][c]:
                    # visible += [(r, c)]
                    counter+=1
    return counter
# time O(n*m)
# space O(n*m)

def init_arrays(rows, cols, num_height, init_val):
    return [[[init_val]*num_height for _ in range(cols)] for _ in range(rows)]

def find_next_highest(val, next_array, forward_pass, default_val, max_height=10):
    next_so_far = None
    for ht in range(val, max_height):
        if next_array[ht] != default_val:
            if next_so_far == None:
                next_so_far = next_array[ht]
            else:
                if forward_pass:
                    next_so_far = max(next_so_far, next_array[ht])
                else:
                    next_so_far = min(next_so_far, next_array[ht])
    return next_so_far

def part2(data):
    """Solve part 2."""
    g = create_graph(data)
    rows = len(g)
    cols = len(g[0])
    size = cols

    # [-1,-1,..] array of size 10 showing the last location in that direction for val = idx
    num_height = 10
    left = init_arrays(rows, cols, num_height, -1)
    right = init_arrays(rows, cols, num_height, cols)
    top = init_arrays(rows, cols, num_height, -1)
    bottom = init_arrays(rows, cols, num_height, rows)

    # Iterate over the graph 4 times, storing state for each direction each time
    # This is storing away the next closest location from scan direction of each height
    for major in range(size):
        for minor in range(size):
            # left to right
            mr, mi = major, minor  # Major, minor
            val = g[mr][mi]
            if mi > 0:
                left[mr][mi] = (left[mr][mi-1]).copy()
            if mi > left[mr][mi][val]:
                left[mr][mi][val] = mi

            # right to left
            mr, mi = major, size-1-minor
            val = g[mr][mi]
            if mi < size - 1:
                right[mr][mi] = (right[mr][mi+1]).copy()
            if mi < right[mr][mi][val]:
                right[mr][mi][val] = mi

            # top to bottom
            mr, mi = minor, major
            val = g[mr][mi]
            if mr > 0:
                top[mr][mi] = top[mr-1][mi].copy()
            if mr > top[mr][mi][val]:
                top[mr][mi][val] = mr

            # bottom to top
            mr, mi = size-1-minor, major
            val = g[mr][mi]
            if mr < size - 1:
                bottom[mr][mi] = bottom[mr+1][mi].copy()
            if mr < bottom[mr][mi][val]:
                bottom[mr][mi][val] = mr

    # res = [[-1]*cols for _ in range(rows)]
    _max = 0
    for r in range(rows):
        for c in range(cols):
            val = g[r][c]

            if c == 0 or r == 0 or c == cols-1 or r == rows-1:
                visible = 0
            else:
                visible = 1

            # Left to right
            if c > 0:
                next_element = find_next_highest(val, left[r][c-1], True, -1)
                if not next_element:
                    next_element = 0
                visible *= (c - next_element)

            # Right to left
            if c < cols - 1:
                next_element = find_next_highest(
                    val, right[r][c+1], False, cols)

                if not next_element:
                    next_element = cols - 1
                visible *= (next_element - (c))

            # top to bottom
            if r > 0:
                next_element = find_next_highest(val, top[r-1][c], True, -1)
                if not next_element:
                    next_element = 0
                visible *= (r - next_element)

            # bottom to top
            if r < rows - 1:
                next_element = find_next_highest(
                    val, bottom[r+1][c], False, rows)
                if not next_element:
                    next_element = rows - 1
                visible *= (next_element - r)

            # res[r][c] = visible
            if visible > _max:
                _max = visible

    # return max([max(r) for r in res])
    return _max

# time O(n*m+(n*m^2)) = O(n*m^2)
# space O(n*m)

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
