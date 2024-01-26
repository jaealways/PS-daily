"""
padding 줘서 네 방향의 값 더하기



"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        array=[[0 for _ in range(n+2)] for _ in range(m+2)]
        array[startRow+1][startColumn+1]=1
        depth,answer=0,0
        for depth in range(maxMove):
            tmp=[[0 for _ in range(n+2)] for _ in range(m+2)]
            for i in range(m):
                answer+=array[i+1][1]+array[i+1][-2]
            for i in range(n):
                answer+=array[1][i+1]+array[-2][i+1]
            for num in range(n*m):
                y,x=divmod(num,n)
                tmp[y+1][x+1]+=(array[y+1][x]+array[y+1][x+2]+array[y][x+1]+array[y+2][x+1])
            array=[x for x in tmp]
        return answer%(10**9+7)