#  Problem Link -> https://leetcode.com/problems/find-pivot-index/



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum, right_sum, left_sum = sum(nums), 0, 0
        for i in range(len(nums)):
            right_sum = total_sum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

# Notes -> We iterate through the array, and at each index, we check if the sum of the left side of the index is equal to the sum of the right side of the index.