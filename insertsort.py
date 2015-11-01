__author__ = 'harryhao'

def insertsort(a):
    len_a = len(a)
    for i in range(len_a):
        for j in range(i):
            if a[i] < a[j]:
                insert_ele = a[i]
                del a[i]
                a.insert(j, insert_ele)
                break


a = [2,4,8,3,4,7]
insertsort(a)
print a

