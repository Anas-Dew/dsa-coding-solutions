# It returns the minimum distance between two elements in an array
# distance will be calculated from first occurence of both x and y.
# like arr = [1,2,3,2], x = 1, y = 2
# answer here will be 1 because 2 first occured at index 1 so 1-0(indexes) = 1

def minDist(arr, n, x, y):
    
        if x not in arr or y not in arr:
            return -1
        minDistance = arr.index(y) - arr.index(x)
        return minDistance



arr = [1,2,3,2] # ANS - 1
# arr = [86,39,90,67,84,90,66,62] # ANS - -1
# arr = "98 78 10 12 59 37 45 18 1 56 37 14 3 32 85 10 69 89 29 93 44 16 26 13 50 75 79 21 20 33 55 17 63 64 80 21 52 24 90 52 80 26 18 34 57 2 95 25 42 23 17 85 39 94 50 40 21 28 12 40 61 67 9 23 30 88 95 34 64 85 85 95 62 54 28 19 55 22 95 49 97 64 33".split(' ')
# arr = "96 82 48 76 34 19 7 80 36 57 77 34 19 35 5 57 16 66 42 62 89 19 60 19 25 16 20 51 77 75 12 73 8 11 100 93 81 58 72 17 14 48 2 33 82 6 41 49 72 34 10 12 53 21 30 77 36 49 79 13 75 42".split(' ')

n = len(arr)
# 34 56
x = 1
y = 2

print(minDist(arr, n, x, y))