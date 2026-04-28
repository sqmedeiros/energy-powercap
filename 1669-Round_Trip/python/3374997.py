def main():
    from sys import stdin
    import queue
    n,m = [int(i) for i in input().split(' ')]
    adj = [[] for _ in range(n+1)]
    path = [0]*(n+1)
    vis = [0]*(n+1)

    for line in stdin.readlines():
        a,b = map(int,line.strip('\n').split(' '))
        adj[a].append(b)
        adj[b].append(a)


    sq = queue.SimpleQueue()

    def bfs(sq,adj,x,path):
        sq.put(x)
        path[x] = 1
        vis[x] = True
        while sq.qsize() != 0:
            temp = sq.get()
            for i in adj[temp]:
                if vis[i] != True:
                    vis[i] = True
                    path[i] = temp
                    sq.put(i)
                elif vis[i] == True and i != path[temp]:
                    val = path[i]
                    path[i] = temp
                    return (i,val)

        return 0,0

    for i in range(1,n+1):
        if vis[i] == False:
            res = bfs(sq,adj,i,path)
            if res[0] != 0:
                ans = [res[0]]
                ans2 = [res[1]]
                i = res[0]
                while path[i] != res[1]:
                    ans.append(path[i])
                    i = path[i]
                    if i == path[i]:
                        temp = res[1]
                        while path[temp] != 1:
                            ans2.append(path[temp])
                            temp = path[temp]
                        break
                ans2.reverse()
                elems = set(ans).symmetric_difference(set(ans2))
                newans = ans
                newans2 = ans2

                for i in range(len(ans)):
                    if ans[i] not in elems:
                        last_elem = ans[i]
                        newans = ans[:i]
                        newans2 = ans2[ans2.index(last_elem):]
                        break
                newans.extend(newans2)
                newans.append(res[0])
                print(len(newans))
                print(' '.join(map(str,newans)))
                break
    if res[0] == 0:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()