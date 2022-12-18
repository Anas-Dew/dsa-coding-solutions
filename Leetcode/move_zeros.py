# Problem Link -> https://leetcode.com/problems/move-zeroes/

# Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums[i])
                nums.remove(nums[i])

# Notes -> iterate through the array and if got 0 in path,
# append it to the last then remove that 0. Simple.