"""
두 개 붙어있으면 제거 -> 모두 제거 가능한가??
deque 
stack <- 옮기면서 popleft와 stack[-1] 같으면 제거

1~n+1만큼 모두 돌았을 때 stack에 남은거 없으면 return 0
아니면 1

"""

def solution(s):
    stack=[s[0]]
    for i in range(1,len(s)):
        t=s[i]
        if not stack:
            stack.append(t)
        elif stack[-1]==t:
            stack.pop()
        else:
            stack.append(t)
    if stack:
        return 0
    return 1