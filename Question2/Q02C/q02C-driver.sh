#!/bin/bash

cat access_log | python3 q02C-mapper.py | sort | python3 q02C-reducer-1.py | python3 q02C-reducer-2.py > q02C-answer.txt