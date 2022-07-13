# TIME > 3.45 sec
def maxIndexDiff(A : list, N : int):
    maxDiff = -1
    for i in range(0, N):
            j = N - 1
            while(j >= i):
                if A[j] >= A[i] and maxDiff < (j - i):
                    maxDiff = j - i
                j -= 1
    return maxDiff
array = [65, 6, 74, 94, 56, 89, 9, 63, 75, 25, 34, 68, 93, 48, 16]
# array = [34,8,10,3,2,80,30,33,1]
# array = [1,10]
# array = [15, 86, 78, 93, 100, 6]
n = len(array)

# print(solve(array, n))
print(maxIndexDiff(array, n))