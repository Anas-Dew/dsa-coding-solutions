import numpy


class Solution:
    # Not so efficient. Time Complexity : n^2
    # def productExceptSelf(self, nums: list):
    #     answer_array = []
    #     for i in range(len(nums)):
    #         product_element = int(numpy.prod(nums[i+1:])) * int(numpy.prod(nums[:i]))
    #         answer_array.append(product_element)
    #     return answer_array

    # This one is good.
    def productExceptSelf(self, nums: list):
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n
        answer_array = [1] * n

        # Calculate prefix product
        for i in range(1, n):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]

        # Calculate suffix product
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]

        # Calculate final answer array
        for i in range(n):
            answer_array[i] = prefix_product[i] * suffix_product[i]

        return answer_array


if __name__ == "__main__":
    test = Solution()
    print(test.productExceptSelf([1, 2, 3, 4]))

# Explanation
# The code takes a list of integers, nums, as input and returns a new list, answer_array, where each element is the product of all elements in nums except for the element at the corresponding index.

# Instead of using a for loop to iterate through the elements of nums and computing the product of sub-arrays for each element, the optimized code uses two additional arrays, prefix_product and suffix_product.

# The prefix_product array holds the product of all elements before the current index, while the suffix_product array holds the product of all elements after the current index.

# The first step is to initialize the prefix_product and suffix_product arrays with 1's and answer_array with 1's.

# Then, the code uses a for loop to iterate through the nums list and calculate the prefix product for each element. It starts with the second element because the first element has no element before it, so the prefix product is 1.

# The next step is to iterate through nums list in reverse order and calculate the suffix product for each element. It starts with the second last element because the last element has no element after it, so the suffix product is 1.

# Finally, the code uses a for loop to iterate through nums and calculate the final answer array by multiplying the corresponding elements of the prefix_product and suffix_product arrays.

# Since we are only iterating through the nums list once for each of the 3 steps, the time complexity is O(n), which is much more efficient than the previous code which needs to slice the array and compute the product of sub-arrays multiple times, resulting in a time complexity of O(n^2)

# By using the prefix and suffix product arrays, we avoid the need to repeatedly compute the product of sub-arrays and significantly improve performance for large inputs.
