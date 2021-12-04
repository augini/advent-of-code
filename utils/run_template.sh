DIR_TEMPLATE="# import required module
import sys
# append the path of the sibling directory
sys.path.append('..')
from utils.get_input import get_sample"

echo "Enter the day number of Advent of Code"
read day_number

cd .. && mkdir day_$day_number && cd day_$day_number && touch index.py && echo $DIR_TEMPLATE > index.py && touch sample_input.txt && touch input.txt