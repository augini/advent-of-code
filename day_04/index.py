# import required module
from os import curdir
import sys

# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_file_content

# function to check if rows or columns have all been bold
def check_bolds(board):
    # check columns
    for y in range(0, 5):
        counter = 0
        for x in board:
            if "*" in x[y]:
                counter += 1
        # print(f"column {x} has {counter} bolds")
        if counter == 5:
            return True

    # check rows
    for x in range(len(board)):
        counter = 0
        for y in board[x]:
            if "*" in y:
                counter += 1
        # print(f"row {x} has {counter} bolds")
        if counter == 5:
            return True

    return False


# find the sum of unbold items in the board
def find_sum(board):
    sum = 0
    for x in range(len(board)):
        for number in board[x]:
            if "*" not in number:
                sum += int(number)
    return sum


# part 1
def play_bingo(input):

    boards = []

    numbers = input[0].split(",")
    boards_1D = input[1 : len(input)]

    temp = []
    # convert 1D list into 2D list
    for x in range(len(boards_1D)):
        temp.append(boards_1D[x])
        if x != 0 and (x + 1) % 5 == 0:
            boards.append(temp)
            temp = []


    # loop through bingo numbers
    current_number = 0
    for x in numbers:
        current_number = int(x)
        for y in boards:
            if x in y:
                for m in range(len(y)):
                    if y[m] == x:
                        y[m] = y[m] + "*"
                        
        for a in range(0, len(boards), 5):
            all_bold = check_bolds(boards[a : a + 5])
            if all_bold:
                sum = find_sum(boards[a : a + 5])
                # print(sum, current_number)
                return sum * current_number
        print(boards)


print(play_bingo(get_file_content("input.txt")))


# put all boards into stack as they win
# pick the last board in the stack once all numbers have been used

# part 2
def play_bingo_2(input):
    boards_stack = []
    boards = []

    numbers = input[0].split(",")
    boards_1D = input[1 : len(input)]

    temp = []
    # convert 1D list into 2D list
    for x in range(len(boards_1D)):
        temp.append(boards_1D[x])
        if x != 0 and (x + 1) % 5 == 0:
            boards.append(temp)
            temp = []

    # loop through bingo numbers
    current_number = 0
    for x in numbers:
        current_number = int(x)
        for y in boards:
            if x in y:
                for m in range(len(y)):
                    if y[m] == x:
                        y[m] = y[m] + "*"
        for a in range(0, len(boards), 5):
            all_bold = check_bolds(boards[a : a + 5])
            if all_bold:
                # push board into stack if all bolds are found
                boards_stack.append(boards[a : a + 5])
                # remove the board from the list
                boards = boards[0:a] + boards[a + 5 : len(boards)]

                if len(boards) == 0:
                    # if all boards have been removed, return the last board in the stack
                    return (
                        find_sum(boards_stack[len(boards_stack) - 1]) * current_number
                    )


print(play_bingo_2(get_file_content("input.txt")))
