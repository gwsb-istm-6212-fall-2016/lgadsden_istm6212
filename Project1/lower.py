#!/usr/bin/env python

"""
A filter that splits words so that there is one word per line.
"""

import fileinput


def process(line):
    """For each line of input, split all words that are followed by a space."""
    print(line.strip().lower())


for line in fileinput.input():
    process(line)