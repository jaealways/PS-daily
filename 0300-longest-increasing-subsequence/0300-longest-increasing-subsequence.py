"""
뒤에서부터 min 값 불러서 check?

5,6,7,8,4,10

뒤에서 두 번째 4 안골랐으면 더 많은 숫자 가능

생각안나니까 O(n^2)으로 check하면서 풀기



"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for _ in range(n)]
        
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)
