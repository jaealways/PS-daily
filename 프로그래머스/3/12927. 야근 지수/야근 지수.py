"""
n에 있는 숫자만큼 뺄 수 있음
총 remain works를 제곱한 값이 최소가 되도록
최대한 평균에 근접하도록 -> 정렬

[2,2,1]
[5,1,1] ->3

counter로 진행
works 평균내서 n 이하인 것만 일단 빼기

"""
import heapq


def solution(n, works):
    sumN=sum(works)
    if sumN<=n:
        return 0
    works=[-x for x in works]
    heapq.heapify(works)
    for i in range(n):
        t=heapq.heappop(works)
        heapq.heappush(works,t+1)
    return sum([x**2 for x in works])