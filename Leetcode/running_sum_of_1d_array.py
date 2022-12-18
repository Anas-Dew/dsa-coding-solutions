#  Problem Link -> https://leetcode.com/problems/running-sum-of-1d-array/

# Solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningArray = [nums[0]]
        for i in range(1, len(nums)):
            runningArray.append(runningArray[i-1]+nums[i])
        return runningArray

# Notes -> simply add first value of original array to running array, and then start a loop from 1.
# with each iteration, append (last element + current element) to the running array. then return it.