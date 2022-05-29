import collections

def transform(A, B):
        def isTransformable(first, second):
    # if the length of both strings differs
            if len(first) != len(second):
                return False
         
            # return true if both strings have the same set of characters
            return collections.Counter(first) == collections.Counter(second)
        if isTransformable(A,B):
            
            count = 0
            i = len(A) - 1
            j = i
            while i >= 0:
                while i >= 0 and A[i] != B[j]:
                    i = i - 1
                    count = count + 1
                i = i - 1
                j = j - 1
            return count
        else:
            return -1

print(transform('abcd','cdba'))


