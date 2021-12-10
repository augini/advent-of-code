# import required module
from abc import abstractproperty
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample

# part 1
def calculate_syntax_error_score(input):
  correct_pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
  }

  wrong_pairs = [")", "}", "]", ">"]
  stack = []
  corrupted_lines = []


  for line in input:
    temp = []
    for char in line:
      if len(temp) == 0:
        temp.append(char)
      elif correct_pairs.get(temp[-1]) == char:
        temp.pop()
      elif correct_pairs.get(temp[-1]) != char and correct_pairs.get(char) not in wrong_pairs:
        corrupted_lines.append(char)
        break
      else:
        temp.append(char)
      

    stack.append(temp)
  
  
  scores ={
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
  }
  sum = 0

  for x in corrupted_lines:
    sum+=scores.get(x)

  return sum


# print(calculate_syntax_error_score(get_sample("input.txt")))

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

# part 2
def autocomplete(input):
  correct_pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
  }

  wrong_pairs = [")", "}", "]", ">"]
  stack = []


  for line in input:
    temp = []
    append = True
    for char in line:
      append = True
      if len(temp) == 0:
        temp.append(char)
      elif correct_pairs.get(temp[-1]) == char:
        temp.pop()
      elif correct_pairs.get(temp[-1]) != char and correct_pairs.get(char) not in wrong_pairs:
        filtered = filter(lambda error_line: error_line != line, input)
        input = list(filtered)
        append = False
        break
      else:
        temp.append(char)

    if append:
      stack.append(temp)

  
  for x in range(len(stack)):
    stack[x].reverse()

  results = []

  for line in stack:
    multiplication = 0

    for char in line:
      multiplication *=5
      if correct_pairs.get(char) == ")":
        multiplication += 1
      if correct_pairs.get(char) == "]":
        multiplication += 2
      if correct_pairs.get(char) == "}":
         multiplication += 3
      if correct_pairs.get(char) == ">":
         multiplication += 4
    results.append(multiplication)

  results.sort()
  return findMiddle(results)

print(autocomplete(get_sample("input.txt")))