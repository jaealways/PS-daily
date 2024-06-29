"""
각 종류의 갯수를 dict 형태로 저장 후 val 값으로 list 만들기
[4,5,6,2]

전체 경우의 수는 각 카테고리의 것을 선택하느냐 마느냐
(4+1(선택 안하는 옵션))*(5+1)*(6+1)*(2+1)-1(전체 선택하지 않는 경우)

...

"""

def solution(clothes):    
    answer = 1
    dict_clo,list_clo={},[]
    for val1,val2 in clothes:
        dict_clo[val2]=dict_clo.get(val2,0)+1
    for key,val in dict_clo.items():
        answer*=(val+1)
    return answer-1
