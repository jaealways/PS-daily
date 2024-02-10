"""
같은 str여도 idx 다르면 다르게 취급

pal1: i-1,i=1로 비교
pal2: i,i+1 -> i-1,i+2 등으로 loop 돌면서 둘 다르면 stop

두 idx 같을 때마다 answer+=1

"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n,answer=len(s),0
        def pal(l,r,answer):
            while 0<=l and r<n and s[l]==s[r]:
                answer+=1
                l-=1
                r+=1
            return answer
        
        for i in range(n):
            answer=pal(i,i,answer)
            answer=pal(i,i+1,answer)
        return answer
            