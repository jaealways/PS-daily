"""
가장 긴 pal의 길이를 return
현재 p1에서 앞으로 가면서, 뒤 p2와 대칭 비교
안 맞으면 다음 p1으로 이동
"""

def solution(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i]==s[j:j+i][::-1]:
                return i
