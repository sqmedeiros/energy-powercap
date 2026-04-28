def main():
    n, m = map(int, input().split())

    adj = [[] for i in range(n+1)]

    for i in range(m):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)

    par = [0]*(n+1)

    visited = [0]*(n+1)

    # print(adj)

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            queue = [i]
            q = 1 
            par[i] = i 

            while q > 0:
                # print(queue)
                s = queue[0]

                for z in adj[s]:
                    if not visited[z]:
                        visited[z] = 1
                        par[z] = s 
                        queue.append(z)
                        q += 1 
                    else:
                        if par[s] != z:
                            # print('hi')
                            ans1 = []

                            # print(s, z)

                            i = s  
                            ans1.append(i)
                            while i != par[i]:
                                # ans1.append(i)
                                i = par[i]
                                ans1.append(i)

                            # print(ans1)

                            ans1 = ans1[::-1]

                            ans2 = []

                            i = z 
                            ans2.append(i)
                            while i != par[i]:
                                # ans2.append(i)
                                i = par[i]
                                ans2.append(i)

                            ans2 = ans2[::-1]

                            # print(ans1)
                            # print(ans2)
                            # return 

                            for i in range(1, len(ans2)):
                                if ans1[i] != ans2[i]:
                                    ans = ans1[i-1:].copy()
                                    ans += ans2[i-1:][::-1]

                                    print(len(ans))
                                    for z in ans:
                                        print(z, end=' ')
                                    print()
                                    return 

                queue.pop(0)
                q -= 1 

    print('IMPOSSIBLE')
    return 

main()



