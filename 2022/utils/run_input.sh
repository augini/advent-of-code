echo "Do you want to run the code for sample input ? y/n"

read answer

if [$answer == "y"]
then
   nodemon --exec python3 index.py sample_input.txt
else
   nodemon --exec python3 index.py input.txt
fi