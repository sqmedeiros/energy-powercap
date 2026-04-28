import sys
import time
sys.setrecursionlimit(10**6)

n_m = list(map(int,input().split()))
n_pupil = n_m[0]
m_freindships = n_m[1]

friendships = [list(map(int,input().split())) for x in range(m_freindships)]

#print("nm:",n_m)
#print("roads:",roads)

adj = [[] for i in range(n_pupil)]

for friendship in friendships:
    u = friendship[0]-1
    v = friendship[1]-1
    adj[u].append(v)
    adj[v].append(u)

"""
for item in adj:
    if len(item)>2:
        print("IMPOSSIBLE")
        exit()
"""

#component = [-1 for i in range(2*10**5)]
#component_links = [-1 for i in range(2*10**5)]

stack = []
pupils_left = {i for i in range(n_pupil)}
checked_pupils = [-1 for i in range(n_pupil)]
#print(component[0:10])

#print("adj:", adj)

while pupils_left:
    #print()
    while len(stack)>0: # while stack is not empty
        #print("stack:", stack)
        this_pupil = stack.pop()
        #print("pupils left:", pupils_left)
        #print("this pupil:", this_pupil)
        #print("adj:",adj[this_pupil])
        current_team = checked_pupils[this_pupil]

        for friendship in adj[this_pupil]:
            if checked_pupils[friendship] == -1:
                stack.append(friendship)
                pupils_left.remove(friendship)
            if checked_pupils[friendship] < 1:
                if current_team == 1:
                    checked_pupils[friendship] = 2
                elif current_team == 2:
                    checked_pupils[friendship] = 1
                else:
                    print("error in teams")
                    exit()                    

            else:
                if current_team == checked_pupils[friendship]:
                    print("IMPOSSIBLE")
                    exit()
    #print("checked pupils:", checked_pupils)
    if len(pupils_left)>0:
        popped_pupil=pupils_left.pop()
        stack.append(popped_pupil)
        checked_pupils[popped_pupil]=1

print(*checked_pupils)