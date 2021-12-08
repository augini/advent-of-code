# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample_seperator

def count_instances(input):
  second_half = []
  for x in input:
    second_half.append(x[x.index('|')+2:len(x)])
  
  counter = 0
  for i in " ".join(second_half).split(" "):
    if len(i) in (2,4,3,7):
      counter += 1

  return counter

# print(count_instances(get_sample_seperator("input.txt", "\n")))

def decode_digits(input):
  first_half = decoded_outputs = []

  for x in input:
    first_half.append(x[0:x.index('|')-1])
  
  for values in first_half:
    for i in values.split(" "):
      if len(i) == 2:
        decoded_outputs.append({"1":i})
      elif len(i) == 4:
        decoded_outputs.append({"4":i})
      elif len(i) == 3:
        decoded_outputs.append({"7":i})
      elif len(i) == 7:
        decoded_outputs.append({"8":i})

  return decoded_outputs

print(decode_digits(get_sample_seperator("sample_input.txt", "\n")))
