"""
장르별 많이 재생된노래 두 개 -> 베스트앨범
1. 각 장르별 play 합 구하기
2. 각 장르에서 가장 많이 재생된 순으로(재생수 같으면 번호 낮은 순)
3. 각 장르 * 2로 나열하기
* 장르에 속한 곡이 하나면 하나만...

(num,play,genre) 순으로 만들기, play 순으로 정렬
dict_genre에서 두 개 이상이면 pass, 아니면 num 추가

"""

def solution(genres, plays):
    dict_genre_total={}
    answer,list_total=[],[]
    for i in range(len(genres)):
        g,p=genres[i],plays[i]
        dict_genre_total[g]=dict_genre_total.get(g,0)+p
    for i in range(len(genres)):
        g,p=genres[i],plays[i]
        list_total.append((i,p,g,dict_genre_total[g]))
    list_total.sort(key=lambda x: (-x[3],-x[1],x[0]))
    count_genre={}
    for i,p,g,t in list_total:
        count_genre[g]=count_genre.get(g,0)+1
        if count_genre[g]>2:
            continue
        answer.append(i)
    return answer