#!/bin/bash

set -eu

url="https://adventofcode.com/$1/day/$2/input"
cookie=$(grep -o "AOC_SESSION=.*" .env | cut -d '=' -f 2)
curl -b "session=$cookie" $url -o inputs/$1/day$2.txt
