"""
이중 list -> 이전 list의 idx, idx+1 -> idx 지점으로
두 이전 list에서의 누적합 값에서 더 큰 값 더해주기


"""

def solution(triangle):
    n=len(triangle)
    for i in range(1,n):
        tmp=[0]+triangle[i-1]+[0]
        for j in range(i+1):
            triangle[i][j]+=max(tmp[j],tmp[j+1])
    return max(triangle[-1])