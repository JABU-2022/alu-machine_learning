#!/usr/bin/env python3

"""Function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Check if the arrays have the same length"""
    if len(arr1) != len(arr2):
        return None

    """Initialize a new array"""
    newarr = []

    """Iterate through arrays and add element-wise"""
    for elem1, elem2 in zip(arr1, arr2):
        newarr.append(elem1 + elem2)

    return newarr
