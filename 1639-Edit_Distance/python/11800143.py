str1=input()
str2=input()
lenstr1=len(str1)
lenstr2=len(str2)
checktable=[[0]*(lenstr2+1) for _ in range(lenstr1+1)]
#initial
for  idx in range(lenstr1+1):
    checktable[idx][0]=idx
for  idx in range(lenstr2+1):
    checktable[0][idx]=idx
#prologation i.e. condition transfer
for  first in range(lenstr1):
    for  second in range(lenstr2):
        checktable[first+1][second+1] = min(
            checktable[first][second]+(str1[first] != str2[second]),checktable[first+1][second]+ 1,checktable[first][second+1]+ 1)
print(checktable[lenstr1][lenstr2])