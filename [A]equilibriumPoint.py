"""

Equilibrium point is the point such that from that position
left all elements of array and right all elements of array of sum will be
equal.

MY NOTES :
        algo +=>

        1. create two variables- left sum and right sum and also get total sum of given array
        2. with each iteration, keep removing (total sum - current element val) from right array. And 
        adding current element to the left array. 
        3. if left == right then you got it.



"""

def equilibriumPoint(A, N):
    # Your code here
    total_sum, right_sum, left_sum = sum(A), 0, 0
    for i in range(N):
        right_sum = total_sum - A[i] - left_sum
        if left_sum == right_sum:
            return i+1
        left_sum += A[i]
    return -1


# TEST
A = [1, 3, 5, 2, 2]
N = len(A)
print(equilibriumPoint(A, N))
