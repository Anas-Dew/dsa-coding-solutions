from collections import defaultdict

"""
NOTES
create a dict that's key is list and value is list also. with each loop, create a list with empty 26 zeros and map each char to index of it (a will be at 0, for example). then do this for all. if we found same list key for another value, store it with that key. In end, return all values of that master dict.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        We create a dictionary with a key of a tuple of the count of each letter in the alphabet and the
        value is a list of strings that have the same count of letters
        
        :param strs: list[str]
        :type strs: list[str]
        :return: A list of lists of strings.
        """
        res = defaultdict(list)
        for S in strs:
            count = [0] * 26
            for C in S:
                count[ord(C) - ord("a")] += 1
            res[tuple(count)].append(S)
        return res.values()


if __name__ == "__main__" :
    test = Solution()
    print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))