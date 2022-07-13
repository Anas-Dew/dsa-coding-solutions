# this is a simple but good method.

# THE PROBLEM
# we have to find the kth (for eg. if k = 3, kth smallest element will be 3rd element of array) smallest element.

# THE MEHTOD
# first sort the array
# then subscript the array like array[index]. -> arr[k-1]. -1 is for avoidnig 0th index trap.
# you got the kth smallest element.


def kthSmallest(arr : list, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]