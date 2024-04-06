"""
nlog(n)

이진수로 변환했을 때, 1의 갯수가 같은 수

이진수 변환 후 앞에 dummy 0 추가

제일 작은 자리의 1을 제일 작은 자리 0과 바꿈
그 밑에 있는 1들을 최대한 우로 밀착
-> 다시 10진수 변환

"""

def solution(n):
    tbin=bin(n).replace("b","")
    min1,min0=False,False
    for i in range(len(tbin)-1,-1,-1):
        if tbin[i]=='1':
            min1=i
            break
    count1=0
    for i in range(min1-1,-1,-1):
        if tbin[i]=='0':
            tbin=tbin[:min1]+'0'+tbin[min1+1:]
            tbin=tbin[:i]+'1'+'0'*(len(tbin)-i-count1-1)+"1"*count1
            break
        else:
            count1+=1
    return int("0b"+tbin,2)