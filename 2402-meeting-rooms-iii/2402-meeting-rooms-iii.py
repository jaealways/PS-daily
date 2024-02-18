"""
미팅을 가장 많이 진행한 room return하기
n -> list 만들어서 하면 됨
room별 count list, meeting list 만들기

loop 돌면서 회의별 방 할당하기

Default -> None
pop hold -> 어느 방이든 할당 -> 다시 pop

heap으로 min end time 판단, start time 필요 없음
몇 번 방인지 어떻게 할당?

"""

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy,available=[],[i for i in range(n)]
        count=[0]*n
        meetings.sort()
        
        for s,e in meetings:
            while busy and busy[0][0]<=s:
                _e,room=heapq.heappop(busy)
                heapq.heappush(available,room)
            if available:
                room=heapq.heappop(available)
                heapq.heappush(busy,(e,room))
            else:
                t,room=heapq.heappop(busy)
                heapq.heappush(busy,(t+e-s,room))
            count[room]+=1
        return count.index(max(count))
            
            