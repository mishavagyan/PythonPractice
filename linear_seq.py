"""
Define a function linear_seq(sequence) which converts a passed sequence to a sequence without nested sequences.

def linear_seq(sequence):
    pass

sequence = [1,2,3,[4,5, (6,7)]]

print(linear_seq(sequence))
[1,2,3,4,5,6,7]
"""
from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    arr = []
    for i in sequence:
        if type(i) is tuple or type(i) is list:
            arr.extend(linear_seq(i))
        else:
            arr.append(i)
    return arr

if __name__ == "__main__":
    sequence = [1, 2, 3, [4, 5, (6, 7)]]
    print(linear_seq(sequence))