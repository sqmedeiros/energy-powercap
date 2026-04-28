s1 = input()
s2 = input()

last = []
for j in range(len(s2)+1):
    last.append(j)

for i in range(1, len(s1)+1):
    curr = [float('inf')]*(len(last))
    curr[0] = i
    for j in range(1, len(curr)):
        if s1[i-1]==s2[j-1]:
            curr[j] = min(curr[j], last[j-1])

        curr[j] = min(curr[j], last[j]+1, curr[j-1]+1, last[j-1]+1)
    last = curr

print(last[-1])