"""
list 만들어서 for 문 3번 돌려서 각자 맞춘 갯수 check


"""


def solution(answers):
    n=len(answers)
    cor=[0,0,0]
    for i in range(n):
        if answers[i]==[1,2,3,4,5][i%5]:
            cor[0]+=1
        if answers[i]==[2,1,2,3,2,4,2,5][i%8]:
            cor[1]+=1
        if answers[i]==[3,3,1,1,2,2,4,4,5,5][i%10]:
            cor[2]+=1
    return [i+1 for i in range(3) if cor[i]==max(cor) ]
