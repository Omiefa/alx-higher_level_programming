#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        nu = 0
        deno = 0
        for tup in my_list:
            nu += (tup[0] * tup[1])
            deno += (tup[1])
        return (nu/deno)
    return 0
