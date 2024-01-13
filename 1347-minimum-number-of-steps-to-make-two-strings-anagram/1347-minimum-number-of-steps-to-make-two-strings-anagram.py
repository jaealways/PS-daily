"""
s: dict 추가해서 count

t에서 s dict 제거하면서 없을 때마다 count+=1

"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s={}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]]=0
            dict_s[s[i]]+=1
        
        answer=0
        for i in range(len(t)):
            if t[i] in dict_s:
                dict_s[t[i]]-=1
                if dict_s[t[i]]==0:
                    del dict_s[t[i]]
            else:
                answer+=1
        return answer
        
        
        