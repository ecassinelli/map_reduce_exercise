#!/bin/bash

cat forum_node.tsv | python3 q03A-mapper.py | sort | python3 q03A-reducer.py > q03A-answer.txt