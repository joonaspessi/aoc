#!/bin/bash

set -eu

url="https://adventofcode.com/2023/day/$1/input"
cookie=$(grep -o "AOC_SESSION=.*" .env | cut -d '=' -f 2)
curl -b "session=$cookie" $url -o inputs/day$1.txt