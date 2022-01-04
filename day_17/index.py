
def shoot_probe(input):
  # store the min and max points
  x_range, y_range = [],[]
  input = input.split(" ")[2:]

  # append min and max ranges in lists
  for value in input:
    if "x" in value:
      value = value.replace("x=","")
      x_range = value.split("..")
    else:
      value = value.replace("y=","")
      y_range = value.split("..")
  
  # store the coors that land in trench
  matching_velocities = []

  # store the current highest y_coor for coors that land in trench
  max_y_height = 0

  for y in range(-300, 300):
    for x in range(1, 300):
      x_velocity, y_velocity = x,y

      # initial coors
      x_point, y_point = 0,0

      # store the history of y heights for all coors temporarily
      temp_y_heights = []

      while x_point <= int(x_range[1]) and y_point >= int(y_range[0]):

        # store the height of the current coors if it is higher than max_y_height
        if y_point > max_y_height:
          temp_y_heights.append(y_point)

        if (y_point in range(int(y_range[0]), int(y_range[1])) and x_point in range(int(x_range[0]),int(x_range[1]))):
          matching_velocities.append(f"{x,y}")

          # update max_y_height with the max in y_height for this coordinate that landes in trench
          # if done previously, returns wrong answer because probe might go higher but that starting velocity might not land in a trench
          if len (temp_y_heights) > 0:
            max_y_height = max(temp_y_heights) if max(temp_y_heights) > max_y_height else max_y_height
          break

        else:
          # update coors
          x_point += x_velocity
          y_point+=y_velocity

          # update velocities
          x_velocity = x_velocity - 1 if x_velocity > 0 else 0
          y_velocity -=1

  print(matching_velocities)
  return len(matching_velocities)


sample_input = "target area: x=20..31 y=-10..-4"
input = "target area: x=195..239 y=-93..-66"

print(shoot_probe(sample_input))

# 144 -> too low
# 145 -> too low