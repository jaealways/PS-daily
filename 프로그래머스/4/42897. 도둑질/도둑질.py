"""
맨 끝 집이 문제

[0 ~ 끝]과 [시작 ~ 0] 두 개 중 max 구하기
"""

def solution(money):
    dp1,dp2=[0,money[1]],[money[0],max(money[:2])]
    for i in range(2,len(money)):
        dp1=[dp1[1],max(dp1[0]+money[i],dp1[1])]
        dp2=[dp2[1],max(dp2[0]+money[i],dp2[1])]
    return max(max(dp1),dp2[0])