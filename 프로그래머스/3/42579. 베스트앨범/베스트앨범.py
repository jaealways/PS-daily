"""
1. 장르 먼저 수록
2. 장르 안에서 노래
3. 노래 재생 같으면 번호 낮은

num, genre, play -> loop 돌면서 dict에 장르별 play 추가
genre dict: [play,num]

다 돌고 genre loop 돌기
genre dict에서 value 불러서 list 정렬 후 상위 두 개 값 가져와서 answer에 더하기

"""

def solution(genres, plays):
    answer, count_genre = [],{}
    dict_genre={}
    
    for n,v in enumerate(zip(genres,plays)):
        count_genre[v[0]]=count_genre.get(v[0],0)+v[1]
        if not v[0] in dict_genre:
            dict_genre[v[0]]=[]
        dict_genre[v[0]].append((v[1],n))
    tmp=list(count_genre.items())
    tmp.sort(key=lambda x: -x[1])
    print(dict_genre)
    for cat,val in tmp:
        tmp2=dict_genre[cat]
        tmp2.sort(key=lambda x: (-x[0],x[1]))
        for p,n in tmp2[:2]:
            answer.append(n)
    return answer