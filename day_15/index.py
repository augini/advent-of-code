# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample


def lowest_risk_level_path(path):
  new_path = []

  for x in path:
    temp = []
    for digit in x:
      temp.append(int(digit))
    new_path.append(temp)

  # new_path equals array of integer arrays [[1,4,5], [4,5,6]]


  
  for line in new_path:
    print(line)

  return new_path

lowest_risk_level_path(get_sample("sample_input.txt"))