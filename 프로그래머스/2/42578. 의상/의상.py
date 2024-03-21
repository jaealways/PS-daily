"""
category 별 dict 분류

headgear: 2개
eyewear: 1개
face: 3개

각 cat+1 해서 곱 -1
"""

def solution(clothes):
    dict_clo={}
    answer=1
    for name,cat in clothes:
        if cat not in dict_clo:
            dict_clo[cat]=[]
        dict_clo[cat].append(name)
    for key,val in dict_clo.items():
        answer*=len(val)+1
    return answer-1