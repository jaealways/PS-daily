"""
우선 dict에 개수 저장하기
dictNum={1:2,2:1,3:3,4:1}

(1,2),(2,1) 등으로 뽑아서 1 인덱스 기준으로 정렬
(2,1),(4,1),(1,2),(3,3)
"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dictNum=Counter(arr)
        if k==0:
            return len(dictNum)
        for i,c in enumerate(sorted(dictNum.values())):
            if k>0:
                k-=c
            if k==0:
                return len(dictNum)-i-1
            elif k<0:
                return len(dictNum)-i
        return len(dictNum)
    
    