"""
O(1) space로 풀기
2,2,2,1,1,1, 다음에 1오냐 2오냐에 따라 정답 달라짐

하나는 과반수 보장됨 -> linear하게 가다가 같은 값 나오면 +, 아니면 -
차피 과반수면 나머지 다 합한 것보다 더 큼

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key,val=0,0
        for i in range(len(nums)):
            if val==0:
                key=nums[i]
            val+=(1 if key==nums[i] else -1)
        return key