#!/bin/bash

cat purchases.txt | python3 q01B-mapper.py | sort | python3 q01B-reducer.py > q01B-answer.txt