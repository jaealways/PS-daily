"""
모든 contiguous sub-array에서 최소값 찾기
그래서 나중에 다 더하기

1~n개의 리스트 길이 중 가장 큰 값으로 return

일일이 체크하면 시간복잡도 최소 n*2*min()

i개의 length마다 sliding window로 check?
같은 i에선 heap으로 체크 -> 매 idx 지날 때마다 다시 빼주는 작업?

만약 key-idx 짝으로 dict 만들어서 

"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        sumOfMinimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                leftBoundary = stack[-1] if stack else -1
                rightBoundary = i

                count = (mid - leftBoundary) * (rightBoundary - mid) % MOD

                sumOfMinimums += (count * arr[mid]) % MOD
                sumOfMinimums %= MOD
            stack.append(i)

        return int(sumOfMinimums)
    