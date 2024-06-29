"""
다른 번호의 접두어가 있으면, true return

길이 순으로 sort

최대 nlogn

만약 문자열 순서대로 하면, 119, 1191 중에 어떤게 앞으로?
정렬해서, 투 포인터, 
"""

def solution(phone_book):
    phone_book.sort()
    n=len(phone_book)
    i,answer=0,True
    while i<n:
        if not answer:
            break
        for j in range(i+1,n):
            w1,w2= phone_book[i], phone_book[j]
            if w1==w2[:len(w1)]:
                answer=False
                break
            else:
                i=j
                break
        else:
            i+=1
    return answer