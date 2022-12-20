#  Problem Link -> https://leetcode.com/problems/majority-element/

# Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = {}
        for i in nums:
            if i in maj:
                maj[i] += 1
            else :
                maj[i] = 1
        return max(zip(maj.values(), maj.keys()))[1]  

# Notes -> We create a dictionary. And add each element to it but with how many times it occured in the list like {value:occurence}. For that we iterate through the list and check if the value is in dictionary: if it is, increase occurence of value by 1; else add that value to the dictionary with the value = 1. and then return the key of the maximum value in the dictionary.