"""
s -> only 1 -> bin
count0+=len(s)-len(only1)
count+=1

s->only1
count1+=1 -> list 만들기
s0

only1 -> bin
s=bin(s0)
count+=1

"""

def solution(s):
    count,count0=0,0
    if s==1:
        return [0,1]
    while len(s)>1:
        count1=0
        for i in s:
            if i=='1':
                count1+=1
        count0+=len(s)-count1
        
        s=str(bin(int(count1)))[2:]
        count+=1

    return [count,count0]