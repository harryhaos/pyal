__author__ = 'harryhao'


def swap(a, i, j):
    temp_ = a[i]
    a[i] = a[j]
    a[j] = temp_


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            swap(a, i, j)
    swap(a, i+1, r)
    return i + 1


def quicksort(a, p, r):
    if p < r:  # end when one element
        q = partition(a, p, r)
        quicksort(a, p, q-1 )
        quicksort(a, q+1, r)


def qsort(a):
    quicksort(a, 0, len(a) - 1)


a = [5, 3, 17, 10, 84, 19, 6, 22, 9]
qsort(a)
print a
