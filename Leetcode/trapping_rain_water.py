class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) -1
        maxL, maxR = height[l], height[r]
        trapped_water = 0
        while l < r :
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trapped_water += maxL - height[l]
            else :
                r -= 1
                maxR = max(maxR, height[r])
                trapped_water += maxR - height[r]

        return trapped_water

if __name__ == "__main__" :
    test = Solution()
    print(test.trap([0,1,0,2,1,0,1,3,2,1,2,1]))