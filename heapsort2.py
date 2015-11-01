def lc(i):
    return 2 * i + 1


def pdown(A, i, length):
    tmp = A[i]
    while lc(i) < length:
        child = lc(i)
        if child + 1 < length and A[child] < A[child + 1]:
            child += 1
        if A[child] > tmp:
            A[i] = A[child]
        else:
            break
        i = child
    A[i] = tmp


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def heapsort(A):
    N = len(A)
    for i in range(N / 2, -1, -1):
        pdown(A, i, N)
    for i in range(N - 1, -1, -1):
        swap(A, 0, i)
        pdown(A, 0, i)

A = [4, 5, 6, 2, 10, 4, 5, 6, 9, 3]
heapsort(A)
print A
