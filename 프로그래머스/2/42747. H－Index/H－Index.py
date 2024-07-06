"""
정렬해서 현재 idx
6,5,3,1,0

if i+1>i:
continue
else:
return i

"""


def solution(citations):
    citations.sort(reverse=True)
    n=len(citations)
    for i in range(n):
        if citations[i]<i+1:
            return i
    return n