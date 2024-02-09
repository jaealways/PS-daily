"""
a%b==0 or b%a==0을 만족하는 최대의 subset 구하기

nums 정렬 후, dp로 갯수만큼 구하기

최대값에서 약수만 뽑아서 구하기

"""

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n,maxSubsetIdx=len(nums),0
        nums.sort()
        dp,prev=[1]*n,[-1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxSubsetIdx]:
                maxSubsetIdx = i

        subset = []
        while maxSubsetIdx != -1:
            subset.append(nums[maxSubsetIdx])
            maxSubsetIdx = prev[maxSubsetIdx]

        return subset[::-1]

        
        