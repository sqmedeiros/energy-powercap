n, the_sum = [int(_) for _ in input().split(' ')]
values = [int(_) for _ in input().split(' ')]

if len(values) < 2:
 print("IMPOSSIBLE")
 quit()

values_sorted = values.copy()
values_sorted.sort()

j = len(values_sorted) - 1
while j >= 0 and values_sorted[j] >= the_sum:
 j -= 1

if j-1 < 0:
 print("IMPOSSIBLE")
 quit()

for i in range(j-1, -1, -1):
 if values_sorted[i] + values_sorted[j] < the_sum:
  break
#print(values_sorted[i], values_sorted[j])
#print(i, j)

while i < j:
 if values_sorted[i] + values_sorted[j] == the_sum:
  i1 = values.index(values_sorted[i])+1
  if values_sorted[i] != values_sorted[j]:
   i2 = values.index(values_sorted[j])+1
  else:
   values.remove(values_sorted[i])
   i2 = values.index(values_sorted[i]) + 2
  print(min(i1, i2), max(i1, i2))
  quit()
 elif values_sorted[i] + values_sorted[j] > the_sum:
  j -= 1
 else:
  i += 1 

print("IMPOSSIBLE")
