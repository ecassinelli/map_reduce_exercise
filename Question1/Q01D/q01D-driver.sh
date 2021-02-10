#!/bin/bash

cat purchases.txt | python3 q01D-mapper.py | sort | python3 q01D-reducer.py > q01D-answer.txt