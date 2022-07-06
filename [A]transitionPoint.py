"""
if 1 is not in arr then return -1 or if 0 is not in arr return 0. BASE CASE.

with help of loop keep tracking where the consistency of first element has changed and that will be
the transition point.

"""

def transitionPoint(arr, n):
    #Code here
    if 1 not in arr:
        return -1
    elif 0 not in arr:
        return 0
    
    first_element = arr[0]
    for i in range(n):
        if arr[i] == first_element:
            pass
        else:
            return i

# TEST_CASE
# arr = [1]
arr = [0,0,0,1,1]
n = len(arr)
# ANS = 3
print(transitionPoint(arr, n))