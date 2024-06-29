"""
1. 각 작업별 걸리는 일수 list 만들기
(100-작업, 나머지 있으면 반올림 없으면 몫 사용)
ex) [93,30,55] -> [7,3,9]
2. 위의 list for문 돌면서
이전 최대값 < 새 값: 이전까지 쌓아온 tmp list에 추가, 최대값 초기화
최대값 > 새 값: tmp+=1
마지막 tmp 추가
"""

import math

def solution(progresses, speeds):
    answer=[]
    list_day=[math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    maxv,c=list_day[0],1
    # 좀 더 단순하고 직관적인 구조 생각해보기
    for d in list_day[1:]:
        if d<=maxv:
            c+=1
        else:
            answer.append(c)
            maxv,c=d,1
    else:
        answer.append(c)
    return answer