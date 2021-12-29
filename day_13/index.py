# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample, get_sample_seperator

def fold_once(input):

  instrucions = []
  # get instructions
  for x in range(len(input)-1, 0, -1):
    if "fold" in input[x]:
      instrucions.append(input[x].replace("fold along ", ""))
      input.pop()

  input = input[0:len(input)-2]
  print(instrucions)

  instrucions.reverse()
  print(instrucions)
  # print(input)

  for i in range(0,len(instrucions)):
    in1 = instrucions[i].split('=')[0]
    in2 = int(instrucions[i].split('=')[1])


    if in1 == "y":
      for c in range(len(input)):
        i1=int(input[c].split(',')[0]) 
        i2=int(input[c].split(',')[1]) 
        if i2 > in2:
          input[c] = f"{i1},{in2-(i2-in2)}"

    elif in1 == "x":
      for c in range(len(input)):

        i1=int(input[c].split(',')[0])
        i2=int(input[c].split(',')[1])

        if i1 > in2:
          input[c] = f"{in2-(i1-in2)},{i2}"
  
  input = list(dict.fromkeys(input))
  # print(input)

  for coors in input:
    print(f"({coors})")

  return len(input)

print(fold_once(get_sample_seperator("input.txt", "\n")))

# 622 too high