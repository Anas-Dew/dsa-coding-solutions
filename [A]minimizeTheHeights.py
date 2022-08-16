def solve(arr, n, k):
    for each in range(n):
            if arr[each] > k:
                arr[each] = arr[each] - k
            else:
                arr[each] = arr[each] + k
    return max(arr) - min(arr)


# A = [3, 9, 12, 16, 20]
# A = [1, 5, 8, 10]
A = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
n = len(A)
k = 5
# k = 2

print(solve(A, n, k))