#!/bin/bash

cat access_log | python3 q02B-mapper.py | sort | python3 q02B-reducer.py > q02B-answer.txt