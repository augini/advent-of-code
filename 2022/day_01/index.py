# import required module
import sys
# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_sample_seperator


# part_1
def get_highest_colorie(input):
    calories = []
    temp = 0
    
    for x in range(len(input) - 1):
        if input[x] != "":
            temp += int(input[x])
        else:
            calories.append(int(temp))
            temp = 0

    return max(calories)


print(get_highest_colorie(get_sample_seperator("input.txt", "\n")))


# part_2
def get_top_three_calories(input):
    calories = []
    temp = 0
    
    for x in range(len(input) - 1):
        if input[x] != "":
            temp += int(input[x])
        else:
            calories.append(int(temp))
            temp = 0
            
    calories = sorted(calories, reverse=True)
    return sum(calories[:3])


print(get_top_three_calories(get_sample_seperator("input.txt", "\n")))
