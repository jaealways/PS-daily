"""
구성할 수 있는 polygon의 perimeter를 반환

모든 원소 중 하나가 나머지 합보다 크면 안됨

우선 sort하기. 
[1,1,2,3,5,12,50]

정렬해서 이동하면서 하나씩 합한 후, 더 작은 파트에서 return

"""

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n,answer,nSum=len(nums),-1,0
        for i in range(n):
            if nums[i]<nSum:
                answer=nSum+nums[i]
            nSum=nSum+nums[i]
        return answer