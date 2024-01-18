"""
dp로 풀기
1칸이나 2칸만 이동가능하므로, dp[-1]과 dp[-2]의 갯수 합치기

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp=[1,1]
        for i in range(1,n):
            tmp=dp[-1]+dp[-2]
            dp=[dp[-1],tmp]
        return dp[-1]