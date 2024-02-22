class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        answer=-1
        if n==1 and len(trust)==0:
            return 1
        tracker=[0 for _ in range(n+1)]
        for f,l in trust:
            tracker[f]-=1
            tracker[l]+=1
        for idx,val in enumerate(tracker):
            if val==n-1:
                answer=idx
                break
        return answer