"""
heap 사용해서 두 개 return
while len(scoville)>1

if pop1>k -> return answer
else pop1+pop2*2 -> 

if scoville[0]<K:
return -1
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>1:
        p1=heapq.heappop(scoville)
        p2=heapq.heappop(scoville)
        if p1>=K:
            return answer
        heapq.heappush(scoville,p1+2*p2)
        answer+=1
        
    if scoville[0]<K:
        return -1
    
    return answer