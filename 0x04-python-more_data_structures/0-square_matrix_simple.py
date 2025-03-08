#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda submap: list(map(lambda e: e**2, submap)), matrix))
