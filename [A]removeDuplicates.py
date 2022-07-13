def remove_duplicate(A, N):
    ptr = A[0]
    temp=1
    i=1
    while i<N:
        if A[i] != ptr:
            A[temp]=A[i]
            ptr=A[i]
            temp+=1
        i+=1
            return temp


# A = [2,2,2,2,2]
A = [1,2,3,5,2,2,4,4,3,2]
N = len(A)
print(remove_duplicate(A, N))
# print(A[1:])