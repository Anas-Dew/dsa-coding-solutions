# spilt the arr into two sub arrays by k (index from which array will be splitted).
# reverse first splitted array using .reverse() and so do for second spiltted array.
# at last join both saparated reversed arrays using extend.


def reverseInGroups(arr, N, K):
    cArr1 = arr[:K]
    cArr1.reverse()

    cArr2 = arr[K:]
    cArr2.reverse()

    cArr1.extend(cArr2)
    arr = cArr1.copy()
    return cArr1


# arr = [1,2,3,4,5]
arr = [5,6,8,9]
N = len(arr)
K = 3
print(reverseInGroups(arr, N, K))
