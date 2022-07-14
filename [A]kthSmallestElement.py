# this is a simple but good method.

# THE PROBLEM
# we have to find the kth (for eg. if k = 3, kth smallest element will be 3rd element of array) smallest element.

# THE MEHTOD
# first sort the array
# then subscript the array like array[index]. -> arr[k-1]. -1 is for avoidnig 0th index trap.
# y

"""
example 1 :

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
"""
def kthSmallest(arr : list,k : int):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]

arr = [6,5,4,3,32,5,7,98,9,8,6,43,2]
k = 4
print(kthSmallest(arr,k))