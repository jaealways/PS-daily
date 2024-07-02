"""
가격이 떨어지지 않는 기간...

현재 시점보다 더 낮은 숫자가 처음 등장하는 시간?

[1, 2, 3, 2, 3]	-> [4, 3, 1, 1, 0]
2,3 pair가 의미하는 것: 2보다 크거나 같은게 끝까지 3개 있다
맨 앞 1은 뒤 정보 + 스스로 대소비교 하면 됨
만약 맨 앞이 3이였으면, 이전 값 중 3보다 큰 값 찾기? -> 근데 직전값이 4면 3은 포함 안시켰음...

그냥 brute force가 정답

앞에서부터 check
더 작은 숫자 나오면, 현재 idx - 작은 숫자 idx
안나오면 len(prices) - 현재 idx

"""

def solution(prices):
    n=len(prices)
    answer = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if prices[j]<prices[i]:
                answer[i]=j-i
                break
        else:
            answer[i]=n-i-1
    return answer