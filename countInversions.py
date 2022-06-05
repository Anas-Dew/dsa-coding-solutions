def solve(arr, n):
    inversion_count = 0
    for i in range(n):
        for j in range(n):
            if arr[i] > arr[j] and i < j:
                inversion_count += 1
    return inversion_count

# ----------------------------------------------
test_cases = [[2, 3, 4, 5, 6],[10, 10, 10],[2, 4, 1, 3, 5]]

for case in test_cases:
    print(solve(case,len(case)), end=' | ')