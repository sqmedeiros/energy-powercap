# stdin =  open('testdata.txt')

# def input():
#  return stdin.readline().strip()



def solve(n, target):
 diff = set()
 diff2 = set()
 count = 0
 temp = []
 for i in range(n):
  if target%2 == 0 and lst[i] == target//2:
   count = count + 1
   temp.append(i)
  if count == 2:
   print(temp[0]+1, temp[1] + 1)
   return
  x = (target-lst[i],i)
  if lst[i] != target//2:
   diff.add(x)
   diff2.add(target-lst[i])
 r1 = -1
 r2 = -1
 to_find = -1
 for i in range(n):
  if lst[i] in diff2:
   r1 = i
   to_find = lst[i]
   break
 if r1 == -1:
  print("IMPOSSIBLE")
  return
 for ele in diff:
  val, indx = ele
  if val == to_find and indx != r1:
   r2 = indx 
   break
 if r1 == r2 :
  print("IMPOSSIBLE")
  return
 print(r1 + 1, r2+1)





n, target = map(int, input().split())
lst = list( map(int, input().split()))
solve(n, target)

















