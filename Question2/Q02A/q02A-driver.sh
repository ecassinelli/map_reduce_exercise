#!/bin/bash

cat access_log | python3 q02A-mapper.py | sort | python3 q02A-reducer.py > q02A-answer.txt