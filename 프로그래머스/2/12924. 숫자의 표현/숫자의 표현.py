"""
O(n^2)으로 풀어야 함
연속된 자연수로 나타내야 함

누적합으로 구하기
addSum=[0,1,3,6,10,15,21]
addSum에서 n보다 크거나 같은 지점부터 시작


"""

def solution(n):
    arraySum=[i for i in range(n+1)]
    for i in range(1,n+1):
        arraySum[i]=arraySum[i-1]+i
    st=int((n*2)**0.5)
    answer=0
    for i in range(st,n+1):
        for j in range(i,i-st-1,-1):
            tmp=arraySum[i]-arraySum[j]
            if tmp==n:
                answer+=1
                break
            elif tmp>n:
                break
    return answer