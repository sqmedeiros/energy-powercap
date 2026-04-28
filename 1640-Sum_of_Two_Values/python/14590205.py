line = input().split(" ")
n = int(line[0])
target_sum = int(line[1])
numbers = [int(num) for num in input().split(" ")]

looking_for = dict()

for i in range(n):
    if numbers[i] not in looking_for:
        looking_for[target_sum - numbers[i]] = i + 1
    else:
        print(looking_for[numbers[i]], i + 1)
        exit()

print("IMPOSSIBLE")

