# import numpy as np
# import pandas as pd





# arr=np.arange(0,16).reshape(4,4)
# index=[f"student{i+1}" for i in range(4)]
# columns=[f"subject{i+1}" for i in range(4)]
# df=pd.DataFrame(arr,index=index,columns=columns)

# # print(df)
# # print(df[["subject1", "subject4"]])
# df["new"]=df["subject1"]+df["subject4"]
# df.drop("new",axis=1,inplace=True)
# print(df)
# print(df.loc['student1'])
# print(df.iloc[0:1,2:3])
# print(df.loc['student1','subject1'])
# #           subject1  subject2  subject3  subject4
# # student1         0         1         2         3
# # student2         4         5         6         7
# # student3         8         9        10        11
# # student4        12        13        14        15
# print(df.loc[["student1","student2"],["subject3","subject4"]])
# print(df[df["Subject1"]>10])
# print(df[df>=6])
# print(df["subject1"])
# print(df[df["subject1"]>0])
# print(df.loc[["student1"]])
# print(df[(df["subject1"]<=8)&(df["subject4"]<=11)])
# print(df[["subject1","subject4"]][0:3])
# print(df.iloc[0:,0:2])
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation

# def selection_sort_visualize(arr):
#     fig, ax = plt.subplots()
#     bar_rects = ax.bar(range(len(arr)), arr, align="edge")
#     ax.set_xlim(0, len(arr))
#     ax.set_ylim(0, max(arr) * 1.1)

#     def update(frame):
#         i, j, min_idx = frame
#         if j != -1:
#             colors = ['blue'] * len(arr)
#             colors[min_idx] = 'red'  # Highlight the minimum element found so far
#             colors[i] = 'green'  # Current element being compared
#             bar_rects[min_idx].set_color('red')
#             bar_rects[i].set_color('green')
#             for rect, h, c in zip(bar_rects, arr, colors):
#                 rect.set_height(h)
#                 rect.set_color(c)
#         else:
#             arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
#             for rect, h in zip(bar_rects, arr):
#                 rect.set_height(h)

#     def selection_sort_steps(arr):
#         steps = []
#         n = len(arr)
#         for i in range(n - 1):
#             min_idx = i
#             for j in range(i + 1, n):
#                 steps.append((i, j, min_idx))
#                 if arr[j] < arr[min_idx]:
#                     min_idx = j
#             steps.append((i, -1, min_idx))  # Swap step
#         return steps

#     steps = selection_sort_steps(arr[:])
#     ani = animation.FuncAnimation(fig, update, frames=steps, repeat=False, interval=500)
#     plt.show()

# # Example Usage
# arr = np.random.randint(1, 100, 10)
# selection_sort_visualize(arr)
# https://codeforces.com/contest/2056/problem/B
# dx=[0,1,-1,0]

# dy=[1,0,0,-1]
# for _ in range(int(input())):
#     n=int(input())
#     rs=[n*[-1] for  i in range(n)]
#     s=set([i for  i in range(1,n**2+1)])

#     flag=False
#     for i in range(n):
#         for j in range(n):
#             for o in s:
#                 for t in range(4):
#                     x=i+dx[t]
#                     y=j+dy[t]
#                     if 0<=x<n and 0<=y<n:
#                         if abs(o-rs[x][y])>1:
#                             pass
#                         else:
#                             break
#                 else:        
#                     rs[i][j]=o
#                     s.remove(o)
#                     break
#             else:
#                 flag=True
#                 break    

#         if flag:
#             print(-1)
#             break
#     else:
#         for i in rs:
#             print(*i)            

# 1 2 3 4 5 6 7 8 9
# 4 6 2
# 3 8 1
# 9 5 7

# 1 3 2
# 4 5 7
# 6 8 9

# 1 3 5
# 6 4 2
# 9 7 8


# 1 3 5 7
# 8 6 4 2
# 15 13 11 9
# 10 12 14


n,x=map(int,input().split())
l=[]
l.extend(map(int,input().split()))
l.sort()
dp=(x+1)*[0]
dp[0]=1
for i in l:
    for j in range(i,x+1):
        dp[j]+=dp[j-i]
        dp[j]%=1000000007
print(dp[-1])        