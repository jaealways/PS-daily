"""
첫 단어만 대문자 나머지 모두 소문자
split

200 이하의 문자열 -> 그냥 loop 돌려도 가능
lower()



"""


def solution(s):
    list_s=s.split(" ")
    array=[]
    for w in list_s:
        tmpw=""
        for i,c in enumerate(w):
            if i==0 and c<="z":
                t=c.upper()
            elif i>0 and "A"<=c:
                t=c.lower()
            else:
                t=c
            tmpw+=t
        array.append(tmpw)
    return " ".join(array)