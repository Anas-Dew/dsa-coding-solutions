# this will remove duplicate elements from a sorted array.

def remove_duplicate(A, N):

    """
    It iterates through the array, and if the current element is not equal to the last element that was
    not a duplicate, it increments the count of non-duplicate elements, and sets the current element to
    the last non-duplicate element
    
    :param A: the array
    :param N: the length of the array
    :return: The number of unique elements in the array.
    """

 # code here
    count_no_duplicate = 0
    for i in range(N):
        if A[i] != A[count_no_duplicate]:
            count_no_duplicate += 1
            A[count_no_duplicate] = A[i]
            
    return count_no_duplicate + 1 
    
A = [2,2,2,2,2]
A = [1,2,2,3,5]
N = len(A)
print(remove_duplicate(A, N))
# print(A[1:])