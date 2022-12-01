
# import required module
import sys
# append the path of the sibling directory
sys.path.append("..")
from utils.get_input import get_sample

# part_1 
def check_measurements(input):
  counter = 0
  for x in range(len(input)-1):
    if int(input[x+1]) > int(input[x]):
      counter += 1
  return counter  

# print(check_measurements(get_sample("sample_input.txt")))


# part_2
def check_sliding_windows(input):
  counter = 0

  for x in range(len(input)-3):
    first_window = int(input[x])+int(input[x+1])+int(input[x+2])
    second_window = int(input[x+1])+int(input[x+2])+int(input[x+3])

    if second_window > first_window :
      counter += 1

  return counter  


check_sliding_windows(get_sample("sample_input.txt"))

