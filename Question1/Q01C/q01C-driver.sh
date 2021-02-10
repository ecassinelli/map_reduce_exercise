#!/bin/bash

cat purchases.txt | python3 q01C-mapper.py | sort | python3 q01C-reducer.py > q01C-answer.txt