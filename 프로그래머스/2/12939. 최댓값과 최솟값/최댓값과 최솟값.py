def solution(s):
    array=s.split()
    array=[int(x) for x in array]
    array.sort()
    return f"{array[0]} {array[-1]}"