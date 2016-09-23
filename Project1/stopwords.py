#!/usr/bin/env python

"""
A filter that splits words so that there is one word per line.
"""

import fileinput


def process(line):
    """For each line of input, split all words that are followed by a space."""
    return(line.strip())


swords = ["a","an","and","are","as","at", "be", "from", "has", "he", "her",
        "she","that","was","were","with","it","the","for","is","of","to"]

for line in fileinput.input():
    word = process(line)
    if word not in swords:
        print(word)
        
    