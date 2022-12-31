class Solution:
    def summer(self, triplets):
        return sum(triplets)

    def threeSum(self, nums):
        ans = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    trips = [nums[i], nums[j], nums[k]]
                    if self.summer(trips) == 0:
                        if j == 1 : ans.append(trips)
                        if len(ans) > 0 == True:
                            if trips != ans[-1]:
                                ans.append(trips)
        return ans

a = [-1,0,1,2,-1,-4]
ans = Solution()
print(ans.threeSum(a))