"""
s: dict 추가해서 count

t에서 s dict 제거하면서 없을 때마다 count+=1
s.length==t.length이므로 loop 한번만 돌게?

"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s={}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]]=0
            if t[i] not in dict_s:
                dict_s[t[i]]=0
            dict_s[s[i]]+=1
            dict_s[t[i]]-=1
        answer=0
        for key,val in dict_s.items():
            if val>0:
                answer+=val
        return answer
        
        
        