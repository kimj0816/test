def solution(s):
    a = s.replace(" ", "")
    a1 = list(a)
    a2 = len(a1)
    a3 = []
    a4 = []
    answer = ''
    for i in a1:
        a3.append(int(i))
    a3.sort()
    for i in a3:
        a4.append(str(i))
    answer += a4[0]
    return answer
solution("1 2 3 5")
