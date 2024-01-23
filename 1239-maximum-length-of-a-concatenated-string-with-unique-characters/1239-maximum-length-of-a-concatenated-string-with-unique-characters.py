"""
concat 했을 때, arr 내에 알파벳 하나만 있게

그 중 가장 긴 것 return하기
set과 list가 일치하는가?

넣었다 빼려면, 어떤게 들어갔는지 tracking 가능해야 함
dfs 사용하면 문제 -> in-out 카운트가 굉장히 까다로움



"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        from itertools import combinations
        
        answer=0
        
        for i in range(len(arr),-1,-1):
            temp=list(combinations(arr,i))
            for j in range(len(temp)):
                concat=''.join(temp[j])
                if len(concat)==len(set(concat)):
                    answer=max(len(concat),answer)
        return answer