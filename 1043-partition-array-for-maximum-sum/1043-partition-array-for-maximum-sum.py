"""
최대 n 길이의 sub-array로 분할
subarray 내의 가장 큰 길이로 대체

가장 큰 모든 val의 값은?

어떤 지점에서 끊는게 max 값 보장할까?

끝지점에 도달할 때까지, 어떤 값이 최대값인지 보장 안됨

dfs?

stack -> [[max value,split idx]]
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        K = k + 1

        dp = [0] * K

        for start in range(N - 1, -1, -1):
            curr_max = 0
            end = min(N, start + k)

            for i in range(start, end):
                curr_max = max(curr_max, arr[i])
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + curr_max * (i - start + 1))

        return dp[0]
