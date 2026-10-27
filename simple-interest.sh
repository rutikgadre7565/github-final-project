#!/bin/bash

echo "Simple Interest Calculator"

read -p "Enter principal amount: " p
read -p "Enter annual rate of interest (%): " r
read -p "Enter time in years: " t

si=$(echo "scale=2; $p * $r * $t / 100" | bc)

echo "Simple Interest: $si"
