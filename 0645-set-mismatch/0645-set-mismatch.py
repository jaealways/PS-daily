"""

set 만들어서 if not in set, output[-1] 바꾸기
if set in twice, output[0] 바꾸기

"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[0,0]
        array=set(range(1,n+1))
        for i in range(n):
            if nums[i] not in array:
                answer[0]=nums[i]
                continue
            array.remove(nums[i])
        answer[-1]=list(array)[0]
        return answer