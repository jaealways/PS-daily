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
        array=[-1 for _ in range(26)]
        for i in range(len(s)):
            n=ord(s[i])-97
            if array[n]>-1:
                array[n]=len(s)
            else:
                array[n]=i
        for i in range(26):
            if array[i]==-1:
                array[i]=len(s)
        answer=min(array)
        if answer==len(s):
            return -1
        return answer
        
        