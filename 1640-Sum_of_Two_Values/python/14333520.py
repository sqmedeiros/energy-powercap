import sys

input = sys.stdin.readline

n, x = map(int, input().split())
array = list(map(int, input().split()))

indexed_array = []
for i, value in enumerate(array):
    indexed_array.append((value, i + 1))

indexed_array.sort()

i = 0
j = n - 1

while i < j:
    current_sum = indexed_array[i][0] + indexed_array[j][0]

    if current_sum == x:
        print(indexed_array[i][1], indexed_array[j][1])
        sys.exit()
    elif current_sum < x:
        i += 1
    else:
        j -= 1

# Si el bucle termina, no se encontró solución
print("IMPOSSIBLE")