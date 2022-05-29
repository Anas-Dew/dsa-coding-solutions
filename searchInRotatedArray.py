def searchA(A : list, key : int):
        for i in range(len(A)):
            if key == A[i]:
                return i
            else:
                continue
        return -1
        

A = [5,6,7,8,9,10,1,2,3]
key = 10

print(searchA(A, key))

# ---- Another Method ----
def searchB(A : list, key : int):
        if key in A:
                   return A.index(key)
        return -1
