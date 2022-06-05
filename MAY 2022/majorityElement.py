def majorityElement(A, N):
        mp = {}
        for i in range(0, N):
              if A[i] in mp.keys():
                 mp[A[i]] += 1
              else:
                         mp[A[i]] = 1
        for key in mp:
              if mp[key] > (N / 2):
                 return key
        return -1
            



A = [1,2,2,2,3]
# A = [1,2,3,2,2,2]
N = len(A)
print(majorityElement(A,N))
