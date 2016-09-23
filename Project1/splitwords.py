#!/usr/bin/env python

"""
A filter that splits words so that there is one word per line.
"""

import fileinput
import re


def process(line):
    """For each line of input, split all words that are followed by a space."""
    return(line.strip())


for line in fileinput.input():
    words = re.split(r'\W+', process(line))
    for word in words:
        if word != '' and len(word) > 1 :
            print(word)
            