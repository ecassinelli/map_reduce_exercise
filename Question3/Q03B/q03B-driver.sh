#!/bin/bash

cat forum_node.tsv | python3 q03B-mapper.py | sort | python3 q03B-reducer.py > q03B-answer.txt