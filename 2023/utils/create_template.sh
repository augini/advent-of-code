echo "Enter day number: "
read day_number
mkdir day_$day_number && cd day_$day_number && touch index.dart && cat ../utils/template.dart >> index.dart && touch sample_input.txt && touch input.txt && echo "Successfully created! "