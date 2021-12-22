# import required module
import sys
import math
from collections import defaultdict
# append the path of the sibling directory

sys.path.append('..')
from utils.get_input import get_sample, get_sample_seperator


def simulate_growth(input):
  # print(input)

  for x in range(0,80):
    for i in range(0,len(input)):
      if input[i] != 0:
        input[i] = int(input[i]) - 1
      else:
        input[i] = 6
        input.append(8)
    # print(input)
  return len(input)

# print(simulate_growth(get_sample_seperator("sample_input.txt", ",")))

def simulate_growth_optimal(input):
  counts = {}

  for x in range(0,9):
    counts[x]=0

  for digit in input:
    counts[int(digit)]+=1

  print(counts)
  # {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 0, 7: 1, 8: 0}
  for days in range(10):
    zeroes = 0
    for key in counts:
      if key == 0 and counts[key] != 0:
        zeroes = counts[key]
        counts[key] = 0
      elif key != 0:
        counts[int(key)-1]+=counts[key]
        counts[key] = 0

    counts[6]+=zeroes
    counts[8]+=zeroes  

  print(counts)
  total = list(counts.values())
  sum = 0
  for number in total:
    sum+=number
  
  return sum

print(simulate_growth_optimal(get_sample_seperator("sample_input.txt",",")))
