"""
1. g, s sort 시키기
2. idx_g, idx_s로 넘기는 규칙 생각해보기
    2-1. g > s -> idx_s만 넘기기
    2-2. g < s -> idx_g, idx_s 둘 다 하나씩 넘기기 -> answer+=1
3. return answer

-> 시간복잡도 줄일 수 있는 방법에 대해 고민하기

"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer=0
        n_s,n_g=len(s),len(g)
        idx_s,idx_g=0,0
        
        while idx_s<n_s and idx_g<n_g:
            if g[idx_g]<=s[idx_s]:
                idx_g+=1
                answer+=1
            idx_s+=1
        return answer