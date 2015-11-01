__author__ = 'harryhao'


def swap(a, i, j):
    temp_ = a[i]
    a[i] = a[j]
    a[j] = temp_


def max_heapify(a, i, len_a=None):
    left = i * 2 + 1
    right = i * 2 + 2
    if len_a is None:
        len_a = len(a)

    largest = i
    if left < len_a and a[left] > a[i]:
        largest = left
    if right < len_a and a[right] > a[largest]:
        largest = right

    if largest != i:
        swap(a, largest, i)
        max_heapify(a, largest, len_a)


def build_max_heap(a):
    len_a = len(a)
    # no need to heapify leafs
    len_ = len_a / 2 - 1
    for i in range(len_, -1, -1):
        max_heapify(a, i)


def heap_sort(a):
    len_a = len(a)
    build_max_heap(a)
    heap_size = len_a
    for i in range(len_a - 1, 0, -1):
        swap(a, 0, i)
        heap_size -= 1
        max_heapify(a, 0, heap_size)


a = [5, 3, 17, 10, 84, 19, 6, 22, 9]
build_max_heap(a)
print a

heap_sort(a)
print a
