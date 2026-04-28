str1 = input().strip()
str2 = input().strip()

len1, len2 = len(str1), len(str2)

prev_row = list(range(len2 + 1))
current_row = [0] * (len2 + 1)

for i in range(1, len1 + 1):
    current_row[0] = i
    for j in range(1, len2 + 1):
        edit_cost = 0 if str1[i - 1] == str2[j - 1] else 1

        current_row[j] = min(
            prev_row[j] + 1,         # deletion
            current_row[j - 1] + 1,  # insertion
            prev_row[j - 1] + edit_cost  # replace if different
        )

    prev_row, current_row = current_row, prev_row

print(prev_row[len2])