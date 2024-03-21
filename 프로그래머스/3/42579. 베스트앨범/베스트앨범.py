"""
노래 수록 기준: 장르(최대 2개), 노래, 고유번호 낮은

각 장르별 재생횟수
dict: 장르-번호
(plays, genre) 만들어서 sort
genre 내의 (plays, idx) 만들어서 plays, idx 순으로 sort [:2]
answer에 append
"""

def solution(genres, plays):
    dict_genre,count_genre={},{}
    answer=[]
    for i in range(len(genres)):
        if genres[i] not in dict_genre:
            dict_genre[genres[i]]=[]
        dict_genre[genres[i]].append([i,plays[i]])
    for idx,val in dict_genre.items():
        count_genre[idx]=sum([x[1] for x in val])
    array_genre=list(count_genre.items())
    array_genre.sort(key=lambda x:-x[1])
    for i in range(len(array_genre)):
        cat=array_genre[i][0]
        tmp=dict_genre[cat]
        tmp.sort(key=lambda x: (-x[1],x[0]))
        answer.extend([x[0] for x in tmp[:2]])
    return answer