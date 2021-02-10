#!/bin/bash

cat forum_node.tsv | python3 q03D-mapper.py | sort | python3 q03D-reducer.py > q03D-answer.txt