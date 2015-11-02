__author__ = 'harryhao'
from random import randint
from alutils import *

# ith number i start from 1
def rand_select(a, p, r, i):
    if p == r:
        return a[r]
    q = rand_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    if k > i:
        return rand_select(a, p, q-1, i)
    else:
        return rand_select(a, q+1, r, i-k)

def rand_partition(a, p, r):
    rand_index = randint(p, r)
    swap(a, rand_index, r)
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            swap(a, i, j)
    swap(a, i+1, r)
    return i + 1


print rand_select([2,6,3,8],0,3,2)





