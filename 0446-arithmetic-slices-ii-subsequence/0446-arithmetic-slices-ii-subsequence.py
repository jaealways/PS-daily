"""
조건 1. 모든 연속된 원소의 차이가 같음
조건 2. nums에 주어진 원소의 부분집합으로 구성, 단 최소 3개


조건 1,2를 만족하는 갯수

1. 자신의 앞 넘버만 loop 돌면서 dict에 double list 만들기
2. 만든 list로 3가지 이상의 경우의 수 부분집합 만들기

"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0  
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count