"""
나머지 있으면 몫+1 
4 // 2 -> 2 // 2 -> 1 // 2 -> 1
7 // 2 -> 4 // 2 -> 2 // 2 -> 1

while a==b
"""

def solution(n,a,b):
    answer = 0
    while a!=b:
        a,r=divmod(a,2)
        if r>0:
            a+=1
        b,r=divmod(b,2)
        if r>0:
            b+=1
        answer+=1
    return answer