#!/bin/bash

cat purchases.txt | python3 q01A-mapper.py | sort | python3 q01A-reducer.py > q01A-answer.txt