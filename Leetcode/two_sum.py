# Problem link -> https://leetcode.com/problems/two-sum/

# Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i
        return

# Video Explanation -> https://www.youtube.com/watch?v=KLlXCFG5TnA