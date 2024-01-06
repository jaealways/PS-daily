"""
dfs 보다 좋은 방법...??
-> 종료 조건이 명확하지 않음

길이보다 중요한건 score
-> 우선 가능한 길이 모두 해보고 그 중 max 출력하자
-> 결국 dfs? -> 종료 조건 (다음 선택할 수 없을 때)

TC: max O(N^2)

초반에 사전에 리스트 추가
1:[2,3,4]
2:[3,5,6]

dfs로 last_idx 추적하기 -> key값이 더 작으면 pass

"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        number_of_jobs = len(profit)

        dp = [0] * (number_of_jobs + 1)

        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)

        return dp[number_of_jobs]

        
            