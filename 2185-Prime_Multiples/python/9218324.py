import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sum_ = 0
    for i1 in range(k):
        mul1 = a[i1]
        sum_ += n // mul1
        for i2 in range(i1+1, k):
            mul2 = mul1 * a[i2]
            sum_ -= n // mul2
            for i3 in range(i2+1, k):
                mul3 = mul2 * a[i3]
                sum_ += n // mul3
                for i4 in range(i3+1, k):
                    mul4 = mul3 * a[i4]
                    sum_ -= n // mul4
                    for i5 in range(i4+1, k):
                        mul5 = mul4 * a[i5]
                        sum_ += n // mul5
                        for i6 in range(i5+1, k):
                            mul6 = mul5 * a[i6]
                            sum_ -= n // mul6
                            for i7 in range(i6+1, k):
                                mul7 = mul6 * a[i7]
                                sum_ += n // mul7
                                for i8 in range(i7+1, k):
                                    mul8 = mul7 * a[i8]
                                    sum_ -= n // mul8
                                    for i9 in range(i8+1, k):
                                        mul9 = mul8 * a[i9]
                                        sum_ += n // mul9
                                        for i10 in range(i9+1, k):
                                            mul10 = mul9 * a[i10]
                                            sum_ -= n // mul10
                                            for i11 in range(i10+1, k):
                                                mul11 = mul10 * a[i11]
                                                sum_ += n // mul11
                                                for i12 in range(i11+1, k):
                                                    mul12 = mul11 * a[i12]
                                                    sum_ -= n // mul12
                                                    for i13 in range(i12+1, k):
                                                        mul13 = mul12 * a[i13]
                                                        sum_ += n // mul13
                                                        for i14 in range(i13+1, k):
                                                            mul14 = mul13 * a[i14]
                                                            sum_ -= n // mul14
                                                            for i15 in range(i14+1, k):
                                                                mul15 = mul14 * a[i15]
                                                                sum_ += n // mul15
                                                                for i16 in range(i15+1, k):
                                                                    mul16 = mul15 * a[i16]
                                                                    sum_ -= n // mul16
                                                                    for i17 in range(i16+1, k):
                                                                        mul17 = mul16 * a[i17]
                                                                        sum_ += n // mul17
                                                                        for i18 in range(i17+1, k):
                                                                            mul18 = mul17 * a[i18]
                                                                            sum_ -= n // mul18
                                                                            for i19 in range(i18+1, k):
                                                                                mul19 = mul18 * a[i19]
                                                                                sum_ += n // mul19
                                                                                for i20 in range(i19+1, k):
                                                                                    mul20 = mul19 * a[i20]
                                                                                    sum_ -= n // mul20

    print(sum_)

if __name__ == "__main__":
    main()