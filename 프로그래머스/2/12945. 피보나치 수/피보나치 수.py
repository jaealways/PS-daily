"""
dp 만들어서 이전 값 계속 더하면서 가게

n-1번 돌게 하기

dp=[0,1]
fiv=dp[0]+dp[1]
dp=dp[1]+[fiv]

"""

def solution(n):
    dp=[0,1]
    for _ in range(n-1):
        fiv=dp[0]+dp[1]
        dp=[dp[1],fiv]
    return dp[-1]%1234567