"""
leet

ord -> [-1]*26
if not -1 -> len(s)
if -1 idx,

-1 -> len(s)
min()

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char,minidx,answer={},{},len(s)
        for idx in range(len(s)):
            char[s[idx]]=char.get(s[idx],0)+1
            if s[idx] not in minidx:
                minidx[s[idx]]=idx
        for key,val in minidx.items():
            if char[key]==1:
                answer=min(answer,val)
        if answer==len(s):
            return -1
        return answer
        
        