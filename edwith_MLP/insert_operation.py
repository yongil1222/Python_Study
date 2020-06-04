import itertools
from functools import reduce
import sys
import time

def insert_operation(length, input_num, input_op):
    ops = {"0" : (lambda x,y : x+y),
           "1" : (lambda x,y : x-y),
           "2" : (lambda x,y : x*y),
           "3" : (lambda x,y : int(x/y))}
    oper_permutation = []
    result = []

    list(oper_permutation.extend( 
        [str(index)]*value) for index, value in enumerate(input_op) if value > 0)
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]

    for i in permutation:
        result.append(reduce(lambda x,y : ops[i.pop()](x,y), input_num))

    print(str(max(result))+"\n" + str(min(result)))

insert_operation(6, [1,2,3,4,5,6], [2,1,1,1])