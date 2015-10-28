__author__ = 'harryhao'

'''
    reverse linked list
'''

class Node:
    def __init__(self, data, next_n):
        self.data = data
        self.next_n = next_n


def reve(head):
    p = head
    q = head.next_n
    head.next_n = None
    while q:
        r = q.next_n
        q.next_n = p

        p = q
        q = r

    return p


def print_arr(head):
    while head:
        print head.data
        head = head.next_n


if __name__ == '__main__':
    a = Node(1, None)
    b = Node(2, None)
    c = Node(3, None)

    a.next_n = b
    b.next_n = c
    c.next_n = None

    print_arr(reve(a))
