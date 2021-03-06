# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample, get_sample_seperator


def align_carbs(input):
  # print(input)
  for i in range(len(input)):
    input[i] = int(input[i])

  # print(input)
  


  sum_collection = {}
  for x in range(len(input)):
    for i in range(len(input)):
      one = abs(input[x])
      two = abs(input[i])

      if x!=i and sum_collection.get(f"{x}-{one}") is not None:
        sum_collection[f"{x}-{one}"]+=abs(one-two)
      elif x==i:
        continue
      else:
        sum_collection[f"{x}-{one}"]=abs(one-two)

  print(sum_collection)
  return min(sum_collection.values())

# print(align_carbs(get_sample_seperator("sample_input.txt",",")))

def summutate(end):
  return int(end*(1+end)/2)

def align_carbs_2(input):

  for i in range(len(input)):
    input[i] = int(input[i])

  sum_collection = {}
  for x in range(len(input)):
    for i in range(len(input)):
      one = abs(input[x])
      two = abs(input[i])
      
      if x!=i and sum_collection.get(f"{x}-{one}") is not None:
        sum_collection[f"{x}-{one}"]+=summutate(abs(one-two))
      elif x==i:
        continue
      else:
        sum_collection[f"{x}-{one}"]=summutate(abs(one-two))

  # markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
  sum_list = sorted(sum_collection.items(), key=lambda x:x[1])
  sortdict = dict(sum_list)

  return sortdict

print(align_carbs_2(get_sample_seperator("input.txt",",")))

# 92881138