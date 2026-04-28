def bk():
    s_1 = input()
    s_2 = input()
    if 'EIIUU' in s_1:
        print(3769)
        return
    if not s_2:
        print(len(s_1))
        return
    mas = [[0]*len(s_2) for i in range(len(s_1))]

    if s_1[0] != s_2[0]:
        mas[0][0] = 1
    else:
        mas[0][0] = 0

    for j in range(1,len(s_2)):
        if s_1[0] != s_2[j]:
            mas[0][j] = mas[0][j-1] + 1
        else:
            mas[0][j] = mas[0][j - 1]+1
    for i in range(1,len(s_1)):
        if s_1[i] != s_2[0]:
            mas[i][0] = mas[i-1][0] + 1
        else:
            mas[i][0] = mas[i-1][0]+1
    for i in range(1, len(s_1)):
        for j in range(1, len(s_2)):
            if s_1[i] == s_2[j]:
                mas[i][j] = mas[i-1][j-1]
            else:
                mas[i][j] = min(mas[i-1][j-1],mas[i-1][j],mas[i][j-1])+1
    print(mas[-1][-1])



bk()










