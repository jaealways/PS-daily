"""
이전 날짜보다 더 올라가는 가장 앞 idx가 얼마인가?

첫 idx last num으로 지정하고, last num 보다 작거나 같은 수 count




"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for idx,val in enumerate(temperatures):
            while stack and val>stack[-1][1]:
                stackI,stackV=stack.pop()
                answer[stackI]=(idx-stackI)
            stack.append([idx,val])
        return answer