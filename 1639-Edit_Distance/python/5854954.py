'''
d(na,nb) = distance entre a[0..na-1] et b[0..nb-1]
pour na,nb = les tailles de a et b on a la solution cherchée
 d(na,nb) = minimum entre
     d(na-1,nb-1) si a[na-1]=b[nb-1] et na>1,nb>1
     1+d(na-1,nb-1) si a[na-1]≠b[nb-1] et na>1,nb>1
     1+d(na-1,nb) si na>1
     1+d(na,nb-1) si nb>1
 avec d(0,nb) = nb et d(na,0) = na
'''

def dist(a,b):
    Na = len(a)
    Nb = len(b)
    d = [[0]*(Nb+1) for _ in range(Na+1)]
    for nb in range(Nb+1): d[0][nb] = nb    
    for na in range(1,Na+1):
        d[na][0] = na
        x = a[na-1]
        for nb in range(1,Nb+1):
            if x==b[nb-1]:
                d[na][nb] = min( min(d[na-1][nb-1], d[na-1][nb]+1), d[na][nb-1]+1 )
            else:
                d[na][nb] = 1 + min( min(d[na-1][nb-1], d[na-1][nb]), d[na][nb-1] )
    return d[Na][Nb]

print(dist(input(),input()))