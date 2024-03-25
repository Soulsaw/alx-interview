#!/usr/bin/python3
"""Doc module"""


def minOperations(n):
    """This function compute the minimum operation"""
    if n <= 1:
        return 0
    nb_op = n_itt = 2  # nb_op: the minimum n operation, n_itt: n ieme
    cur_op_val = 1  # the current op value
    while n_itt < n:
        if n % n_itt == 0:
            nb_op += 2
            cur_op_val = n_itt
            n_itt *= 2
        else:
            nb_op += 1
            n_itt += cur_op_val
    return nb_op
