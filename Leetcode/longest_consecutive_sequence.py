class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
        # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max (length, longest)
        return longest

        # THIS NOT WORKS SO GOOD. "DOESN'T COVER EDGE CASES". And Not Accepted in Leetcode.
        # nums.sort()
        # count = 0
        # if len(nums) == 1:
        #     return 1
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         count += 1
        #         pass
        #     elif nums[i] + 1 == nums[i+1]:
        #         count += 1
        #     else :
        #         return count + 1
        # return count

if __name__ == "__main__" :
    test = Solution()
    # print(test.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(test.longestConsecutive([100,4,200,1,3,2]))