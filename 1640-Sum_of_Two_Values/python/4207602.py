def sum_of_values(array, target):
    seen = {}

    for i, num in enumerate(array):
        if num in seen:
            return f'{seen[num]} {i + 1}'
        seen[target - num] = i + 1
    return 'IMPOSSIBLE'



def main():
    _, target = map(int, input().split())
    array = map(int, input().split())
    print(sum_of_values(array, target))



if __name__ == '__main__':
    main()