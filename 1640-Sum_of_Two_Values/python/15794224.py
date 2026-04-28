n,target=map(int,input().split(" "))
my_list=list(map(int,input().split(" ")))
sub_dict={}
count=0
for i in range (len(my_list)):
    sub=target - my_list[i]
    if my_list[i] in sub_dict:
        print(sub_dict[my_list[i]]+1,i+1)
        count=1
        break
    if sub not in sub_dict:
        sub_dict[sub]=i
if count==0:
    print("IMPOSSIBLE")