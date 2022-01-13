def get_decimal_value(board, x, y):
    seq = ""
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            seq += str(board[(i, j)])
    
    return int(seq, 2)
        
def get_bounds(board):
    xmin = ymin = 1e9
    xmax = ymax = -1e9
    
    for y, x in board:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    
    return xmin, xmax, ymin, ymax

def add_layer(board, fill: int):
    xmin, xmax, ymin, ymax = get_bounds(board)
    x1 = xmin - 1
    y1 = ymin - 1
    x2 = xmax + 2
    y2 = ymax + 2
    
    for j in range(x1, x2):
        board[(y1, j)] = fill
        board[(y2 - 1, j)] = fill
    
    for i in range(y1 + 1, y2 - 1):
        board[(i, x1)] = fill
        board[(i, x2 - 1)] = fill

# def print_board(board):
#     chars = {0: ".", 1: "#"}
#     xmin, xmax, ymin, ymax = get_bounds(board)
#     for i in range(ymin, ymax + 1):
#         for j in range(xmin, xmax + 1):
#             print(chars[board[(i,j)]], end="")
#         print()
#     print()

with open("input.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    image = [l.strip() for l in lines[2:]]

key = [1 if c == "#" else 0 for c in key]
  
# convert the image into a board represented by a dictionary
# key is the index
# value is zero or one

board = dict()
for i, row in enumerate(image):
    for j, cel in enumerate(row):
        if cel == "#":
            board[(i,j)] = 1
        else:
            board[(i,j)] = 0

# start applying image enhancement algorithm
for k in range(50):
    # check the element at zero index of algorithm to determine surrounding layers
    if key[0] == 1:
        fill = k % 2
    else:
        fill = 0

    add_layer(board, fill)
    add_layer(board, fill)
    
    xmin, xmax, ymin, ymax = get_bounds(board)
    
    x1 = xmin + 1
    y1 = ymin + 1
    x2 = xmax
    y2 = ymax
    
    new_board = dict()
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            code = get_decimal_value(board, j, i)
            new_board[(i,j)] = key[code]

    board = new_board

print(sum(board.values()))
    
    
    