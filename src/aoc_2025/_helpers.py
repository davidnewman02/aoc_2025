import numpy as np


def parse_input_int_array(in_file):
    with open(in_file, "r") as fh:
        return np.array(
            [[int(i) for i in line.strip()] for line in fh.read().split("\n")]
        )


def parse_input_str_array(in_file):
    with open(in_file, "r") as fh:
        return np.array([[i for i in line.strip()] for line in fh.read().split("\n")])


def bounds_check(pos, arr):
    """
    Utility function to check whether co-ords are within array-bounds
    """
    assert len(pos) == len(arr.shape), f"Shape mismatch: {pos} vs. {arr.shape}"
    pos = np.array(pos)
    return (0 <= pos).all() & (pos < arr.shape).all()
