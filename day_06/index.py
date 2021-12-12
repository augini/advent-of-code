# import required module
import sys
import math
# append the path of the sibling directory


sys.path.append('..')
from utils.get_input import get_sample


def simulate_growth(input):
  for x in range(0,256):
    for i in range(0,len(input)):
      if input[i] != 0:
        input[i] = int(input[i]) - 1
      else:
        input[i] = 6
        input.append(8)
  return len(input)



def simulate_growth_optimal(input, days):
  new_lantern_count = 0

  for x in range(1,days+1):
    # print(x)
    for i in range(0,len(input)):
      if input[i] != 0:
        input[i] = int(input[i]) - 1
      else:
        print(math.floor((days-x)/8)+1)
        new_lantern_count+=math.floor((days-x)/8)+1
        input[i] = 6
        
  return new_lantern_count

print(simulate_growth_optimal(get_sample("sample_input.txt"), 18))
