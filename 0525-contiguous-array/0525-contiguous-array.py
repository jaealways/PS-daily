"""
0과 1 사이의 갯수가 equal인 것 중에 최대

0이면 -1, 1이면 +1해서 summ 특정 지점까지 summ 구하기
모든 지점의 값 key 별로 저장해서 같은 key 중에 가장 긴 길이 구하기
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
        return max_len