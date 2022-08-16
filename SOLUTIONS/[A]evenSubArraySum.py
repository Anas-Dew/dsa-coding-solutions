def solve(N,arr):
        """
        It returns "YES" if the sum of every pair of adjacent elements in the array is 0, and "NO" otherwise
        
        :param N: the number of elements in the array
        :param arr: an array of integers
        :return: a string.
        """
        for i in range(0,N-1):
            if arr[i] + arr[i+1] != 0:
                return "NO"
        return "YES"
        



# arr = [8, -8, 7, 9] # no
# arr = [0,-1,-1,2,-1,1] # no
# arr = [6 ,-6, -10, 2, 2, 2, 4, -5] # no
# arr = [-72, 72, 8] #no
# arr = [-6, 6, -6 ,6, -6, 6, -6 ,6 ,-6, 6, -6] #yes

test_cases = [[8, -8, 7, 9],[0,-1,-1,2,-1,1],[6 ,-6, -10, 2, 2, 2, 4, -5],[-72, 72, 8],[-6, 6, -6 ,6, -6, 6, -6 ,6 ,-6, 6, -6]]
for i in test_cases:
    N = len(i)
    print(solve(N, i))
