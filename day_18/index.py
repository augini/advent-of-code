# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample


def snail_sum_numbers(input):
  for x in input:
    print(x)
    
  return ""

print(snail_sum_numbers(get_sample("sample_input.txt")))
