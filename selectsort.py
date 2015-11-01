__author__ = 'harryhao'

def swap(a, i, j):
    temp_ = a[i]
    a[i] = a[j]
    a[j] = temp_

def selectsort(a):
    len_a = len(a)
    for i in range(len_a):
        min_ = a[i]
        for j in range(i+1, len_a):
            if a[j] < min_:
                select_j = j
                min_ = a[j]
        swap(a, i, select_j)

a = [5, 3, 17, 10, 84, 19, 6, 22, 9]
selectsort(a)
print a
