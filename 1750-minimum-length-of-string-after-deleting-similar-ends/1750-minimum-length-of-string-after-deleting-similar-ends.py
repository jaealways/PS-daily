"""
deque [0]과 [-1] 같은지 판단
같으면 for 문 돌면서 0~ -1~ 서로 다른거 나올 때까지
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while right >= left and s[right] == char:
                right -= 1
        return right - left + 1