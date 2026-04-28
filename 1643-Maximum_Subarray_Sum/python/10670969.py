# from collections import Counter

# def count_distinct_values_counter(numbers):
#   counter = Counter(numbers)
#   return len(counter)

    # unique_values = set(numbers)

    # return len(unique_values)


# import numpy as np

# def count_distinct_values_numpy(numbers):
#     unique_values = np.unique(numbers)
#     return len(unique_values)


# def count_distinct_values(numbers):
#   unique_values = set()
#   for num in numbers:
#     unique_values.add(num)
#   return len(unique_values)


# n = int(input())

# # قراءة القائمة وتحويلها إلى مجموعة للحصول على القيم الفريدة
# numbers = set(map(int, input().split()))

# # طباعة عدد القيم الفريدة
# print(len(numbers))

# import sys

# # قراءة الإدخال بالكامل دفعة واحدة
# input = sys.stdin.read

# # قراءة المدخلات
# data = input().split()

# # عدد القيم الفريدة
# n = int(data[0])
# numbers = set(data[1:])

# # طباعة عدد القيم الفريدة
# sys.stdout.write(str(len(numbers)) + "\n")


# n, x = map(int, input().split())
# weights = list(map(int, input().split()))
# weights.sort()
# i = 0 
# j = n - 1 
# gondolas = 0
# while i <= j:
#     if weights[i] + weights[j] <= x:
#         i += 1  
#     j -= 1 
#     gondolas += 1
# print(gondolas)

n = int(input())
arr = list(map(int, input().split()))

max_sum = float('-inf')
current_sum = 0

for num in arr:
    current_sum += num
    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < 0:
        current_sum = 0

print(max_sum)