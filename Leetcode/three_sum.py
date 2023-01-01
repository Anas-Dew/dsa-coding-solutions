class Solution:

    def threeSum(self, nums):
        """
        We sort the array, then iterate through the array, and for each element, we use two pointers to
        find the other two elements that sum to the target
        
        :param nums: the list of numbers
        :return: A list of lists of integers.
        """
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
           # This is to avoid duplicates.
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else :
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    # This is to avoid duplicates.
                    while nums[l] == nums[l - 1] and l < r :
                        l += 1
        return ans


a = [-1,0,1,2,-1,-4]
ans = Solution()
print(ans.threeSum(a))