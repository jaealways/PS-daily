"""
언제 ladder 사용하고, 언제 brick 쓸지 잘 생각하기

긴 곳에 ladder 쓰는게 유리
-> 엔드 포인트가 어디냐에 따라 언제 ladder 쓸지 계속 바뀜

for문 돌면서 다음 height 보다 낮은 지점에 몇 개 필요한지 기록
-> heap으로 ladder list 갱신
-> top N개 만큼 ladder 사용
bricks 0 되면 그 포인트 end로 사용

heap 써서 bricks 먼저 채우자 -> 차피 heap 뒷쪽에는 최대값만 남기 때문에 남는거 ladder 쓰면 됨

"""

import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        n=len(heights)
        for i in range(n-1):
            diff=heights[i+1]-heights[i]
            if diff<0: continue
            heapq.heappush(heap,diff)
            # ladders 이상부터 heappop하면 heap에 ladders 갯수만큼 남음
            if len(heap)>ladders:
                bricks-=heapq.heappop(heap)
            if bricks<0: return i
        return n-1