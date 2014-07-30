# coding=utf-8
import numpy
from collections import deque
import sys
import copy

MAX_INT = 100000

parent = []


def subgraph(a, b):
    return a - b

#反向边的作用在于我们给了算法回溯的机会，当后续的算法
#选择了反向边说明之前的路径被撤销，具体证明很复杂，略
def augmentPath(graph, s, t):
    queue = deque()
    vertex_num = len(graph)
    maxflow = MAX_INT

    queue.append(s)
    global parent
    parent = [-1] * 6
    parent[s] = s
    flag = False 
    while queue:
        curr = queue.popleft()
        if not flag and curr == s:
            flag == True
        if flag and curr == s:
            break
        if curr == t:
            break
        for i in range(vertex_num):
            if i != curr and parent[i] == -1 and graph[curr][i] > 0:
                if maxflow > graph[curr][i]:
                    maxflow = graph[curr][i]
                parent[i] = curr
                
                queue.append(i)

    if parent[t] != -1:
        return maxflow
    return -1

@profile
def networkflow(graph, s, t):
    vertex_num = len(graph)
    f = numpy.zeros((vertex_num, vertex_num))

    r = subgraph(graph, f)
    result = augmentPath(r, s, t)
    sums = 0
    
    while result != -1:
        cur = t
        while cur != s:
            r[parent[cur]][cur] -= result
            r[cur][parent[cur]] += result

            cur = parent[cur]

        sums += result
        result = augmentPath(r, s, t)

    return sums, f

if __name__ == '__main__':
    g = [[0, 3, 2, 0, 0, 0],
         [0, 0, 1, 3, 4, 0],
         [0, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0]]

    print networkflow(g, 0, 5)
