#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    '''Returns a list with all values multiplied by a number w/o loops'''
    return list(map(lambda x: x * number, my_list))
