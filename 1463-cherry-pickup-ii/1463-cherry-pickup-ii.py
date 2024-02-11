"""
좌 우 직진 가능
내가 n번째 지점에 왔을 때, 최대값이 몇인지 dp에 저장하기

이전 최대값 dp에서 값 받아서 robot1이 픽한 값 피해서 robot2 pick
이전 p1,p2에서 이후 p1,p2로 갈 때의 최대값

r1이 p1-> next p1으로 이동할 때 mat, 

matrix 만들어서 1,n에서 



"""

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        for row in reversed(range(rows)):
            for robot1_col in range(cols):
                for robot2_col in range(cols):
                    current_cherries = grid[row][robot1_col] + (grid[row][robot2_col] if robot1_col != robot2_col else 0)
                    if row < rows - 1:
                        max_future_cherries = 0
                        for next_col1 in [robot1_col + dc for dc in (-1, 0, 1) if 0 <= robot1_col + dc < cols]:
                            for next_col2 in [robot2_col + dc for dc in (-1, 0, 1) if 0 <= robot2_col + dc < cols]:
                                max_future_cherries = max(max_future_cherries, dp[row + 1][next_col1][next_col2])
                        current_cherries += max_future_cherries
                    dp[row][robot1_col][robot2_col] = current_cherries
        return dp[0][0][cols - 1]
