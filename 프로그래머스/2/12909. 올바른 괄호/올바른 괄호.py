"""
(는 +,)는 - 부여
총 합이 한 번이라도 음수면 false, break

"""

def solution(s):
    t=0
    for i in s:
        if i=="(":
            t+=1
        else:
            t-=1
        if t<0:
            return False
    else:
        if t!=0:
            return False   
    return True