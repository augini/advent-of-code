# import required module
import sys
from collections import Counter
# append the path of the sibling directory
from collections import defaultdict
sys.path.append('..')
from utils.get_input import get_sample, get_sample_strip

def find_pairs(input):
  template = input[0:1][0]
  pairs = dict()

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

# print(find_pairs(get_sample("input.txt")))

def find_pairs_2(input):
   template = input[0:1][0]
   pairs = {}

   for x in range(1, len(input)-2, 3):
    pairs[f"{input[x]}"] = input[x+2]
   
   template_pairs = defaultdict(int)
   for x in range(len(template)-1):
       template_pairs[f"{template[x]}{template[x+1]}"]+=1

   variable = defaultdict(int)

   for counter in range(10):
     for x in template_pairs:
       new_pairs = f"{x[0]}{pairs[x]}{x[1]}"
       variable[new_pairs[0:2]]+=1
       variable[new_pairs[1:len(new_pairs)]]+=1
    
     template_pairs = defaultdict(int)
     for i in list(variable):
       template_pairs[i] = variable[i]

   return ""


def parse(lines):
    template = lines[0]
    insertions = dict()

    for line in lines[2:]:
        pair, new_ch = line.split('->')
        insertions[pair.strip()] = new_ch.strip()

    return template, insertions



def calculate(template, insertions, steps):
    char_counter = Counter(template)
    pairs = Counter()

    for i in range(len(template) - 1):
        pairs[template[i:i + 2]] += 1

    for step in range(steps):
        step_counter = Counter()

        for pair, new_ch in insertions.items():
            if pair in pairs and pairs[pair] > 0:
                step_counter[f"{pair[0]}{new_ch}"] += pairs[pair]
                step_counter[f"{new_ch}{pair[1]}"] += pairs[pair]

                char_counter[new_ch] += pairs[pair]
                step_counter[pair] -= pairs[pair]

        pairs += step_counter

    most_frequent = max([v for k, v in char_counter.items()])
    least_frequent = min([v for k, v in char_counter.items()])

    return most_frequent - least_frequent

input_string = get_sample_strip("input.txt","\n")
template, instrs =  parse(input_string)

print(calculate(template, instrs, 40))