class SumOfTwoValues:
    def __init__(self, n, x, array):
        self.n = n
        self.x = x
        self.array = array

    def get_numbers(self):
        sorted_list = []
        for i, ele in enumerate(self.array, start=1):
            sorted_list.append((ele, i))

        sorted_list.sort(key=lambda x: x[0])
        left, right = 0, len(sorted_list) - 1
        while left < right:
            mid = sorted_list[left][0] + sorted_list[right][0]
            if mid == self.x:
                if sorted_list[left][1] < sorted_list[right][1]:
                    print(sorted_list[left][1], sorted_list[right][1], sep=' ')
                else:
                    print(sorted_list[right][1], sorted_list[left][1], sep=' ')
                return
            elif mid > self.x:
                right -= 1
            else:
                left += 1
        print("IMPOSSIBLE")

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    n, x = list(map(int, input().split()))
    array = list(map(int, input().split()))

    obj = SumOfTwoValues(n, x, array)
    obj.get_numbers()