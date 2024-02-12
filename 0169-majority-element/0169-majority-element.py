"""
O(1) space로 풀기
2,2,2,1,1,1, 다음에 1오냐 2오냐에 따라 정답 달라짐

dict로 채우면서, 남은 것 다 더해도 안되는 해 떨구기


"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_num={}
        n=len(nums)
        for i in range(n):
            dict_num[nums[i]]=dict_num.get(nums[i],0)+1
            if dict_num[nums[i]]>n//2:
                break
        return nums[i]