def solve(A : list, B : list, M : int, N : int, X : int):
    list_pair = []
    for i in range(M):
        for j in range(N):
            if A[i] + B[j] == X:
                list_pair.append([A[i],B[j]])
    list_pair.sort()
    return list_pair


A = [-113, 147, 65, 37, 6, -27, -73, 109, 31, -8, -102, -74, -183, -186, 131, 40, 150, -123, -111, -91, 176, 170, -4 ,-165, -49, 93, -68, 142, 171, 98, -60, -196, 99, 69, 138, -20, -143, -63, 129, -158, -103, -30, 73, 32, 151, 136, 82 ,-150, -31, -37, -164, 101, -69 ,-62 ,-100 ,-14 ,111 -97, 119 ,-137 ,68 ,-130, -127, -161, 124]
B = [-122, 102, -67, 152, -169, 48, -52, -134, 33, -91, 188 ,6 ,-148, -109, -35, 64 ,32 ,75 ,198, 22, 65, -168, 185, -66, -127, -147, 145, -29, 104, 51 ,93 ,71 ,129, 39, 76, 10 ,70]
X=2

print(solve(A, B, len(A), len(B), X))