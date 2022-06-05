s = 'hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs'
from collections import Counter
def ss(s): # BAD ALGO BECAUSE IT CANT HANDLE BIG INPUT
    A = list(s)
    mp = {}
    for i in range(0, len(s)):
            if A[i] in mp.keys():
                mp[A[i]] += 1
            else:
                mp[A[i]] = 1
    for key in mp:
        if mp[key] == 1:
            return key
        else:
            continue

def nonrepeatingCharacter(s):
        #code here
        freq = Counter(s)
        for i in s:
            if freq[i]==1:
                return i
        return -1

print(nonrepeatingCharacter(s))

