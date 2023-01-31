class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.sort()
        return_value = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = '_'
                return_value -= 1
        # return return_value
        print(return_value)
                

        print(nums)

if __name__ == "__main__" :
    answer = Solution()
    a = [0,1,2,2,3,0,4,2]
    a.sort()
    print(a)
    answer.removeElement(a, 2)    