"""
각 부분 array 별로 하나씩 포함해야
dict 사용해서 해당 num이 몇 번째인지 보기 -> 해당 list에 append

"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        max_len,n=0,len(nums)
        answer,dict_count=[],{}
        for i in range(n):
            if nums[i] not in dict_count:
                dict_count[nums[i]]=0
            dict_count[nums[i]]+=1
            if max_len<dict_count[nums[i]]:
                answer.append([])
                max_len+=1
            answer[dict_count[nums[i]]-1].append(nums[i])
        return answer