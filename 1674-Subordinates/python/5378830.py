from array import array

n = int(input())
employees = array("i", map(int, input().split()))
degrees = array("i", [0] * n)

for employee in employees:
    degrees[employee - 1] += 1

values = array("i", [0] * n)

stack = [i for i, degree in enumerate(degrees) if degree == 0]
while stack:
    current = stack.pop()
    if current == 0:
        break
    parent = employees[current - 1] - 1
    degrees[parent] -= 1
    if degrees[parent] == 0:
        stack.append(parent)
    values[parent] += values[current] + 1

print(" ".join(map(str, values)))