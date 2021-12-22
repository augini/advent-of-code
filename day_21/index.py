# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample, get_sample_seperator


def practice_dice(input):
  player_1_position = int(input[0])
  player_2_position = int(input[1])

  player_1_score=player_2_score=0

  rolling_dice = 0
  num_rolls=0

  player_1_turn = True
  player_2_turn = False

  while player_1_score < 1000 and player_2_score<1000:
    temp_steps = 0
    for i in range(1,4):
      num_rolls+=1
      rolling_dice+=1

      temp_steps+=rolling_dice

      if (rolling_dice == 100): 
        rolling_dice = 0

    if(player_1_turn):
      # move player one position
      landing_position = (temp_steps+player_1_position)%10
      player_1_position = 10 if landing_position % 10 == 0 else landing_position % 10

      # increment player one score
      player_1_score+=player_1_position

    elif(player_2_turn):
      # move player two position
      landing_position = temp_steps+player_2_position
      player_2_position = 10 if landing_position % 10 == 0 else landing_position % 10

      # increment player two score
      player_2_score+=player_2_position

    player_1_turn^=True
    player_2_turn^=True
  
  poor_player_score = player_1_score if player_1_score < player_2_score else player_2_score
  return poor_player_score*num_rolls


# print(practice_dice(get_sample("input.txt")))
possible_states = {}
def play_quantum_dice(position_1, position_2, score_1, score_2):
   if score_1 >= 21:
    return (1,0)

   if score_2 >= 21:
    return (0, 1)

   if (position_1, position_2, score_1, score_2) in possible_states:
    return possible_states[(position_1, position_2, score_1, score_2)]
   
   ans = (0,0)
   for d1 in range(1,4):
    for d2 in range(1,4):
      for d3 in range(1,4):
        new_p1 = (int(position_1)+d1+d2+d3)%10
        new_s1 = score_1 + new_p1 + 1

        x1, y1 = play_quantum_dice(position_2, new_p1, score_2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)

   possible_states[(position_1, position_2, score_1, score_2)] = ans
   return ans


print(max(play_quantum_dice(5,0,0,0)))

