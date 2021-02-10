#!/bin/bash

cat forum_node.tsv | python3 q03C-mapper.py | sort | python3 q03C-reducer-1.py | python3 q03C-reducer-2.py > q03C-answer.txt