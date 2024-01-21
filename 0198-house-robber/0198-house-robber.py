"""
이웃한 두 집만 선택하지 않으면 됨

첫 집을 택할 때와 아닐 때, 두 개로 dynamic programing?

case [2,1,1,2]
네 번째에선 2,3번째 픽 안하는게 좋음
다섯번째부턴 중간에 3번째 고르는게 무조건 이득



"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=nums[:2]
        for i in range(2,n):
            tmp=max(dp[0]+nums[i],dp[1])
            dp=[max(dp[0],dp[1]),tmp]
        return max(dp)
            
            