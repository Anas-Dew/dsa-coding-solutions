
# def rotateArr(A,D,N):
#         for i in range(D):
#             temporary_value_of_first_index = 0
#             temporary_value_of_first_index += int(A[0])
#             A.remove(A[0])
#             A.append(temporary_value_of_first_index)
            
#         return A
def rotateArr(A,D,N):
        D = D%N
        x = A[:D]
        z = A[D:]
        z.extend(x)
        A.clear()
        A.extend(z)
        return A


A = [1,2,3,4,5]
# A = "47 77 25 6 20 55 69 5 50 63 61 41 87 80 2 96 77 70 12 43 31 8 64 41 68 18 95 79 52 74 1 98 3 26 3 74 32 23 79 81 37 39 21 24 18 22 71 47 44".split(' ')
N = len(A)
D = 2
print(rotateArr(A,D,N))