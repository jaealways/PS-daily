"""
우선 부분합의 절대값이 가장 큰 수 구하기
펄스 사용하면 항상 양수로 만들 수 있음

첫 번째 전부 - 곱하기

[-2,3,6,1,-3,-1,-2,4] -> [0,-2,1,7,8,5,4,2,6]
b-a 절대값이 가장 큰 지점 찾아야 함
-> 제일 큰 값에서 제일 작은 값 빼면 됨

"""

def solution(sequence):
    n=len(sequence)
    sumlist=[0]
    for i in range(1,n+1):
        pulse = 1 if i%2==0 else -1
        sumlist.append(sumlist[-1]+pulse*sequence[i-1])
    return abs(max(sumlist)-min(sumlist))