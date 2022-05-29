from collections import Counter

def singleNumber(nums):
    leastnums = []
    dictof = Counter(nums)
    for i in nums:
            if dictof[i] == 1:
                leastnums.append(i)
    leastnums.sort()
    return leastnums


arr = [1,2,3,2,1,4]
print(singleNumber(arr))
