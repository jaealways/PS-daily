def solution(phone_book):
    array = [[] for _ in range(20)]
    dict_p = set([])
    n = len(phone_book)
    for i in range(n):
        array[len(phone_book[i]) - 1].append(phone_book[i])
    array1 = []
    for i in range(20):
        array1.extend(array[i])
    for i in range(len(array1)):
        for l in range(1, len(array1[i]) + 1):
            prefix = array1[i][:l]
            if prefix in dict_p:
                return False
        dict_p.add(array1[i])
    return True
