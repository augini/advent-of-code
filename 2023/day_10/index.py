def get_neighs(z):
    # to get valid maze neighbors
    if maze[z] != "S":
        return [z + w for w in direcs[maze[z]]]
    else:  # z = starting point, so check for which neighbors start is a valid neighbor
        neighbors = [
            z + (1 + 0j),
            z + (-1 + 0j),
            z + (1 + 1j),
            z + (-1 + 1j),
            z + (1 - 1j),
            z + (-1 - 1j),
            z + (0 + 1j),
            z + (0 - 1j),
        ]
        return [n for n in neighbors if z in [n + w for w in direcs[maze[n]]]]


def all_neighs(z):
    # returns all 8 complex neighbors of z
    return [
        z + (1 + 0j),
        z + (-1 + 0j),
        z + (1 + 1j),
        z + (-1 + 1j),
        z + (1 - 1j),
        z + (-1 - 1j),
        z + (0 + 1j),
        z + (0 - 1j),
    ]


def display(maze):
    # optional/handy function to print out the current maze space
    for j in range(len(data)):
        line = ""
        for x in range(len(data[0])):
            line += maze[complex(x, j)]
        print(line)
    return ()


# parse data and pad left and right for easier parsing
data = [
    ["."] + [y for y in x] + ["."] for x in open("2023_10_input.txt").read().split("\n")
]
# pad the data above and below for easier parsing...
data = [["."] * len(data[0])] + data + [["."] * len(data[0])]
# possible neighbor directions for each character
direcs = {
    "F": [0 + 1j, 1 + 0j],
    "7": [-1 + 0j, 0 + 1j],
    "J": [0 - 1j, -1 + 0j],
    "L": [1 + 0j, 0 - 1j],
    "-": [1 + 0j, -1 + 0j],
    "|": [0 + 1j, 0 - 1j],
    ".": [],
}

# to store complex #: character
maze = {}

# populate maze and find start
for h in range(len(data)):
    for w in range(len(data[0])):
        if data[h][w] == "S":
            start = complex(w, h)
        maze[complex(w, h)] = data[h][w]

# initialize current position in finding the circuit/path back to S
cur = start
path = [cur]

while True:
    # get the path points
    # find valid possible new neighbors on the path
    new = [x for x in get_neighs(cur) if x not in path]
    if len(new) > 0:
        cur = new[0]
        path.append(cur)
    else:
        # must be back at the start...
        break

# re-trace along the path, keeping one side to our right,
# and the other to our left.  we will then flood fill
frontier = []
for i in range(1, len(path)):
    # direction vector between prior and current path point
    d = path[i] - path[i - 1]
    # stepping forward to path[i] and backward to path[i-1] this way helps us deal with
    # going around corners without extra complication
    for n in [path[i - 1], path[i]]:
        # turn 90º right of the direction of movement by multiplying d by -i
        right = n + d * complex(0, -1)
        ##turn 90º left of the direction of movement by multiplying d by i
        left = n + d * complex(0, 1)
        if right not in path:
            # label points just to the right of the path in our direction of traversal
            maze[right] = "X"
            frontier.append(right)
        if left not in path:
            # label points just to the left of the path in our direction of traversal
            maze[left] = "Y"
            frontier.append(left)

# flood fill the rest of the non-path spaces
while frontier != []:
    new_front = []
    for f in frontier:
        for n in all_neighs(f):
            if n not in path and maze.get(n, "X") not in ["X", "Y"]:
                new_front.append(n)
                # label the new point correctly
                maze[n] = maze[f]
    frontier = [x for x in new_front]

# suppose the inside has the X label
to_get = "X"
if maze[0 + 0j] == "X":
    # the padding (including the origin) is outside the maze, so switch labels to count
    to_get = "Y"

print(sum([1 for y in maze.values() if y == to_get]))
