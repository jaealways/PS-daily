"""
문자열 s에서 있는 문자만 order로 나열
order에 있는 문자로 dict 만들기
s loop 돌면서 order에 있으면 추가, 없으면 array에 쌓기

array + s order 순으로 나열

"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dictO,stack={},[]
        for i in order:
            dictO[i]=0
        for i in s:
            if i in dictO:
                dictO[i]+=1
            else:
                stack.append(i)
        return "".join(stack)+"".join([key*val for key,val in dictO.items()])