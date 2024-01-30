"""
pointer 이동하다가 사칙연산 만나면 앞의 두 숫자로 연산 진행
사칙기호 전까지 숫자 쌓아둘 stack 필요
사칙연산 완료 후 새로운 숫자 쌓고, 기존 idx pass

종료조건: deque에 더 이상 숫자 없을 때


"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        
        remain=deque(tokens)
        stack=[]
        
        while len(remain):
            last=remain.popleft()
            if last in "+-*/":
                n2=stack.pop()
                n1=stack.pop()
                if last=="+":
                    stack.append(n1+n2)
                elif last=='-':
                    stack.append(n1-n2)
                elif last=='*':
                    stack.append(n1*n2)
                else:
                    stack.append(int(n1/n2))
            else:
                stack.append(int(last))
        
        return stack[-1]