"""
( : +=1
) : -=1

중간에 count가 -1 되면 answer=False
또는 다 돌았는데 0 아니면 False
"""

def solution(s):
    n,count=len(s),0
    for i in range(n):
        if s[i]=="(":
            count+=1
        else:
            count-=1
        if count<0:
            return False
    if count>0:
        return False
    return True