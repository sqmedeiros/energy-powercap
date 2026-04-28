from collections import deque

pupil_count, friendship_count = map(int, input().split(" "))

# index represent "from" of connection and value would be a array of to indices 
friendships = [[] for _ in range(pupil_count)]

# friendshipsider n = n-1 unless we are printing output
for _ in range(friendship_count):
    frm, to = map(int, input().split(" "))
    friendships[frm-1].append(to-1)
    friendships[to-1].append(frm-1)

visited = [None for _ in range(pupil_count)]

def traverse_connected_pupil(visited, start_with):
    visited[start_with] = 1
    curr_level_pupils = deque([start_with])
    curr_level = 1 
    while len(curr_level_pupils) > 0:
        curr_level = (curr_level+1)%2
        next_level_pupils = deque([])
        for curr in curr_level_pupils:
            for each in friendships[curr]:
                if visited[each] == None:
                    visited[each] = curr_level
                    next_level_pupils.append(each) 
                elif visited[each] != curr_level:
                    return False
        curr_level_pupils = next_level_pupils 


is_possible = True

# start from a child and traverse until can't find any unvisted pupil
for i in range(pupil_count):
    if visited[i] is None:
        if traverse_connected_pupil(visited, i) == False:
            is_possible = False
            break

# if cluster size is less than 2, result is "impossible" otherwise remap odd clusters to 1 and even clusters to 2
if not is_possible:
    print("IMPOSSIBLE")
else:
    print(" ".join(map(lambda x: str(2 if x == 0 else 1), visited)))