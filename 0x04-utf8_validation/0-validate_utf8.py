#!/usr/bin/python3
'''
Doc of the module in this file
'''


def validUTF8(data):
    '''
    Count of bytes expected after the current one
    '''
    num_bytes = 0
    for byte in data:
        '''
        Check if this byte is a continuation byte
        '''
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    if num_bytes != 0:
        return False
    return True
