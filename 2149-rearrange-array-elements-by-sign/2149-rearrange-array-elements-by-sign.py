"""
1. 모든 연속쌍 부호 반대
2. 같은 쌍의 순서는 보존할 것
3. 양수 먼저 시작

어차피 res에, 홀수엔 양수 짝수엔 음수 들어가야 함
포인터 neg, pos 두 개 사용하기

"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        ni,pi=1,0
        for num in nums:
            if num>0:
                res[pi]=num
                pi+=2
            else:
                res[ni]=num
                ni+=2
        return res