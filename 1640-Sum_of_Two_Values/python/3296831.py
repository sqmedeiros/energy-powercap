def input_to_list(str_input):
    numbers = []
    first = 0
    last = 0
    for char in str_input:
        if char != " ":
            last += 1
        else:
            numbers.append(int(str_input[first:last]))
            last += 1
            first = last
    numbers.append(int(str_input[first:]))
    return numbers


def values_indexes(array, val1, val2):
    index1 = 0
    index2 = 0
    for i in range(len(array)):
        if array[i] == val1:
            index1 = i
            break
    for j in range(len(array)-1, 0, -1):
        if array[j] == val2:
            index2 = j
            break
    print(index1+1, index2+1)

def ferris_wheel():
    n_x = input_to_list(input())  # n-array size, x-target sum
    array_values = input_to_list(input())
    sorted_array_values = sorted(array_values)

    max_value_index = len(array_values) - 1
    min_value_index = 0

    found_values = False
    while max_value_index > min_value_index:
        if sorted_array_values[max_value_index] + sorted_array_values[min_value_index] == n_x[1]:
            values_indexes(array_values, sorted_array_values[max_value_index], sorted_array_values[min_value_index])
            found_values = True
            break
        elif sorted_array_values[max_value_index] + sorted_array_values[min_value_index] > n_x[1]:
            max_value_index -= 1
        elif sorted_array_values[max_value_index] + sorted_array_values[min_value_index] < n_x[1]:
            min_value_index += 1

    if not found_values:
        print("IMPOSSIBLE")


ferris_wheel()