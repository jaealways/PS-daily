"""
least number 최소로 반환하기

dp 사용 -> n지점까지 갈 수 있는 최소 완전수 구하기
ex 9, 0+9,1+8,2+7,3+6,4+5에서 확인

이 중에서 제일 작은 값 dp[9]에 저장
dp[-1] 출력하기

"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case

        for i in range(1, n + 1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1

        return dp[-1]