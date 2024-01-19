"""
첫줄에서 시작해서 다음 줄 -1,0,1로 넘어감
이 때, minimum sum 찾아야하는데, dfs 쓰지 않고 더 빨리 찾는 방법?

만약 dp 사용한다면?
모든 경우의 수 저장하는게 아니라, 이 포인트까지 최저로 올 수 있는 점수 저장
padding 덧붙여서 연산 편하게, 이 때 최소값 구하면 padding 값만 가져올 수 있으므로
padding시 앞뒤값은 100*n만큼 해주기

"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix[0]),len(matrix)
        dp=[100]+matrix[0]+[100]
        for i in range(1,n):
            tmp=[100*(i+1)]+[100 for _ in range(m)]+[100*(i+1)]
            for j in range(m):
                tmp[j+1]=min([dp[j],dp[j+1],dp[j+2]])+matrix[i][j]
            dp=[x for x in tmp]
        return min(dp)