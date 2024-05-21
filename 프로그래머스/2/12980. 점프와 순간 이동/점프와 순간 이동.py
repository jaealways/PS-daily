"""
k칸 앞으로: 건전지 k만큼 감소
현재까지 온 거리 x 2: 건전지 x

점프로 이동은 최소, 사용해야 하는 건전지 최소?

나누기 2 -> 나머지만큼 +1
"""

def solution(n):
    answer=0
    while n>0:
        n,r=divmod(n,2)
        answer+=r
    return answer