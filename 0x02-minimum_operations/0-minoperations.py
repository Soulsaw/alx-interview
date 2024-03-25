#!/usr/bin/python3
"""Doc module"""


def minOperations(n):
    """This function compute the minimum operation"""
    if n <= 1:
        return 0
    cpt = 2
    nb_op = 2
    inc = 1
    while cpt < n:
        if n % cpt == 0:
            nb_op += 2
            inc = cpt
            cpt = inc * 2
        else:
            nb_op += 1
            inc *= 1
            cpt += inc
    return nb_op
