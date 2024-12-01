echo "Enter day number: "
read day_number
mkdir day_$day_number && cd day_$day_number && touch index.js && cat ../utils/node_template.js >> index.js && touch sample_input.txt && touch input.txt && echo "Successfully created directory for day $((10#$day_number))! Happy coding!"