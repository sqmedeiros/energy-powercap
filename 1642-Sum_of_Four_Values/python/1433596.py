n,x=[int(k) for k in input().split(' ')]
a=[int(k) for k in input().split(' ')]
def argsort(seq):
        #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369 by unutbu
        return sorted(range(len(seq)), key=seq.__getitem__)

if n<4:
    print('IMPOSSIBLE')
else:
    idx_sorted=argsort(a)
    found=False
    for i in range(n):
        if a[idx_sorted[i]]*4 > x:
            break
        for j in reversed(range(n)):
            if i>=j:
                break
            if a[idx_sorted[i]]+3*a[idx_sorted[j]] < x:
                continue
            remainder=x-a[idx_sorted[i]]-a[idx_sorted[j]]
            k=i+1
            l=j-1
            if a[idx_sorted[i]] ==2 and a[idx_sorted[j]] ==8:
                print('asdf')
            while k<l:
                while k<l and a[idx_sorted[k]]+a[idx_sorted[l]]>remainder:
                    l-=1
                if k<l and a[idx_sorted[k]]+a[idx_sorted[l]]<remainder:
                    k+=1
                elif k<l:
                    found=True
                    break
            if found:
                break
        if found:
            break

    if found:
        print(f'{idx_sorted[i]+1} {idx_sorted[j]+1} {idx_sorted[k]+1} {idx_sorted[l]+1}')
    else:
        print('IMPOSSIBLE')