"""
A,B 각각에서 곱의 누적합이 최소가 되려면?
A를 오름차순, B를 내림차순으로 정렬 후 곱할 경우 최소

"""

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer=0
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer