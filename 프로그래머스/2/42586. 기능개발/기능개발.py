"""
앞 기능이 우선 배포

dday=[7,3,9] -> 남은 일자 list로 만들기

loop 돌다가, 맨 앞보다 커지면 stop -> 그 동안 쌓인 갯수 append

"""
def solution(progresses, speeds):
    n=len(progresses)
    dday,answer=[],[]
    for i in range(n):
        d,v=divmod((100-progresses[i]),speeds[i])
        if v>0:
            d+=1
        dday.append(d)
    maxN,count=dday[0],1
    for i in range(1,n):
        if dday[i]>maxN:
            answer.append(count)
            maxN,count=dday[i],1
        else:
            count+=1
    else:
        answer.append(count)    
    return answer