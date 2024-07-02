"""
100개 O(n^4)까지는 가능
(p,i) <- 쌍으로 만들기
시작: (10,-1)

1) 같은 p 중에 i가 뒤에 있는 값들만 가져오기 -> 정렬해서 point 갱신
2) 같은 p 중에 i가 앞에 있는 값들 가져오기 -> 정렬해서 point 갱신

for loop 사용

"""

from collections import deque

def solution(priorities, location):
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    answer = 0

    while queue:
        current = queue.popleft()
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer

    return answer