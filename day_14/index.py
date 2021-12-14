# import required module
import sys
# append the path of the sibling directory
from collections import defaultdict
sys.path.append('..')
from utils.get_input import get_sample

def find_pairs(input):
  template = input[0:1][0]
  pairs = {}

  for x in range(1, len(input)-2, 3):
    pairs[f"{input[x]}"] = input[x+2]

  joint_pairs = []
  temp = template

  for counter in range(10):
    variable = temp
    for i in range(1, len(temp)):
      variable = variable[0:i+(i-1)] + pairs[f"{temp[i-1]}{temp[i]}"] + variable[i+(i-1):len(variable)]
    
    # print(variable)
    temp = variable
    joint_pairs.append(variable)
  
  last_code = joint_pairs[-1]
  counts = defaultdict(int)

  for letter in last_code:
    counts[letter]+=1
  
  total_counts = list(counts.values())
  total_counts.sort()

  return total_counts[-1] - total_counts[0]



def find_pairs_2(input):
   template = input[0:1][0]
   pairs = {}

   for x in range(1, len(input)-2, 3):
    pairs[f"{input[x]}"] = input[x+2]
   
   print(template)
   template_pairs = defaultdict(int)
   for x in range(len(template)-1):
       template_pairs[f"{template[x]}{template[x+1]}"]+=1

   variable = defaultdict(int)

   for counter in range(10):
     for x in template_pairs:
       new_pairs = f"{x[0]}{pairs[x]}{x[1]}"
       variable[new_pairs[0:2]]+=1
       variable[new_pairs[1:len(new_pairs)]]+=1
    
     print(variable)
     template_pairs = defaultdict(int)
     for i in list(variable):
       template_pairs[i] = variable[i]

   return ""
print(find_pairs_2(get_sample("sample_input.txt")))
