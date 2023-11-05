#! /bin/bash

function yes_or_no {
    while true; do
        read -p "$* Run test input ?: y/n  " yn
        read -p "$* Day number: " day_number
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) return  1 ;;
        esac
    done
}

yes_or_no

if [[ "$yn" == [Yy]* ]]
then
   nodemon --exec python3 day_$day_number/index.py day_$day_number/sample_input.txt
elif [[ "$yn" == [Nn]* ]]
then
   nodemon --exec python3 day_$day_number/index.py day_$day_number/input.txt
fi