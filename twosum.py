__author__ = 'harryhao'

def maxsubarr(a):
    curr = 0
    max_sum = a[0]
    start_index = 0
    end_index = 0

    for index, i in enumerate(a):
        if curr <= 0:
            curr = i
            start_index = index
        else:
            curr = curr + i

        if curr > max_sum:
            max_sum = curr
            end_index = index
    print start_index, end_index
    return max_sum


print maxsubarr([1, -2, 3, 10, -4, 7, 2, -5, -3, 4, -20, 1])








