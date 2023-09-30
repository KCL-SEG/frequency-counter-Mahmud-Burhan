"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    list = [str(item) for item in items]

    for item in list:
        if not frequencies.get(item):
            frequencies.update({item: 1})
        else:
            frequencies.update({item: frequencies.get(item) + 1})

    return frequencies
