#! /bin/bash

function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) echo "Aborted" ; return  1 ;;
        esac
    done
}

yes_or_no

if [[ "$yn" == [Yy]* ]]
then
   nodemon --exec python3 index.py sample_input.txt
elif [[ "$yn" == [Nn]* ]]
then
   nodemon --exec python3 index.py input.txt
fi