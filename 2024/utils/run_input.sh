#! /bin/bash

function yes_or_no {
    while true; do
        read -p "$*Run test input?: y/n " yn
        read -p "$*Day number (padded or not): " day_number

        # Remove leading zeros for consistent directory lookup
        day_number=$((10#$day_number))

        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) return  1 ;;
        esac
    done
}

yes_or_no

if [[ "$yn" == [Yy]* ]]
then
   nodemon day_$(printf "%02d" $day_number)/index.js day_$(printf "%02d" $day_number)/sample_input.txt
elif [[ "$yn" == [Nn]* ]]
then
   nodemon day_$(printf "%02d" $day_number)/index.js day_$(printf "%02d" $day_number)/input.txt
fi
