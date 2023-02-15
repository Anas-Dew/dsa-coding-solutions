# Solution 1
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for charecter in s:
            if charecter.isalnum():
                newString += charecter.lower()

        return newString == newString[::-1]

# Solution 2
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1  
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, char: str):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

if __name__ == "__main__" :
    test = Solution2()
    print(test.isPalindrome('.a'))