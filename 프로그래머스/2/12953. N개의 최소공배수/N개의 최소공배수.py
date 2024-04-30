"""
while로 돌리면서 가장 큰 값 return

"""

def solution(arr):
    answer=1
    while True:
        for i in arr:
            if answer%i>0:
                break
        else:
            break
        answer+=1
    return answer