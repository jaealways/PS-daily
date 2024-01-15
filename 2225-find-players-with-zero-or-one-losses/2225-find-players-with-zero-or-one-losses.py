"""
시간복잡도 어떻게 줄일 수 있을까

0번 패배한 것도 count 해야하므로, 승리횟수도 세야 함

"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict_m={}
        n=len(matches)
        answer=[[],[]]
        for i in range(n):
            w,l=matches[i]
            if w not in dict_m:
                dict_m[w]=0
            if l not in dict_m:
                dict_m[l]=0
            dict_m[l]+=1
        
        for k,v in dict_m.items():
            if v==0:
                answer[0].append(k)
            elif v==1:
                answer[1].append(k)
        return [sorted(answer[0]),sorted(answer[1])]