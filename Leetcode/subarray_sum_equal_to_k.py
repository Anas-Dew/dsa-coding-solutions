def subarraySum(nums: list[int], k: int):
    res = 0
    curSum = 0
    prefixSum = { 0 : 1 }

    for n in nums:
        curSum += n
        diff = curSum - k

        res += prefixSum.get(diff, 0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

    return res


if __name__ == "__main__" :
    print(subarraySum([1,1,1,1], k=3))