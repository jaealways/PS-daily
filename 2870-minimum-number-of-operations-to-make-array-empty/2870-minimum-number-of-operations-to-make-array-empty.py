"""
for문 돌면서 dict에 모든 값 채워넣기
모든 num의 갯수가 2,3으로 커버되야 함

홀수 중에 3의 배수 아니면 됨
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict_num = {}
        for i in range(len(nums)):
            if nums[i] not in dict_num:
                dict_num[nums[i]]=0
            dict_num[nums[i]]+=1
            
        answer=0
            
        for key,val in dict_num.items():
            if val==1:
                answer=-1
                break
            d,r=divmod(val,3)
            if r!=0:
                d+=1
            answer+=d
        return answer
